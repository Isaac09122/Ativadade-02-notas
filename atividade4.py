
print (" ________  _________  ___  ___      ___ ___  ________  ________  ________  _______   ________  ___   ___      ")
print ("|\   __  \|\___   ___\\  \|\  \    /  /|\  \|\   ___ \|\   __  \|\   ___ \|\  ___ \ |\   __  \|\  \ |\  \     ")
print ("\ \  \|\  \|___ \  \_\ \  \ \  \  /  / | \  \ \  \_|\ \ \  \|\  \ \  \_|\ \ \   __/|\ \  \|\  \ \  \\_\  \    ")
print (" \ \   __  \   \ \  \ \ \  \ \  \/  / / \ \  \ \  \ \\ \ \   __  \ \  \ \\ \ \  \_|/_\ \  \\\  \ \______  \   ")
print ("  \ \  \ \  \   \ \  \ \ \  \ \    / /   \ \  \ \  \_\\ \ \  \ \  \ \  \_\\ \ \  \_|\ \ \  \\\  \|_____|\  \  ")
print ("   \ \__\ \__\   \ \__\ \ \__\ \__/ /     \ \__\ \_______\ \__\ \__\ \_______\ \_______\ \_______\     \ \__\ ")
print ("    \|__|\|__|    \|__|  \|__|\|__|/       \|__|\|_______|\|__|\|__|\|_______|\|_______|\|_______|      \|__| ")

# calcula o valor da gorjeta 
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    # Calcula a gorjeta 
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


print("=== Calculadora de Gorjeta ===")


valor = float(input("Digite o valor total da conta (R$): "))


porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))

resultado = calcular_gorjeta(valor, porcentagem)

print(f"O valor da gorjeta é: R$ {resultado:.2f}")