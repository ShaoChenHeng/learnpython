import array

#初始化一个数祖
#array.array(typecode,[initializer]) 
# --typecode:元素类型代码；
# initializer:初始化器，若数组为空，则省略初始化器
n = 10
a = array.array('i',[0,1,2,3])
b = array.array('i',[0,1,2,3,4])
c = array.array('i',[n])
myList = [5,5,5,6,6,6]

def test_through(arr):
     #遍历
     for i in arr:
          print(i)
def test_typecode():     
     #输出数组的数据类型
     print(a.typecode)

def test_len():
     #输出数组长度 len(a)
     print(a.itemsize)

def test_append():
     #添加新值到末尾
     a.append(5)
     print(a)

def test_append2():
     #给数组赋值
     for i in range(0,10):
          c.append(i)
def test_count():
     #array.count(x) -- 对象方法 获取元素x在数组中出现的次数
     print(a.count(4))

def test_merge(_arr,_list):
     #将_list合并到arr1末尾
     _arr.fromlist(_list)


def others(arr):
     #array.index(x) --对象方法：返回数组中x的最小下标
     print('\n返回数组中1的最小下标：')
     print(arr.index(1))

     #array.insert(1) --对象方法：在下表i（负值表示倒数）之前插入值x
     print('\n在下表1（负值表示倒数）之前插入值0：')
     arr.insert(1,0)
     print(arr)

     #array.pop(i) --对象方法：删除索引为i的项，并返回它
     print('\n删除索引为4的项，并返回它:')
     print(arr.pop(4))
     print(arr)

     #array.remove(x) --对象方法：删除第一次出现的元素x
     print('\n删除第一次出现的元素5：')
     arr.remove(5)
     print(arr)

     #array.reverse() --对象方法：反转数组中的元素值
     print('\n将数组arr中元素的顺序反转：')
     arr.reverse()
     print(arr)

     #array.tolist()：将数组转换为具有相同元素的列表（list）
     print('\n将数组arr转换为已给具有相同元素的列表：')
     li = arr.tolist()
     print(li)
