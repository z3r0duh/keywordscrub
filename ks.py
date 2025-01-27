import requests
from bs4 import BeautifulSoup

def search_for_words(url, search_words):
    """
    Searches a website for a list of words.

    Parameters:
        url (str): The website URL to search.
        search_words (list): A list of words to search for.

    Returns:
        tuple: Two lists - found words and not found words.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP request errors
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text().lower()  # Convert text to lowercase for case-insensitive matching
        
        # Check for each word in the page content
        found_words = [word for word in search_words if word.lower() in page_text]
        not_found_words = [word for word in search_words if word.lower() not in page_text]
        
        return found_words, not_found_words

    except Exception as e:
        return [], [f"Error: {e}"]

# List of URLs to search
urls = [
    "https://www.investopedia.com/terms/n/networking.asp"]

# List of words to search for
search_words = ["password", "networking", "network", "security", "technician", "cybersecurity", "Technology", "computer", "IOT", "connection", "TCP", "Internet", "Switch", "Router", "Cable", "LAN", "WAN", "wireless", "protocol", "ports"]

# Ask the user what they want to see
choice = input("Do you want to see (1) only URLs with matches, or (2) both found and not found words for each URL? Enter 1 or 2: ")

# Loop through each URL and execute based on choice
if choice == "1":
    print("\nURLs with matches to the keywords:")
    for url in urls:
        found, _ = search_for_words(url, search_words)
        if found:
            print(f"- {url}")
elif choice == "2":
    for url in urls:
        found, not_found = search_for_words(url, search_words)
        print(f"\nResults for {url}:")
        print("Found:")
        for word in found:
            print(f"- {word}")
        print("Not Found:")
        for word in not_found:
            print(f"- {word}")
else:
    print("Invalid choice. Please enter 1 or 2.")
