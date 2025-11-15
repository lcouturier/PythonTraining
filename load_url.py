import requests
# import re

url = "https://gitlab.socrate.vsct.fr/invictus/invictus-root/-/jobs/78905057/trace"


# line = "Error: creating Lambda Function (ivts-75550-iv-tic-event-lambda):"
# match = re.search(r"Lambda Function \((.*?)\)", line)
# if match:
#     print(match.group(1))


# with requests.get(url) as response:
#     response.raise_for_status()
#     html = response.text


# line = """
# Error: creating Lambda Function (ivts-75550-iv-tic-event-lambda):
# Something else...
# Error: updating Lambda Function (my-second-lambda):
# Error: removing Lambda Function (third-lambda-test):
# """

# items = re.findall(r"[Ll]ambda\s+Function\s*\(([^)]+)\)", html)


# error_lines = [
#     line for line in html.splitlines() if "Error: creating Lambda Function" in line
# ]

# for line in items:
#     print(line)


PROJECT_ID = 11308
JOB_ID = 78905057
GITLAB_HOST = "https://gitlab.socrate.vsct.fr"
TOKEN = "TON_PRIVATE_TOKEN"  # ou "Bearer <token>"

# url = f"{GITLAB_HOST}/api/v4/projects/{PROJECT_ID}/jobs/{JOB_ID}/trace"

# headers = {
#     "PRIVATE-TOKEN": TOKEN,  # ou "Authorization": f"Bearer {TOKEN}"
#     "Accept": "text/plain",
# }

r = requests.get(url, timeout=30)
r.raise_for_status()

trace_text = r.text
print(len(trace_text), "caractères reçus")
print(trace_text[:400])  # aperçu
