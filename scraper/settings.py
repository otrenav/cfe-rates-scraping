
# DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

BOT_NAME = 'iberdrola'
SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1
CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 5

AUTOTHROTTLE_TARGET_CONCURRENCY = 0.2
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = False

DOWNLOADER_MIDDLEWARES = {
    # 'scraper.middlewares.UserAgentsMiddleware': 400,
    # 'scraper.middlewares.ProxiesMiddleware': 410,
    'scraper.middlewares.SeleniumMiddleware': 950
}
