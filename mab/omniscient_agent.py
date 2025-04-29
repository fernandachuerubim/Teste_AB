import numpy as np

class OmniscientAgent(object):
    def __init__(self, prop_list):
        self.prop_list = prop_list

    def pull(self, bandit_machine):
        if np.random.random() < self.prop_list[bandit_machine]:
            reword = 1
        else:
            reword = 0
        return reword

# probabilidade de ter um resultado possitivo da pagina
prob_list = [0.25, 0.30]

# parametros do experimento
trials = 1000
episodes = 200

# agent
bandit = OmniscientAgent(prob_list)

prob_reword_array = np.zeros(len(prob_list))
accumulated_reward_array = list()
avg_accumulated_reword_array = list()

for episode in range(episodes):

    reword_array = np.zeros(len(prob_list))
    bandit_array = np.full(len(prob_list), 1.0e-5)
    accumulated_reward = 0

    for trial in range(trials):
        
        # agent - escolha
        bandit_machine = np.argmax(prob_list)

        # agent - recompensa
        reword = bandit.pull(bandit_machine)

        # agent - guarda recompensa
        reword_array[bandit_machine] += reword
        bandit_array[bandit_machine] += 1
        accumulated_reward += reword

    prob_reword_array += reword_array / bandit_array
    accumulated_reward_array.append(accumulated_reward)
    avg_accumulated_reword_array.append(np.mean(accumulated_reward_array))

prob01 = 100 * np.round(prob_reword_array[0] / episode, 2)
prob02 = 100 * np.round(prob_reword_array[1] / episode, 2)


print(f'\nProb bandit 01: {prob01}% - Prob bandit 02: {prob02}%')
print(f'\nAvg accumulate reword: {np.mean(avg_accumulated_reword_array)}\n')
    