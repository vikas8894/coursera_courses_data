# -*- coding: utf-8 -*-
"""Untitled30.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KQl0r2XaHQpUIQd1k91N2R1rRCwVH5Yp
"""

import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import time

df=pd.read_csv('/content/coursera_courses.csv')
df

df.drop_duplicates()

df.info()

df.describe(include='object')

df.isnull().sum()

df.dropna(inplace=True)

df.isnull().sum()

df.info()

for i in df.describe(include='object'):
  print(i)
  print(df[i].unique())
  print('-'*75)

df['course_students_enrolled']=df['course_students_enrolled'].str.replace(',','').astype(int)
df

df.info()

df.head(10)

""" Distribution of course ratings in dataset

"""

plt.figure(figsize=(10,6))
sns.histplot(data=df['course_rating'],kde=True,color='red')
plt.xlabel('customer ratings')
plt.ylabel('count')
plt.title('customer ratings distribution')
plt.show()

"""Reading= Most of the courses offered by coursera has customer rating from 4.6 to 4.9 out of 5 which tells the curses offered by coursera are worth to get enrolled for future studies.

How the courses are measured on difficulty level
"""

sns.countplot(data=df, x="course_difficulty")
plt.xlabel("Difficulty Level")
plt.ylabel("Count")
plt.title("Distribution of Course Difficulty Levels")
plt.show()

"""Out of four categories maximum courses offered are meant for beginners level.

what duration course is most offered?
"""

sns.countplot(data=df, x='course_time')
plt.xlabel("course_time")
plt.ylabel("Count")
plt.title("Distribution of Course as per time",fontdict={'color':'teal','size':20})
plt.show()



"""out from the courses offered maximum courses are between time duration of 3-6 months"""

sns.countplot(data=df, x='course_certificate_type',palette='Set2')
plt.xlabel("course_certificate_type")
plt.ylabel("Count")
plt.title("Distribution of Course as pertype",fontdict={'color':'green','size':20})
plt.xticks(rotation=45)
plt.show()

sns.barplot(data=df,x='course_certificate_type', y='course_students_enrolled')
plt.xticks(rotation=9)
plt.xlabel('course certificate type')
plt.ylabel('number of students enrolled')
plt.show()

"""we can say the total of students that enroll themselves into total of three types viz., specialization, professional certificate and guided project is almost equal to number of students that enroll themselves into a course."""

import spacy
from wordcloud import WordCloud

pip install textblob

import textblob

course_summary=df['course_summary']
key_phrases=' '.join(course_summary)

wordcloud = WordCloud(width=800, height=400, background_color="black", colormap="viridis").generate(key_phrases)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Top Key Phrases in Course Summaries")
plt.show()

course_skills = df["course_skills"]

# Here Combining all skills into a single string
all_skills_text = " ".join(course_skills)

wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="cividis").generate(all_skills_text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Most Frequently Mentioned Skills in Course Skills")
plt.show()

"""to find number of students enrolled into different type of courses

"""

new_df=df.sort_values('course_students_enrolled',ascending=False)
new_df=new_df.head(10)
plt.barh(new_df['course_title'],new_df['course_students_enrolled'],color='lightgreen')
plt.ylabel('top 10 course title')
plt.xlabel('number of students enrolles')
plt.title('top 10 courses as per students enrolment')
plt.gca().invert_yaxis()
plt.show()

"""Maximum number of students get themselves enroll into the course which are for beginners and for time duration of 3-6 months where one course name is The Science Of Well Being with maximum enrollments."""