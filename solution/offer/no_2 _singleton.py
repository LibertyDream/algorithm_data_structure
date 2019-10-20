'''
    面试题2：实现Singleton模式
    题目：设计一个类，我们只能生成该类的一个实例。
'''
import threading

class Singleton(object):

    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(cls, '_instance'):
                    Singleton._instance = object.__new__(cls, *args, **kwargs)
            
        return Singleton._instance


def task(arg):
    obj = Singleton()
    print(id(obj))

if __name__ == "__main__":

    for i in range(10):
        t = threading.Thread(target=task, args = [i,])
        t.start()
