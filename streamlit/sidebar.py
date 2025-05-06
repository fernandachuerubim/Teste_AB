import os # importar o sistema operacional
import time # referente a tempo
import requests # requisição de API
import streamlit as st

class sidebar:
    def __init__(self):
        self.show_sidebar() # quando incializa a classe

    def show_sidebar(self):
        st.title('Opções')

        web_url = os.getenv('WEB_URL')
        link = f'[Página Web]({web_url}/home)'
        st.markdown(link, unsafe_allow_html=True)
        
        st.write('Click no botão começar para iniciar o experimento:')
        st.button('Começar', on_click=self.comecar)
        
        st.write('Click no botão para apagar o experimento :')
        st.button('Apagar', on_click=self.apagar)
        
    def comecar(self):
        url = os.getenv('WEBSCRAPER_URL')
        r = requests.get(url)
        time.sleep(1)
        
    def apagar(self):
        web_url = os.getenv('WEB_URL')
        url = web_url + '/apagar'
        r = requests.get(url)
        st.write(r.text)
        time.sleep(1.5)