import arxiv
import requests
import pandas as pd
import os
import logging

# Set up logging
logging.basicConfig(
    filename='arxiv_search.log',
    filemode='w',  # Overwrite the log file each time
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define the search keyword
keyword = 'Australia'

# Directory to save the PDF files
pdf_dir = 'files'
os.makedirs(pdf_dir, exist_ok=True)

# Log the search keyword
logging.info(f"Searching for papers with keyword: {keyword}")


# Query arXiv using the arxiv library
search = arxiv.Search(
    query=f'ti:{keyword}',  # Search across all fields for the keyword
    #query=f'all:{keyword}',  # Search across all fields for the keyword
    max_results=10,  # Adjust the number of results as needed
    sort_by=arxiv.SortCriterion.Relevance
)

# Initialize a list to store metadata
papers_metadata = []

# Initialize a counter for the number of search results
num_results = 0

# Iterate through the search results
for result in search.results():
    num_results += 1
    title = result.title
    authors = ', '.join(author.name for author in result.authors)
    published_date = result.published.strftime('%Y-%m-%d')
    abstract = result.summary
    pdf_url = result.pdf_url
    entry_id = result.entry_id

    # Log the paper details before downloading
    logging.info(f"Processing paper: {title}, Authors: {authors}, Published: {published_date}")

    if pdf_url:
        try:
            # Download the PDF file
            pdf_response = requests.get(pdf_url)
            pdf_response.raise_for_status()  # Raise an error for bad responses

            # Create a valid filename
            pdf_filename = '{}.pdf'.format(title[:50].replace(" ", "_").replace("/", "_"))
            pdf_path = os.path.join(pdf_dir, pdf_filename)

            # Save the PDF file locally
            with open(pdf_path, 'wb') as pdf_file:
                pdf_file.write(pdf_response.content)

            # Log successful download
            logging.info(f"Successfully downloaded: {pdf_filename}")

            # Append metadata to the list
            papers_metadata.append({
                'Title': title,
                'Authors': authors,
                'Published Date': published_date,
                'Abstract': abstract,
                'PDF Path': pdf_path,
                'Entry ID': entry_id
            })

        except requests.exceptions.RequestException as e:
            # Log any download errors
            logging.error(f"Failed to download {title}: {e}")

    # Convert metadata list to DataFrame
    df = pd.DataFrame(papers_metadata)

    # Display the DataFrame
    print(df)

    # Print the number of search results
    print(f"Number of search results: {num_results}")

    # Optionally save DataFrame to CSV file
    csv_file_path = 'arxiv_papers_summary.csv'
    df.to_csv(csv_file_path, index=False)

    print(f"Metadata saved to {csv_file_path}")

    # Log the completion of the process
    logging.info(f"Process completed. Total papers processed: {num_results}")
