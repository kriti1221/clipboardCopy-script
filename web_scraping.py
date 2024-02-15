import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_intro(article_title):

    url = f"https://en.wikipedia.org/wiki/{article_title}"
    response = requests.get(url)

    if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            intro_paragraph = soup.find("div", class_="mw-parser-output").p
            intro_text = intro_paragraph.get_text()

            return intro_text  

    else:
            print("Failed to retrieve Wikipedia page.")
            return None     
 
article_title = "python"

# Call the function to scrape the introduction paragraph
intro = scrape_wikipedia_intro(article_title)

# Print the introduction paragraph
print("Introduction Paragraph:")
print(intro)
