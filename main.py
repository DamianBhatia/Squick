import tkinter as tk
from newspaper import Article

url = "https://edition.cnn.com/2020/09/13/tech/microsoft-tiktok-bytedance/index.html"

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')