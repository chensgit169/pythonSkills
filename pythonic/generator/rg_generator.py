def rg(a: int):
    return a ** 2


def generator(temp: float):
    lnz = temp
    while True:
        temp = rg(temp)
        yield lnz

        df = temp
        lnz += df
        if df/lnz < 1e-10:
            break


if __name__ == '__main__':
    for ln_z in generator(temp=0.5):
        print(ln_z)
