import numpy as np

class GreedyAgent(object):
    def __init__(self, prop_list):
        self.prop_list = prop_list

    def pull(self, bandit_machine):
        if np.random.random() < self.prop_list[bandit_machine]:
            reward = 1
        else:
            reward = 0
        return reward

# probabilidade de ter um resultado possitivo da pagina
prob_list = [0.3, 0.8]

# parametros do experimento
trials = 1000
episodes = 200
eps_init = 0

# agent
bandit = GreedyAgent(prob_list)

prob_reward_array = np.zeros(len(prob_list))
accumulated_reward_array = list()
avg_accumulated_reward_array = list()

for episode in range(episodes):

    reward_array = np.zeros(len(prob_list))
    bandit_array = np.full(len(prob_list), 1.0e-5)
    accumulated_reward = 0

    for trial in range(trials):
        
        # agent - escolha
        if eps_init == 0:
            bandit_machine = 0

        elif eps_init == 1:
            bandit_machine = 1

        elif eps_init == 2:
            prob_reward = reward_array / bandit_array
            max_prob_reward = np.where(prob_reward == np.max(prob_reward))[0]
            bandit_machine = max_prob_reward[0]
        
        else:
            eps_init += 1

        eps_init += 1

        bandit_machine = np.random.randint(low=0, high=2, size=1)[0]

        # agent - recompensa
        reward = bandit.pull(bandit_machine)

        # agent - guarda recompensa
        reward_array[bandit_machine] += reward
        bandit_array[bandit_machine] += 1
        accumulated_reward += reward

    prob_reward_array += reward_array / bandit_array
    accumulated_reward_array.append(accumulated_reward)
    avg_accumulated_reward_array.append(np.mean(accumulated_reward_array))

prob01 = 100 * np.round(prob_reward_array[0] / episode, 2)
prob02 = 100 * np.round(prob_reward_array[1] / episode, 2)


print(f'\nProb bandit 01: {prob01}% - Prob bandit 02: {prob02}%')
print(f'\nAvg accumulate reward: {np.mean(avg_accumulated_reward_array)}\n')
    