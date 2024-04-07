import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from typing import List


def extract_links(url: str, text: str='') -> List[str]:
    """
    Extracts links from a webpage containing a specified text.

    Args:
        url (str): The URL of the webpage to extract links from.
        text (str): The text to search for in the links.

    Returns:
        List[str]: A list of extracted links.
    """
    links = []
    try:
        # Raise an exception for HTTP errors
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all links that contain the specified text
        for link in soup.find_all('a', href=True):
            href = link['href']
            if text in href:
                if href.startswith("http"):  # Check if it's an absolute URL
                    links.append(href)
                else:  # Convert relative URL to absolute URL
                    links.append(urljoin(url, href))
    except requests.HTTPError as e:
        print("Failed to fetch the webpage: ", e)
    except Exception as e:
        print("Failed to fetch the webpage: ", e)
    
    # Remove duplicates and return the list
    return list(set(links))



def process_link(link: str) -> str:
    """
    Extracts the last part of the URL.

    Args:
        link (str): The URL.

    Returns:
        str: The last part of the URL.
    """
    return urlparse(link).path.split('/')[-1]


def download_pdf_from_links(links: List[str], output_folder: str) -> None:
    """
    Downloads PDF files from a list of links.

    Args:
        links (List[str]): A list of URLs to download PDF files from.
        output_folder (str): The folder where the PDF files will be saved.

    Returns:
        None
    """
    for index, link in enumerate(links, start=1):
        print(f"Processing {index}/{len(links)} ...")
        # Skip non-HTTP links
        if not link.startswith("http"):
            continue
        try:
            # Raise an exception for HTTP errors
            response = requests.get(link)
            response.raise_for_status()  
            
            # Get all the links that ends with '.pdf' a.k.a. All pdf files
            soup = BeautifulSoup(response.content, 'html.parser')
            pdf_links = soup.find_all('a', href=lambda href: (href and href.endswith('.pdf')))
            
            # Get the folder name from the last part of the URL
            folder_name = process_link(link)

            # Create the folder if it doesn't exist
            folder_path = os.path.join(output_folder, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Download each PDF file
            for index, pdf_link in enumerate(pdf_links, start=1):
                pdf_url = urljoin(link, pdf_link['href'])
                filename = os.path.join(folder_path, os.path.basename(pdf_url))

                print(f"Downloading {index}/{len(pdf_links)}: {filename}")
                with open(filename, 'wb') as f:
                    f.write(requests.get(pdf_url).content)
            
            # Remove empty folders
            if not os.listdir(folder_path):
                os.rmdir(folder_path)

        except requests.HTTPError as e:
            print("Failed to fetch the webpage:", e)