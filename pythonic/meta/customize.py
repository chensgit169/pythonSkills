class GateMeta(type):
    def __new__(mcls, name, bases, attrs):
        gate_list = attrs.get('gate_list', [])

        def init_wrapper(self, *args, **kwargs):
            for gate in gate_list:
                setattr(self, gate, f"This is {gate}")
            super(self.__class__, self).__init__(*args, **kwargs)

        attrs['__init__'] = init_wrapper
        cls = super().__new__(mcls, name, bases, attrs)  # 修复这里的代码
        return cls


class Oracle(metaclass=GateMeta):
    pass


# 动态生成多个类，并传入不同的gate_list参数
gate_list1 = ['GateA', 'GateB']
DynamicClass1 = GateMeta('DynamicClass1', (Oracle,), {'gate_list': gate_list1})

gate_list2 = ['GateX', 'GateY', 'GateZ']
DynamicClass2 = GateMeta('DynamicClass2', (Oracle,), {'gate_list': gate_list2})

# 实例化并访问类属性
obj1 = DynamicClass1()
print(obj1.GateA)  # 输出: This is GateA
print(obj1.GateB)  # 输出: This is GateB

obj2 = DynamicClass2()
print(obj2.GateX)  # 输出: This is GateX
print(obj2.GateY)  # 输出: This is GateY
print(obj2.GateZ)  # 输出: This is GateZ
