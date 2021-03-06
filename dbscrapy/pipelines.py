# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import copy
from twisted.enterprise import adbapi
import json

class TutorialPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        '''1、@classmethod声明一个类方法，而对于平常我们见到的叫做实例方法。
           2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
           3、可以通过类来调用，就像C.f()，相当于java中的静态方法'''
        # 读取settings中配置的数据库参数
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            # cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        return cls(dbpool)  # 相当于dbpool付给了这个类，self中可以得到

    # pipeline默认调用
    def process_item(self, item, spider):
        # 深拷贝 否则出现数据库中数据重复的情况
        asynItem = copy.deepcopy(item)

        if spider.name == 'ZufangSpider':
            query = self.dbpool.runInteraction(self._conditional_Zufang_insert, asynItem)
        elif spider.name =='ZufangContentsSpider':
            query = self.dbpool.runInteraction(self._conditional_Contents_insert, asynItem)

        #query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    # 写入数据库中
    # SQL语句在这里
    def _conditional_Zufang_insert(self, tx, item):
        sql = "insert into zufang(title,link,pushtime,commentcount) values(%s,%s,%s,%s)"
        params = (
        item['title'], item['link'], item['time'],item['commentCount'])
        tx.execute(sql, params)

    def _conditional_Contents_insert(self, tx, item):
        sql = "insert into zf_contents(linkid,fromuser,detailtime,userlink,contents,pic) values(%s,%s,%s,%s,%s,%s)"
        data = json.loads(item['contents']);
        data['contents'].strip() if not "" else None
        data['img'].strip() if not "" else None
        print(data['contents'])
        print(data['img'])
        params = (item['linkId'].strip(),item['fromUser'].strip(), item['detailTime'].strip(), item['userLink'].strip(),data['contents'].strip(),data['img'].strip())

        tx.execute(sql, params)


    # 错误处理方法
    def _handle_error(self, failue, item, spider):
        print failue


    # def process_item(self, item, spider):
    #     return item
