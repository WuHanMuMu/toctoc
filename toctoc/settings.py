# -*- coding: utf-8 -*-

# Scrapy settings for toctoc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'toctoc'

SPIDER_MODULES = ['toctoc.spiders']
NEWSPIDER_MODULE = 'toctoc.spiders'

# THE FILE YOU WANT TO COMPARE

COMPARE_FILE = './out.csv'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'toctoc (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     ":authority": "www.toctoc.com",
#     ":method": "POST",
#     ":path": "/api/mapa/getpropiedades",
#     ":scheme":"https",
#     "accept": "application/json, text/javascript, */*; q=0.01",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "zh-CN,zh;q=0.9",
#     # "content-length": 724,
#     "content-type": "application/json",
#     # "cookie": 'X-DATA=f7811709-37ff-4670-9bfe-7c04ac3ca80f; __RequestVerificationToken=d-iMIL0Q7h5Fglrt-zN6CuLn9u85Mgy5Md68lwiBaP3CA7fy9mPDS2AQ34QOOOCH1fhLWWfS1wmltj9a_C_yoozbSwMhzwY84gwR8fbB_Nw1; optimizelyEndUserId=oeu1525136541039r0.7623129735413938; optimizelySegments=%7B%222204271535%22%3A%22gc%22%2C%222215970531%22%3A%22false%22%2C%222232940041%22%3A%22referral%22%7D; optimizelyBuckets=%7B%7D; _ga=GA1.2.1482230272.1525136541; _gid=GA1.2.1051418429.1525136541; __insp_wid=2107690165; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudG9jdG9jLmNvbS9zZWFyY2gvaW5kZXgyLz9kb3JtaXRvcmlvcz0wJmFtcDtiYW5vcz0wJmFtcDtzdXBlcmZpY2llRGVzZGU9MCZhbXA7c3VwZXJmaWNpZUhhc3RhPTAmYW1wO3ByZWNpb0Rlc2RlPTAmYW1wO3ByZWNpb0hhc3RhPTAmYW1wO21vbmVkYT1VRiZhbXA7dGlwb0FycmllbmRvPWZhbHNlJmFtcDt0aXBvVmVudGFVc2Fkbz10cnVlJmFtcDt0aXBvVmVudGFOdWV2bz1mYWxzZSZhbXA7dGlwb1VsdGltYXNWZW50YXM9ZmFsc2UmYW1wO2Nhc2FEZXB0bz0xJmFtcDtvcmRlbmFyUG9yTW9uZWRhPVVGQ0xQJmFtcDtvcmRlbmFyRGVzYz1mYWxzZSZhbXA7b3JkZXJuYXJQb3JGZWNoYVB1YmxpY2FjaW9uPWZhbHNlJmFtcDtvcmRlcm5hclBvclN1cGVyZmljaWU9ZmFsc2UmYW1wO29yZGVybmFyUG9yUHJlY2lvPWZhbHNlJmFtcDtwYWdpbmE9MSZhbXA7dGV4dG9CdXNxdWVkYT1wcm92aWRlbmNpYSZhbXA7dGlwb1Zpc3RhPWxpc3RhJmFtcDt2aWV3cG9ydD0tMzQuMjg3ODE0OCUyQy03MS43MDg4MTAyMDAwMDAwMiUyQy0zMi45MTk0NTElMkMtNjkuNzY4OTk0MzAwMDAwMDMmYW1wO2NvbXVuYT1Qcm92aWRlbmNpYSZhbXA7cmVnaW9uPVJlZ2klQzMlQjNuJTIwTWV0cm9wb2xpdGFuYSZhbXA7YXRyaWJ1dG9zPSZhbXA7aWRsZT1mYWxzZSZhbXA7em9vbT0xMyZhbXA7YnVzY2FuZG89ZmFsc2UmYW1wO3Z1ZWx2ZUJ1c2Nhcj1mYWxzZSZhbXA7ZGlidWphUG9saWdvbm89dHJ1ZSZhbXA7cmVzZXRNYXBhPXRydWUmYW1wO2FuaW1hY2lvbj1mYWxzZSZhbXA7aWRab25hSG9tb2dlbmVhPTAmYW1wO2VzUHJpbWVyYUJ1c3F1ZWRhPWZhbHNl; __insp_targlpt=QnVzY2FyIHkgY29tcHJhciBjYXNhIHBvciBtYXBhIGVuIFRvYyBUb2M%3D; __insp_norec_sess=true; NPS_93546e30_last_seen=1525137064458; X-DATA-NPSW={"CantidadVisitas":1,"FechaCreacion":"2018-04-30T22:02:19.8336624-03:00","FechaUltimoIngreso":"2018-04-30T22:14:40.4448643-03:00","Detalles":[{"TipoVistaNPS":2,"Cantidad":4,"FechaUltimoIngreso":"2018-04-30T22:14:40.4448643-03:00"},{"TipoVistaNPS":1,"Cantidad":1,"FechaUltimoIngreso":"2018-04-30T22:03:20.4249595-03:00"},{"TipoVistaNPS":3,"Cantidad":3,"FechaUltimoIngreso":"2018-04-30T22:14:05.6806571-03:00"}]}; mp_29ae90688062e4e2e6d80b475cef8685_mixpanel=%7B%22distinct_id%22%3A%20%221631939188a5a0-0f03580850d109-3961430f-1fa400-1631939188baf6%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.freelancer.com%2Fdashboard%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.freelancer.com%22%7D; __insp_slim=1525137281382',
#     "origin": "https://www.toctoc.com",
#     "referer": "https://www.toctoc.com/search/index2/?dormitorios=0&banos=0&superficieDesde=0&superficieHasta=0&precioDesde=0&precioHasta=0&moneda=UF&tipoArriendo=false&tipoVentaUsado=true&tipoVentaNuevo=false&tipoUltimasVentas=false&casaDepto=1&ordenarPorMoneda=UFCLP&ordenarDesc=false&ordernarPorFechaPublicacion=false&ordernarPorSuperficie=false&ordernarPorPrecio=false&pagina=1&textoBusqueda=Marchant%20Pereira&tipoVista=mapa&viewport=-33.4546322%2C-70.61415569999997%2C-33.4251101%2C-70.60690369999998&comuna=&region=&idle=false&buscando=true&vuelveBuscar=false&dibujaPoligono=false&resetMapa=true&animacion=false&idZonaHomogenea=0&esPrimeraBusqueda=false",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
#     "x-requested-with":"XMLHttpRequest",
#     # "x-xsrf-token": "c0XJvq6rTwZU7oqPM4LsGpbp_pNfBQIZzFUgyPZh3A-cCwV0gJE_gw7cSAGAqM-wrE-dbikAiw2eVy-SN9mq490jroUyAyjfraQcnaaTbcw1",
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'toctoc.middlewares.ToctocSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'toctoc.middlewares.ToctocDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'toctoc.pipelines.ToctocPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
