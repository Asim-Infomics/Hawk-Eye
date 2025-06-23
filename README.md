# Hawk-Eye
This tool allows you to search the dark web for specific keywords, fetch relevant .onion links, and crawl them for additional information. It leverages the Tor network to ensure anonymity and privacy while performing searches on onion sites. More actions
Hawk Eye -  A Dark Web Search Tool
This tool allows you to search for .onion links on the dark web using a Tor network connection. It uses the Ahmia search engine to find .onion links based on a user-specified keyword. After retrieving the search results, the tool offers the option to crawl the resulting links and save them to a file.

Prerequisites
Before you can run this tool, ensure that you have the following software installed:

Python 3.x: Make sure you have Python 3 or above installed. 
Tor: You need to have the Tor service running on your local machine. The tool uses a SOCKS5 proxy to connect to Tor.
FoxyProxy for Firefox: A browser extension that configures Firefox to use Tor as a proxy.
Required Python Libraries:
requests
bs4 (BeautifulSoup)
urllib
You can install the required libraries using pip:


pip install requests beautifulsoup4
Setting Up Tor
Follow these steps to configure Tor and FoxyProxy:

Step 1: Install Tor
Download and install the Tor software from Tor Project.
Run the Tor service.
Step 2: Install FoxyProxy Extension
Open Firefox.
Go to the FoxyProxy Add-on page and click Add to Firefox.
Click Add when prompted.
Step 3: Configure FoxyProxy
Click on the FoxyProxy icon in Firefox and select Options.
Add a new proxy configuration:
Title: Tor (or any name you prefer).
Proxy Type: SOCKS5.
IP Address: 127.0.0.1.
Port: 9150 (or 9050 if using a different setup).
Enable the option SOCKS v5 Proxy DNS when available.
Save the settings.
Step 4: Test Tor Connection
Visit https://check.torproject.org to confirm that you are connected to Tor. If the page shows "Congratulations. This browser is configured to use Tor.", you're all set.
Running the Tool
Start the Tor Service: Ensure that Tor is running on your machine.
Configure FoxyProxy: Ensure that the FoxyProxy extension in Firefox is set to use the Tor proxy configuration you created.
Run the Python Script: Execute the Python script to start searching the dark web.
python hawk_eye.py
Interacting with the Tool
Upon running the script, the tool will ask you to input a search keyword to search for on the Tor network.
It will display the search results with .onion links found on Ahmia.
You will then be asked if you want to crawl these results to retrieve more detailed URLs.
Finally, the script will save all valid URLs to a text file named dark_web_links.txt.
Example Output:
Hawk Eye by asim-infomics
=====================
Testing Tor connection...
Connected to Tor! Current IP: "Your Tor IP here"
Enter the keyword to search on the dark web: "bitcoin"

Searching for 'bitcoin' on the dark web...
Debug URL: https://ahmia.fi/search/?q=bitcoin
Search Results:
http://example1.onion
http://example2.onion

Do you want to crawl the results? (yes/no): yes

Crawling: http://example1.onion
Title: Example Onion Site 1
Crawling: http://example2.onion
Title: Example Onion Site 2

Saved 2 URLs to hawk_eye.txt
File Output
The list of .onion URLs will be saved in a file called hawk_eye.txt. Each URL will be saved on a new line, and the file will be created in the same directory as the script.

Notes
Tor Setup: Make sure that Tor is running and that FoxyProxy is properly configured in Firefox. The script relies on the Tor network to retrieve results and crawl .onion sites.
Crawler Limitations: The script may not be able to crawl certain .onion sites due to connection issues, misconfigurations, or access restrictions.
Ethical Considerations: Always use caution when browsing the dark web. While some content is legitimate, others may be harmful or illegal. Make sure you're in compliance with all applicable laws.
Troubleshooting
Tor Not Connecting: If you're unable to connect to the Tor network, make sure that the Tor service is running and that the SOCKS5 proxy is configured correctly in FoxyProxy.
Timeouts: If you're getting timeouts while crawling .onion sites, try increasing the timeout value in the session.get() requests.
Invalid URLs: If the script skips URLs with the error "Invalid URL skipped", check that the URLs returned by the search engine are properly formatted.

