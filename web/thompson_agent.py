import os
import pandas as pd
import numpy as np
from variante import variante

class thompson_agent:
    def get_page():
        data = variante.load_data()
        data = thompson_agent.convert_to_dataFrame(data)
        
        if thompson_agent.empty_or_values_not_exists(data):
            return thompson_agent.random_page()

        data["no_click"] = data["visit"] - data["click"]
        click_array = data.groupby("group").sum().reset_index()
        click_array = click_array[["click", "no_click"]].T.to_numpy()

        success = click_array[0]
        failed = click_array[1]

        try:
            prob_reward = np.random.beta(success, failed)
            return "blue" if np.argmax(prob_reward) == 0 else "red"
        except ValueError:
            return thompson_agent.random_page()


    def random_page():
        random_page = np.random.randint(low=0, high=2, size=1)
        return "blue" if random_page == 0 else "red"

    def convert_to_dataFrame(data):

        columns = ["click", "visit", "group"]
        df = pd.DataFrame(data, columns=columns)
        return df

    def empty_or_values_not_exists(data):
        values_exists = data.isin({'group':['control', 'treatment']}).any().any()

        return (data.empty | (not values_exists))

if __name__ == "__main__":
    pass