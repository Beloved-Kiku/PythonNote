
Input  = list(map(int,input('>>>输入数字').split()))
print(sum(Input)/len(Input))
# 给出一个半径 求圆的面积和周长 圆周率为3.14
R = int(input('>>>输入半径:'))
if R < 0:
    print('半径不能为负数')
while R  >=0:
    print('圆的面积是:',int(3.14*R*R))
    print('圆的周长是:',int(2*3.14*R))
    break
## 输入两个数字判断大小
Double_num = list(map(int,input('>>>输入数字').split()))
if int(len(Double_num))>2:
    print('输入的数字个数不能大于2')
while int(len(Double_num)) == 2:
      if Double_num[len(Double_num)-1] ==Double_num[0]:
          print('第二个数字等于第一个数字')
          break
      if Double_num[len(Double_num)-1]> Double_num[0]:
          print('第二个数字大于第一个数字')
          break
      else:
          print('第二个数字小于第一个数字')
          break
##输入若干个数字 判断最大值
List = list(map(int,input('>>>输入若干个数字:').split()))
if len(List) == 0:
    print('输入的数字个数不能为0')
while len(List) > 0:
    MaxValue = int(0)
    for K  in List:
        if K >MaxValue:
            MaxValue = K
    print(MaxValue)
    break
##输入五位数判断位次
Value = int(input('>>>输入五位数数字:'))
if Value > 99999 or Value < 10000:
    print('输入的数字不是五位数')
else:
    print('个位数为:',int(Value % 10),'十位数为:',int(Value % 100 // 10),'百位数为:',int(Value % 1000 // 100),'千位数为:',int(Value % 10000 // 1000),'万位数为:',int(Value // 10000))
## 输入N个数字求平均值
Input_N = list(map(int,input('输入N个数字:').split()))
print(sum(Input_N)/len(Input_N))
## 求0-100奇数和
Sum =int(0)
for  Ks in range(0,101):
    if Ks %2 !=0:
        Sum +=Ks
print(Sum)

##阶乘求和
SSum =int(0)
for T in range(1,6):
    KI = int(1)
    for I in range(1,T+1):
        KI *=I
    SSum +=KI
print(SSum)
width = int(input('>>>输入宽度:'))
def ComputerWidth(width):
    for i  in range(width):
        for j in range(width):
            if i == 0 or i == width-1 or j == 0 or j == width-1:
                print('*',end='')
            else:
                print(' ',end='')
        print()
ComputerWidth(width)
User_Input = list(map(int,input('>>>输入数字').split()))
Temp = list()
for  S   in  User_Input:
    for K  in  range(len(User_Input)-1):
        if User_Input[K] >S:
            Temp.append(User_Input[K])
print(Temp)

