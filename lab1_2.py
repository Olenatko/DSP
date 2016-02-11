import matplotlib.pyplot as plt


class D:
    def __init__(self, x_k, y_k):
        self.x_k = x_k
        self.y_k = y_k

    def zg(self):
        result = []
        length = min(len(self.y_k), len(self.x_k))
        for shift in range(1, 2*len(self.x_k)):
            f_x = []
            right_shift = shift
            left_shift = 0
            if right_shift > length:
                left_shift = right_shift - length
                right_shift = length
            for i in range(left_shift, right_shift):
                #print(self.x_k[i],self.y_k[len(self.y_k)- right_shift - left_shift + i])
                f_x.append(self.x_k[i]*self.y_k[len(self.y_k)- right_shift - left_shift + i])
            print(f_x)
            sum = 0
            for i in f_x:
                sum += i
            result.append(sum)
        return result

    def zg_print(self):
        print(self.zg())

#D(x_k=[6, 4, 2, 7, 9, 3 ], y_k=[4, 9, 0, 8, 1, 7, 2]).zg_print()
#D(x_k=[8, 1, 0], y_k=[5, 6, 9]).zg_print()
D(x_k=[6, 4, 7, 0, 8, 1, 2], y_k=[3, 4, 8, 7, 0, 6]).zg_print()