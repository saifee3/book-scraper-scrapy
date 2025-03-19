# 📚 Book Scraper using Scrapy
![image](https://github.com/user-attachments/assets/1677293a-9b6b-4b4c-872b-c66008442f34)

![Scrapy](https://img.shields.io/badge/Scrapy-2.11%2B-blue?logo=scrapy&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8%2B-green?logo=python)
![Data](https://img.shields.io/badge/Data-1000%2B%20books-yellow)

A high-performance web scraper built with **Scrapy** to extract detailed book metadata from [books.toscrape.com](https://books.toscrape.com). Ideal for building book catalogs, price comparison datasets, and inventory analysis.

---

## 🛠️ Built with Scrapy

[Scrapy](https://scrapy.org/) is a fast open-source web crawling framework that provides:
- **Asynchronous processing** for high concurrency
- Built-in **XPath/CSS selector support**
- Automatic **request throttling**
- **Pipeline system** for data processing
- **Export formats** (JSON/CSV/XML) support
- **Middleware** for proxies/headers management

This project leverages Scrapy's strengths to handle pagination, relative URLs, and anti-bot protections gracefully.

---

## 📥 Installation & Setup

### Requirements
- Python 3.8+
- pip package manager
- Virtual environment (recommended)

1. **Clone Repository**:
   ```bash
   git clone https://github.com/yourusername/book-scraper.git
   cd book-scraper
   ```

2. **Create Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

📁 **requirements.txt**:
```text
Scrapy>=2.11.0
```

---

## Data Extraction Process 📝

### Inspecting the Website Structure
To effectively extract data from AliExpress or any website, it's crucial to understand the underlying HTML structure. Here's how to approach it:

1. **Open Developer Tools**: Right-click on the webpage and select "Inspect" or press `F12` to open Chrome Developer Tools.
2. **Locate Target Elements**: Find the elements containing the data you want to extract (product titles, prices, etc.).
3. **Identify Unique Selectors**: Look for unique class names, IDs, or other attributes that can be used to reliably select these elements.
4. **Consider Hierarchy**: Note the nesting of elements to create more precise selectors that reduce the chance of selecting unintended elements.

### Choosing Between XPaths and CSS Selectors
Both XPaths and CSS selectors have their strengths:
- **CSS Selectors**: Generally faster and more readable, especially for simpler selections. Ideal when targeting elements based on class names, IDs, or direct parent-child relationships.
- **XPaths**: More powerful for complex queries, especially when needing to navigate the DOM tree in more flexible ways or when text content needs to be matched.

### Best Practices for Robust Data Extraction
- **Avoid Fragile Selectors**: Don't rely on classes or IDs that might change frequently or are used inconsistently across the site.
- **Use Relative Paths**: When using XPaths, prefer relative paths over absolute paths to make your selectors more resilient to structure changes.
- **Test Selectors Thoroughly**: Validate your selectors against multiple pages and different search results to ensure consistency.
- **Handle Dynamic Content**: Be aware of elements that might load asynchronously and implement appropriate waiting mechanisms.
- **Document Your Selectors**: Keep a record of the selectors you're using and their purpose, which will be invaluable when maintaining or updating the scraper.

---

## 🗂️ Project Structure

```
book-scraper/
├── book_scraper/
│   ├── spiders/
│   │   └── myspider.py       # Spider implementation
│   ├── items.py              # Data schema
│   ├── pipelines.py          # CSV export logic
│   └── settings.py           # Configuration
├── books_data.csv            # Sample output (CSV)
├── books.json                # Sample output (JSON)
└── requirements.txt          # Dependency list
```

---

## 🔍 Data Collection Scope

**Target Metrics**:
- Book titles and categorization
- Pricing data with currency
- Real-time stock availability
- User ratings (1-5 stars)
- Cover art URLs

**Categories Covered**:
```python
["Travel", "Mystery", "Science Fiction", "History", "Art", 
 "Business", "Psychology", "Food & Drink", "Horror", ...]  # 25+ genres
```

---

## 🏃♂️ Running the Scraper

**Basic Command**:
```bash
scrapy crawl myspider
```

**Expected Output**:
```
✔️ 2024-02-20 12:34:56 [scrapy.core.engine] INFO: Spider opened
🔄 Crawled 127 pages (45 requests/minute)
📥 Scraped 1023 items
💾 CSV/JSON files updated
```

**Output Files**:
- `books_data.csv`: Structured data for spreadsheet analysis
  ```csv
  Category,Title,Price,Availability,Rating,image_url
  "Science Fiction","Dune","£54.23","In stock (11 available)","Three","https://..."
  ```
- `books.json`: Machine-readable format for APIs
  ```json
  {
    "category": "Art",
    "title": "The Art Book", 
    "price": "£35.00",
    "availability": "In stock (3 available)",
    "rating": "Five",
    "image_url": "https://.../cover.jpg"
  }
  ```

---

## ⚙️ Customization Guide

**Modify Categories**:
```python
# myspider.py
start_urls = [
    "https://.../category/books/fantasy_19/index.html",
    # Add/remove URLs
]
```

**Change Output Format**:
```python
# settings.py
FEED_FORMAT = 'xml'  # json/csv/xml
FEED_URI = 'output.xml'
```

**Add New Fields**:
1. Update `items.py` with new field
2. Modify spider extraction logic
3. Update pipeline CSV headers

---

## 🚨 Troubleshooting

**Common Issues**:
1. **Missing Dependencies**:
   ```bash
   pip install --force-reinstall -r requirements.txt
   ```

2. **Encoding Errors**:
   - Use UTF-8 in text editors
   - Add `# -*- coding: utf-8 -*-` to file headers

3. **Blocked Requests**:
   - Increase `AUTOTHROTTLE_START_DELAY` in settings
   - Rotate User-Agents using middleware

---

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
**License**: MIT - Free for academic/commercial use with attribution.

## 🙏 Credits

- **[Scrapy](https://scrapy.org/)** - The main web scraping framework used in this project.  
- **[Python](https://www.python.org/)** - The programming language powering this scraper.  
- **[Real Python](https://realpython.com/web-scraping-with-scrapy-and-mongodb/)** - Banner image sourced from their tutorial.  
- **[Books.toscrape.com](https://books.toscrape.com/)** - The test website used for data extraction.  
- Banner Image by **Real Python** on https://realpython.com/web-scraping-with-scrapy-and-mongodb/
