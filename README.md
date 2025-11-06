# Projeto de Testes Automatizados com Selenium (Python)

## Enunciado Geral

Desenvolva **dois testes automatizados** utilizando **Python** e **Selenium WebDriver**, cada um em um arquivo separado.  
Os arquivos devem seguir o formato:


Exemplo:
- `test_calculo_simples.py`
- `test_fluxo_interacao.py`

Ambos os testes devem ser compatíveis com **pytest**


## Teste 1 — Foco em Cálculo ou Lógica Simples

Escolha **um site** que realize **um único tipo de cálculo ou conversão simples**, como:
- Conversor de moedas  
- Calculadora de gorjeta  
- Cálculo de frete  
- Conversor de unidades de medida (km ↔ milhas, °C ↔ °F, etc.)

### Requisitos:
1. Acessar o site de cálculo escolhido.  
2. Inserir valores de exemplo nos campos adequados.  
3. Acionar o cálculo ou conversão.  
4. Validar o resultado exibido na página (comparando com o valor esperado).  
5. Exibir mensagem de sucesso ou erro conforme o resultado da validação.  



## Teste 2 — Foco em Fluxo e Estado

Escolha **um segundo site** que envolva **interação com fluxo de ações ou mudança de estado**, como:
- Formulário de cadastro com validações  
- Login/logout em página de demonstração  
- Pesquisa com filtros dinâmicos  
- Checkout simples em e-commerce  

### Requisitos:
1. Abrir o site selecionado.  
2. Executar o fluxo proposto (ex: preencher e enviar um formulário).  
3. Aguardar a resposta do sistema (mensagem, alerta ou redirecionamento).  
4. Validar a presença da resposta esperada na interface.  
5. Encerrar o navegador corretamente ao final do teste.  

### Entrega: 12/11

1. Os testes desenvolvidos devem estar na pasta tests

2. Para executar os testes o ambiente virtual deve estar ativado e as bibliotecas instaladas

3. O Firefox deve estar instalado no computador