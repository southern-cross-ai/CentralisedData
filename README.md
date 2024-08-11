# Academic Paper Dataset

# Arxiv papers

## Announcement
- Copyright: The crawling used Arxiv API to get the papers
- Repository public available

## Overview of Arxiv

- What this dataset is about?
  - The first commit include the code for arXiv pdf papers including "Australia" keyword in titles.
- Where does the dataset come from?
  - Axiv official site
- What timespan is the data collected from?
  - 1993-2024

## Data Source / Credit

- Where does this dataset come from?
  - Crawling.
- What license is the dataset under?
  - Not allowed for commercial use, modification, publication.

## Dataset Structure / Size / Type

- What format of data is inside?
  - pdf
- What's the size of data for each topic/type/category?
  - 5GB in total
 
## How to Access Dataset

- Huggiface url

## Code structure
files: include the .pdf of papers

text_files: include the text files of .pdf papers (can be optimized for better text extraction)

arxiv_crawler.py: the code to crawl the arXiv papers. You might modify line #29 to get more papers but notify 
that if you do not run it in one shot you might get the same papers again.

pdf2txt.py: the code to extract text from .pdf files. You might need to install pdfminer.six library to run it.

## More paper sites for tryout
PubMed Central (PMC)

Directory of Open Access Journals (DOAJ)

CORE

Semantic Scholar


## License of Your Repo

This repository is licensed under [license name](License content URL).

How to choose your license: 

- [Licensing a repository - GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [Choose an open source license - Choose a License](https://choosealicense.com/)
- [License Selector - ufal.github.io](https://ufal.github.io/public-license-selector/)

---

## What else can you do in your repo?

- On the right column that shows repo information, click the gear icon ⚙️ to set up your repo:
  - Description: A short sentence about the repo
  - Website: The link to the dataset's official webpage 
  - Topics: Help others to find your repo. For example, setting "corpus", "australia", "dataset" can help people who are looking for Australian datasets or corpora.

- Find and add `.gitignore` template:
  - [gitignore - GitHub](https://github.com/github/gitignore)

- How to contribute to your repo?
  
  - Provide your contact information here.
  
  

