import torch as T


class Softmax():

    def __call__(self, tensor):
        self.tensor = tensor
        exp_x = T.exp(self.tensor)
        return exp_x / T.sum(exp_x)


class softmax_stable():

    def __call__(self, tensor):
        self.tensor = tensor
        c = T.max(self.tensor)
        exp_x_shifted = T.exp(self.tensor - c)
        return exp_x_shifted / T.sum(exp_x_shifted)


if __name__ == "__main__":

    data = T.Tensor([1, 2, 3])
    softmax = Softmax()
    output = softmax(data)

    softmax_stable = softmax_stable()
    output_1 = softmax_stable(data)
    print(output)
    print(output_1)
