import requests as re
import bs4

def webtoon():
    url = "https://comic.naver.com/webtoon/weekday.nhn"
    res = re.get(url).text
    soup = bs4.BeautifulSoup(res)

    # data = soup.find("div", class_="list_area daily_all").find_all("div", class_="col_inner")
    data = soup.find_all("div", class_="col_inner")
    webtoons = {"mon" : [],"tue" : [],"wed" : [],"thu" : [],"fri" : [],"sat" : [],"sun" : [],}

    for n, i in enumerate(data):
        real_data = i.find_all("li")
        for j in real_data:
            title = j.find("a", class_="title").text
            link = j.find("a", class_="title")["href"]
            if n == 0:
                webtoons["mon"].append({"title" : title, "link" : link})
            elif n == 1:
                webtoons["tue"].append({"title" : title, "link" : link})
            elif n == 2:
                webtoons["wed"].append({"title" : title, "link" : link})
            elif n == 3:
                webtoons["thu"].append({"title" : title, "link" : link})
            elif n == 4:
                webtoons["fri"].append({"title" : title, "link" : link})
            elif n == 5:
                webtoons["sat"].append({"title" : title, "link" : link})
            elif n == 6:
                webtoons["sun"].append({"title" : title, "link" : link})

    return webtoons

if __name__ == "__main__":
    print(webtoon())