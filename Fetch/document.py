from tools import fetch_github_repos

TOKEN = "YOUR_TOKEN"

# Split the search query into smaller parts
SEARCH_DOCUMENT_PART_1 = (
    '"document workflow" OR "document management system" OR "DMS software"'
)
SEARCH_DOCUMENT_PART_2 = (
    '"file approval system" OR "content management system" OR "knowledge base platform"'
)
SEARCH_DOCUMENT_PART_3 = (
    '"collaborative editing"'
)

# List of queries
search_queries = [SEARCH_DOCUMENT_PART_1, SEARCH_DOCUMENT_PART_2, SEARCH_DOCUMENT_PART_3]

# Iterate through each query and fetch results
for query in search_queries:
    print(f"正在爬取：{query}")
    fetch_github_repos(TOKEN, query)
