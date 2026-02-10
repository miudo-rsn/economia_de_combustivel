import os

def limpar_tela():
  os.system("cls" if os.name == "nt" else "clear")

limpar_tela()

def calcular_minimo():
  print("")
  print("=====[Vamos calcular o valor e litragem mínima para compensar a ida e a volta até o posto mais barato]=====")
  print("")
  consumo = float(input("Qual o consumo do seu veículo em kilometros por litro? : ").replace(",", "."))
  print("")
  gasolina_cara = float(input("Qual o  valor do combustível no posto que você costuma abastecer (posto mais caro)? : ").replace(",", "."))
  print("")
  gasolina_barata = float(input("Qual o valor do combustível no posto mais barato? : ").replace(",", "."))
  print("")
  distancia_barata = float(input("Quantos KM você está do posto mais barato? : ").replace(",", "."))
  print("")

  if consumo <= 0 or distancia_barata <= 0:
    print("Consumo ou distância inválidos.")
    return

  if gasolina_cara <= gasolina_barata:
    print("O posto mais barato não é realmente mais barato. Verifique os valores.")
    return

  diferenca_preco = (gasolina_cara - gasolina_barata)
  custo_km_cara = (gasolina_cara / consumo)
  custo_km_barata = (gasolina_barata / consumo)
  valor_pv = ((custo_km_cara * distancia_barata) + (custo_km_barata * distancia_barata))
  valor_sv = (custo_km_barata * (distancia_barata * 2))
  minimo_litros_pv = (valor_pv / diferenca_preco)
  minimo_litros_sv = (valor_sv / diferenca_preco)
  minimo_valor_pv = (minimo_litros_pv * gasolina_barata)
  minimo_valor_sv = (minimo_litros_sv * gasolina_barata)

  limpar_tela()

  print("=====[Se a gasolina que estiver no seu tanque ainda NÃO for a do posto mais barato]=====")
  print("Você precisa colocar no mínimo R$%.2f de combustível (%.2f litros) para compensar ir até o posto mais barato."
        % (minimo_valor_pv, minimo_litros_pv), end="\n\n")

  print("=====[Agora, se a gasolina que estiver no seu tanque JÁ for a do posto mais barato]=====")
  print("Você precisa colocar no mínimo R$%.2f de combustível (%.2f litros) para compensar ir até o posto mais barato."
        % (minimo_valor_sv, minimo_litros_sv), end="\n\n")


def calcular_compensa_economizou():
  print("")
  print("=====[Vamos calcular se o valor que você pretende abastecer irá compensar e o quão irá compensar]=====")
  print("")
  qual_vez = str(input("A gasolina que está no seu tanque ja é do posto mais barato? (sim/não) : ").replace("não", "nao"))
  print("")
  valor_abastecer = float(input("Qual o valor que você pretende abastecer? : ").replace(",", "."))
  print("")
  consumo = float(input("Qual o consumo do seu veículo em kilometros por litro? : ").replace(",", "."))
  print("")
  gasolina_cara = float(input("Qual o  valor do combustível no posto que você costuma abastecer (posto mais caro)? : ").replace(",", "."))
  print("")
  gasolina_barata = float(input("Qual o valor do combustível no posto mais barato? : ").replace(",", "."))
  print("")
  distancia_barata = float(input("Quantos KM você está do posto mais barato? : ").replace(",", "."))
  print("")

  if consumo <= 0 or distancia_barata <= 0:
    print("Consumo ou distância inválidos.")
    return

  if gasolina_cara <= gasolina_barata:
    print("O posto mais barato não é realmente mais barato. Verifique os valores.")
    return

  diferenca_preco = (gasolina_cara - gasolina_barata)
  custo_km_cara = (gasolina_cara / consumo)
  custo_km_barata = (gasolina_barata / consumo)
  valor_pv = ((custo_km_cara * distancia_barata) + (custo_km_barata * distancia_barata))
  valor_sv = (custo_km_barata * (distancia_barata * 2))
  minimo_litros_pv = (valor_pv / diferenca_preco)
  minimo_litros_sv = (valor_sv / diferenca_preco)
  minimo_valor_pv = (minimo_litros_pv * gasolina_barata)
  minimo_valor_sv = (minimo_litros_sv * gasolina_barata)
  quanto_economizara_pv = (((valor_abastecer - minimo_valor_pv) / gasolina_barata) * diferenca_preco)
  quanto_economizara_sv = (((valor_abastecer - minimo_valor_sv) / gasolina_barata) * diferenca_preco)

  limpar_tela()

  if qual_vez == "sim":
    if valor_abastecer > minimo_valor_sv:
      print("=====[Você fará economia colocando esse valor pois o mínimo é R$%.2f]=====" % minimo_valor_sv)
      print("Você irá economizar R$%.2f colocando R$%.2f" % (quanto_economizara_sv, valor_abastecer))
    elif valor_abastecer < minimo_valor_sv:
      print("=====[Você não fará economia colocando esse valor pois o mínimo é R$%.2f]=====" % minimo_valor_sv)
    else:
      print("=====[Você fará economia exata colocando R$%.2f]=====" % minimo_valor_sv)

  if qual_vez == "nao":
    if valor_abastecer > minimo_valor_pv:
      print("=====[Você fará economia colocando esse valor pois o mínimo é R$%.2f]=====" % minimo_valor_pv)
      print("Você irá economizar R$%.2f colocando R$%.2f" % (quanto_economizara_pv, valor_abastecer))
    elif valor_abastecer < minimo_valor_pv:
      print("=====[Você não fará economia colocando esse valor pois o mínimo é R$%.2f]=====" % minimo_valor_pv)
    else:
      print("=====[Você fará economia exata colocando R$%.2f]=====" % minimo_valor_pv)


def economias():
  print("=====[Você quer saber]=====")
  print("O mínimo que tem que abastecer para compensar a locomoção até o posto mais barato [1]")
  print("Se o valor que você pretende abastecer compensa a locomoção até o posto mais barato [2]\n")
  escolha = int(input("Qual deseja, [1] ou [2] ? "))

  if escolha == 1:
    calcular_minimo()
  if escolha == 2:
    calcular_compensa_economizou()

economias()
