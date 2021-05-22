import queue


class StackUsingQueues:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, data):
        while (self.q1.qsize()) != 0:
            self.q2.put(self.q1.get())
        self.q1.put(data)
        while (self.q2.qsize()) != 0:
            self.q1.put(self.q2.get())
        return

    def pop(self):
        if (self.q1.qsize()) == 0:
            return -1
        return self.q1.get()

    def top(self):
        return self.q1.queue[0]

    def getSize(self):
        return self.q1.qsize()


s = StackUsingQueues()
li = [int(ele) for ele in input().split()]
i = 0
while i < len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i + 1])
        i += 1
    elif choice == 2:
        ans = s.pop()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        l = []
        while s.q1.qsize() != 0:
            l.append(s.q1.get())
        print(*l[::-1])

    i += 1
