input_str = input("请输入一个数字:").strip('0').split('.')
newStr = list()
index = 0
CurrentNameList = [0]*9
if input_str[0].isdigit():
    for k in input_str[0]:
        print( int(k) in CurrentNameList)

        if int(k) in CurrentNameList:
            #说明找到了值 不需要再添加 只需要+1即可
            print(index)
            CurrentNameList[CurrentNameList.index(int(k))] += 1
            print(CurrentNameList,'找到了')
        else:
            CurrentNameList[index] = int(k)
            print(CurrentNameList,'首次进入')
            index += 1