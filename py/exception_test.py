while(True):
    try:
        num = int(input('请输入数字:'))
        break
    except Exception as e:
        print(e)
print(num)