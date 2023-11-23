# simple python code
def add(a,b):
    result = a+b
    return result

def subtract(a, b):
    result = a -b
    return result

def main():
    x= 10
    y = 5
    z = add(x,y)
    w =subtract(x,y)
    print("sun:",z)
    print("difference:",w)

if __name__ == "__main__":
    main()