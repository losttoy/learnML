# http://fund.eastmoney.com/allfund.html
import sys
from bs4 import BeautifulSoup
import datetime
import xlsxwriter
workbook = xlsxwriter.Workbook('基金%s.xlsx'%(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")))
worksheet = workbook.add_worksheet()

# text = ""
# file =
# for line in file:
#     text += line

# print(text)

def process(node):
    # if None == node.children:
    #     print(node)
    # else:
    for child in node.descendants:
        process(child)

soup = BeautifulSoup(
    open("/Users/zhuwei/PycharmProjects/learnML/stock/p3/基金代码查询一览表(按基金代码排序)_天天基金网.htm",
         "r", encoding="gbk")
    , "html.parser")
# print(soup.prettify())
# print(soup.div)
# print(soup.a)
# jobs = set()
# for job in soup.body.section('div.a'):
#     jobs.add('{} ({})'.format(job.a.string, job.a['href']))

# process(soup.head)
# process(soup.descendants)

# soup.ha

seq = 0
worksheet.write(seq, 0, '基金ID')
worksheet.write(seq, 1, '基金名称')
seq += 1

for one in soup.find_all('a'):
    if one.get('href') != None:
        # print(one['href'])
        if not ("基金吧" == one.string or "档案" == one.string or "基金品种" == one.string):
            if(one['href'].find('http://fund.eastmoney.com/') == -1 or not one['href'].endswith('.html')
            or len(one['href']) != 37):
                continue
            # print(one)
            # print(one.string)
            print(one.string[1:7])
            print(one.string[8:])
            worksheet.write(seq, 0, one.string[1:7])
            worksheet.write(seq, 1, one.string[8:])
            seq += 1

# 保存
workbook.close()