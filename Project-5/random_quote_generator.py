# -*- coding: utf-8 -*-
"""Random_Quote_Generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LbGQ25_vi62gYdG43Z5cik6cohjyWYVK
"""

import requests, random

url = "https://type.fit/api/quotes"
quotes = requests.get(url).json()

random_quote = random.choice(quotes)
print(f"{random_quote['text']}\n  author: {random_quote['author']}")