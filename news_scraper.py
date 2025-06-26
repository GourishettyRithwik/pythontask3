import requests
from bs4 import BeautifulSoup
URL = "https://www.bbc.com/news"
response = requests.get(URL)
if response.status_code != 200:
    print(f"Failed to retrieve webpage. Status code: {response.status_code}")
    exit()
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find_all('h2')
#headlines
headline_list = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]
#save
output_file = "headlines.txt"
with open(output_file, "w", encoding='utf-8') as file:
    for i, title in enumerate(headline_list, 1):
        file.write(f"{i}. {title}\n")

print(f"✅ {len(headline_list)} headlines saved to '{output_file}'")
