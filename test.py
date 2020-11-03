class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

class maxx(Calculator):
    def add(self, num):
        self.result += num
        if self.result > 100:
            self.result = 100

cal = maxx()
cal.add(101)

print(cal.result)