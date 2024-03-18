import requests
from bs4 import BeautifulSoup

def get_baidu_homepage():
    url = "https://www.baidu.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup.prettify()

if __name__ == "__main__":
    baidu_homepage = get_baidu_homepage()
    print(baidu_homepage)



