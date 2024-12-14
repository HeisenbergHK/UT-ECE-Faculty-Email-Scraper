# UT-ECE Faculty Email Scraper

A Python-based tool for crawling and scraping publicly available email addresses of faculty members listed on the University of Toronto Electrical and Computer Engineering (ECE) Faculty Directory.

### This project includes two scripts:
1. __Crawler:__ Downloads the HTML pages of individual faculty profiles.
2. __Scraper:__ Extracts faculty names and email addresses from the saved HTML files and saves the data into a CSV file.

## Features
- Automates the process of crawling and scraping faculty member data.
- Saves individual faculty profile pages for offline access.
- Extracts names and email addresses, storing them in a structured CSV format.

## Installation
1.	Clone the repository:
```
git clone https://github.com/yourusername/UT-ECE-Faculty-Email-Scraper.git
cd UT-ECE-Faculty-Email-Scraper
```

2.	Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
### 1.	Run the crawler script:
This script crawls the faculty directory and saves each faculty member’s profile as an HTML file.
```
python crawler.py
```
The HTML files will be saved in the faculty_members directory.

### 2.	Run the scraper script:
This script processes the saved HTML files, extracts faculty names and email addresses, and saves the data in a CSV file.
```
python scraper.py
```
The extracted data will be saved in Faculty_Emails.csv.

## Folder Structure
```
UT-ECE-Faculty-Email-Scraper/
│
├── crawler.py             # Crawler script
├── scraper.py             # Scraper script
├── requirements.txt       # Dependencies
├── Faculty_Emails.csv     # Output CSV file with extracted data
├── faculty_members/       # Folder containing downloaded HTML files
│   ├── member1.html
│   ├── member2.html
│   └── ...
└── README.md              # Project documentation
```

## Output
The extracted data will be saved in a CSV file named Faculty_Emails.csv in the following format:

| Name                | Email                  |
|---------------------|------------------------|
| Dr. John Doe        | john.doe@utoronto.ca  |
| Dr. Jane Smith      | jane.smith@utoronto.ca|

## Disclaimer

This project is intended for educational and research purposes only.

- Ensure you comply with the website’s Terms of Service and applicable privacy laws.
- Do not use this tool for unsolicited communication or other unethical activities.

---
Feel free to reach out or contribute if you’d like to improve this project!
