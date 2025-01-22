from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import os

# Configurar o perfil do Firefox diretamente no objeto Options
options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference(
    "browser.download.dir", r"C:\Users\Gabriel N\Documents\CursosDevSamurai")
options.set_preference(
    "browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
# Desativar visualizador de PDF interno
options.set_preference("pdfjs.disabled", True)
# Ativar o modo headless (sem interface gráfica)
options.headless = True

# Inicializar o navegador com o GeckoDriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

# URL da página que contém os links
url = "https://class.devsamurai.com.br"

try:
    # Abrir a página
    driver.get(url)
    time.sleep(3)  # Aguarde o carregamento da página

    # Número total de elementos (conforme os seus xpaths)
    total_links = 67  # Ajuste conforme necessário

    for i in range(1, total_links + 1):
        # Construir o XPath dinâmico
        xpath = f"/html/body/div/ul/li[{i}]/a"

        try:
            # Encontrar o elemento pelo XPath e clicar
            link_element = driver.find_element(By.XPATH, xpath)
            link_element.click()
            time.sleep(20)  # Tempo de espera até clicar no próximo link

        except Exception as e:
            print(f"Erro ao processar o XPath {xpath}: {e}")

    # Verificar se todos os downloads foram concluídos
    download_dir = r"C:\Users\Gabriel N\Documents\CursosDevSamurai"
    while any(
            [
                filename.endswith(
                    ".part") for filename in os.listdir(download_dir)]):
        time.sleep(20)  # Aguarda 20 segundos antes de verificar novamente

finally:
    # Fechar o navegador
    driver.quit()
