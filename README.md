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
    calendar.month(2008, 1)\
    
##6.函数 function
* 函数代码块以def关键词开头，后接函数标识符名称和圆括号()。
* 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
* 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
* 函数内容以冒号起始，并且缩进。
* Return[expression]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。


    def functionname( parameters ):
       "函数_文档字符串"
       function_suite
       return [expression]
       
###值传递参数和引用传递参数
所有参数（自变量）在Python里都是按引用传递。如果你在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：

    # 可写函数说明
    def changeme( mylist ):
       "修改传入的列表"
       mylist.append([1,2,3,4]);
       print "函数内取值: ", mylist
       return
     
    # 调用changeme函数
    mylist = [10,20,30];
    changeme( mylist );
    print "函数外取值: ", mylist
    
###缺省参数
调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：

    def printinfo( name, age = 35 ):
       "打印任何传入的字符串"
       print "Name: ", name;
       print "Age ", age;
       return;
       
###不定长参数
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：

    def functionname([formal_args,] *var_args_tuple ):
       "函数_文档字符串"
       function_suite
       return [expression]
       
###匿名函数
* 用lambda关键词能创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤。
* Lambda函数能接收任何数量的参数但只能返回一个表达式的值，同时只能不能包含命令或多个表达式。
* 匿名函数不能直接调用print，因为lambda需要一个表达式。
* lambda函数拥有自己的名字空间，且不能访问自有参数列表之外或全局名字空间里的参数。
* 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。


    lambda [arg1 [,arg2,.....argn]]:expression

##7.文件I/O
###读取键盘输入
Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘。如下：

* raw_input:函数从标准输入读取一个行，并返回一个字符串
* input:函数基本可以互换，但是input会假设你的输入是一个有效的Python表达式，并返回运算结果。


    str = raw_input("Enter your input: ");
    str = input("Enter your input: ");
    
###open()方法
* file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
* access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
* buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。


    file object = open(file_name [, access_mode][, buffering])

###close()方法
File对象的close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。
    
    fileObject.close();
    
###write()方法
write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。

    fileObject.write(string);
   
###read()方法
read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。

    fileObject.read([count]);
    

