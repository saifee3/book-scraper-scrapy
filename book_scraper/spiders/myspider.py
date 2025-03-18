
import scrapy
from book_scraper.items import BookScraperItem
from urllib.parse import urljoin

class BookSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["books.toscrape.com"]
    
    start_urls = [
        "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
        "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
        "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html",
        "https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html",
        "https://books.toscrape.com/catalogue/category/books/childrens_11/index.html",
        "https://books.toscrape.com/catalogue/category/books/religion_12/index.html",
        "https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
        "https://books.toscrape.com/catalogue/category/books/music_14/index.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/index.html",
        "https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html",
        "https://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html",
        "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html",
        "https://books.toscrape.com/catalogue/category/books/new-adult_20/index.html",
        "https://books.toscrape.com/catalogue/category/books/paranormal_24/index.html",
        "https://books.toscrape.com/catalogue/category/books/art_25/index.html",         
        "https://books.toscrape.com/catalogue/category/books/psychology_26/index.html",
        "https://books.toscrape.com/catalogue/category/books/autobiography_27/index.html",
        "https://books.toscrape.com/catalogue/category/books/parenting_28/index.html",
        "https://books.toscrape.com/catalogue/category/books/humor_30/index.html",
        "https://books.toscrape.com/catalogue/category/books/horror_31/index.html",
        "https://books.toscrape.com/catalogue/category/books/history_32/index.html",
        "https://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html",
        "https://books.toscrape.com/catalogue/category/books/business_35/index.html",
        "https://books.toscrape.com/catalogue/category/books/spirituality_39/index.html",
    ]

    def parse(self, response):
        category = response.css('h1::text').get()
        books = response.css('article.product_pod')
        
        for book in books:
            item = BookScraperItem()
            item['category'] = category
            item['title'] = book.css('h3 a::attr(title)').get()
            item['price'] = book.css('p.price_color::text').get()
            availability_parts = book.css('p.availability::text').getall()
            item['availability'] = ''.join(availability_parts).strip()
            rating_class = book.css('p.star-rating::attr(class)').get()
            item['rating'] = rating_class.split()[-1]
            relative_image_url = book.css('a img::attr(src)').get()
            item['image_url'] = urljoin("https://books.toscrape.com/", relative_image_url)
            
            yield item
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)