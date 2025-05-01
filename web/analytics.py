import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def animate (i):
    data = pd.read_csv("dataset\data_experiment.csv")
    data['click'] = data['click'].astype(int)
    data['visit'] = data['visit'].astype(int)
    x1 = np.arange(len(data[data['group'] == 'control']))
    y1 = data.loc[data['group'] == 'control', 'click'].cumsum()  / data.loc[data['group'] == 'control', 'visit'].cumsum()

    x2 = np.arange(len(data[data['group'] == 'treatment']))
    y2 = data.loc[data['group'] == 'treatment', 'click'].cumsum() / data.loc[data['group'] == 'treatment', 'visit'].cumsum()

    plt.cla()
    plt.plot(x1, y1, label='Control Group')
    plt.plot(x2, y2, label='Treatment Group')

    plt.legend(loc='upper right')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 1000, cache_frame_data=False)

plt.show()