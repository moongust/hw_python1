# print ("1 ",max)
#
# max="global max"
# print("2 ",max)
#
# def func1():
#
#     def func2():
#         def func3():
#             nonlocal max
#             print("func3 ", max)
#          # max = "func2 max"
#         nonlocal max
#         print("func2 ",max)
#         func3()
#         # max="func2 max"
#         # print("Define max in func2")
#         # print(max)
#     print("Define max in func1")
#     global max
#     # max="func1 max"
#     print("func1 ", max)
#     func2()
#
# func1()
import re

pattern = 'test'
string = 'This is a simple test message for test'
found = re.findall(pattern, string)
print(len(found) == string.count('test'))
print(found)
print("-"*10)
pattern = '[0-9]+'
string = 'If 300 spartans were so brave, so 500 spartans could destroy more than 10k warriors of Darius, but 15k and even 20k'
print(re.findall(pattern, string))


