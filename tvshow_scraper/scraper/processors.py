# -*- coding: UTF-8 -*-   
import sys,re
reload(sys)
sys.setdefaultencoding("utf-8")

# attention: you will get nothing from loader_context
def pre_douban_date(text, loader_context):
    douban_date_filter_re = re.compile('\(.*\)+')
    content = re.sub(douban_date_filter_re, '', text)

    return content


