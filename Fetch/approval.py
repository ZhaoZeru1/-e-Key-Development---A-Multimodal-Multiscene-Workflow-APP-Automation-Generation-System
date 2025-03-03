from tools import fetch_github_repos

TOKEN = "YOUR_TOKEN"

# Split the search query into smaller parts
SEARCH_APPROVAL_PART_1 = (
    '"approval workflow" OR "process automation" OR "business process management"'
)
SEARCH_APPROVAL_PART_2 = (
    '"BPM system" OR "workflow automation" OR "request approval system"'
)
SEARCH_APPROVAL_PART_3 = (
    '"leave approval"'
)

# List of queries
search_queries = [SEARCH_APPROVAL_PART_1, SEARCH_APPROVAL_PART_2, SEARCH_APPROVAL_PART_3]

# Iterate through each query and fetch results
for query in search_queries:
    print(f"正在爬取：{query}")
    fetch_github_repos(TOKEN, query)
