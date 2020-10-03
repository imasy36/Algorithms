# stack imlpementation
#author @imasy36
class stack:
    def __init__(self, size):
        self.top = 0
        self.size = size
        self.stack = []
        
    def push(self, val):
        if self.top==self.size:
            return " -- Overflow!!"
        else:
            self.top+=1
            self.stack.append(val)
            return "Pushed element: {}".format(val)

    def pop(self, peek=False):
        if self.top==0:
            return " -- Underflow"
        else:
            last_value = self.stack[self.top-1]
            if not peek:
                self.stack.pop()
                self.top-=1
                return "Popped element: {}".format(last_value)
            return "Peek element: {}".format(last_value)
    def isEmpty(self):
        return True if self.top==0 else False
    def isFull(self):
        return True if self.top==size else False
   
if __name__=='__main__':
    size = int(input("Enter size of Stack: "))
    sk = stack(size)
    print("Usage: Operation[Push value, Pop, Peek, Print, check isEmpty/isFull, Exit]")
    while True:
        op = input("Enter operation: ").strip().lower()
        if op.split()[0] == "push":
            print(sk.push(int(op.split()[1])))
        elif op.split()[0] == "check":
            if op.split()[1] == "isempty":
                print(sk.isEmpty())
            elif op.split()[1] == "isfull":
                print(sk.isFull())
            else:
                print("Wrong usage of choice")
        elif op=="pop":
            print(sk.pop())
        elif op=="peek":
            print(sk.pop(peek=True))
        elif op=="print":
            print("Stack: ",sk.stack)
        elif op=="exit":
            break;
        else:
            print("Wrong usage of choice:")
