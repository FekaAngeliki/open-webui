import requests
import json
import os

BASE_URL = 
SSO_JWT_TOKEN = 

COOKIES = {
    "ARRAffinity": ,
    "ARRAffinitySameSite": ,
    "token": ,
    "oauth_id_token":
}

def test_admin_chat_export_with_browser_headers():
    headers = {
        "Authorization": f"Bearer {SSO_JWT_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
        "Referer": BASE_URL + "/admin/settings",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,el;q=0.8",
        "Origin": BASE_URL,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    url = BASE_URL + "/api/v1/chats/all/db"
    response = requests.get(url, headers=headers, cookies=COOKIES)
    print("Chat export status:", response.status_code)
    #print("Chat export response:", response.text)
    try:
        chats = response.json()
        #print("Chats:", chats)
        # Write export to JSON file
        export_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "docs", "chats")
        os.makedirs(export_path, exist_ok=True)
        export_file = os.path.join(export_path, "all-chats-export.json")
        with open(export_file, "w", encoding="utf-8") as f:
            json.dump(chats, f, ensure_ascii=False, indent=2)
            #print(f"Exported chats to {export_file}")
    except Exception as e:
        print("Chat export JSON decode error:", e)
        #soup = BeautifulSoup(response.content, "html.parser")
        #print("HTML title:", soup.title.string if soup.title else "No title found")
        #print("HTML preview:", soup.prettify()[:500])

if __name__ == "__main__":
    test_admin_chat_export_with_browser_headers()