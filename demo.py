"""Demonstrate the available classes."""
from scrapy.crawler import CrawlerProcess
from scrapy_athlinks import RaceSpider, AthleteItem, RaceItem

# Make settings for two separate output files: one for athlete data,
# one for race metadata.
settings = {
  'FEEDS': {
    # Athlete data. Inside this file will be a list of dicts containing
    # data about each athlete's race and splits.
    'athletes.json': {
      'format':'json',
      'overwrite': True,
      'item_classes': [AthleteItem],
    },
    # Race metadata. Inside this file will be a list with a single dict
    # containing info about the race itself.
    'metadata.json': {
      'format':'json',
      'overwrite': True,
      'item_classes': [RaceItem],
    },
  }
}
process = CrawlerProcess(settings=settings)

# Crawl results for the 2022 Leadville Trail 100 Run
process.crawl(RaceSpider, 'https://www.athlinks.com/event/33913/results/Event/1018673/')
process.start()