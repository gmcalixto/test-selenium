# conftest.py
import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    opts = Options()
    # modo headless (sem abrir janela); comente se quiser ver a janela
    # opts.add_argument("-headless")
    with Firefox(options=opts) as d:
        d.set_window_size(1366, 768)
        yield d  # entrega o driver para o teste
        # ao sair do with, o driver é fechado
