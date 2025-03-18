import csv
class BookScraperPipeline:
    def open_spider(self, spider):
        self.file = open('books_data.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['Category', 'Title', 'Price', 'Availability', 'Rating', 'image_url'])

    def process_item(self, item, spider):
        self.writer.writerow([
            item['category'],
            item['title'],
            item['price'],
            item['availability'],
            item['rating'],
            item['image_url']
        ])
        return item

    def close_spider(self, spider):
        self.file.close()
