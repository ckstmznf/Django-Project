from django.shortcuts import render, redirect, HttpResponse
from .img_download import *
from .img_sum import *
from .naver_webtoon_download import *

def test(request):
    return render(request, "test.html")

def main(request):
    data = get_naver_webtoon_list()
    data = switch_row_col(data)
    content = {"data" : data}
    return render(request, "index.html", content)

def webtoon(request, code):
    data = get_webtoon_data(code, 1)
    ep_list = get_webtoon_ep_list(code)
    content = {
        "data" : data,
        "ep_list" : ep_list,
    }
    return render(request, "webtoon.html", content)

def download(request, mode, code):
    # code = request.GET.get("code")
    data = get_webtoon_data(code, 1)
    no = request.GET.get("no")
    content = {
        "title" : data["title"],
    }

    # if mode == "all":
    #     pass
    if mode == "choice":
        no_list = request.GET.getlist("no")
        for i in no_list:
            webtoon_download_all(code, i)
        content["no"] = no_list

    elif mode == "all":
        bot_send("START")
        list_ = get_webtoon_ep_list(code)
        content["no"] = "전체"
        for i in range(1, len(list_) + 1):
            try:
                webtoon_download_all(code, i)
            except:
                bot_send(f"ER {i}화")
                continue

        bot_send("END!!!!!!!!")
    else:
        return redirect("/")

    # return redirect("../bot/Hello_World")
    return render(request, "completion.html", content)

def testRe(request):
    
    return HttpResponse(request.GET.getlist("no"))


def bot_send(text): #나에게 메시지 보내는 함수
    import telegram
    bot_id = "1047630281:AAECVgc8DQ2fzxuyrEuPfn8s6DIRUmEEudk" #bot Id
    bot = telegram.Bot(token = bot_id)
    user_id = "673180629"
    bot.send_message(chat_id = user_id, text = text)

def bot(request, text):
    bot_send(text)
    return redirect("/")
