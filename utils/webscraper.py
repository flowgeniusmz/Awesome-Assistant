import requests
from bs4 import BeautifulSoup
import os

def utils_webscraper_singleURL(varURL):
  response = requests.get(varURL)
  content = response.content
  
  return 

def utils_webscraper_multiURL_indexURL(varIndexURL, varBaseURL):
    
  # The base URL
  base_url = "https://saylordotorg.github.io/text_risk-management-for-enterprises-and-individuals/"
  
  # Fetch the index.html
  index_url = base_url + "index.html"
  index_response = requests.get(index_url)
  index_html = index_response.text
  
  # Parse the HTML to find URLs
  soup = BeautifulSoup(index_html, 'html.parser')
  relative_urls = [a['href'] for a in soup.find_all('a', href=True)]
  
  # Resolve relative URLs to absolute URLs
  absolute_urls = [base_url + url for url in relative_urls]
  
  # Ensure /data directory exists
  data_directory = '/mnt/data'
  if not os.path.exists(data_directory):
      os.makedirs(data_directory)
  
  # Visit each URL, scrape content, and save to file
  contents = []
  for url in absolute_urls:
      try:
          page_response = requests.get(url)
          page_content = page_response.text
          contents.append(page_content)  # Add to contents array
  
          # Save content to a text file
          file_name = os.path.join(data_directory, url.split('/')[-1] + '.txt')
          with open(file_name, 'w', encoding='utf-8') as file:
              file.write(page_content)
  
      except requests.RequestException as e:
          print(f"Error fetching {url}: {e}")
  # At this point, 'contents' contains the HTML content of each page
  # and each page's content is saved as a text file in the /data directory
  return contents

def utils_webscraper_multiURL_listURL(varURLList):
  contents = []
  for varurl in varURLList:
    try:
      response = requests.get(varurl)
      content = response.text
      contents.append(content)
    except requests.RequestException as e:
      contents.append(e)
  return contents


    
