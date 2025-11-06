# tests/test_homepage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_exemplo_homepage(driver):
    # 1) abrir a página
    driver.get("https://example.org/")

    # 2) esperar o título conter "Example"
    WebDriverWait(driver, 10).until(EC.title_contains("Example"))
    assert "Example Domain" in driver.title

    # 3) localizar elementos por seletores típicos
    h1 = driver.find_element(By.TAG_NAME, "h1")
    assert h1.text == "Example Domain"

    p = driver.find_element(By.CSS_SELECTOR, "p")
    assert "illustrative examples" in p.text

    # 4) clicar no link "More information..."
    more_info = driver.find_element(By.CSS_SELECTOR, "a")
    more_info.click()

    # 5) validar que navegou para o IANA (nova URL)
    WebDriverWait(driver, 10).until(EC.url_contains("iana.org"))
    assert "iana.org" in driver.current_url
