import os, time, random
import requests as re
import bs4 as bs


# homePAth = "C:/Users/user/"

def downloadIMG(url, name, save_path):
    """이미지의 주소로 이미지를 저장한다."""
    from io import BytesIO
    from PIL import Image

    # 다운받을 이미지 url
    #     url = "https://image-comic.pstatic.net/webtoon/758037/12/20210115183728_09fb65f4c074b9f958b409f75c108aaf_IMAG01_1.jpg"

    # request.get 요청
    res = re.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    # Img open
    # img = Image.open(BytesIO(res.content))
    img = Image.open(BytesIO(res.content))
    img.save(f"{save_path}{name}.png")


def makedirs(path):
    """
    해당 주소의 폴더가 있는지 확인하고 없으면 폴더를 만든다.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def get_webtoon_data(code, no):
    """선택한 웹툰의 제목, 작가, 선택한 화의 이미지 갯수, 이미지 url을 가져온다."""
    url = f"https://comic.naver.com/webtoon/detail.nhn?titleId={code}&no={no}"
    html = re.get(url).text
    soup = bs.BeautifulSoup(html)

    # 웹툰의 제목과 작가를 가져온다.
    data_1 = soup.find("div", class_="comicinfo").find("h2")
    title = data_1.text.split("\t")[0].rstrip()
    writer = data_1.find("span", class_="wrt_nm").text[8:].split("\t")[1][1:]

    # 성택한 화의 이미지 갯수, 기본 url을 가져온다.
    data_2 = soup.find("div", class_="wt_viewer").find_all("img")
    nomal_urls = []

    for i in data_2:
        if i["alt"] == "comic content":
            nomal_urls.append(i["src"])
    count = len(nomal_urls)
    return {"title": title, "writer": writer, "count": count, "nomal_urls": nomal_urls, "code": code}


def download_webtoon(webtoon_code, webtoon_no):
    data = get_webtoon_data(webtoon_code, webtoon_no)
    webtoon_title = data["title"]
    nomal_urls = data["nomal_urls"]
    count = data["count"]
    savePath = f"save/{webtoon_title}/{webtoon_no}화/"

    makedirs(savePath)

    for n, url in enumerate(nomal_urls):
        #         url = nomal_url + str(i) + ".jpg"

        downloadIMG(url, "%.3d" % n, savePath)

        # 현재 진행 로딩바
        # 나중에 수정할 예정
        """
        p = round(n / count * 100, 2)
        print(f"{'■' * int(p / 10 + 0.5)}{'□' * int(10 - p / 10)} {n}/{count}({p}%)", end="\r")
        """

        time.sleep(1 + random.random())
    print(f"Webtoon download END!!\n({webtoon_title} {webtoon_no}화)         ")


def get_naver_webtoon_list():
    url = "https://comic.naver.com/webtoon/weekday.nhn"
    html = re.get(url).text
    soup = bs.BeautifulSoup(html)
    webtoon_list = {}
    data = soup.find_all("div", class_="col_inner")
    for n, i in enumerate(data):
        webtoon_list["%02d" % n] = []
        #     print("="*100)
        data_2 = i.find_all("li")
        for j in data_2:
            data_3 = j.find("a")
            code = data_3["href"].split("titleId=")[1].split("&")[0]
            title = data_3.find("img")["title"]

            webtoon_list["%02d" % n].append({"title": title, "code": code})
    #         print({"title" : title, "code" : code})
    return webtoon_list


def switch_row_col(data):
    max_ = max([len(i) for i in data.values()])
    new_data = []
    list_ = []
    for i in ["월", "화", "수", "목", "금", "토", "일"]:
        list_.append({"title": i})
    new_data.append(list_)
    for i in range(max_):
        list_ = []
        for j in range(7):
            try:
                list_.append(data["%02d" % j][i])
            #             print(data["%02d" % j][i])
            except IndexError:
                #                 list_.append({"title" : 1, "code" : 1})
                list_.append(1)
        #     print(list_)
        #     print("=" * 100)
        new_data.append(list_)
    return new_data


def get_webtoon_ep_list(code):
    """웹툰 코드를 받아서 해당 웹툰의 에피소드 목록을 가져온다."""
    import requests as re
    import bs4 as bs

    list_ = []
    page = 1
    # code = 702608
    while 1:
        url = f"https://comic.naver.com/webtoon/list.nhn?titleId={code}&page={page}"
        html = re.get(url).text
        soup = bs.BeautifulSoup(html)

        #     page_data = soup.find("div", class_="page_wrap")
        #     now_page = page_data.find("strong", class_="page").find("em").text
        #     print(now_page)
        #     break

        page_data = soup.find("div", class_="page_wrap")
        now_page = page_data.find("strong", class_="page").find("em").text
        if str(page - 1) == now_page:
            break
        else:
            page += 1

        data = soup.find("table").find_all("tr")[1:]
        for i in data:
            try:
                if i["class"] == "band_banner v2":
                    continue
            except:
                title = i.find("td", class_="title").text.replace("\n", "")
                list_.append(title)
    #                 print(title)
    data = []
    for n, i in enumerate(list_[::-1]):
        data.append({n + 1: i})
    return data


def get_webtoon_ep_list(code):
    """웹툰 코드를 받아서 해당 웹툰의 에피소드 목록을 가져온다."""
    import requests as re
    import bs4 as bs

    list_ = []
    page = 1
    # code = 702608
    while 1:
        url = f"https://comic.naver.com/webtoon/list.nhn?titleId={code}&page={page}"
        html = re.get(url).text
        soup = bs.BeautifulSoup(html)

        #     page_data = soup.find("div", class_="page_wrap")
        #     now_page = page_data.find("strong", class_="page").find("em").text
        #     print(now_page)
        #     break

        page_data = soup.find("div", class_="page_wrap")
        now_page = page_data.find("strong", class_="page").find("em").text
        if str(page - 1) == now_page:
            break
        else:
            page += 1

        data = soup.find("table").find_all("tr")[1:]
        for i in data:
            try:
                if i["class"] == "band_banner v2":
                    continue
            except:
                title = i.find("td", class_="title").text.replace("\n", "")
                list_.append(title)
    #                 print(title)

    #     return list_[::-1]
    data = []
    for n, i in enumerate(list_[::-1]):
        data.append({"no": n + 1, "title": i})
    return data

# def get_webtoon_data(code):
#     """기존의 get_webtoon_data와 합쳐짐, 내가 ㅂㅅ이었다...."""
#     """웹툰 코드를 받아와서 웹툰 제족, 작가의 정보를 가져옵니다."""
#     url = f"https://comic.naver.com/webtoon/list.nhn?titleId={code}"
#     html = re.get(url).text
#     soup = bs.BeautifulSoup(html)
#     data = soup.find("div", class_="comicinfo").find("h2")
#     writer = data.find("span", class_="wrt_nm").text[8:]#.split("\n")
#     title = data.text.split("        ")[1].split("\n")[0]
# #     print(f"{title}, {writer}")
#     return {"title" : title, "writer" : writer}