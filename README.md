# Python学习
[@讨厌茄子的老科特](http://weibo.com/wodis)

这个工程保留一些Python学习的例子，并不全面，只限于区别其他语言的特性

##1.中文编码 encoding
用 Python 输出 "Hello, World!"，英文没有问题，但是如果你输出中文字符"你好，世界"就有可能会碰到中文编码问题。

##2.变量类型 variable
变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间。
基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。
###变量赋值
Python中的变量不需要声明，变量的赋值操作既是变量声明和定义的过程。
每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

    #coding=utf-8
    #!/usr/bin/python
    
    counter = 100 # 赋值整型变量
    miles = 1000.0 # 浮点型
    name = "John" # 字符串
    
    print counter
    print miles
    print name
###多个变量赋值
Python允许你同时为多个变量赋值。例如：

	a = b = c = 1
以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
您也可以为多个对象指定多个变量。例如：

    a, b, c = 1, 2, "john"
以上实例，两个整型对象1和2的分配给变量a和b，字符串对象"john"分配给变量c。
###标准数据类型
Python有五个标准的数据类型：

* Numbers（数字）
* String（字符串）
* List（列表）
* Tuple（元组）
* Dictionary（字典）

##3.条件语句 decision
Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
Python 编程中 if 语句用于控制程序的执行，基本形式为：

    if 判断条件：
        执行语句……
    else：
        执行语句……
        
if 语句的判断条件可以用>（大于）、<(小于)、==（等于）、>=（大于等于）、<=（小于等于）来表示其关系。
当判断条件为多个值是，可以使用以下形式：

    if 判断条件1:
        执行语句1……
    elif 判断条件2:
        执行语句2……
    elif 判断条件3:
        执行语句3……
    else:
        执行语句4……
        
由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。

##4.循环语句 loop
Python提供了for循环和while循环（在Python中没有do..while循环）:

while:在给定的判断条件为 true 时执行循环体，否则退出循环体。

    while 判断条件：
        执行语句……

for:重复执行语句

    for iterating_var in sequence:
       statements(s)

break 语句:在语句块执行过程中终止循环，并且跳出整个循环

continue 语句:在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。

pass 语句:pass是空语句，是为了保持程序结构的完整性。

##5.日期和时间
Python程序能用很多方式处理日期和时间。转换日期格式是一个常见的例行琐事。Python有一个time and calendar模组可以帮忙。

    import time
    import calendar
    
    time.time()
    time.localtime(time.time())
    time.asctime( time.localtime(time.time()) )
    calendar.month(2008, 1)