import requests
import datetime
from bs4 import BeautifulSoup as bs
from lxml import html
url = 'http://www.realmadrid.com/en/football/schedule'
response = requests.get(url)
html = response.content
soup = bs(html)
loc = soup.find('p', {'class': 'm_highlighted_next_game_location'}).contents
loc1 = loc[0]
if "Santiago" in loc1:
    opp = soup.find('div',{'class':'m_highlighted_next_game_team m_highlighted_next_game_second_team'}).strong.contents
else:
    opp = soup.find('div', {'class': 'm_highlighted_next_game_team'}).strong.contents
opp1=opp[0]
time = soup.find('div', {'class': 'm_highlighted_next_game_info_wrapper'}).time.contents
time1 = time[0]
date = soup.find('header', {'class': 'm_highlighted_next_game_header'}).time.contents
date1 = date[0]
times = time1.split(":")
dates = date1.split("/")

hour = times[0]
mintemp = times[1]
minutes = mintemp[:-2]
year = dates[0]
month = dates[1]
day = dates[2]
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',hour=hour,minutes=minutes,year=year,month=month,day=day,loc=loc1,opp=opp1)

if __name__ == '__main__':
    app.run(debug=True)
