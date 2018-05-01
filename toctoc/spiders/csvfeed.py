# -*- coding: utf-8 -*-
import scrapy
import re
import json
from ..items import ToctocItem


class CsvfeedSpider(scrapy.Spider):
    name = 'toctoc'
    # allowed_domains = ['toctoc']
    # start_urls = ['https://www.toctoc.com']
    api_ = 'https://www.toctoc.com/api/mapa/getpropiedades'

    def __init__(self, text=None, outfile=None,*args, **kwargs):
        super(CsvfeedSpider, self).__init__(*args, **kwargs)
        self.search_word = text
        self.outfile = outfile
        # if text:
        #     self.start_urls = ['https://www.toctoc.com/api/mapa/GetPropiedadesMapa']
        # else:
        #     self.start_urls = ['https://www.toctoc.com/api/mapa/getpropiedades']

    def start_requests(self):
        return [scrapy.Request("https://www.toctoc.com/search/index2/?dormitorios=0&banos=0&superficieDesde=0&superficieHasta=0&precioDesde=0&precioHasta=0&moneda=UF&tipoArriendo=true&tipoVentaUsado=true&tipoVentaNuevo=true&tipoUltimasVentas=false&casaDepto=undefined&ordenarPorMoneda=UFCLP&ordenarDesc=false&ordernarPorFechaPublicacion=false&ordernarPorSuperficie=false&ordernarPorPrecio=false&pagina=1&textoBusqueda=&tipoVista=lista&viewport=&region=&idle=false&buscando=true&vuelveBuscar=false&dibujaPoligono=false&resetMapa=true&animacion=false&idZonaHomogenea=0&esPrimeraBusqueda=false",
                               callback=self.parse)]

    def parse(self, response):
        req_data = self.getPayLoad()
        headers = self.getHeaders(response)
        self.log(headers)
        req = scrapy.Request(self.api_,headers=headers,body=json.dumps(req_data),callback=self.parseJson,method='POST')
        req.meta['headers'] = headers
        req.meta['first'] = True
        yield req

    def parseSetCookie(self, s):
        res = {}
        tmp = s.split(';')
        for i in tmp:
            t = i.split('=')
            res[t[0]] = t[1] if len(t) > 1 else ''
        return res

    def getHeaders(self, response):
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "content-type": "application/json",
            "cookie": '; optimizelyEndUserId=oeu1525136541039r0.7623129735413938; optimizelySegments=%7B%222204271535%22%3A%22gc%22%2C%222215970531%22%3A%22false%22%2C%222232940041%22%3A%22referral%22%7D; optimizelyBuckets=%7B%7D; _ga=GA1.2.1482230272.1525136541; _gid=GA1.2.1051418429.1525136541; __insp_wid=2107690165; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudG9jdG9jLmNvbS9zZWFyY2gvaW5kZXgyLz9kb3JtaXRvcmlvcz0wJmFtcDtiYW5vcz0wJmFtcDtzdXBlcmZpY2llRGVzZGU9MCZhbXA7c3VwZXJmaWNpZUhhc3RhPTAmYW1wO3ByZWNpb0Rlc2RlPTAmYW1wO3ByZWNpb0hhc3RhPTAmYW1wO21vbmVkYT1VRiZhbXA7dGlwb0FycmllbmRvPWZhbHNlJmFtcDt0aXBvVmVudGFVc2Fkbz10cnVlJmFtcDt0aXBvVmVudGFOdWV2bz1mYWxzZSZhbXA7dGlwb1VsdGltYXNWZW50YXM9ZmFsc2UmYW1wO2Nhc2FEZXB0bz0xJmFtcDtvcmRlbmFyUG9yTW9uZWRhPVVGQ0xQJmFtcDtvcmRlbmFyRGVzYz1mYWxzZSZhbXA7b3JkZXJuYXJQb3JGZWNoYVB1YmxpY2FjaW9uPWZhbHNlJmFtcDtvcmRlcm5hclBvclN1cGVyZmljaWU9ZmFsc2UmYW1wO29yZGVybmFyUG9yUHJlY2lvPWZhbHNlJmFtcDtwYWdpbmE9MSZhbXA7dGV4dG9CdXNxdWVkYT1wcm92aWRlbmNpYSZhbXA7dGlwb1Zpc3RhPWxpc3RhJmFtcDt2aWV3cG9ydD0tMzQuMjg3ODE0OCUyQy03MS43MDg4MTAyMDAwMDAwMiUyQy0zMi45MTk0NTElMkMtNjkuNzY4OTk0MzAwMDAwMDMmYW1wO2NvbXVuYT1Qcm92aWRlbmNpYSZhbXA7cmVnaW9uPVJlZ2klQzMlQjNuJTIwTWV0cm9wb2xpdGFuYSZhbXA7YXRyaWJ1dG9zPSZhbXA7aWRsZT1mYWxzZSZhbXA7em9vbT0xMyZhbXA7YnVzY2FuZG89ZmFsc2UmYW1wO3Z1ZWx2ZUJ1c2Nhcj1mYWxzZSZhbXA7ZGlidWphUG9saWdvbm89dHJ1ZSZhbXA7cmVzZXRNYXBhPXRydWUmYW1wO2FuaW1hY2lvbj1mYWxzZSZhbXA7aWRab25hSG9tb2dlbmVhPTAmYW1wO2VzUHJpbWVyYUJ1c3F1ZWRhPWZhbHNl; __insp_targlpt=QnVzY2FyIHkgY29tcHJhciBjYXNhIHBvciBtYXBhIGVuIFRvYyBUb2M%3D; __insp_norec_sess=true; NPS_93546e30_last_seen=1525137064458; ; mp_29ae90688062e4e2e6d80b475cef8685_mixpanel=%7B%22distinct_id%22%3A%20%221631939188a5a0-0f03580850d109-3961430f-1fa400-1631939188baf6%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.freelancer.com%2Fdashboard%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.freelancer.com%22%7D; __insp_slim=1525137281382',
            "origin": "https://www.toctoc.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
            "x-xsrf-token": "c0XJvq6rTwZU7oqPM4LsGpbp_pNfBQIZzFUgyPZh3A-cCwV0gJE_gw7cSAGAqM-wrE-dbikAiw2eVy-SN9mq490jroUyAyjfraQcnaaTbcw1",
        }
        html = response.text.strip().replace(" ",'')
        resHeaders = response.headers
        setCook = resHeaders.getlist('Set-Cookie')
        setCook = [i.decode() for i in setCook]
        setCook = ''.join(setCook)
        setCook = self.parseSetCookie(setCook)
        headers["x-xsrf-token"] = re.findall('__RequestVerificationToken"type="hidden"value="(.+)?"', html)[0]
        headers['cookie'] = headers['cookie'] + ';__RequestVerificationToken=' + setCook[ ' HttpOnly__RequestVerificationToken'] + ';X-DATA=' + setCook['X-DATA'] + ';' + 'X-DATA-NPSW=' + setCook[
                                ' HttpOnlyX-DATA-NPSW']
        return headers

    def parseJson(self, response):
        data = json.loads(response.text)
        totalPage = data['TotalPaginas']
        if totalPage > 1 and response.meta['first']:
            headers = response.meta['headers']
            for i in range(1,int(totalPage) + 1):
                payload = self.getPayLoad()
                payload['pagina'] = i
                req = scrapy.Request(self.api_, headers=headers, body=json.dumps(payload), callback=self.parseJson,
                                     method='POST')
                req.meta['headers'] = headers
                req.meta['first'] = False
                yield req
        houseInfo = data['Propiedades']
        for i in houseInfo:
            yield self.handleData(i)

    def handleData(self,info):
        info['MetrajeTooltip'] = info['MetrajeTooltip'].replace("&#178",'^2')
        item = ToctocItem(info)
        return item

    def getPayLoad(self):
        text = self.search_word or ''
        return {
            "dormitorios": "0",
            "banos": "0",
            "superficieDesde": "0",
            "superficieHasta": "0",
            "precioDesde": "0",
            "precioHasta": "0",
            "moneda": "UF",
            "tipoArriendo": "true",
            "tipoVentaUsado": "true",
            "tipoVentaNuevo": "false",
            "tipoUltimasVentas": "false",
            "casaDepto": "undefined",
            "ordenarPorMoneda": "UFCLP",
            "ordenarDesc": "false",
            "ordernarPorFechaPublicacion": "false",
            "ordernarPorSuperficie": "false",
            "ordernarPorPrecio": "false",
            "pagina": "1",
            "textoBusqueda": text,
            "tipoVista": "lista",
            "viewport": "",
            "region": "",
            "idle": "false",
            "buscando": "false",
            "vuelveBuscar": "false",
            "dibujaPoligono": "false",
            "resetMapa": "true",
            "animacion": "false",
            "idZonaHomogenea": "0",
            "esPrimeraBusqueda": "false"
        }