import os
import pandas as pd
from infra.repository.experimento_repository import ExperimentoRepository


class variante(object):
    def __init__(self, visit, click, group): # self é para se referenciar a propria classe
        self.visit = visit # criando na variavel classe self a variavel visitante
        self.click = click # criando na variavel classe self a variavel click
        self.group = group  # criando na variavel classe self a variavel group

    def salvar_experiment(self):
       repo = ExperimentoRepository()
       repo.insert(self.click, self.visit, self.group)

    def load_data():
        repo = ExperimentoRepository()
        return repo.select()

    def delete_experiment():
        repo = ExperimentoRepository()
        return repo.delete()