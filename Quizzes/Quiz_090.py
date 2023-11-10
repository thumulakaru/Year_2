def doSomething(n:int):
    if n>0:
        doSomething(n-1)
        print(n)
        doSomething(n-1)
    return None
