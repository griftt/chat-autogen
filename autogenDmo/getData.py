import requests
import html2text
from bs4 import BeautifulSoup

def contains_specific_path(url):
    paths_to_check = ["/SessionPage", "/ChromiumPage", "/WebPage"]
    return any(path in url for path in paths_to_check)



url = "/get_start/installation"
def getPageData(url:str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # 寻找页面中所有的链接
    links = soup.find_all('a')
    print(links)
    # 创建html2text处理器
    h = html2text.HTML2Text()
    h.ignore_links = False
    for link in links:
        page_url = link.get('href')
        if contains_specific_path(page_url):
            page_response = requests.get(page_url)
            page_content = page_response.text
            print('## ' + link.text + '\n')  # 打印链接的文本作为标题
            print(h.handle(page_content))  # 将页面内容转为markdown并输出

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
}
url_list=[]
def contains_ext_path(url):
    return url not in url_list
def remove_all_attrs_except(soup):
    whitelist = []  # 白名单
    for tag in soup.findAll(True):
        if tag.name not in whitelist:
            tag.attrs = {}
    return soup

def parse_page(url, prefix, h):
    response = requests.get(prefix+url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # new_soup = BeautifulSoup(response.text, 'html.parser')
    # 寻找页面中所有的链接
    links = soup.find_all('a')
    # soup = remove_all_attrs_except(soup)

    for link in links:
        page_url = link.get('href')
        if page_url.startswith("/") and   contains_specific_path(page_url) and  contains_ext_path(page_url):
            print(page_url)
            url_list.append(page_url)
            page_response = requests.get(prefix+page_url, headers=headers)
            soup_page = BeautifulSoup(page_response.text, 'html.parser')
            #context=response.content.decode(response.encoding, errors='replace')
            context=soup_page.body.get_text()
            with open("dr/"+page_url.replace("/","_")+".txt", "a", encoding=response.encoding) as f:
                f.write('## ' + link.text + '\n')  # 打印链接的文本作为标题
                f.write(context)  # 将页面内容转为markdown并输出

            parse_page(page_url,prefix, h)  # 递归地抓取链接指向的页面


h = html2text.HTML2Text()
h.ignore_links = False

parse_page(url,"https://drissionpage.cn", h)