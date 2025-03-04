from tools import fetch_github_repos
TOKEN = "YOUR_TOKEN"

# Split the search query into smaller parts
SEARCH_CRM_PART_1 = (
    '"CRM system" OR "customer management platform" OR "sales tracking tool"'
)
SEARCH_CRM_PART_2 = (
    '"lead management system" OR "customer database" OR "marketing automation"'
)
SEARCH_CRM_PART_3 = (
    '"contact management"'
)

# List of queries
search_queries = [SEARCH_CRM_PART_1, SEARCH_CRM_PART_2, SEARCH_CRM_PART_3]

# Iterate through each query and fetch results
for query in search_queries:
    print(f"正在爬取：{query}")
    fetch_github_repos(TOKEN, query,"crm.json")
