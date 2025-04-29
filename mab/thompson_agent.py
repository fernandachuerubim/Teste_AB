import numpy as np
from scipy.stats import beta
from matplotlib import pyplot as plt

def reward_plot(success_array, failures_array):
    linestyle = ['-', '--']

    x = np.linspace(0, 1, 1002)[1:-1]

    plt.clf()
    plt.xlim(0,1)
    plt.ylim(0,30)

    for a, b, ls in zip(success_array, failures_array, linestyle):
        dist = beta(a, b)

        plt.plot(x, dist.pdf(x), ls=ls, c='black', label=f'Alpha:{a}, Beta:{b}')
        plt.draw()
        plt.pause(0.1)
        plt.legend(loc=0)

class ThompsonAgent(object):
    def __init__(self, prop_list):
        self.prop_list = prop_list

    def pull(self, bandit_machine):
        if np.random.random() < self.prop_list[bandit_machine]:
            reward = 1
        else:
            reward = 0
        return reward

# probabilidade de ter um resultado possitivo da pagina
prob_list = [0.25, 0.35]

# parametros do experimento
trials = 1000
episodes = 200

# agent
bandit = ThompsonAgent(prob_list)

prob_reward_array = np.zeros(len(prob_list))
accumulated_reward_array = list()
avg_accumulated_reward_array = list()

for episode in range(episodes):
    
    success_array = np.ones(len(prob_list))
    failure_array = np.full(len(prob_list), 1.0e-5)

    reward_array = np.zeros(len(prob_list))
    bandit_array = np.full(len(prob_list), 1.0e-5)
    accumulated_reward = 0

    for trial in range(trials):
        # agent - escolha
        prob_reward = np.random.beta(success_array, failure_array)
        bandit_machine = np.argmax(prob_reward)

        # agent - recompensa
        reward = bandit.pull(bandit_machine)

        if reward == 1:
            success_array[bandit_machine] += 1
        else:
            failure_array[bandit_machine] += 1
        
        # agent - guarda recompensa
        reward_array[bandit_machine] += reward
        bandit_array[bandit_machine] += 1
        accumulated_reward += reward

        # plot
        reward_plot(success_array, failure_array)

    prob_reward_array += reward_array / bandit_array
    accumulated_reward_array.append(accumulated_reward)
    avg_accumulated_reward_array.append(np.mean(accumulated_reward_array))

prob01 = 100 * np.round(prob_reward_array[0] / episode, 2)
prob02 = 100 * np.round(prob_reward_array[1] / episode, 2)


print(f'\nProb bandit 01: {prob01}% - Prob bandit 02: {prob02}%')
print(f'\nAvg accumulate reward: {np.mean(avg_accumulated_reward_array)}\n')