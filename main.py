import random
import math
import datetime

# 曜日
jpn_weekday = ["月", "火", "水", "木", "金", "土", "日"]

current_year = datetime.date.today().year        # 今年
date_first = datetime.date(current_year, 1, 1)   # 処理対象の初日
date_last  = datetime.date(current_year, 12, 31) # 処理対象の最終日

for i in range(10):
    rand = random.randint(0, abs(date_last - date_first).days)
    rand_date = date_first + datetime.timedelta(days=rand)
    print(rand_date)
