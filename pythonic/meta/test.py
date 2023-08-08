class MyMeta(type):
    def __call__(cls, name, *args, **kwargs):
        print("Initializing...")
        instance = super().__call__(*args, **kwargs)
        instance.name = name
        return instance


# class MyClass(metaclass=MyMeta):
#     def __init__(self, name):
#         self.name = name

MyClass = MyMeta("MyClass", (), {})
obj = MyClass("Alice")
print(obj.name)
print(type(type(obj)))

