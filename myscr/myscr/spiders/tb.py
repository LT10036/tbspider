# -*- coding: utf-8 -*-
import scrapy
import json


# 注 释 掉 了 ，做 筛 选 时 候 可 以 打 开
# ls=[]
# n = input('请输入关键词：')


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=吐槽']





    def parse(self, response):
        global ls
        global n

        list_scr=response.xpath('//*[@id="thread_list"]/li/div/div[2]/div')


        print(len(list_scr))


        for i in list_scr:

            temp={}
            temp['title']=i.xpath('./div/a/text()')
            # temp['auth']=i.xpath('./div/span/span/a/text()')
            # temp['href'] = i.xpath('./div/a/@href)')
            if temp['title']==[]:
                pass
            else:
               # temp['title'] = i.xpath('./div/a/text()')[0].extract()
               # temp['auth'] = i.xpath('./div/span/span/a/text()')[0].extract()
               temp['con'] = i.xpath('./div/a/text()')[0].extract()
               temp['href'] = response.urljoin(i.xpath('./div/a/@href').extract_first())
               yield temp
               #
               # # 跟 据 输 入 的 条 件 搜 索 每 一 页 数 据， 如 果 符 合 就 写 入 文 件
               # if n in (temp['title'] or temp['auth']):
               #      # f.write(str(temp))
               #      # f.write('\n')
               #      ls.append(temp)
               # else:
               #     pass
        # for i in range(1,455):
        #     url='https://tieba.baidu.com/f?kw=%E5%90%90%E6%A7%BD&ie=utf-8&pn='+str(i*50)
        #
        #     yield scrapy.Request(url, callback=self.parse)
        # print(len(ls))
        # print(ls)
        # f = open('123.txt', 'w')
        # for i in ls:
        #
        #     f.write('标题:'+i['title'])
        #     f.write('\n')
        #     f.write('链接：'+i['href'])
        #     f.write('\n')
        # f.close()









