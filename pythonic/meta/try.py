class OracleMeta(type):
    def __new__(cls, name, bases, attrs):
        # Here we may do something
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        # Here we may do something
        super().__init__(name, bases, attrs)


class QuantumGate:
    _sd_name = None

    def __init__(self, para: float):
        self.para = para

    @classmethod
    def get_sd_name(cls):
        return cls._sd_name


def customize_oracle(cls_name: str, sd_name: str):
    attrs = {'_sd_name': sd_name}
    return OracleMeta(cls_name, (QuantumGate,), attrs)


if __name__ == '__main__':
    Customized = customize_oracle('Customized', 'oracle')
    # The following line acts as a kind of typing annotation (at least in PyCharm).
    assert issubclass(Customized, QuantumGate)

    obj = Customized(1.0)
    print('standard name = ', obj.get_sd_name())  # 输出: oracle
    print('parameter = ', obj.para)  # 输出: 1.0

    print(Customized.__bases__)  # 输出: (<class '__main__.QuantumGate'>,)
    print(type(obj))  # 输出: <class '__main__.Customized'>
    print(type(Customized))  # 输出: <class 'type'>
