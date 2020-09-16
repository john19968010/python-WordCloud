from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import jieba
import numpy as np
from collections import Counter
import nltk
from newsapi import NewsApiClient
import requests

newsapi = NewsApiClient(api_key='db6f518f7a5349d98c710da1bcae06b9')
res =requests.get('https://newsapi.org/v2/top-headlines?country=tw&category=business&q=美豬from=2020-08-30&to=2020-08-30&sortBy=popularity&apiKey=db6f518f7a5349d98c710da1bcae06b9')
news = newsapi.get_everything(q='美豬',
                              language='zh',
                              from_param='2020-08-30',
                              to='2020-08-30',
                              sort_by='popularity',)
des = ""
for i in news['articles']:
    des += i['description']

    
jieba.set_dictionary('jieba-zh_TW/jieba/dict.txt') 

with open('jieba-zh_TW/jieba/stop_word.txt', 'r',encoding="utf-8") as f:
    stops = f.read().split('\n')

terms = []
for t in jieba.cut(des, cut_all=False):
    if t not in stops:
        terms.append(t)
diction = Counter(terms)

# 從 Google 下載的中文字型
font = 'GenJyuuGothicX-P-Normal.ttf'
mask = np.array(Image.open("output.png"))
wordcloud = WordCloud(background_color="white",mask=mask,font_path=font)
wordcloud.generate_from_frequencies(diction)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file("new_Wordcloud.png")