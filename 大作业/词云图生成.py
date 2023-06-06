import pandas as pd
from wordcloud import WordCloud
import jieba  # 结巴分词，设置停用词的时候需要用到
from tkinter import _flatten
import matplotlib.pyplot as plt  # plt展示图像，设置图例和参数


filepath = "评论信息.xlsx"
data = pd.read_excel(filepath, names=["名字", "性别", "等级", "评论内容", "点赞数"], usecols=[0, 1, 2, 3, 4])




with open('hit_stopwords.txt', 'r', encoding='utf-8') as f:
    stopword = f.read()


def my_word_cloud(data_=None, stopword=None, img=None):
    dataCut = data_.apply(jieba.cut)  # 分词
    dataAfter = dataCut.apply(lambda x: [i for i in x if i not in stopword])  # 去除停用词
    wordFre = pd.Series(_flatten(list(dataAfter))).value_counts()  # 统计词频
    mask = plt.imread(img)
    plt.figure(figsize=(20,20))
    wc = WordCloud(scale=10,font_path='C:/Windows/Fonts/STXINGKA.TTF',background_color="white")
    wc.fit_words(wordFre)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

my_word_cloud(data_=data["评论内容"],stopword=stopword,img="1.jpg")
