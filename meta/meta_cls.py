class MetaCls(type):
    def __new__(cls, name, bases, attrs):
        # print('MetaCls.__new__')
        # print('cls: ', cls)
        # print('name: ', name)
        # print('bases: ', bases)
        # print('attrs: ', attrs)
        # print('attrs.get(\'__repr__\'): ', attrs.get('__repr__'))
        if attrs.get('__repr__') is None:
            attrs['__repr__'] = lambda self: self.label
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        # print('MetaCls.__init__')
        # print('cls: ', cls)
        # print('name: ', name)
        # print('bases: ', bases)
        # print('attrs: ', attrs)
        super().__init__(name, bases, attrs)


NewCls = MetaCls('NewCls', (), {'__repr__': lambda self: self.label})
print(NewCls.__repr__)
new_cls = NewCls()
print(new_cls.__repr__)
