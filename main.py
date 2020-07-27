# from bs4 import BeautifulSoup
# import requests
# import json,re,requests,os
# # from requests.auth import HTTPBasicAuth
# from nltk.tokenize import word_tokenize,sent_tokenize
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.chrome.options import Options
# from imgurpython import ImgurClient
# # from nltk.corpus import stopwords
# # from nltk.cluster.util import cosine_distance
# # import numpy as np
# # import networkx as nx
# import random

 

# class Brainsfeed:
#     def __init__(self):
#         self.headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
#         self.output = []

#     # funtion for extracting data from url

#     def Extact_data(self,url,driver):
#         page=requests.get(url,headers=self.headers)
#         soup=BeautifulSoup(page.content,'html.parser')
#         title=soup.find('title').get_text()
#         title=title.strip()
#         title = word_tokenize(title)
#         name =[]
#         ti = []
#         details = {}

#         # finding company name and title

#         for t in title:
#             if t.lower() in url.lower():
#                 name.append(t)
#             else:
#                 if t.isalpha() and t not in ti:
#                     ti.append(t)
#         name =' '.join(name)
#         ti = ' '.join(ti)
#         details['given_website'] = url
#         details['company name']=name
#         details['title'] = ti
        
#         # taking screen shot of the given webpage

#         driver.get(url)
#         sleep(1)
#         ssname = name+"_screenshot.png"
#         img =driver.get_screenshot_as_file(ssname)
#         print(img)
#         #uploading the screen shot to cloud i.e. imgur.com

#         client = ImgurClient('4f96f803994e408','a6454bc1d78317f1076f6abab1b3d1b270f56ee7')
#         image = client.upload_from_path(ssname)
#         os.remove(ssname)
#         details['website screenshot'] = image['link']
#         contact = 'unknown'
#         content = re.sub(r'[^\x00-\x7F]+',' ', soup.text.replace('\n', ''))

#         # finding contact email

#         mails = lst = re.findall('\S+@\S+', content) 
#         for mail in mails:
#             if name.lower() in mail.lower():
#                 contact = mail
#                 break
        
#         # fetching data from website for short description and webite summary

#         #open source api for text summarization
#         r = requests.post(
#             "https://api.deepai.org/api/summarization",
#             data={
#                 'text':content.strip() ,
#             },
#             headers={'api-key': '4d380c43-71aa-4875-b864-ebb57fc98f98'}
#         )
        
#         try:
#             details['short_description'] = random.choice(sent_tokenize(r.json()['output']))
#             details['website_summary'] = r.json()['output']

#         except:
#             details['short description'] = 'request time out'
#             details['website summary'] = 'request timeout'
       
#         # for finding wheter a website has pricing or subscription or not 

#         pricing = soup.findAll('ul')
#         flag = 0
#         for x in pricing:
#             if ('pricing' in x.text.lower() or 'subscription' in x.text.lower() or 'customers' in x.text.lower()) and flag ==0:
#                 details['Is the website has paid service?'] = 'has paid services'
#                 flag =1
#         if flag ==0:
#             pricing = soup.findAll('a')
#             for y in pricing:
#                 if ('pricing' in y.text.lower() or 'subscription' in y.text.lower() or 'customers' in y.text.lower()) and flag ==0:
#                     details['Is the website has paid service?'] = 'has paid services'
#                     flag =1
#             if flag == 0:
#                 details['Is the website has paid service?'] = 'unknown'
        
#         self.output.append(details)
   
#    # function to push data into csv file

#     def Add_information(self,to_store):
#         import csv

#         keys = to_store[0].keys()
#         with open('demo1_brainsfeed_junior_data_&_automation_engineer.csv', 'w') as output_file:
#             dict_writer = csv.DictWriter(output_file, keys)
#             dict_writer.writeheader()
#             dict_writer.writerows(to_store)
    
    

    
# if __name__ =='__main__':
#     url_list = ['http://aytm.com','http://www.datawallet.com','https://www.fancyhands.com/','https://starmind.ai/','http://stackoverflow.com/']
#     obj = Brainsfeed()
#     options = webdriver.ChromeOptions()
#     options.headless = True
#     # driver = webdriver.Firefox()
#     driver = webdriver.Chrome(executable_path = 'C:\\Users\\Abdul salam\\Desktop\\chromedriver.exe',options=options)
#     for url in url_list:
        
#         obj.Extact_data(url,driver)
       
#     to_store = obj.output
#     obj.Add_information(to_store)
#     driver.quit()


from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'done!'

if __name__ == '__main__':
    app.run()

