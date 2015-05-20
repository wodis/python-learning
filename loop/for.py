# encoding: utf-8
__author__ = 'wudi'

for letter in 'Python':  # First Example
    print 'Current Letter :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # Second Example
    print 'Current fruit :', fruit

print "Good bye!"

for index in range(len(fruits)):
    print 'Current fruit :', fruits[index]

print "Good bye!"

for letter in 'Python':
    if letter == 'h':
        pass
        print 'This is pass block'
    print 'Current Letter :', letter

print "Good bye!"