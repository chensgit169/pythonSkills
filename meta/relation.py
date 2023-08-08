class MyClass:
    pass


class MySubClass(MyClass):
    pass


print(issubclass(MyClass, object))
print(isinstance(MyClass, MyClass))  # False
obj = MyClass()
# sub_obj = MySubClass()

print(isinstance(obj, MyClass))  # True
# print(isinstance(obj, MySubClass))  # False
# print(isinstance(sub_obj, MyClass))  # True




# print(issubclass(MySubClass, MyClass))  # True
# print(isinstance(MySubClass, MyClass))  # False
# print(isinstance(MyClass, MyClass))  # False
#
#
# print(issubclass(MyClass, object))  # True
#
#
# print(isinstance(obj, object))  # True
# print(isinstance(obj, type))  # False
#
# print(isinstance(MyClass, object))  # True
# print(isinstance(MyClass, type))  # True
#
# print(issubclass(type, object))  # True
# print(issubclass(object, type))  # False
# print(isinstance(type, object))  # True
# print(isinstance(object, type))  # True
#
# print(isinstance(type, type))  # True
# print(isinstance(object, object))  # True
#
# print(type(obj))  # <class '__main__.MyClass'>
# print(type(MyClass))  # <class 'type'>
# print(type(type(obj)))  # <class 'type'>
