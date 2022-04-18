import os
import sys
import urllib.request
import requests as re
import json


def get_translation(source, target, text):
    client_id = "KiKBI7U6MP7_ETeviBYf"
    client_secret = "N_t5x8fBG_"
    encText = urllib.parse.quote(text)
    data = f"source={source}&target={target}&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if (rescode == 200):
        response_body = json.loads(response.read().decode("utf-8"))

        return response_body
    #     print(response_body.decode('utf-8'))
    else:
        return rescode


#         print("Error Code:" + rescode)


def translation(source, target, text):
    translation = get_translation(source, target, text)

    translation_data = translation["message"]["result"]
    s_lang = translation_data["srcLangType"]
    t_lang = translation_data["tarLangType"]
    translation_text = translation_data["translatedText"]

    return {"s_lang": s_lang, "t_lang": t_lang, "text": translation_text}


#     print(f"{s_lang} -> {t_lang} / {translation_text}")

def all(s_lang, t_lang, text):
    first = translation(s_lang, "ja", text)
    scond = translation("ja", t_lang, first["text"])
    direct = translation(s_lang, t_lang, text)

    if s_lang == "ko":
        s_lang = "한국어"
        t_lang = "영어"
    else:
        s_lang = "영어"
        t_lang = "한국어"
    return {"source_lang": s_lang, "target_lang": t_lang, "text": text, "indirect": scond, "direct": direct}


def n_to_brTag(text):
    return text.replace("\n", "<br>")

# text_en = """Hello, viewers. Thank you for clicking on this video. I’m Ronnie Drain, and
# I’ve been a personal fitness trainer for over 15 years. Today, I’d like to tell
# you about my channel, Build Your Body. On my channel, you can watch
# videos showing you how to do a variety of exercises that you can do at
# home or at your office. If you’ve experienced difficulty exercising regularly,
# my videos can provide easy guidelines and useful resources on exercise
# routines. New videos will be uploaded every Friday. Visit my channel and
# build a stronger, healthier body."""

# text_ko = """동해 물과 백두산이 마르고 닳도록
# 하느님이 보우하사 우리나라 만세.
# 무궁화 삼천리 화려 강산
# 대한 사람, 대한으로 길이 보전하세."""

# t = all("ko", "en", text_ko)
# print(f'{"ko"}->{"ja"}->{"en"}\n\n{t["indirect"]["text"]}\n\n{"ko"}->{"en"}\n\n{t["direct"]["text"]}')