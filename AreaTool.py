# -*- coding=utf-8 -*-
from log.jdlogger import logger

'''
找一条第一个版本的url
'''
url = 'https://c0.3.cn/stock?skuId=6909876&area=3_51043_2907_0&venderId=1000002429&buyNum=1&choseSuitSkuIds=&cat=737,752,15124&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=%E6%B5%93%E6%B0%91%E6%B5%93%E6%B0%91&pduid=15518924836561024189040&ch=1&callback=jQuery7458800'
skuId = url.split('skuId=')[1].split('&')[0]
area = url.split('area=')[1].split('&')[0]
logger.info('你的area是[ %s ]，链接的商品id是[ %s ]', area, skuId)
