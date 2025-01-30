import os

def load_chapters():
    """Load text files from the directory specified by TARGET_BOOK_CHAPTERS environment variable."""
    
    import os
    from dotenv import load_dotenv
    
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
                chapters[filename] = file.read()
    
    return chapters

if __name__ == "__main__":
    chapters = load_chapters()
    for chapter_name, content in chapters.items():
        print(f"Chapter: {chapter_name}")
        print(content[:100])  # Print the first 100 characters of each chapter
