# -*- coding: utf-8 -*-
'''
--------------------------------------------------------------------
~ www.99.co.id house listing scraper ~
DISCLAIMER: please use it for research or educational purpose only!
--------------------------------------------------------------------
'''
import os
import scrapy
import time
import socks
import socket
import requests
import string
import logging
import re
from random import randint

'''
Untuk mendapatkan data selector seperti di bawah ini, lakukan interogasi data secara manual dengan scrapy shell terlebih dahulu,
$> scrapy shell 'url'

response.xpath("//*[@class='__item']/div/div//button/@data-property-id").extract_first()            # id property
response.css('li.__item div.search-card__info__title h2 a.long-title::text').extract_first()        #judul properti
response.css('li.__item div.search-card__info__title li.complexName::text').extract_first()         #nama komplek
response.css('li.__item div.search-card__info__title li.locality::text').extract_first()            #lokasi
response.css('li.__item div.search-card__info__title li.province::text').extract_first()            #provinsi
response.css('li.__item div.search-card__info__title li.bedrooms abbr::text').extract_first()       #jumlah kamar
response.css('li.__item div.search-card__info__title li.bathrooms abbr::text').extract_first()      #jumlah km
response.css('li.__item div.search-card__info__title li.landSize abbr::text').extract_first()       #luas lahan
response.css('li.__item div.search-card__info__title li.buildingSize abbr::text').extract_first()   #luas bangunan
response.css('li.__item  div.search-card__footer div.search-card__type::text').extract_first()      #dijual/disewakan
response.css('li.__item  div.search-card__footer div.nego::text').extract_first()                   #nego/fixed
response.css('li.__item  div.search-card__footer span.search-card__price span::text').extract_first()   #harga
response.xpath("//*[@class='__item']//span[@class='price search-card__price']/span/@content").extract_first()   # harga
response.css('li.__item  div.search-card__premium-agent-box div.search-card__premium-agent-box__agent-title h4::text').extract_first()   #nama agen
response.xpath("//*[@class='__item']//div[@class='search-card__footer']//span[@class='agent-info__fullname']/text()").extract_first()    #nama property/agen
response.xpath("//*[@class='__item']/div/div//button/@data-agent-username").extract_first()         # username
response.xpath("//*[@class='__item']/div/div//button/@data-agent-telephone").extract_first()        # telepon
response.xpath("//*[@class='__item']/div/div//button/@data-is-premium").extract_first()             # whether premium agent atau tidak
response.xpath("//*[@class='__item']//a[@class='btn btn--whatsapp button-callback']/@href").extract_first()    # send whatsapp message
response.xpath("//*[@class='__item']//div[@class='property-list-view__card']/div/@data-property-type").extract_first()    # tipe properti
response.xpath("//*[@class='__item']//div[@class='property-list-view__card']/div/@data-listing-type").extract_first()    # tipe listing dijual atau disewakan
response.xpath("//*[@class='__item']//div[@class='property-list-view__card']/div/@data-href").extract_first()    # url properti
'''

regex = re.compile("[,]") #compile regex

def getTerminalSize():
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,'1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

    ### Use get(key[, default]) instead of a try/catch
    #try:
    #    cr = (env['LINES'], env['COLUMNS'])
    #except:
    #    cr = (25, 80)
    return int(cr[1]), int(cr[0])

def ToRify():
    socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
    socket.socket = socks.socksocket
    currentip = requests.get("http://icanhazip.com").text
    (width, height) = getTerminalSize()
    print "_" * width
    print "ToRify Using IP Address: " + currentip
    print "_" * width

class PropertiSpider(scrapy.Spider):
    name = "rumah"
    start_urls = ['https://www.99.co/id/jual/rumah']
    currentpage = 1
    def parse(self,response):
        x = 0
        ToRify()
        for rumah in response.css('li.__item'):
            yield {
            'tipe_properti': rumah.xpath("//*[@class='__item']//div[@class='property-list-view__card']/div/@data-property-type").extract_first(),
            'tipe_listing': rumah.xpath("//*[@class='__item']//div[@class='property-list-view__card']/div/@data-listing-type").extract_first(),
            'is_negotiable': rumah.css('li.__item  div.search-card__footer div.nego::text').extract_first(),
            'judul': regex.sub("",rumah.css('li.__item div.search-card__info__title h2 a.long-title::text').extract_first()),
            'nama_komplek': rumah.css('li.__item div.search-card__info__title li.complexName::text').extract_first(),
            'lokasi': rumah.css('li.__item div.search-card__info__title li.locality::text').extract_first(),
            'provinsi': rumah.css('li.__item div.search-card__info__title li.province::text').extract_first(),
            'jumlah_kamar': rumah.css('li.__item div.search-card__info__title li.bedrooms abbr::text').extract_first(),
            'jumlah_km_wc': rumah.css('li.__item div.search-card__info__title li.bathrooms abbr::text').extract_first(),
            'luas_lahan': rumah.css('li.__item div.search-card__info__title li.landSize abbr::text').extract_first(),
            'luas_bangunan' : rumah.css('li.__item div.search-card__info__title li.buildingSize abbr::text').extract_first(),
            'harga': rumah.xpath("//*[@class='__item']//span[@class='price search-card__price']/span/@content").extract_first(),
            'agen': rumah.xpath("//*[@class='__item']//div[@class='search-card__footer']//span[@class='agent-info__fullname']/text()").extract_first(),
            'username': rumah.xpath("//*[@class='__item']/div/div//button/@data-agent-username").extract_first(),
            'kontak': rumah.xpath("//*[@class='__item']/div/div//button/@data-agent-telephone").extract_first(),
            'is_premium_agent': rumah.xpath("//*[@class='__item']/div/div//button/@data-is-premium").extract_first(),
            'company': rumah.xpath("//*[@class='__item']//div[@class='search-card__footer']//a[@class='agent-info__company-id']/text()").extract_first(),
            'send_whatsapp_message': rumah.xpath("//*[@class='__item']//a[@class='btn btn--whatsapp button-callback']/@href").extract_first(),
            'url_properti': rumah.xpath("//*[@class='__item']//div[@class='property-list-view__card']/div/@data-href").extract_first(),
            }

            if x == 9:
            	break
            x=x+1

        self.logger.info('Parse function called on %s', response.url)
     
        time.sleep(randint(1,7))

        page = self.currentpage + 1
        next_page= "/id/jual/rumah?radius=-1&hlmn=%s" % page
        if response.css('div.property-list-pagination li.next') is not None:
            next_page = response.urljoin(next_page)
            self.currentpage = page
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)
        else:
            print "Finished."
