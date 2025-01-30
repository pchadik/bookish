import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

def html_to_text(html_content):
    """Convert HTML content to plain text."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

def load_chapters():
    """Load text files from the directory specified by TARGET_BOOK_CHAPTERS environment variable."""
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the target directory from the environment variable
    target_directory = os.getenv('TARGET_BOOK_CHAPTERS')
    
    if not target_directory:
        raise ValueError("TARGET_BOOK_CHAPTERS environment variable is not set.")
    
    chapters = {}
    
    # Iterate over all files in the target directory
    for filename in os.listdir(target_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(target_directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
                chapters[filename] = html_to_text(html_content)
    
    return chapters

if __name__ == "__main__":
    chapters = load_chapters()
    for chapter_name, content in chapters.items():
        print(f"Chapter: {chapter_name}")
        print(content[:100])  # Print the first 100 characters of each chapter
