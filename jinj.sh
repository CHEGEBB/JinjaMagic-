#!/bin/bash

# Function to convert HTML files to Jinja2 format
convert_to_jinja() {
    local file="$1"
    sed -i '' -E 's/src\s*=\s*["'"'"'](.*?)["'"'"']/src="{{ url_for(\'static\', filename=\1) }}"/g' "$file"
    sed -i '' -E 's/href\s*=\s*["'"'"'](.*?)["'"'"']/href="{{ url_for(\'static\', filename=\1) }}"/g' "$file"
}

# Main function
main() {
    # Ask user for directory containing HTML files
    read -p "Enter the directory containing HTML files: " html_dir

    # Convert HTML files to Jinja2 format
    find "$html_dir" -type f -name "*.html" | while read -r file; do
        convert_to_jinja "$file"
    done

    echo "Conversion completed!"
}


main
