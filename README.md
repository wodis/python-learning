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
    

##8.HTTP
使用requests进行http请求处理

requests.get(url, params=payload)

requests.post(url, data=json.dumps(payload), headers=headers)

r.text

##9.JSON
使用demjson进行转换

demjson.encode(data)

demjson.decode(json)

##10.Log
使用logging开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件。

    logging.getLogger([name])
    
返回一个logger实例，如果没有指定name，返回root logger。只要name相同，返回的logger实例都是同一个而且只有一个，即name和logger实例是一一对应的。

    Logger.setLevel(lvl)
    
设置logger的level， level有以下几个级别：
NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL

    Logger.addHandler(hdlr)

logger可以雇佣handler来帮它处理日志， handler主要有以下几种：
StreamHandler: 输出到控制台
FileHandler:   输出到文件
handler还可以设置自己的level以及输出格式。

    logging.basicConfig([**kwargs])

* 这个函数用来配置root logger， 为root logger创建一个StreamHandler，设置默认的格式。
* 这些函数： logging.debug()、logging.info()、logging.warning()、logging.error()、logging.critical() 如果调用的时候发现root logger没有任何handler， 会自动调用basicConfig添加一个handler
* 如果root logger已有handler， 这个函数不做任何事情

##11.面向对象 OOP
Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。语法和Java相似，但是Python支持多继承。
###创建类
使用class语句来创建一个新类，class之后为类的名称并以冒号结尾，类的帮助信息可以通过ClassName.__doc__查看。class_suite 由类成员，方法，数据属性组成。
如下实例:

    class ClassName:
        '类的帮助信息'   #类文档字符串
        class_suite  #类体

###创建实例对象
要创建一个类的实例，你可以使用类的名称，并通过__init__方法接受参数。

###Python内置类属性
* .__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
* .__doc__ :类的文档字符串
* .__name__: 类名
* .__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
* .__bases__ : 类的所有父类构成元素（包含了以个由所有父类组成的元组）

###python对象销毁(垃圾回收)
同Java语言一样，Python使用了引用计数这一简单技术来追踪内存中的对象。

在Python内部记录着所有使用中的对象各有多少引用。
一个内部跟踪变量，称为一个引用计数器。

当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。

    a = 40
    del a
    
###类的继承
在python中继承中的一些特点：

1. 在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
2. 在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
3. Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。

如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。


    class SubClassName (ParentClass1[, ParentClass2, ...]):
        'Optional class documentation string'
        class_suite
        
你可以使用issubclass()或者isinstance()方法来检测。

* issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
* isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。

###方法重写
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：

    #coding=utf-8
    #!/usr/bin/python
    
    class Parent:        # 定义父类
       def myMethod(self):
          print '调用父类方法'
    
    class Child(Parent): # 定义子类
       def myMethod(self):
          print '调用子类方法'
    
    c = Child()          # 子类实例
    c.myMethod()         # 子类调用重写方法
    
###类属性与方法
类的私有属性：__private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

类的方法：在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数

类的私有方法：__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 slef.__private_methods

##12.多线程 Thread
Python中使用线程有两种方式：函数或者用类来包装线程对象。

####函数式：调用thread模块中的start_new_thread()函数来产生新线程。
语法如下:

    thread.start_new_thread ( function, args[, kwargs] )

参数说明:

* function - 线程函数。
* args - 传递给线程函数的参数,他必须是个tuple类型。
* kwargs - 可选参数。

####thread 模块提供的其他方法：

* threading.currentThread(): 返回当前的线程变量。
* threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
* threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:

* run(): 用以表示线程活动的方法。
* start():启动线程活动。
* join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
* isAlive(): 返回线程是否活动的。
* getName(): 返回线程名。
* setName(): 设置线程名。

##13.Redis
Redis客户端需要导入redis package

通常我们需要创建一个连接池

    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    
然后从连接池中得到redis实例进行相应的操作

    r = redis.Redis(connection_pool=pool)

相应的redis方法请参考文档[http://redisdoc.com/](http://redisdoc.com/)

##14.MySQLdb
MySQLdb 是用于Python链接Mysql数据库的接口，它实现了 Python 数据库 API 规范 V2.0，基于 MySQL C API 上建立的。

####引用MySQLdb
为了用DB-API编写MySQL脚本，必须确保已经安装了MySQL

    # encoding: utf-8
    #!/usr/bin/python
    import MySQLdb
    
####数据库连接

    # 打开数据库连接
    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    
    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")
    
    # 关闭数据库连接
    db.close()

####数据库插入更新操作

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

####数据库查询操作
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

* fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
* fetchall():接收全部的返回结果行.
* rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。


    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()

