# 1 Easy 1 In số ngày
from datetime import datetime
rd="19/12/2021"
date_format="%d/%m/%Y"
release_date = datetime.strptime(rd,date_format)
cd= "2021/17/5"
date_format1="%Y/%d/%m"
code_complete_day = datetime.strptime(cd,date_format1)
def day_diff(release_date,code_complete_day):
    result=release_date-code_complete_day
    print("số ngày mà team test có để test sản phẩm: ",result)
day_diff(release_date,code_complete_day)


# 2 Easy 2 In ra từ có cả ký tự chữ và số
import re
sentence = "Emma25 is Data scientist50 and AI Expert 2gild"
def alpha_num(sentence):
    str=sentence.split()
    result_str=re.findall("\d+[a-zA-Z]+|[a-zA-Z]*\d+",sentence)
    print(result_str)
alpha_num(sentence)

