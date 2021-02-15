import requests
from re import search
from datetime import datetime

from bs4 import BeautifulSoup

class ConsultaMulta:
    def __init__(self, browser):
        self.browser = browser
        self.time_now = datetime.now()
        self.get_url = 'https://www.detran.mg.gov.br/veiculos/situacao-do-veiculo/emitir-de-extrato-de-multas'
        self.post_url = 'https://www.detran.mg.gov.br/veiculos/situacao-do-veiculo/emitir-de-extrato-de-multas/listar-infracoes-multas'

    def __send_alert(self, page_source, placa, is_selenium=False):
        if search('Multas Vencidas', page_source):
            print("Possui Multas Vencidas!")
            if is_selenium:
               self.browser.save_screenshot(f"PLACA_{placa}-{self.time_now}.png")
        elif search('PLACA NAO POSSUI INFRACOES', page_source):
            print("Não Possui Multas !")
        else:
            print("Erro: Não foi possivel consultar")        

    def consultar_selenium(self, placa, renavam):
        self.browser.get(self.get_url)    

        self.browser.find_element_by_xpath('//*[@id="placa"]').send_keys(placa)
        self.browser.find_element_by_xpath('//*[@id="renavam"]').send_keys(renavam)
        self.browser.find_element_by_xpath('//*[@id="content"]/form/button').click()

        self.__send_alert(self.browser.page_source, placa, True)        

    def consultar(self, placa, renavam):
        with requests.Session() as session:
    
            response = session.get(self.get_url)

            soup = BeautifulSoup(response.text, 'html.parser')
            
            form = soup.find('form', {'class':'form-aguarde'})
            csrfToken = form.find('input', {'name':'_csrfToken'}).get('value')
            redirect_post_token = form.find('input', {'name':'_redirectPostToken'}).get('value')
            token_fields = form.find('input', {'name':'_Token[fields]'}).get('value')
            
            payload = {
                '_method': 'POST',
                '_csrfToken': csrfToken,
                '_redirectPostToken': redirect_post_token,
                'placa': placa,
                'renavam': renavam,
                '_Token[fields]': token_fields,
                '_Token[unlocked]': ''
            }

            response = session.post(self.post_url, data=payload)

            self.__send_alert(response.text, placa)
