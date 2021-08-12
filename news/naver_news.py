import urllib.request
import datetime
import json
from .config import *

def do_request(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", app_id)
    req.add_header("X-Naver-Client-Secret", secret_id)
    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            print("Url Request Success")
            return res.read().decode('utf-8')
    except Exception as e:
        print("Error for URL :", e)
        return None

def append_post(post, json_result):
    # 요일, 일 월 년 시:분:초 +0900 -> 연-월-일 시:분:초
    pubDate = datetime.datetime.strptime(post['pubDate'],
                                    '%a, %d %b %Y %H:%M:%S +0900') \
                .strftime('%Y-%m-%d %H:%M:%S')
    
    json_result.append({
        'title': post['title'],
        'description': post['description'],
        'originallink': post['originallink'],
        'link': post['link'],
        'pubDate': pubDate
    })

def get_news_json(search_text, page_start, display):
    query = urllib.parse.quote(search_text)
    parameters = f"?query={query}&start={page_start}&display={display}"
    url = "https://openapi.naver.com/v1/search/news.json" + parameters

    ret_data = json.loads(do_request(url))
    json_result = []
    if (ret_data):
        for post in ret_data['items']:
            append_post(post, json_result)
        return json_result

def main():
    search_text = '와인'
    start = 1
    display = 100
    
    json_result = get_news_json(search_text, start, display)
    print(json_result)
    

if __name__ == '__main__':
    main()
