import os
import re
from tqdm import tqdm

def convert_to_jinja(html):
    # Define regular expressions to match paths and URLs
    path_pattern = r'src\s*=\s*["\'](.*?)["\']'
    url_pattern = r'href\s*=\s*["\'](.*?)["\']'

    # Replace paths and URLs with appropriate Jinja2 format
    html = re.sub(path_pattern, r'src="{{ url_for(\'static\', filename=\1) }}"', html)
    html = re.sub(url_pattern, r'href="{{ url_for(\'static\', filename=\1) }}"', html)

    return html

def process_file(file_path):
    # Read HTML file
    with open(file_path, 'r') as f:
        html_content = f.read()

    # Convert HTML to Jinja2 format
    jinja_html = convert_to_jinja(html_content)

    # Write converted HTML back to the file
    with open(file_path, 'w') as f:
        f.write(jinja_html)

def main():
    # Ask user for directory containing HTML files
    html_dir = input("Enter the directory containing HTML files: ")

    # Get list of HTML files
    html_files = [filename for filename in os.listdir(html_dir) if filename.endswith('.html')]

    with tqdm(total=len(html_files), desc="Converting HTML files...", unit="file") as pbar:
        for filename in html_files:
            file_path = os.path.join(html_dir, filename)
            process_file(file_path)
            pbar.update(1)

    print("[green]Conversion completed!")

if __name__ == "__main__":
    main()
