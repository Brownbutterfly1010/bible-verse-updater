import requests

NOTION_TOKEN = "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"
PAGE_ID = "20096b82e05d807d9664c9d50c0c7219"

def main():
    # Get verse of the day
    verse_response = requests.get("https://beta.ourmanna.com/api/v1/get/?format=json")
    verse_json = verse_response.json()
    verse_text = verse_json['verse']['details']['text']
    verse_ref = verse_json['verse']['details']['reference']
    full_verse = f"{verse_text} – {verse_ref}"

    # Update Notion page
    url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": full_verse
                            }
                        }
                    ]
                }
            }
        ]
    }
    response = requests.patch(url, headers=headers, json=data)
    print("Status code:", response.status_code)
    print("Verse sent:", full_verse)

if __name__ == "__main__":
    main()
