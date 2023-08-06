# 过滤收集到的文本
# 文本以下面的形式保存
# --书名1
#     -1.txt
#     -2.txt
#     - ...
# --书名2
#     -1.txt
#     -2.txt
#      - ...
# -- ...

import os
#遍历当前文件夹下所有文件
path = '.'
books = os.listdir(path)
for book in books:
    if book == '.git':
        continue
    if os.path.isdir(book):
        print(book)
        #遍历当前文件夹下所有文件
        files = os.listdir(book)
        with open(book + '/' + book + '.txt', 'w', encoding='utf-8') as fw:
            for file in files:
                if os.path.isfile(book + '/' + file):
                    #读取文件内容
                    with open(book + '/' + file, 'r', encoding='utf-8') as f:
                        text = f.read()
                        #过滤文本
                        text = text.replace(' ', '')
                        # text = text.replace('\n', '')
                        text = text.replace('\r', '')
                        text = text.replace('\t', '')
                        text = text.replace('　', '')
                        fw.write(text)