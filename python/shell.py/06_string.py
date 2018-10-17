#!/usr/bin/python3

'''
输入一个年份，判断这一年是不是闰年
  能被4整除的是闰年，能被100整除的不是闰年，能被400整除的是闰年
'''

s=int(input('请输入年份: '))
if int(s%400) == 0:
  print('这年是闰年: ',s)
elif int(s%100) ==0:
  print('这年不是闰年: ',s)
elif int(s%4) == 0:
  print('这年是闰年: ',s)
else:
  print('这年不是闰年: ',s)
  



'''
坐出租车三公里以内13元，超过3公里在13公里以内每公里2.3元，13公里以上每公里多收%50
'''

s=int(input('请输入公里数: '))
if s<=3:
  pay=13
if s>3:
  pay=13+2.3*(s-3)
if s>13:
  pay=pay+1.15*(s-13)
s=round(pay)
print(s)



