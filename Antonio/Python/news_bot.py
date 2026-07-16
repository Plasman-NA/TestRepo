import sys
import requests
from bs4 import BeautifulSoup

def fetch_news(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        # Tries to access the provided website
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Since every website is different, we search for <h1>, <h2> or <h3> tags
        # which usually contain the main/breaking news
        headlines = soup.find_all(['h1', 'h2', 'h3'])
        
        print(f"\n--- FETCHING NEWS FROM: {url} ---\n")
        
        count = 1
        for h in headlines:
            text = h.get_text().strip()
            # Filters out very short text that might be menus
            if len(text) > 20:
                print(f"{count}. {text}")
                print("-" * 30)
                count += 1
            if count > 10: break # Limit of 10 news items
            
    except Exception as e:
        print(f"Error accessing {url}: {e}")

if __name__ == "__main__":
    # Checks if you passed a website as an argument
    if len(sys.argv) > 1:
        site = sys.argv[1]
        fetch_news(site)
    else:
        # If nothing is passed, it uses a default (e.g., CBC News)
        print("No website provided. Using default: CBC News")
        fetch_news("http://www.cbc.ca")

    input("\nPress Enter to exit\close...")
