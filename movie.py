import requests
from bs4 import BeautifulSoup
def get_rank():
    titles = []
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('.tit3 > a')
        for i, title in enumerate(titles):
            print(f"{i+1}. {title.get_text()}")

    else : 
        print(response.status_code)

    return titles