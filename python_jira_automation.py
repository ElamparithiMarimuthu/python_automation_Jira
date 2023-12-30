import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://parithie713.atlassian.net/rest/api/3/issue"

# here iam not hardcode my api token, intead of i was using environment variable to set my "API_TOKEN" in jira
api_token = os.getenv("JIRA_API_TOKEN")

if api_token is None:
    print("API token not found. Please set the 'JIRA_API_TOKEN' environment variable.")
    exit()

auth = HTTPBasicAuth("parithie713@gmail.com", api_token)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = json.dumps({
    "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "My first jira ticket",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                }
            ],
            "type": "doc",
            "version": 1
        },
        "project": {
            "key": "KAN"
        },
        "issuetype": {
            "id": "10001"
        },
        "summary": "First JIRA Ticket",
    },
    "update": {}
})

response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
