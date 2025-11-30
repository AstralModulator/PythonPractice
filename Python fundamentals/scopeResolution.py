def func1():
    x = 1
    def func2():
        x = 2
        print(x)
    func2()
    print(x)

func1()

y = 3

def func3():
    print(y)
func3()
