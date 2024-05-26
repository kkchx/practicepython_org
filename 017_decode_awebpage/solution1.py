import requests
from bs4 import BeautifulSoup

# URL of The New York Times homepage
url = "https://www.nytimes.com/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the <h2> tags
    titles = soup.find_all('h2')
    ttl = []
    # Extract the text of each title and store it in a list
    title_list = [title.text.strip() for title in titles if title.text.strip()]

    # Print the list of titles
    print("Titles from The New York Times homepage:")
    for title in title_list:
        ttl.append(title)
    print(ttl)
else:
    print("Failed to retrieve the webpage.")