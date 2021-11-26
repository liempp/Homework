# Bài Function - Chỉ số thống kê mô tả
# Cách 1
# import statistics
# A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
# mean =statistics.mean(A)
# median=statistics.median(A)
# mode=statistics.mode(A)
# print('(','mean(A)','Median(A)','Mode(A)',')','==''(', mean,',', median,',','[', mode,']',')')


# B=[4,4,5,4,5,5] 
# mean =statistics.mean(B)
# median=statistics.median(B)
# mode=statistics.mode(B)
# print('(','mean(B)','Median(B)','Mode(B)',')','==''(', mean,',', median,',','[', mode,']',')')


# Cách 2
A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
def mean(A):
  return sum(A)/len(A)
mean=mean(A)
# print (mean)
def median(A):
  A= sorted(A)
  n=len(A)
  if n % 2 == 1:
      return A[n//2]
  else:
      i = n//2
      return (A[i - 1] + A[i])/2
median= median(A)

def mode(A):
    Amax = A[0]
    for d in A:
        if A.count(d) > A.count(Amax):
            Amax = d
    return Amax
mode= mode(A)
  
print('(','mean(A)','median(A)','mode(A)',')','==''(', mean,',', median,',','[', mode,']',')')

B=[4,4,5,4,5,5]
def mean(B):
  return sum(B)/len(B)
mean=mean(B)
# print (mean)
def median(B):
  B= sorted(B)
  n=len(B)
  if n % 2 == 1:
      return B[n//2]
  else:
      i = n//2
      return (B[i - 1] + B[i])/2
median= median(B)

def mode(B):
    Amax = B[0]
    for d in A:
        if B.count(d) > B.count(Amax):
            Amax = d
    return Amax
mode= mode(B)
  
print('(','mean(B)','median(B)','mode(B)',')','==''(', mean,',', median,',','[', mode,']',')')


# bài 2: Function - Đếm loại ký tự
dict={}
string="Hello World! 123"

alpha= sum(map(str.isalpha, string))
upper= sum(map(str.isupper, string))
lower= sum(map(str.islower, string))
digit= sum(map(str.isdigit, string))

def count_char_type(string):
  dict= {"LETTERS":alpha, "CASE": {"UPPER CASE":upper, "LOWER CASE":lower}, "DIGITS":digit} 
  return dict
print('Đếm loại kí tự: ', count_char_type(string))



