import requests
from bs4 import BeautifulSoup

# URL of the news website
url = "https://www.bbc.com/news"

# Send HTTP request
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    # Parse HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all h2 tags
    headlines = soup.find_all("h2")

    news_titles = []
    for headline in headlines:
        title = headline.get_text(strip=True)
        if title:
            news_titles.append(title)

    # Save to text file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, title in enumerate(news_titles, start=1):
            file.write(f"{i}. {title}\n")

    print("Headlines saved to headlines.txt")

else:
    print("Failed to fetch the webpage")
