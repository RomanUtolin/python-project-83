import requests
from bs4 import BeautifulSoup


def get_seo_data(url):
    tags = ['meta', 'h1', 'title']
    dict_tags = {'description': None,
                 'h1': None,
                 'title': None,
                 'status_code': None}
    try:
        get_html = requests.get(url)
        status_code = get_html.status_code
        dict_tags['status_code'] = status_code
        return find_tag(get_html, tags, dict_tags)
    except Exception as e:
        print(e)
        return dict_tags


def find_tag(html, tags, dict_tags):
    soup = BeautifulSoup(html.text, 'html.parser')
    for t in tags:
        if t == 'meta' and soup.find("meta", attrs={"name": "description"}):
            dict_tags['description'] = \
                soup.find("meta", attrs={"name": "description"}).get("content")
        else:
            if soup.find(t):
                dict_tags[t] = soup.find(t).getText()
    return dict_tags
