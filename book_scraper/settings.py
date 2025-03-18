# Project name and settings
BOT_NAME = 'book_scraper'
SPIDER_MODULES = ['book_scraper.spiders']
NEWSPIDER_MODULE = 'book_scraper.spiders'

# Crawl responsibly by identifying yourself and your website
USER_AGENT = 'book_scraper (+http://www.books.toscrape.com)'


# Disable cookies by default
COOKIES_ENABLED = False

# Enable Telnet Console for debugging
TELNETCONSOLE_ENABLED = True

# Default request headers
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# Configure item pipelines
ITEM_PIPELINES = {
    'book_scraper.pipelines.BookScraperPipeline': 300,
}

# Enable and configure the AutoThrottle extension
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable logging
LOG_ENABLED = True
LOG_LEVEL = 'INFO'

# Enable feed exports
FEED_FORMAT = 'json'
FEED_URI = 'books.json'