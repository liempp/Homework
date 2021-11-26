# Sorting - Sắp xếp điểm thi
def sort_list(elem):
    return elem[2]
ls= [(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]
sort_list_last = sorted(ls, key=sort_list)

print('Sắp xếp điểm thi:', sort_list_last)

#bài 2: Xử lý chuỗi - Đảo ngược từ và kiểu hoa thường
string='tHE fOX iS cOMING fOR tHE cHICKEN'
def reverse_sring(string):
  word=string.split()
  reverse_sring=' '.join(reversed(word))
  return reverse_sring 

print("Chuỗi sau khi đảo ngược là: ", reverse_sring(string))
print("Chuỗi sau khi đổi các kí tự hoa sang kí tự thường là: ",reverse_sring(string).swapcase())