import json
import requests
import random

# 定义一个名为 select 的函数，接受一个参数 a。
# 此函数基于给定的参数 a 从预定义的字典中选择一个对应的值。
# 如果参数 a 不在字典的键中，则随机选择一个键的值返回。
import logging

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
def select(a):
    print('is in select a')
    logging.info("url00000000000000:")



# 定义处理函数 handler，它处理事件触发时的逻辑。
def handler(event, context):
    logging.info("11111111111:")

    print('is in handler')

