from functions import (
    extract_links,
    process_link,
    download_pdf_from_links
)


if __name__ == '__main__':
    params = {
        'link': "https://www.mavicompany.com/en/menu/investor-relations",
        'output_folder': 'pdf_files'
    }
    
    text = process_link(params['link'])
    links_to_scrape = extract_links(params['link'], text)

    download_pdf_from_links(links_to_scrape, params['output_folder'])