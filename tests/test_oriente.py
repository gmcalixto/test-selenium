# test_oriente_botao_enviar.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://mackcloud.mackenzie.br/apps/oriente/"

# Procura <button> cujo texto contenha "enviar" OU <input type="submit" value*="enviar"
# Normaliza acentos e caixa via translate (XPath)
XPATH_ENVIAR = (
    "//button[ contains( "
    "translate(normalize-space(.),"
    "'ÁÂÃÀÉÊÍÓÔÕÚÇABCDEFGHIJKLMNOPQRSTUVWXYZ',"
    "'aaaaeeioooucabcdefghijklmnopqrstuvwxyz'),"
    "'enviar')]"
    " | "
    "//input[ translate(@type,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='submit' "
    "and contains( translate(@value,"
    "'ÁÂÃÀÉÊÍÓÔÕÚÇABCDEFGHIJKLMNOPQRSTUVWXYZ',"
    "'aaaaeeioooucabcdefghijklmnopqrstuvwxyz'), 'enviar')]"
)

def test_oriente_tem_botao_enviar(driver):
    # 1) abrir a página
    driver.get(URL)

    # 2) garantir que a página carregou (body presente)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # 3) aguardar por um botão/submit visível com "enviar"
    botao = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, XPATH_ENVIAR))
    )
    assert botao.is_displayed()
