'''
    This program gathers the latest news from the sqecific website and 
    display the surmarized contents with URLs to users 
'''

class DisplayNews:
    api_key='4c1a1c54c33448769c28562963273919' # have to hide it if it opens to public
    def __init__(self):
        # initialize the variables and libraries
        # self.url = url + self.api_key
        self.titles = []
        self.links = []
        self.news_lst = []
        self.analysis = []

    # Gain all article's title and links
    def News(self, url):
        import copy
        import requests
        self.news = requests.get(url+DisplayNews.api_key).json()
        self.articles = self.news['articles']
        link_lst = [arti['url'] for arti in self.articles]
        title_lst = [arti['title'] for arti in self.articles]
        self.links = copy.copy(link_lst)
        self.titles = copy.copy(title_lst)

    def Summarize(self):
        # import libraries
        from newspaper import Article
        import nltk
        # update punkt just in case
        # nltk.download('punkt')
        
        # Summarize article
        for i in range(len(self.links)):
            try:
                article = Article(self.links[i]) # make obj using the specific article
                article.download() # download the article
                article.parse() # divide article into each part such as title, text, etc
                article.nlp() # nutral language process
                self.news_lst.append(article)
            except:
                self.news_lst.append('No_summary')
                continue
    
    # Use just to check if it rightly downloads
    def Display_News(self):
        for i in range(len(self.news_lst)):
            print(i+1)
            if self.news_lst[i] == 'No_summary':
                print('Title: ', self.titles[i])
                print('No Summary Click the link below')
                print(self.links[i])
            else:
                print('Title: ', self.news_lst[i].title)
                print('Authors: ', self.news_lst[i].authors)
                print('Publication Date: ', self.news_lst[i].publish_date)
                print('Summary: ', self.news_lst[i].summary)
                print('Links: ', self.links[i])
            print()

    def SentimentAnalysis(self):
        from textblob import TextBlob as tb
        for i in range(len(self.news_lst)):
            if self.news_lst[i] == 'No_summary':
                self.analysis.append(' ')
                continue
            self.analysis.append(tb(self.news_lst[i].text))

    def Get_links(self):
        return self.links

    def Initialize(self):
        self.titles.clear()
        self.links .clear()
        self.news_lst.clear()
        self.analysis.clear()

# bus_url = 'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey='
# dn = DisplayNews(us_url)
# dn.news()
# dn.Display()
# print(dn.url)