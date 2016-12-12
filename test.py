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

t_gcd1=0
t_gcd2=0
n=200
rn = 1000

for i in range(n):
    z=random.randint(2,rn)
    x=random.randint(0,rn)*z
    y=random.randint(0,rn)*z
    t_gcd1-=time.time()
    for j in range(n):
        res1 = gcd1(x,y)
    t_gcd1+=time.time()
    t_gcd2-=time.time()
    for j in range(n):
        res2 = gcd(x,y)
    t_gcd2+=time.time()
    if res1 != res2:
        print ("Error!")
    #print("x={}, y={}, gcd1={} ({}), gcd2={} ({})".format(x,y,res1,t_gcd1,res2,t_gcd2))
t_gcd1 = t_gcd1/n*2
t_gcd2 = t_gcd2/n*2
print("Проходов: {}, среднее время gcd1: {}с, среднее время gcd2: {}с, {}".format(n,t_gcd1,t_gcd2,t_gcd1/t_gcd2))


