import time

"""
Демонстрация действия менеджера контекста with
"""

class demo:
    def __init__(self, label):
        print("demo.__init__, label=",label,", time=",time.time())
        self.label = label

    def __enter__(self):
        print("demo.__enter__",", time=",time.time())
        self.start = time.time()

    def __exit__(self, exc_ty, exc_val, exc_tb):
        print("demo.__exit__",", time=",time.time())
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))

with demo('counting'):
    n = 10000000
    while n > 0:
        n -= 1

"""
Демонстрация класса-функции, в т.ч. как декоратора
"""
print("_"*50)

print("Перед определением класса Sleep")

class Sleep:
    print("Объявление класса Sleep")
    def __init__(self, sec):
        print("__init__: Вызов Sleep.__init__()")
        self.sec = sec
    def __call__(self,func):
        print("__call__: Вызов Sleep.__call__()")
        def decorated(*args,**kwargs):
            # Вложенная (nested) функция, имеет доступ к переменным родительской scope.
            # Переменные родительской scope доступны для чтения (при объявлении nonlocak становятся доступны для записи).
            # Если возвратить ссылку на вложеную функцию, внутри неё есть ссылки будет ссылка на родительскую scope
            # в свойстве __closure__, в т.ч. в нашем случае на значение func. Это - замыкание в Питоне.
            print("decorated: Вызов Sleep.__call__.decorated()")
            time.sleep(self.sec)
            print("decorated: Вызов обёрнутой функции")
            print(func)
            res = func(*args,**kwargs)
            print("decorated: После вызова обёрнутой функции")
            return res
        return decorated
print("Перед инструкцией @Sleep")

# 1) Выполняется Sleep(2).
#    Возвращается ссылка на объект класса Sleep с self.sleep=2 (назовём его условно Sleep_object).
# 2) Выполняется вызов метода созданного на шаге 1 объекта Sleep_object.__call__(self,Mul).
#    Возвращается ссылка на функцию-обёртку Sleep_object.__call__.decorated. Внутри неё
#    сохраняется ссылка на функцию func.

@Sleep(2)
def Mul(a,b):
    print ("Mul: вызов собственно Mul()")
    return a*b
print("Перед вызовом Mul")
print("Результат: ",Mul(10,2))
#print("Mul.__name = ",Mul.__name__)
print(Mul)
for i in dir(Mul):
    print ("    ",i," = ",getattr(Mul,i))
