#!/usr/bin/python
# coding=utf-8
LOGIN_URL = "https://trade.cgws.com/cgi-bin/user/Login?function=tradeLogout"
ENTRUST_QUERY = "https://trade.cgws.com/cgi-bin/stock/EntrustQuery?function=MyAccount"
NEW_STOCK_URL = "http://newstock.cfi.cn/"
FUTU_HOST = "172.18.3.101"
FUTU_PORT = 11111
USER_FILE = "user.json"
SLEEP_TIME = 3
SHORT_SLEEP_TIME = 1
SLEEP_INTERVAL = 30
##########stock type##########
MARKET_SZ = 0
MARKET_SH = 1
MARKET_CYB = 2
MARKET_ALL = 3
SUB_NEW_STOCK = 4 
MARKET_ELSE = 10
##########order type##########
SUBMITTED = 0
ONGOING = 1
##############################
DB_NAME = 'stock'
DB_USER = 'root'
DB_PASSWD = '123456'
DB_HOSTNAME = 'localhost'
UTF8 = "utf8"
SQL = "select * from %s"
RETRY_TIMES = 3
##############################
class gw_ret_code:
    # 150906130资金不足
    # 150906135股数不够
    # 长城的出错都是这个鸟样 alert("-990297020[-990297020]，出错了就反馈空的订单号，看看是不是自己定义一些exception来搞
    NOT_ENOUGH_MONEY = 1
    NOT_ENOUGH_STOCK = 2
    SETTLEMENT_TIME = 3 #999003088
    NOT_DEAL_TIME =4 #990297020
    NOT_RIGHT_ORDER_ID = 5 #990268040订单号不对
    LOGIN_FAIL = 100 #login fail
    OTHER_ERROR = 999
