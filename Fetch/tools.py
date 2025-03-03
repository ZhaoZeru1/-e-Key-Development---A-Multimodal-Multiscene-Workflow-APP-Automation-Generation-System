from github import Github
import json
import signal
import sys


def is_text_file(file_content):
    """
    判断文件是否为文本文件
    """
    try:
        file_content.decoded_content.decode("utf-8")
        return True
    except:
        return False


def classify_component(file_name, content, component_keywords):
    """
    根据关键字分类组件
    """
    components = {}
    for keyword, component in component_keywords.items():
        if keyword in file_name.lower() or keyword in content.lower():
            components[component] = file_name
    return components


def fetch_repo_code(repo, component_keywords, frontend_extensions, backend_extensions):
    """
    获取仓库代码
    """
    code_data = {
        "repo_name": repo.name,
        "frontend": [],
        "backend": [],
        "components": {}
    }

    def recursive_fetch(contents):
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "file":
                file_name = file_content.path
                if not is_text_file(file_content):
                    continue
                try:
                    file_code = file_content.decoded_content.decode("utf-8", errors="ignore")
                except:
                    file_code = ""

                components = classify_component(file_name, file_code, component_keywords)
                code_data["components"].update(components)

                if file_name.endswith(frontend_extensions):
                    code_data["frontend"].append({"file_name": file_name, "code": file_code})
                elif file_name.endswith(backend_extensions):
                    code_data["backend"].append({"file_name": file_name, "code": file_code})
            elif file_content.type == "dir":
                try:
                    sub_contents = repo.get_contents(file_content.path)
                    recursive_fetch(sub_contents)
                except:
                    print(f"无法访问 {file_content.path}")

    try:
        contents = repo.get_contents("")
        recursive_fetch(contents)
    except:
        print(f"无法获取 {repo.name} 的内容")

    return code_data


def save_data_to_json(data, output_file):
    """
    保存数据到 JSON 文件
    """
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    print(f"数据已保存到 {output_file}")


def handle_exit_signal(signum, frame, all_data, output_file):
    """
    处理退出信号，确保数据保存
    """
    print("\n程序被中断，正在保存当前进度...")
    save_data_to_json(all_data, output_file)
    sys.exit(0)


def fetch_github_repos(token, search_query, output_file="code.json"):
    """
    从 GitHub 搜索并爬取符合查询条件的仓库
    """
    g = Github(token)
    all_data = []

    component_keywords = {
        "approval": "审批",
        "workflow": "工作流",
        "process": "流程管理",
        "request": "请求处理",
        "user": "用户管理",
        "auth": "认证",
        "admin": "管理员功能"
    }
    frontend_extensions = (".html", ".css", ".js", ".ts", ".tsx", ".jsx", ".vue", ".json")
    backend_extensions = (
    ".py", ".java", ".go", ".php", ".cs", ".cpp", ".c", ".rb", ".swift", ".dart", ".sh", "Dockerfile")

    signal.signal(signal.SIGINT, lambda s, f: handle_exit_signal(s, f, all_data, output_file))

    repositories = g.search_repositories(search_query)
    for repo in repositories:
        print(f"正在爬取 {repo.name}...")
        repo_data = fetch_repo_code(repo, component_keywords, frontend_extensions, backend_extensions)
        all_data.append(repo_data)
        save_data_to_json(all_data, output_file)

    save_data_to_json(all_data, output_file)
    return all_data
