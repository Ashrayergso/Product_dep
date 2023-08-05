```python
import requests
from bs4 import BeautifulSoup

def search_product_alternatives(product_name):
    # Define the base URL for the search
    base_url = "https://www.google.com/search?q="

    # Create the search URL
    search_url = base_url + product_name + "+alternative"

    # Send a GET request to the search URL
    response = requests.get(search_url)

    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the search result links
    links = soup.find_all('a')

    # Filter the links to get only the ones that lead to product alternatives
    product_links = [link['href'] for link in links if "product" in link['href']]

    return product_links
```