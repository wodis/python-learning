# encoding: utf-8
__author__ = 'wudi'
import os

str = raw_input("Enter your input: ");
print "Received input is : ", str

str = input("Enter your input: ");
print "Received input is : ", str

# 打开一个文件
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

fo.write( "Python is a great language.\nYeah its great!!\n");

str = fo.read(10);
print "Read String is : ", str

# 关闭打开的文件
fo.close()

# 重命名文件test1.txt到test2.txt。
os.rename( "test1.txt", "test2.txt" )

# 删除一个已经存在的文件test2.txt
os.remove("text2.txt")

# 创建目录test
os.mkdir("test")

# 将当前目录改为"/home/newdir"
os.chdir("/home/newdir")

# 给出当前的目录
os.getcwd()

# 删除”/tmp/test”目录
os.rmdir( "/tmp/test"  )