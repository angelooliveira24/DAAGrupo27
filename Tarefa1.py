# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:37:33 2022

@author: Utilizador
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\Utilizador\Desktop\Universidade\Mestrado\DAA\Trabalho\DAAGrupo27\final_book_dataset_kaggle.csv')
df.info()
df.describe()
df.isnull().any()
df.replace('Nan', np.nan, inplace = True)
df.dropna(axis = 0, inplace = True)
df.columns


max_reviews = df['n_reviews'].max() 
review_book = df.loc[df['n_reviews'] == max_reviews, 'title'].iloc[0]
print(review_book, 'is the most reviewed book with max ', max_reviews, 'reviews')


plt.figure(figsize=(20,20))
sns.barplot(x='n_reviews',y='title', data = df.head(20))
sns.set(rc={'figure.figsize':(11.7,8.27)})
plt.yticks(fontsize= 6)
plt.ylabel('Book Title')
plt.xlabel('Number of Reviews')
plt.title('Number of reviews per book')

#df.head()
#df.shape #attribute not method
#df.sort_values(['price'], ascending=False).head(10)#organizados por preço só 10 primeiros
#df.sort_values(['avg_reviews'],ascending=False)#todos
#df.sort_values(['star5'], ascending = False)
#df.sort_values(['n_reviews','avg_reviews'],ascending=False)
#df.language.value_counts()
#df.pages.value_counts(bins=5)
#df.publisher.isna().any().sum()
#df.filter(regex ='[Pearson]').count()
