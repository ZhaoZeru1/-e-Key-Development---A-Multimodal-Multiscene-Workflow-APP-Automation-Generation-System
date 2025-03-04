from tools import fetch_github_repos
TOKEN = "YOUR_TOKEN"

# Split the search query into smaller parts
SEARCH_HR_PART_1 = (
    '"HR management system" OR "employee performance tracking" OR "human resource management"'
)
SEARCH_HR_PART_2 = (
    '"HRM software" OR "recruitment platform" OR "payroll management"'
)
SEARCH_HR_PART_3 = (
    '"employee engagement"'
)

# List of queries
search_queries = [SEARCH_HR_PART_1, SEARCH_HR_PART_2, SEARCH_HR_PART_3]

# Iterate through each query and fetch results
for query in search_queries:
    print(f"正在爬取：{query}")
    fetch_github_repos(TOKEN, query,"hr.json")

