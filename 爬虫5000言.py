from bs4 import BeautifulSoup
import requests
import time
import re
import os

html_dict = {}
title_dict = {}

def useless(url):
    pattern = re.compile(r'5000yan')
    matches = pattern.findall(url)
    if len(matches) > 0:
        return False
    return True

def process_link(url):
    if useless(url):
        return
    print(url)
    time.sleep(0.15)
    try:
        response = requests.get(url)
    except:
        return
    response.encoding = "utf-8"
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    titles = soup.find_all('a', {'title': True})
    if len(titles) > 0:
        # 确认是否为[0-9].html结尾，筛选有效链接
        pattern = re.compile(r'[0-9]\.html$')
        matches = pattern.findall(url)
        if len(matches) > 0:
            pattern = re.compile(r'<a href="/" title="">(.*?)</a>')
            matches = pattern.findall(str(titles[0]))
            book_name = str(matches[0])
            grap_div_elements = soup.find_all('div', class_='grap')
            if len(grap_div_elements) > 0 and len(book_name) > 0:
                if book_name not in title_dict:
                    title_dict[book_name] = 1
                    print(book_name)
                else:
                    title_dict[book_name] += 1
                # 创建/book_name/title_dict[book_name].txt文件
                if not os.path.exists(book_name):
                    os.mkdir(book_name)
                with open(book_name + '/' + str(title_dict[book_name]) + '.txt', 'w', encoding='utf-8') as f:
                    for grap_div in grap_div_elements:
                        # 写入删除多余空格后的文件
                        f.write(grap_div.text.strip())
                        
                        

    # 找到所有超链接
    links = soup.find_all("a")
    # 遍历超链接并处理
    for link in links:
        href = link.get("href")
        if href is None or href in html_dict:
            continue
        html_dict[href] = 1

        # 递归处理嵌套的超链接
        if href.startswith("http"):  # 确保链接是以http或https开头
            process_link(href)


# 调用递归函数开始遍历
print("爬取开始")
start_url = "https://5000yan.com"
process_link(start_url)
print("爬取结束")
