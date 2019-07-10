# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MyscrPipeline(object):
    # 创 建 数 据 库 连 接 及  游 标
    def __init__(self):
        self.con = pymysql.connect(
            host = 'localhost',
            password = 'abc10036',
            user = 'root',
            # charset = 'utf-8',
            db = 'lt10036',
            use_unicode = True,
            )
        self.sur = self.con.cursor()


    def process_item(self, temp, spider):
        # 游 标 要 执 行 的 函 数
        self.sur.execute(
            "insert into tb2 (href,con)values (%s,%s)",(temp['href'],temp['con'])
        )

        # 执 行 以 上 操 作
        self.con.commit()
        return temp
    # 关 闭 数 据 库 连 接
    def close_sp(self):
        self.con.close()