import random

random.seed(1)


class EpsilonGreedy:
    def __init__(self, epsilon, pulls_per_arm, avg_vals):
        self.epsilon = epsilon  # probability of explore
        self.pulls_per_arm = pulls_per_arm  # number of pulls for each arms
        self.avg_vals = avg_vals  # average amount of reward we've gotten from each arms
        return

    def initialize(self, n_arms):
        self.pulls_per_arm = [0] * n_arms
        self.avg_vals = [0.0] * n_arms
        return

    def arm_selection(self):
        # For 1-epsilon probability the current average maximum valued arm will be chosen
        if random.random() > self.epsilon:
            return self.avg_vals.index(max(self.avg_vals))
        # A random other arm will be chosen
        else:
            return random.randrange(len(self.avg_vals))

    def update(self, chosen_arm, reward):
        avg_val = self.avg_vals[chosen_arm]
        self.pulls_per_arm[chosen_arm] += 1
        pulls = self.pulls_per_arm[chosen_arm]
        updated_val = (((pulls - 1) * avg_val) + reward) / float(pulls)
        self.avg_vals[chosen_arm] = updated_val
        return


class StockHistoryArm:
    def __init__(self, gains):
        self.gains = gains

    def draw(self, ind):
        return self.gains[ind]
