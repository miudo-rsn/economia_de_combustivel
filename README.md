#  Calculadora de Economia de Combustível

Este projeto é uma **calculadora em Python** que ajuda o motorista a decidir se **vale a pena ou não** se deslocar até um posto de combustível mais barato, considerando:

 Consumo do veículo
 
 Preço da gasolina em diferentes postos
 
 Distância até o posto mais barato
 
 Valor que pretende abastecer
 

O programa informa:
 O **valor mínimo** e a **litragem mínima** para que a viagem compense
 
 Se um valor específico de abastecimento **gera economia ou prejuízo**
 
 Quanto o usuário **economizará em reais**

---

##  Funcionalidades

 Limpa a tela automaticamente (Windows, Linux e macOS).
 Cálculo do **mínimo necessário para compensar a ida ao posto mais barato**.
 Cálculo se um **valor específico de abastecimento compensa**.
 
 Considera dois cenários:

   Quando a gasolina atual **não é** do posto mais barato

   Quando a gasolina atual **já é** do posto mais barato

 Aceita valores com **vírgula ou ponto**

 Valida entradas inválidas

---

##  Lógica utilizada

O cálculo leva em conta:

 Diferença de preço entre os postos

 Custo por quilômetro rodado

 Custo total de ida e volta até o posto mais barato

 Economia gerada por litro abastecido no posto mais barato

Assim, o programa compara o **custo da locomoção** com a **economia obtida no combustível**.

---

Após isso, siga as instruções exibidas no terminal.

---

##  Exemplo de uso

O usuário informa:

 Consumo do veículo (km/l)
 
 Preço do combustível no posto caro
 
 Preço no posto barato
 
 Distância até o posto mais barato
 
 Valor que pretende abastecer (opcional)
 

O programa retorna:

 Se compensa ou não
 
 O valor mínimo necessário
 
 Quanto será economizado

---

##  Tecnologias utilizadas

 Python 3
 
 Biblioteca padrão `os`

---

