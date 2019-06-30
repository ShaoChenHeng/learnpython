import array
import numpy as np
a = []
arr_matrix = array.array('i',[])
#n = int(input())
#input()输入的是一个str

def common_input(n,m):      #n为行，m为列。
    for i in range(n):
        a.append([])
        for j in range(m):
            a[i].append(int(input()))

def common_output(n,m):
    for i in range(n):
        for j in range(n):
            print(str(a[i][j]) + ' ',end = '')
            #默认情况下print后自带‘\n’
            #因为要用‘ ’分隔，所以将类型转为str
        print('')

def inputAfile(list_matrix):
    with open('/home/scheng/PYcode/inputAndOutput/input', 'r') as f:
        line = f.readline()      #readline()读取一行数据 
        while line:
            data = list(map(int,line.split()))
            #split()分割字符串，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
            #map(function,ite),对ite进行function的操作。此处将当前行的数据按空格分割并转为int类型。
            list_matrix.append(data)
            line = f.readline()
    f.close()
    #print(list_matrix)
    array_matrix = np.array(list_matrix)
    print(array_matrix)

def outputArr():
    pass
inputAfile(a)
print(arr_matrix)
