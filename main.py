'''
    This is the main program to run the NewsScrayping app
    gather all headline news related to technology
'''
# import the libraries
import DisplayLatestNews
# import tkinter as tk
import gui
i = 0
us_url = 'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey='
tech_news = DisplayLatestNews.DisplayNews()
ui = gui.GUI('Breaking News')

# Delete previous one and insert the new article
def Delete_Insert(obj):
    if obj.news_lst[i] == 'No_summary':
        # Title
        title.delete('1.0', 'end')
        title.insert('1.0', f'{i+1}: {obj.titles[i]}')
        # Summary
        summary.delete('1.0', 'end')
        summary.insert('1.0', f'Cannot make the summarization.\nJump to the Website from the link below')
    else:
        # Title
        title.delete('1.0', 'end')
        title.insert('1.0', f'{i+1}: {obj.news_lst[i].title}')
        # Author
        author.delete('1.0', 'end')
        author.insert('1.0', f'{obj.news_lst[i].authors}')
        # Publish Date
        date.delete('1.0', 'end')
        date.insert('1.0', f'{obj.news_lst[i].publish_date}')
        # Summary
        summary.delete('1.0', 'end')
        summary.insert('1.0', f'{obj.news_lst[i].summary}')
        # Sentiment Analysis
        sentiment.delete('1.0', 'end')
        sentiment.insert('1.0', f'Polarity: {obj.analysis[i].polarity}, Sentiment: {"positive" if obj.analysis[i].polarity > 0 else "negative" if obj.analysis[i].polarity < 0 else "neutral"}')
    # Link 
    link.delete('1.0', 'end')
    link.insert('1.0', obj.links[i])

# Sumarize all information
def Summarize(initialize=True, ne=False, prev=False):
    global i
    global tech_news
    title.config(state='normal')
    author.config(state='normal')
    date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
    link.config(state='normal')
    if initialize:
        i = 0
        tech_news.Initialize()
        tech_news.News(us_url)
        tech_news.Summarize()
        tech_news.SentimentAnalysis()
        Delete_Insert(tech_news)
    elif ne:
        if i+1 < len(tech_news.news_lst):
            i += 1
            Delete_Insert(tech_news)
        else:
            i = 0
            Delete_Insert(tech_news)
    elif prev:
        if i-1 >= 0:
            i -= 1
            Delete_Insert(tech_news)
        else:
            i = len(tech_news.news_lst) - 1
            Delete_Insert(tech_news)
    title.config(state='disabled', bg='#dddddd')
    author.config(state='disabled', bg='#dddddd')
    date.config(state='disabled', bg='#dddddd')
    summary.config(state='disabled', bg='#dddddd')
    sentiment.config(state='disabled', bg='#dddddd')


# Jump to next article
def Next():
    Summarize(initialize=False, ne=True, prev=False)

# Back to previous one
def Previous():
    Summarize(initialize=False, ne=False, prev=True)

def jump_to_link():
    import webbrowser
    webbrowser.open_new(tech_news.links[i])

# Frame1
frame1 = ui.frame()

# Label & Text
ui.label(frame1, text='Title', side='TOP')
title = ui.text(frame1, height=1, width=140)
ui.label(frame1, text='Author', side='TOP')
author = ui.text(frame1, height=1, width=140)
ui.label(frame1, text='Publication', side='TOP')
date = ui.text(frame1, height=1, width=140)
ui.label(frame1, text='Summary', side='TOP')
summary = ui.text(frame1, height=20, width=140)
ui.label(frame1, text='Sentiment Analysis', side='TOP')
sentiment = ui.text(frame1, height=1, width=140)
ui.label(frame1, text='Link', side='TOP')
link = ui.text(frame1, height=1, width=140)
ui.pack(frame1)

# Frame2
frame2 = ui.frame()
# add button to get user input
ui.button(frame2, Summarize, text='Get the Latest News', side='LEFT')
ui.button(frame2, Previous, text='Previous', side='LEFT')
ui.button(frame2, Next, text='Next', side="LEFT")
ui.button(frame2, jump_to_link, text='Jump To the Web', side="LEFT")
ui.pack(frame2)

ui.end()