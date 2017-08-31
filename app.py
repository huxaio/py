import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

# 创建连接池
@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global _pool
    _pool = yield from aiomysql.create_pool(
        host = kw.get('host','localhost'),
        port = kw.get('port',3306),
        user = kw['root'],
        password = kw['123456'],
        db = kw['db'],
        charset = kw.get('charset','utf8'),
        autocommit = kw.get('autocommit',True),
        maxsize = kw.get('maxsize',10),
        minsize = kw.get('minsize',1),
        loop = loop
    )
# 执行SELECT语句
@asyncio.coroutine
def select(sql,args,size=None):
    log(sql,args)
    global _pool
    with(yield from _pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?','%s'),args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs
# 执行INSERT,UPDATA,DELETE语句
@asyncio.coroutine
def execute(sql,args):
    log(sql)
    with (yield from _pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?','%s'),args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected
# 建立ORM
from orm import Model,StringField,IntegerField

class User(Model):
    _table_ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()
# 创建实例：
user = User(id=123,name='Michael')
# 存入数据库：
user.insert()
# 查询所有User对象：
users = User.findAll()

# 定义所有ORM映射的基类Model
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def _getattr_(self,key):
        try:
            return self[key]
        except KeyError:
            reise AttributeError(r "'Model' object has no attribute '%s'" % key)

    def __setattr__(self,key):
        self[key] = value
    def getValue(self,key):
        return getattr(self,key,None)

    def getValueOrDefault(self,key):
        value = getattr(self.key,None)
        if value is None:
            field = self._mappings_[key]
            if field.default is not None:
                value = field.default()if callable(field.default) else field.default
                logging.debug('using default value for %s %s' % (key,str(value)))
                setattr(self,key,value)
            return value

user['id'] # 123
user.id    # 123

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()