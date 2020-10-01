import tkinter as tk
from newspaper import Article

"""
    Fetch article data using newspaper library
"""
def gather_data(url):
    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    fill_data(article)


"""
    Insert article data into entry fields
"""
def fill_data(article):
    if article.title != None:
        title_text.delete(0, tk.END)
        title_text.insert(0, article.title)
    if article.authors != None:
        author_text.delete(0, tk.END)
        author_text.insert(0, article.authors)
    if article.publish_date != None:
        date_text.delete(0, tk.END)
        date_text.insert(0, article.publish_date)
    if article.summary != None:
        sum_text.delete("1.0", tk.END)
        sum_text.insert(tk.END, article.summary)


root = tk.Tk()
root.geometry("600x300")

# Entry for url
url_label = tk.Label(root, text="Article URL:").grid(row=0)
url_entry = tk.Entry(root)
url_entry.grid(row = 0, column = 1, ipadx=180)

# Button
submit_btn = tk.Button(root, text="GO", width=6, command=lambda: gather_data(url_entry.get()))
submit_btn.grid(row = 0, column=2)

# Title
title_label = tk.Label(root, text="Title:").grid(row=4, sticky="W")
title_text = tk.Entry(root)
title_text.grid(row=4, column=1, ipadx=180)

# Author
author_label = tk.Label(root, text="Author:").grid(row=8, sticky="W")
author_text = tk.Entry(root)
author_text.grid(row=8, column=1, ipadx=180)

# Date
date_label = tk.Label(root, text="Date:").grid(row=12, sticky="W")
date_text = tk.Entry(root)
date_text.grid(row=12, column=1, ipadx=180)

# Summary
sum_label = tk.Label(root, text="Summary:").grid(row=16, sticky="W")
sum_text = tk.Text(root, width=60, height=10)
sum_text.grid(row=16, column=1)

root.mainloop()

    