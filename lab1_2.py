import matplotlib.pyplot as plt


class D:
    def __init__(self, x_k, y_k):
        self.x_k = x_k
        self.y_k = y_k
        #self.f_k = f_k

    def zg(self):
        self.x_k = [8, 1, 0]
        self.y_k = [5, 8, 9]
        self.y_k = self.y_k[::-1]
        print(self.y_k)


D(x_k=[], y_k=[]).zg()
