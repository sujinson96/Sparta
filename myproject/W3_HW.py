import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

chart = soup.select('div#body-content > div.newest-list > div.music-list-wrap > table.list-wrap > tbody > tr.list')
ranking = 0
for songs in chart:
    ranking += 1
    title = songs.select_one('td.info > a.title.ellipsis')
    artists = songs.select_one('td.info> a.artist.ellipsis')
    if title is not None:
        print(ranking, "/", title.text.lstrip(), "/", artists.text)

