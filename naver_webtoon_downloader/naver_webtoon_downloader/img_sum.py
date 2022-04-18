import glob
from PIL import Image

from .img_download import *

def img_sum(img_list, name, size, save_path):
    """이미지 경로가 담겨있는 리스트와 저장할 이름, 크기, 저장 경로를 입력 받아서 경로로 받은 이미지를 세로형으로 합쳐준다."""
    # input 파일 path
#     imgs = glob.glob("C:/Users/user/save/외모지상주의/1화/*.png")#[:30]
    makedirs(save_path)
#     width = size[0]
#     total_height = size[1]
    canvas = Image.new("RGB", size, (255, 255, 255))
    # canvas.show()
    now_height = 0
    for n, i in enumerate(img_list):
        im = Image.open(i)
        height = im.size[1]
        canvas.paste(im, (0, now_height))
        now_height += height

    canvas.save(f"{save_path}{name}.png")


def webtoon_sum(webtoon_name, no):
    """저장된 웹툰 이미지를 합쳐준다."""
#     webtoon_name = "랜덤채팅의 그녀!"
#     no = 3

    img_list = glob.glob(f"save/{webtoon_name}/{no}화/*.png")
    # img_list
    sum_img_list = []
    max_width, total_height = 0, 0
    count = 1
    for n, i in enumerate(img_list):
        im = Image.open(i)
        width, height = im.size
        if max_width < width:
            max_width = width
        total_height += height
        sum_img_list.append(i)

        if total_height > 6000:
            img_sum(sum_img_list, "%02d" % count, (width, total_height), f"save/{webtoon_name}/정리/{no}화/")
            sum_img_list = []
            max_width, total_height = 0, 0
            count += 1
    img_sum(sum_img_list, "%02d" % count, (width, total_height), f"save/{webtoon_name}/정리/{no}화/")