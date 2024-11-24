import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

def get_tor_session():
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return session

def search_onion(session, query, limit):
    """
    Searches for a keyword on an onion search engine and returns the found .onion links.
    Allows advanced search queries with operators like AND, OR, NOT, and quotes.
    """
    print(f"Searching for '{query}' on the dark web...")
    search_url = f"https://ahmia.fi/search/?q={query}"  # Clear-web search engine URL
    
    # Debugging the URL
    print(f"Debug URL: {search_url}")
    
    try:
        response = session.get(search_url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True) if ".onion" in a['href']]
        
        # If limit is provided, slice the list of links
        if limit != "all":
            links = links[:int(limit)]
        
        return links
    except Exception as e:
        print(f"Error during search: {e}")
        return []

def crawl_onion(session, base_url, url, keywords):
    """
    Crawls an onion link to fetch its title and checks for keyword relevance.
    Returns the title and URL if the content matches the keywords.
    """
    # If the URL is relative, make it absolute by joining with base URL
    if url.startswith("/"):
        url = urljoin(base_url, url)
    
    print(f"Crawling: {url}")
    try:
        if not url.startswith("http://") and not url.startswith("https://"):
            print(f"Invalid URL skipped: {url}")
            return None

        response = session.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No Title"
        content = soup.get_text()  # Extract the visible text on the page

        # Check for keyword relevance
        if any(keyword.lower() in content.lower() for keyword in keywords):
            print(f"Title: {title} - Relevant Content Found")
            return title, url
        else:
            print(f"Title: {title} - Irrelevant Content")
            return None
    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return None

def save_urls_to_file(urls, keyword):
    """
    Saves the list of URLs and their titles to a text file with the current date, time, and keyword in the filename.
    """
    # Sanitize the keyword to remove invalid characters for filenames
    sanitized_keyword = "".join(c if c.isalnum() or c in (' ', '_', '-') else "_" for c in keyword).strip()
    current_time = time.strftime("%Y%m%d_%H%M%S")  # Get current time in YYYYMMDD_HHMMSS format
    filename = f"hawk_eye_{sanitized_keyword}_{current_time}.txt"
    with open(filename, "w") as file:
        for title, url in urls:
            file.write(f"Title: {title}\nURL: {url}\n\n")
    print(f"Saved {len(urls)} URLs to {filename}")

if __name__ == "__main__":
    print("""
         █████╗         ██╗    
        ██╔══██╗        ██║   
        ███████║███████ ██║    
        ██╔══██║        ██║    
        ██║  ██║        ██║    
        ╚═╝  ╚═╝        ╚═╝    
    """)
    print ("asim-infomics")
    print("==============")

    # Create a Tor session
    session = get_tor_session()

    # Test Tor connection
    try:
        print("Testing Tor connection...")
        tor_ip = session.get("http://httpbin.org/ip", timeout=10).text
        print(f"Connected to Tor! Current IP: {tor_ip}")
    except Exception as e:
        print(f"Error connecting to Tor: {e}")
        exit()

    # Input keyword to search
    keyword = input("Enter the keyword to search on the dark web (use AND, OR, NOT, quotes for advanced search): ").strip()

    # Input the number of URLs to fetch
    url_limit = input("Enter the number of URLs to fetch (or 'all' for unlimited): ").strip().lower()

    # Perform the search
    links = search_onion(session, keyword, url_limit)

    # Display search results
    if links:
        print(f"\nFound {len(links)} URLs:")
        for link in links:
            print(link)
    else:
        print("No results found.")

    # Ask if user wants to crawl the results
    crawl_choice = input("\nDo you want to crawl the results? (yes/no): ").strip().lower()
    valid_links = []
    if crawl_choice == 'yes':
        keywords = keyword.split()  # Split the keyword into a list of words for relevance checking
        base_url = "https://ahmia.fi"  # The base URL for Ahmia, change if using a different source
        for link in links:
            crawled_url = crawl_onion(session, base_url, link, keywords)
            if crawled_url:
                valid_links.append(crawled_url)

    # Save the URLs and their titles to a text file with current date-time and keyword in the filename
    if valid_links:
        save_urls_to_file(valid_links, keyword)
    else:
        print("No valid URLs found to save.")
