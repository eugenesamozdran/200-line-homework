import os

class Cpypl:
    def __init__(self, directory):
        self.directory = directory

    def c_ext(self):
        c_list = [i for i in os.listdir(self.directory) if i.endswith((".c", ".h"))]
        return c_list

    def py_ext(self):
        py_list = [i for i in os.listdir(self.directory) if i.endswith((".py", ".pyc"))]
        return py_list

    def pl_ext(self):
        pl_list = [i for i in os.listdir(self.directory) if i.endswith((".pl", ".pm"))]
        return pl_list
                
a = Cpypl(r"C:\Users\admin\Desktop\python test")

print(a.c_ext())
print(a.py_ext())
print(a.pl_ext())
