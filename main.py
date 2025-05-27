import requests
import os

def get_verse():
    response = requests.get("https://beta.ourmanna.com/api/v1/get/?format=json")
    data = response.json()
    verse_text = data["verse"]["details"]["text"]
    verse_ref = data["verse"]["details"]["reference"]
    return f"{verse_text} — {verse_ref}"

def update_notion(verse):
    notion_token = os.environ["NOTION_TOKEN"]
    page_id = os.environ["NOTION_PAGE_ID"]

    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    payload = {
        "children": [{
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": verse
                    }
                }]
            }
        }]
    }

    requests.patch(url, headers=headers, json=payload)

if __name__ == "__main__":
    verse = get_verse()
    update_notion(verse)
