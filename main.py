# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
#     import requests
#     import bs4 as bs
#
#     url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
#     html = requests.get(url).text
#     soup = bs.BeautifulSoup(html, "html")
#     data = soup.find("body")
#
#     coronaApi = {"API Name": "Corona API"}
#
#     criteria = data.find("span", class_="t_date").text.split("기")[0][1:-1]  # 기준이 되는 시각을 가져와서 저장한다.
#     coronaApi["criteria"] = criteria
#
#     real_data = data.find("div", class_="caseTable").find_all(class_="ca_value")
#
#     total = real_data[0].text  # 현재 총 확진자수
#
#     total_add_all = real_data[1].find_all("p", class_="inner_value")[0].text  # 전날 대비 증가 확진자
#     total_add_in = real_data[1].find_all("p", class_="inner_value")[1].text  # 전날 대비 증가 확진자중 국내발생
#     total_add_out = real_data[1].find_all("p", class_="inner_value")[2].text  # 전날 대비 증가 확진자중 해외유입
#
#     heal = real_data[2].text  # 완치 환자수
#     heal_add = real_data[3].find("span").text  # 완치 환자수 전날 대비 증가수
#
#     ing = real_data[4].text  # 현재 치료중 환자 수
#     ing_add = real_data[5].find("span").text  # 현재 치료중 환자수 전날 대비 증가수
#
#     pass_away = real_data[6].text  # 사망자수
#     pass_away_add = real_data[7].find("span").text  # 사망자수 전날대비 증가수
#
#     coronaApi["total"] = total
#     coronaApi["total_add_all"] = total_add_all
#     coronaApi["total_add_in"] = total_add_in
#     coronaApi["total_add_out"] = total_add_out
#
#     coronaApi["heal"] = heal
#     coronaApi["heal_add"] = heal_add
#
#     coronaApi["ing"] = ing
#     coronaApi["ing_add"] = ing_add
#
#     coronaApi["pass_away"] = pass_away
#     coronaApi["pass_away_add"] = pass_away_add
#
#     print(coronaApi)
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
