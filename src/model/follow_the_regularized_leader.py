import random
import math
import numpy as np

random.seed(1)


class FollowTheRegularizedLeader(object):
    def __init__(self, alpha, beta, l1, l2, features, reg_func, indices):
        self.alpha = alpha
        self.beta = beta
        self.l1 = l1
        self.l2 = l2
        self.reg_func = reg_func
        self.indices = [0]
        self.count = 0
        for index in indices:
            self.indices.append(index)
        self.sum_of_gradients_squared = [0.] * features
        self.weights = {}
        self.temp_weights = []
        i = 0
        while i < features:
            self.temp_weights.append(random.random())
            i += 1

    def update(self, probability, result):
        gradient = probability - result
        gradient_squared = math.pow(gradient, 2)
        self.count += 1
        if self.reg_func is "RDA":
            for i in self.indices:
                sigma = (math.sqrt(self.sum_of_gradients_squared[i] + gradient_squared)) / (self.alpha * self.count)
                self.temp_weights[i] += -(sigma * self.weights[i]) + gradient
                self.sum_of_gradients_squared[i] += gradient_squared
        elif self.reg_func is "OPG":
            for i in self.indices:
                sigma = (math.sqrt(self.sum_of_gradients_squared[i] + gradient_squared) - math.sqrt(self.sum_of_gradients_squared[i])) / self.alpha
                self.temp_weights[i] += -(sigma * self.weights[i]) + gradient
                self.sum_of_gradients_squared[i] += gradient_squared

    def predict(self):
        weights = {}
        function = "Sigmoid"
        w_inner_x = float(0)
        for i in self.indices:
            sign = float(np.sign(self.temp_weights))
            if sign * self.temp_weights[i] <= self.l1:
                weights[i] = float(0)
            else:
                weights[i] = (sign * self.l1 - self.temp_weights[i]) / ((self.beta + math.sqrt(self.sum_of_gradients_squared[i])) / self.alpha + self.l2)
            w_inner_x += weights[i]

        self.weights = weights

        if function is "Sigmoid":
            probability = float(1) / (float(1) + math.exp(-max(min(float(w_inner_x), float(100)), float(-100))))
        elif function is "ReLU":
            probability = max(float(0), max(min(float(w_inner_x), float(100)), float(-100)))

        return probability

    @staticmethod
    def log_loss(true_label, predicted, eps=1e-15):
        p = np.clip(predicted, eps, 1 - eps)
        if true_label > 0:
            return -math.log(p)
        else:
            return -math.log(1 - p)
