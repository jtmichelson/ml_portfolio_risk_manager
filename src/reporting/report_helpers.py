from src.model.follow_the_regularized_leader import FollowTheRegularizedLeader


def epsilon_greedy_output_formatted(epsilon_greedy_instance, arms, number_of_entries):
    iterator = [0.0] * number_of_entries
    chosen_arms = [0.0] * number_of_entries
    rewards = [0.0] * number_of_entries
    cumulative_rewards = [0.0] * number_of_entries
    epsilon_greedy_instance.initialize(len(arms))

    i = 0
    while i < number_of_entries:
        iterator[i] = i + 1
        chosen_arm = epsilon_greedy_instance.arm_selection()
        chosen_arms[i] = chosen_arm
        reward = arms[chosen_arm].draw(i)
        rewards[i] = reward

        if i == 0:
            cumulative_rewards[i] = reward
        else:
            cumulative_rewards[i] = cumulative_rewards[i - 1] + reward + (cumulative_rewards[i - 1] * reward)

        epsilon_greedy_instance.update(chosen_arm, reward)
        i += 1

    return [iterator, chosen_arms, rewards, cumulative_rewards]


def ftrl_output_formatted(ftrl_model_set, stock_set, number_of_entries):
    iterator = [0.0] * number_of_entries
    chosen_stocks = [0.0] * number_of_entries
    rewards = [0.0] * number_of_entries
    cumulative_rewards = [0.0] * number_of_entries

    possible_rewards = [0.0] * len(stock_set)
    losses = [0.0] * len(stock_set)
    probabilities = [0.0] * len(stock_set)

    i = 0
    while i < number_of_entries:
        iterator[i] = i + 1
        j = 0
        while j < len(stock_set):
            possible_rewards[j] = stock_set[j][i]
            probabilities[j] = ftrl_model_set[j].predict()
            losses[j] += FollowTheRegularizedLeader.log_loss(stock_set[j][i], probabilities[j])
            ftrl_model_set[j].update(probabilities[j], stock_set[j][i])
            j += 1
        index_of_maximum_probability = probabilities.index(max(probabilities))
        chosen_stocks[i] = index_of_maximum_probability
        rewards[i] = possible_rewards[index_of_maximum_probability]

        if i == 0:
            cumulative_rewards[i] = rewards[i]
        else:
            cumulative_rewards[i] = cumulative_rewards[i - 1] + rewards[i] + (cumulative_rewards[i - 1] * rewards[i])
        i += 1

    return [iterator, chosen_stocks, rewards, cumulative_rewards]


