import os
import requests 
import pandas as pd
import numpy as np
from scipy.stats import beta, norm
import streamlit as st

def bayesian_inference(acc_clicks_A, acc_clicks_B, acc_visits_A, acc_visits_B):
    qtd_amostas = 1000
    
    # Mean and Variance
    media_a, variancia_a = media_variance(acc_clicks_A, acc_visits_A)
    media_b, variancia_b = media_variance(acc_clicks_B, acc_visits_B)
    
    # Amostras da distribuição Normal
    distruibuicao_normal_a = amostra_normal(media_a, variancia_a, qtd_amostas)
    distruibuicao_normal_b = amostra_normal(media_b, variancia_b, qtd_amostas)
    
    # Beta Probability Density Function of page
    probabilidade_beta_a = probabilidade_beta(distruibuicao_normal_a, acc_clicks_A, acc_visits_A)
    probabilidade_beta_b = probabilidade_beta(distruibuicao_normal_b, acc_clicks_B, acc_visits_B)
    
    # Normal Probability Density Function of page
    probabilidade_normal_a = probabilidade_normal(distruibuicao_normal_a, media_a, variancia_a)
    probabilidade_normal_b = probabilidade_normal(distruibuicao_normal_b, media_b, variancia_b)

    # beta / Normal
    constante_normalizacao = (probabilidade_beta_a * probabilidade_beta_b) / (probabilidade_normal_a * probabilidade_normal_b)

    # Somente valores onde o B é maior do que A
    valores_maior_b = constante_normalizacao[distruibuicao_normal_b >= distruibuicao_normal_a]

    # Propabilidade de B ser melhor do que A
    probabilidade = (1 / qtd_amostas) * np.sum(valores_maior_b)

    # Erro ao assumir B melhor do que A
    expected_loss_A = (1 / qtd_amostas) * np.sum(((distruibuicao_normal_b - distruibuicao_normal_a) * constante_normalizacao )[distruibuicao_normal_b >= distruibuicao_normal_a])
    expected_loss_B = (1 / qtd_amostas) * np.sum(((distruibuicao_normal_a - distruibuicao_normal_b) * constante_normalizacao )[distruibuicao_normal_a >= distruibuicao_normal_b])

    return [probabilidade, expected_loss_A, expected_loss_B]

def media_variance(acc_clicks, acc_visits):
    media, variance = beta.stats(a = 1 + acc_clicks,  
                                 b = 1 + acc_visits - acc_clicks, 
                                 moments = 'mv')
    
    return media, variance

def amostra_normal(media, variancia, qtd_amostas):
    return np.random.normal(loc = media,
                            scale = 1.25*np.sqrt(variancia),
                            size = qtd_amostas )

def probabilidade_beta(distruibuicao_normal, acc_clicks, acc_visits):
    return beta.pdf(distruibuicao_normal,
                    a = 1 + acc_clicks,
                    b = 1 + acc_visits - acc_clicks)

def probabilidade_normal(distruibuicao_normal, media, variancia):
    return norm.pdf(distruibuicao_normal,
                    loc = media,
                    scale = 1.25*np.sqrt(variancia))

def get_chart_data():
    data = load_data()

    data = values_not_exists(data)

    #dtypes
    data['click'] = data['click'].astype(int)
    data['visit'] = data['visit'].astype(int)

    # pivot table
    data= data.reset_index().rename(columns={'index':'day'})
    data = data.pivot(index='day', columns='group', values=['click', 'visit']).fillna(0)
    data.columns = ['click_control', 'click_treatment', 'visit_control', 'visit_treatment']
    data = data.reset_index(drop=True)

    data['acc_visits_A'] = data['visit_control'].cumsum()
    data['acc_clicks_A'] = data['click_control'].cumsum()
    data['acc_visits_B'] = data['visit_treatment'].cumsum()
    data['acc_clicks_B'] = data['click_treatment'].cumsum()

    # inference bayesian
    bayesian = pd.DataFrame()
    
    colunas = ['Probabilidade de B ser melhor que A','Risco de Escolher A', 'Risco de Escolher B']
                     
    bayesian[colunas] = pd.DataFrame(
        np.row_stack(
            np.vectorize(
                bayesian_inference, otypes=['O'])
                (data['acc_clicks_A'], 
                data['acc_clicks_B'], 
                data['acc_visits_A'], 
                data['acc_visits_B'])))

    return bayesian

def load_data():
    url = os.getenv('WEB_URL')
    url = url + '/dados'
    r = requests.get(url)
    
    data = pd.DataFrame(r.json(), columns=r.json()[0].keys())
    return data

def values_not_exists(data):
    controle = ~data.isin({'group':['control']}).any().any() # o primeiro any traz uma série do pandas com TRUE e FALSE e o segundo any transforma a série do pandas em bolean.
    treatment = ~data.isin({'group':['treatment']}).any().any() # o primeiro any traz uma série do pandas com TRUE e FALSE e o segundo any transforma a série do pandas em bolean.

    if treatment:
        df = pd.DataFrame({'click': [0], 'visit': [0], 'group':['treatment']})
        return pd.concat([data, df])

    if controle:
        df = pd.DataFrame({'click': [0], 'visit': [0], 'group':'control'})
        return pd.concat([data, df])
    
    return data