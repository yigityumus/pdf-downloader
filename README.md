# PDF Downloader

The PDF Downloader is a Python script designed to extract PDF files from web pages and organize them into folders based on the URLs of the web pages. It uses the requests library to fetch web pages, BeautifulSoup for parsing HTML, and urllib to handle URL-related operations. The script can be executed either directly or within a Docker container.

## Description

The PDF Downloader script provides a convenient way to download PDF files from web pages that contain links to such files. It extracts links from a specified web page, filters out those links that lead to PDF files, and then downloads the PDF files into appropriately named folders.

## Usage

To use the PDF Downloader:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Choose one of the following methods:

### Method 1: Using Docker (Recommended)

- Ensure Docker is installed on your system.
- Build the Docker image using the command: `docker build -t pdf_downloader .`
- Run the Docker container: `docker run -v $(pwd)/pdf_files:/app/pdf_files pdf_downloader`

### Method 2: Without Docker

#### For Linux and macOS:

- Install Python 3.x and pip if not already installed.
- Optionally, create and activate a Python virtual environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- Install the required Python packages: `pip install -r requirements.txt`
- Run the main script: `python main.py`

#### For Windows:

- Install Python 3.x and pip if not already installed.
- Optionally, create and activate a Python virtual environment:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
- Install the required Python packages: `pip install -r requirements.txt`
- Run the main script: `python main.py`

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to fork it and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
