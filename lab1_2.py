import matplotlib.pyplot as plt


class D:
    def __init__(self, x_k, y_k):
        self.x_k = x_k
        self.y_k = y_k

    def zg(self):
        self.x_k = [8, 1, 0]
        self.y_k = [5, 8, 9]
        self.y_k = self.y_k[::-1]
        print(self.y_k)
        print(self.x_k)
        f_x = ([])
        for i in range(0, len(self.x_k)):
            for j in range(0, len(self.y_k)):
                f_x.append(self.x_k[i]*self.y_k[j-1])
                print('y_k:', self.y_k[j-1])
            print('x_k:', self.x_k[i])
        print(f_x)


D(x_k=[], y_k=[]).zg()
