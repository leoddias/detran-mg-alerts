import time, sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from ConsultaMulta import ConsultaMulta

def init_browser(headless):
    
    if headless:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
        browser.set_window_size(1024, 1366)
        time.sleep(2)
        return browser
    else:
        browser = webdriver.Remote(
           command_executor='http://192.168.0.201:9515',
           desired_capabilities=DesiredCapabilities.CHROME)

        browser.maximize_window()
        time.sleep(2)
        return browser

def main():
    if len(sys.argv) < 3:
        print("Usage: main.py PLACA RENAVAM")
        exit(-1)
    
    placa = sys.argv[1]
    renavam = sys.argv[2]

    #browser = init_browser(True)
    #consulta_multas = ConsultaMulta(browser)
    #consulta_multas.consultar_selenium(placa=placa, renavam=renavam)
    #browser.quit()

    consulta_multas = ConsultaMulta(None)
    consulta_multas.consultar(placa=placa, renavam=renavam)

if __name__ == "__main__":
    main()
