from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def preencher_formulario(dados_lista):
    for dados in dados_lista:

        navegador = webdriver.Chrome()
        link = 'https://docs.google.com/forms/d/e/1FAIpQLScKEtDtf19PAjLimmjOeHVsXTrlG-7aCqSY6uALdrmgWlGfEg/viewform?pli=1'
        navegador.get(link)
        time.sleep(2)

        campos = navegador.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    
        campos[0].send_keys(dados['nome'])
        campos[1].send_keys(dados['email'])
        campos[2].send_keys(dados['telefone'])
        campos[3].send_keys(str(dados['idade']))
        campos[4].send_keys(dados['sexo'])

        botao_enviar = navegador.find_element(By.XPATH, '//span[text()="Enviar"]/ancestor::div[@role="button"]')
        botao_enviar.click()
        time.sleep(3)
        navegador.quit()
    print('Todos os formulários preenchidos. Processo finalizado')
    
lista_pessoaas = [
    {"nome": "Mileno", "email": "email@gmail.com", "telefone": "8495465880731", "idade": 30, "sexo": "M"},
    {"nome": "Maria", "email": "maria@gmail.com", "telefone": "8985644555", "idade": 28, "sexo": "F"}
]

preencher_formulario(lista_pessoaas)