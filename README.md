# Jumia Ecommerce Flash Sales Scraper
Welcome to the Jumia Ecommerce Flash Sales Scraper project! This web scraper, built using Scrapy, is designed to crawl the Flash Sales section of the Jumia Ecommerce site, extracting valuable data for analysis.

# Project Overview
The primary goal of this project is to collect data from Jumia's Flash Sales section, providing insights into the products offered during special promotions. The scraper navigates the site, extracts relevant information, and stores it in two formats: "products.csv" for easy tabular analysis and "products.json" for structured data storage.

# Usage
## Prerequisites
- Python 3.x
- Scrapy

## Installation
1. Clone the repository:
"git clone https://github.com/your-username/jumia-flash-sales-scraper.git"
"cd jumia-flash-sales-scraper"

2. Install dependencies:
pip install -r requirements.txt

## Running the Scraper
Execute the following command to start the scraping process:
"scrapy crawl flash_sales -o products.csv -t csv"

This command will crawl the Flash Sales section and save the data in both CSV and JSON formats.

# Data Output
The scraped data is saved in two formats in the project repo:
- products.csv: Tabular format for easy analysis.
- products.json: Structured JSON format for flexibility and data integrity.
