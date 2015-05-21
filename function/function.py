# encoding: utf-8
__author__ = 'wudi'


def printme(str):
    "打印传入的字符串到标准显示设备上"
    print str
    return


printme("我要调用用户自定义函数!")
printme("再次调用同一函数")

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return

# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist

# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;

# 调用printinfo函数
printinfo(age=50, name="miki");
printinfo(name="miki");


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return;

# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);

#可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

#调用sum函数
print "Value of total : ", sum(10, 20)
print "Value of total : ", sum(20, 20)

total = 0;  # This is global variable.
# 可写函数说明
def sum(arg1, arg2):
    #返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print "Inside the function local total : ", total
    return total;

#调用sum函数
sum(10, 20);
print "Outside the function global total : ", total