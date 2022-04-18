import requests
import bs4 as bs


# 뉴스토픽 목록을 가져온다.
def get_news_topics():
    url = "https://search.naver.com/search.naver?query="
    html = requests.get(url).text
    soup = bs.BeautifulSoup(html)
    data = soup.find_all("div", class_="list_wrap _content")[0].find_all("span", class_="txt")
    data = [i.text for i in data]
    return data


# 네이버 뉴스 rss에 검색을 한다.
def get_search_news(key):
    url = "http://newssearch.naver.com/search.naver?where=rss&query=" + key
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    html = requests.get(url).text.encode("latin")
    soup = bs.BeautifulSoup(html, "xml")
    data = soup.find_all("item")

    text = f"{key}로 검색한 결과입니다.\n\n"
    for i in data:
        title = i.find("title").text
        link = i.find("link").text
        description = i.find("description").text
        text += f"제목 : {title}\n링크 : {link}\n미리보기 : {description}\n\n"

    return text


# 뉴스를 검색해서 미리보기 내용들을 다 가져온다.
def get_search_news_description(key):
    url = "http://newssearch.naver.com/search.naver?where=rss&query=" + key
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    html = requests.get(url).text.encode("latin")
    soup = bs.BeautifulSoup(html, "xml")
    data = soup.find_all("item")

    text = ""
    for i in data:
        title = i.find("title").text
        description = i.find("description").text
        text += title + description

    return text


# 인자로 받은 텍스트로 워드 클라우드를 만들고, 저장한다.
def make_Wordcloud(name, text):
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    # font = "C:/Windows/Fonts/malgun.ttf"
    font = "C:/Users/user/AppData/Local/Microsoft/Windows/Fonts/NotoSansCJKkr-Regular.otf"

    wc = WordCloud(width=1600, height=900, font_path=font)  # 워드 클라우드를 만드는 객체
    result = wc.generate_from_text(text).to_array()
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(result, interpolation="bilinear")
    # print(name)

    plt.savefig(f"img/{name}.png")


def naver_news_all():
    list_ = get_news_topics()
    for n, i in enumerate(list_):
        print(f"{n+1}/10",end="\r")
        text = get_search_news_description(i)
        make_Wordcloud(i, text)

    return list_

if __name__ == "__main__":
    naver_news_all()