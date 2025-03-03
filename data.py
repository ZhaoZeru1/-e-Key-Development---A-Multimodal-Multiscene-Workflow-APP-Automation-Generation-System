from tools import fetch_github_repos

TOKEN = "YOUR_TOKEN"

# Split the search query into smaller parts
SEARCH_DATA_FORM_PART_1 = (
    '"data collection platform" OR "form management system" OR "survey tool"'
)
SEARCH_DATA_FORM_PART_2 = (
    '"form builder" OR "data submission system" OR "online survey platform"'
)
SEARCH_DATA_FORM_PART_3 = (
    '"form automation"'
)

# List of queries
search_queries = [SEARCH_DATA_FORM_PART_1, SEARCH_DATA_FORM_PART_2, SEARCH_DATA_FORM_PART_3]

# Iterate through each query and fetch results
for query in search_queries:
    print(f"正在爬取：{query}")
    fetch_github_repos(TOKEN, query)
