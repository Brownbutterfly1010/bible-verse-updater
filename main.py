import requests

# 🔐 Your Notion Integration Token
NOTION_TOKEN = "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"

# 📄 Your Notion Page ID
PAGE_ID = "20096b82e05d807d9664c9d50c0c7219"

# 📖 Fetch Verse of the Day
verse_response = requests.get("https://beta.ourmanna.com/api/v1/get/?format=json")
verse_json = verse_response.json()
verse_text = verse_json['verse']['details']['text']
verse_ref = verse_json['verse']['details']['reference']

# 📘 Combine text + reference
full_verse = f"{verse_text} – {verse_ref}"

# ✏️ Send to Notion
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
print("✅ Status:", response.status_code)
print("📖 Verse:", full_verse)
