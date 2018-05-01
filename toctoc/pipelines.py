# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class ToctocPipeline(object):
    def __init__(self,outfile):
        self.data = {}
        self.update = []
        self.headers = []
        try:
            with open(outfile) as f:
                f_csv = csv.reader(f)
                headers = next(f_csv)
                self.headers = headers
                for row in f_csv:
                    id = row[18]
                    self.data[id] = row
        except Exception as e:
            print(e)

    @classmethod
    def from_crawler(cls,crawler):
        setting = crawler.settings
        print('=============>', setting.get("COMPARE_FILE"))
        out_file = setting.get("COMPARE_FILE")
        return cls(out_file)

    def process_item(self, item, spider):
        if item['Id'] in self.data:
            if item['PrecioDespliegue'] != self.data[item['Id']][39] :
                self.update.append(self.tunr_in(item))
                self.update.append(self.data[item['Id']])
        if '&' in item['MetrajeTooltip']:
            item['MetrajeTooltip'] = item['MetrajeTooltip'].replace("&#178",'^2')
        return item

    def tunr_in(self,dic):
        res = []
        for i in self.headers:
            res.append(dic.get(i,''))

    def close_spider(self,spider):
        if self.update:
            with open('update.csv','w') as f:
                f_csv = csv.writer(f)
                f_csv.writerow(self.headers)
                f_csv.writerows(self.update)