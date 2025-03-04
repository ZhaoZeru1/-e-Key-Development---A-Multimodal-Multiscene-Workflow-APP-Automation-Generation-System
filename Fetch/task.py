from tools import fetch_github_repos
TOKEN = "YOUR_TOKEN"

# Split the search query into smaller parts
SEARCH_TASK_PROJECT_PART_1 = (
    '"task management system" OR "project management tool" OR "kanban board"'
)
SEARCH_TASK_PROJECT_PART_2 = (
    '"scrum board" OR "task workflow" OR "agile project management"'
)
SEARCH_TASK_PROJECT_PART_3 = (
    '"to-do list app"'
)

# List of queries
search_queries = [SEARCH_TASK_PROJECT_PART_1, SEARCH_TASK_PROJECT_PART_2, SEARCH_TASK_PROJECT_PART_3]

# Iterate through each query and fetch results
for query in search_queries:
    print(f"正在爬取：{query}")
    fetch_github_repos(TOKEN, query,"task.json")
