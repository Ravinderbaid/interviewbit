class A:
    def __init__(self, *args):
        args = args[0]
        self.name = args[0]
        self.height = args[1]

    def g(self):
        return self.height


class B:
    def __init__(self, *args):
        self.sex = args[0]

    def g2(self):
        return 2


if __name__ == "__main__":
    list_l = {}
    while True:
        a = input()
        if not a:
            break
        a = a.split(" ")
        if a[0] == "new":
            list_l[a[2]] = eval(a[1])(a[2:])
        if a[0] == "g":
            # import pdb;pdb.set_trace()
            f = getattr(list_l[a[2]], a[3])
            print(f())
    d = list_l
    for i in d:
        print(d[i])
