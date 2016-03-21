import matplotlib.pyplot as plt


class D:
    def __init__(self, x_k, y_k):
        self.x_k = x_k
        self.y_k = y_k

    def mashtabuvanna(self):
        a = 2
        b = -2
        plt.plot(self.x_k, 'ro--')
        for i in range(0, len(self.x_k)):
            self.x_k[i] *= a
        plt.plot(self.y_k)
        for i in range(0, len(self.y_k)):
            self.y_k[i] *= b

        plt.plot(self.x_k, 'ro--')
        plt.plot(self.y_k)
        plt.grid()
        plt.title('Масштабування')
        plt.show()

    def mashtabuvanna_print(self):
        print(self.mashtabuvanna())

    def reverse(self):
        plt.plot(self.x_k, 'b--')
        plt.plot(self.x_k[::-1])
        plt.grid()
        plt.title('Реверс по часу')
        plt.show()

    def reverse_print(self):
        print(self.reverse())

    def shift(self):
        a = 2
        b = -2

        plt.plot(self.x_k, 'ro--')
        for i in range(0, len(self.x_k)):
            self.x_k[i] -= a
        plt.plot(self.y_k)
        for i in range(0, len(self.y_k)):
            self.y_k[i] -= b

        plt.plot(self.x_k, 'ro--')
        plt.plot(self.y_k)
        plt.grid()
        plt.title('Зсув по часу')
        plt.show()

    def shift_print(self):
        print(self.shift())

    def rozh(self):
        a = -1
        b = 1
        plt.plot(self.x_k, 'ro-')
        for i in range(0, len(self.x_k)):
            self.x_k[i] *= a * self.x_k[i]
        plt.plot(self.y_k)
        for i in range(0, len(self.y_k)):
            self.y_k[i] *= b * self.y_k[i]

        plt.plot(self.x_k, 'ro-')
        plt.plot(self.y_k)
        plt.grid()
        plt.title('Розширення')
        plt.show()

    def rozh_print(self):
        print(self.rozh())


    def dodavanna(self):
        print('Додавання')
        return list(map(lambda a, b: a + b, self.x_k, self.y_k))

    def dodavanna_print(self):
        print(self.dodavanna())

    def mnog(self):
        print('Множення')
        return list(map(lambda a, b: a * b, self.x_k, self.y_k))

    def mnog_print(self):
        print(self.mnog())



Object_m = D(x_k=[7, 4, 8, 0, 1, 3, 2, 7], y_k=[8, 7, 7, 5, 8, 1, 0])
Object_m.mashtabuvanna_print()

Object_r = D(x_k=[7, 4, 8, 0, 1, 3, 2, 7], y_k=[8, 7, 7, 5, 8, 1, 0])
Object_r.reverse_print()

Object_s = D(x_k=[7, 4, 8, 0, 1, 3, 2, 7], y_k=[8, 7, 7, 5, 8, 1, 0])
Object_s.shift_print()

Object_rh = D(x_k=[7, 4, 8, 0, 1, 3, 2, 7], y_k=[8, 7, 7, 5, 8, 1, 0])
Object_rh.rozh_print()

Object_add = D(x_k=[7, 4, 8, 0, 1, 3, 2, 7], y_k=[8, 7, 7, 5, 8, 1, 0])
Object_add.dodavanna_print()

Object_mn = D(x_k=[7, 4, 8, 0, 1, 3, 2, 7], y_k=[8, 7, 7, 5, 8, 1, 0])
Object_mn.mnog_print()


