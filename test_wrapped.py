class Wrapper:
    def __init__(self,obj):
        self.wrapped = obj
    def __getattr__(self, attrname):
        print("__getattr__")
        return getattr(self.wrapped,attrname)
    def __str__(self):
        return str(self.wrapped)

lst=[1,2,3,4,5]
wr_lst = Wrapper(lst)
wr_lst.append(10)
# wr_lst[0]=111   # тут будет ошибка, __getattr__ работает только с методами

print(wr_lst)