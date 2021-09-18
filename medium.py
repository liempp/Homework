# Medium 1: Kiểm trả True False

n=121121
def anagram_number(n):
    str1 = f"{n}"    
    str2 = str1[::-1] 
    if (str1 == str2):
        return True
    else:
        return False
anagram_number(n)
print (anagram_number(n))

# Medium 2: In số La Mã

