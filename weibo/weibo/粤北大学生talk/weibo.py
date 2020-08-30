# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2020-08-28 23:40:24
# @Last Modified by:   Marte
# @Last Modified time: 2020-08-29 00:06:08
# !usr/bin/env python
# -*-coding:utf-8 -*-
import os
import re
import jieba
from pyecharts import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

def file_name():
    name = []
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            this_file = os.path.splitext(file)
            if this_file[1].lower() == '.txt':
                name.append(this_file[0])
        return name


def add_dict(dic, words):
    for word in words:
        if len(word.strip()):
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1


def remove_point(dic):
    apl = list(r'\/|{}[]@#$^&*~`;:"<>?,，。、？“”')
    chara = list(r'的了吗吧的么呢啊哪')
    rabsh = [u'位置',u'微博', u'RBaFzxp',u'时间',u'评论',u'发布',
                u'点赞数',u'工具',u'cnRBaFzxp',
                u"吧",u"转发",u"Hi",u"httpt"]

    remove_key = list(chr(i) for i in range(0, 128)) + apl + chara +rabsh
    for each in remove_key:
        try:
            dic.pop(each)
        except:
            pass


def dict_sort(dic):
    d = list(zip(dic.keys(), dic.values()))
    dd = sorted(d, key=lambda x: x[1], reverse=True)
    return list(zip(*dd))


def wordCloud(title, key, value):
    wordcloud = WordCloud(width=1000, height=700)

    wordcloud.add('', key, value, word_size_range=[17, 100], rotate_step=20, shape='circle')
    # 'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'
    wordcloud.render(title + '.html')


def main(name):
    with open('%s.txt' % name, 'r', encoding='utf-8') as f:
        file = f.read()
    reg = re.compile(r'\w*[\u4e00-\u9fa5A-Za-z.]{3,}\w*')
    mylist = reg.findall(file)
    print(len(mylist))

    #对mylist进行遍历,并将其做分词切割后做成列表
    word_list = [''.join(jieba.cut(sentence)) for sentence in mylist]
    #将word_list内的元素用空格连接起来，以便于计算词频
    new_text = ''.join(word_list)
       #设置词云的字体和背景颜色
       #
    # wordcloud = WordCloud(font_path='C:\Windows\Fonts\msyhl.ttc',background_color='black').generate(new_text)

    con_words = [x for x in jieba.cut(new_text) if len(x) >= 2]
    fq = Counter(con_words).most_common()
    fq = dict(fq)
    remove_point(fq)
    print(fq)
    ttl_key, ttl_value = dict_sort(fq)

    wordCloud(name, ttl_key[:1000], ttl_value[:1000])





if __name__ == '__main__':
    files = file_name()
    for file in files:
        print('当前文件：', file, '\n提取聊天信息数量：', end='')
        main(file)
