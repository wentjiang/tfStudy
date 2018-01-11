text = 'jiangwnetao'

file_name = 'testFile.txt'

#写入
my_file=open(file_name,'w')
my_file.write(text)
my_file.close()

#增加
my_file=open(file_name,'a')
my_file.write('\nappend content')
my_file.close()

#读取
my_file=open(file_name,'r')
content = my_file.read()
print(content)
my_file.close()

#按行读取
my_file=open(file_name,'r')
line = my_file.readline()
print(line)
my_file.close()

#读取所有行
print('读取所有行')
my_file=open(file_name,'r')
lines = my_file.readlines()
for temp in lines:
    print(temp)





