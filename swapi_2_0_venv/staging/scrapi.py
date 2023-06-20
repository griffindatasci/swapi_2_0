import requests
from math import ceil

def api_wan(resource):
    print(f"Scraping {resource}.")

    # Get number of pages to scrape (ensures all data is scraped with minimal requests)
    api_return = requests.get(f"https://swapi.dev/api/{resource}", timeout=90)
    api_json = api_return.json()
    n_pages = ceil(api_json["count"]/len(api_json["results"]))
    resource_list = [item for item in api_json["results"]]

    # Scrape data from each (remaining) page
    if n_pages>1:
        for page in range(2, n_pages+1):
            print(f"Scraping {resource} (page {page} of {n_pages}).")
            api_return = requests.get(
                f"https://swapi.dev/api/{resource}/?page={page}", timeout=90)
            api_json = api_return.json()
            resource_list = resource_list + [item for item in api_json["results"]]
        
    print(f"Scrape complete. These are the {resource} you are looking for...")
    return resource_list
