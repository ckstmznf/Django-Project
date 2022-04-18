from .img_download import *
from .img_sum import *


def webtoon_download_all(code, no):
    data = get_webtoon_data(code, no)
    download_webtoon(code, no)
    webtoon_sum(data["title"], no)