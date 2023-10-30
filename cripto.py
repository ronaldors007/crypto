import requests
import time
from secreto import TOKEN, CHAT_ID
moeda="nim_usdt"
Mensagem = "vender nimiq "
def obter_e_armazenar_preco(lista): #Função para obter o último preço e armazená-lo na lista
    url = 'https://data.gateapi.io/api/1/tickers'
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        if moeda in data and "last" in data[moeda]:
            last_price = data[moeda]["last"]            
            print(f"Último preço de {moeda}:", last_price)            
            lista.append(last_price)#Adicione o último preço à lista
        else:
            print("A chave 'nim_usdt' ou 'last' não foi encontrada na resposta.")
    else:
        print("Falha na solicitação com código de status:", r.status_code)
lista_de_precos = [] #Lista para armazenar os preços

while True: #Executa a função a cada 30 segundos
    obter_e_armazenar_preco(lista_de_precos)
    time.sleep(30)    
    ultimo = float(lista_de_precos[-1])    
    if ultimo > 0.0011500:
        print('Preço atende aos critérios - Vender Nimiq')        
        # Construa a URL e envie a mensagem somente se o preço for maior que 0.0011500
        URL = (f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={Mensagem} {ultimo}")
        resposta = requests.get(URL)
        print(resposta.json())
