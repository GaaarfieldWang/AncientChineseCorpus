# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

# 发送HTTP请求并获取响应
url = 'https://liaozhai.5000yan.com/19944.html'
response = requests.get(url)
response.encoding = 'utf-8'

# 检查响应状态码
if response.status_code == 200:
    # 提取HTML内容
    html_content = response.text

    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找所有具有class="grap"的<div>元素
    grap_div_elements = soup.find_all('div', class_='grap')

    # 输出结果
    for grap_div in grap_div_elements:
        print(grap_div.text)
            # # 使用正则表达式匹配<div>...</div>中的内容
            # pattern = re.compile(r'<div>((.)*?)</div>', re.DOTALL)
            # matches = pattern.findall(str(grap_div))

            # for match in matches:
            #     print(match)


else:
    print('Failed to retrieve the HTML file. Status code:', response.status_code)
