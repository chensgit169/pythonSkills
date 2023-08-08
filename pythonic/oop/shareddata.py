class SharedData:
    spam = 1


if __name__ == '__main__':
    x = SharedData()
    x.spam = 2
    y = SharedData()
    print(y.spam)
