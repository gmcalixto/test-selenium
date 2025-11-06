from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_pudim_homepage(driver):
    # 1) abrir a página
    driver.get("https://www.pudim.com.br/")

    # 2) esperar o título conter "Pudim"
    WebDriverWait(driver, 10).until(EC.title_contains("Pudim"))
    assert "Pudim" in driver.title

    # 3) esperar por uma <img> visível e confirmar que está exibida
    img = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "img"))
    )
    assert img.is_displayed()