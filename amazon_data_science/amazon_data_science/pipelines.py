from scrapy import signals
from scrapy.exporters import CsvItemExporter


class CsvExportPipeline(object):

    def __init__(self):
        self.file = None
        self.exporter = None

    def open_spider(self, spider):
        self.file = open('output.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
