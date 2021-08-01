# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 19:33:59 2021

"""

'''
To get this to work with Selenium, include:
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
Download Chromedriver
Add selenium==3.141.0 and webdriver-manager==3.4.2 to requirements.txt
Add buildpack for chromedriver and chrome to heroku

To get this to work with requests, include:
import requests
Add beautifulsoup4==4.7.1, requests==2.22.0, and lxml to requirements.txt 
<< unfortunately, due to U.GG's inclusion of more JS, page_source no longer has the key data this script relies on
'''

import requests
from bs4 import BeautifulSoup, SoupStrainer
#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

class WebScraper:
    
    headers = {'User-Agent': 'User agent here', 
               'Accept-Encoding': 'gzip'}

    def __init__(self,url = 'https://u.gg/lol/champions/talon/build?rank=diamond_plus',rank = 'Platinum+',region = 'worldwide',role = 'mid'):
        self.url = url
        if rank == '': 
            self.rank = 'Platinum+'
        else: 
            self.rank = rank
        self.region = region
        self.role = role
    def champName(self):
        parseUrl = self.url.split('/')
        return parseUrl[len(parseUrl)-2].capitalize()
    def roleName(self):
        if self.role == 'top':
            return 'top'
        elif self.role in {'jg','jungle'}:
            return 'jungle'
        elif self.role in {'mid','middle'}:
            return 'mid'
        elif self.role in {'adc','bot'}:
            return 'adc'
        elif self.role in {'supp','support'}:
            return 'supp'
        else:
            return 'mid'
    def regionName(self):
        if self.region == 'kr':
            return 'KR'
        elif self.region == 'na':
            return 'NA'
        elif self.region in {'eu','euw'}:
            return 'EUW'
        elif self.region == 'br':
            return 'BR'
        elif self.region in {'eune','eun'}:
            return 'EUNE'
        elif self.region == 'jp':
            return 'JP'
        elif self.region == 'lan':
            return 'LAN'
        elif self.region == 'las':
            return 'LAS'
        elif self.region == 'oce':
            return 'OCE'
        elif self.region == 'ru':
            return 'RU'
        elif self.region == 'tr':
            return 'TR'
        else:
            return 'worldwide'
    def parse(self):
        '''
        !! Uncomment this section for Selenium here !!
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('--disable-gpu')
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--disable-dev-shm-usage')       
        driver = webdriver.Chrome(chrome_options = chromeOptions, executable_path = ChromeDriverManager().install())
        driver.get(self.url)
        htmlText = driver.page_source
        '''
        #This block uses requests
        html = requests.get(self.url, headers = self.headers)
        if html.status_code != 200:
            return
        htmlText = html.text
        #
        parse_only = SoupStrainer('div', class_ = 'content-section champion-ranking-stats')
        soup = BeautifulSoup(htmlText, 'lxml', parse_only = parse_only)
        values = soup.find_all('div', class_ ='value')
        if not values:
            return 'Not enough data'
        elo = self.rank
        role = self.roleName()
        champName = 'Talon'
        region = self.regionName()
        statsBar = []
        for entry in values:
            statsBar.append(entry.text)
        if region == 'worldwide':
            return '{champName} {role} has a {winrate} winrate with a pickrate of {pickrate} and a banrate of {banrate} in {elo} over {numGames} game(s) {region}.'.format(
                    champName = champName, role = role, winrate = statsBar[0], pickrate = statsBar[2], banrate = statsBar[3], elo = elo, numGames = statsBar[4], region = region)
        return '{champName} {role} has a {winrate} winrate with a pickrate of {pickrate} and a banrate of {banrate} in {elo} over {numGames} game(s) in {region}.'.format(
                champName = champName, role = role, winrate = statsBar[0], pickrate = statsBar[2], banrate = statsBar[3], elo = elo, numGames = statsBar[4], region = region)
'''
if __name__ == '__main__':
    webScrape = WebScraper('https://u.gg/lol/champions/talon/build?region=br1&role=adc&rank=diamond_plus')
    print(webScrape.parse())
'''