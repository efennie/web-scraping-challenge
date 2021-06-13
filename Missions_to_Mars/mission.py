# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#I worked with Arianne on this homework

#import dependencies
from splinter import Browser
import pandas as pd
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests


# %%
#splinter set up
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# %%
#set url and visit it
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)


# %%
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
soup


# %%
#find container for news titles
results = soup.find_all('div', class_='features')
results


# %%
for result in results:

        news_title = result.find('div', class_='content_title').text
        news_p = result.find('div', class_='rollover_description_inner').text
        print(news_title)
        print(news_p)


# %%
#get latest title
results = soup.find('div', class_='content_title').text
print(results)


# %%
#paragraph
results = soup.find('div', class_='rollover_description_inner').text
print(results)


# %%
#splinter set up
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# %%
#second scrape
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# %%
response = requests.get(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
soup


# %%
#header image fade in
results = soup.find_all('div', class_='header')

for result in results:
    picture = result.find('a', class_='showimg fancybox-thumbs')
    link = picture['href']

    print(link)


# %%
#mars facts
url = 'https://space-facts.com/mars/'


# %%
#pull table from url
tables = pd.read_html(url)
tables


# %%
#make the table into a dataframe and rename columns
dataframe = tables[0]
dataframe = dataframe.rename(columns={0:'Point of Interest'})
dataframe = dataframe.rename(columns={1:'Mars'})
dataframe


# %%
#convert dataframe to an html string
html_table = dataframe.to_html()
html_table


# %%
#get the urls to the hi-res images of mars hemispheres
hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}
]
hemisphere_image_urls


# %%



