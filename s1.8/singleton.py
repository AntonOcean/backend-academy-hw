class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self, i):
        print("i", i)


l = Logger("pp") # instance
k = Logger("dd") # instance
print(k)






# class Singleton(object):
#   _instances = {}
#   def __new__(class_, *args, **kwargs):
#     if class_ not in class_._instances:
#         class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
#     return class_._instances[class_]
#
# class MyClass(Singleton):
#   pass