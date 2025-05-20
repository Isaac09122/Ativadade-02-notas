



print (" █████╗ ████████╗██╗██╗   ██╗██╗██████╗  █████╗ ██████╗ ███████╗     ██████╗ ██████╗ ")
print ("██╔══██╗╚══██╔══╝██║██║   ██║██║██╔══██╗██╔══██╗██╔══██╗██╔════╝    ██╔═████╗╚════██╗ ")
print ("███████║   ██║   ██║██║   ██║██║██║  ██║███████║██║  ██║█████╗      ██║██╔██║ █████╔╝ ")
print ("██╔══██║   ██║   ██║╚██╗ ██╔╝██║██║  ██║██╔══██║██║  ██║██╔══╝      ████╔╝██║██╔═══╝  ")
print ("██║  ██║   ██║   ██║ ╚████╔╝ ██║██████╔╝██║  ██║██████╔╝███████╗    ╚██████╔╝███████╗")
print ("╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝     ╚═════╝ ╚══════╝ ")
print ("                                                                                     ")

notas = []

while True:
    # colocar a nota
    entrada = input("Digite uma nota de 0 a 10 ou 'fim' para encerrar: ")

    # verificar
    if entrada.lower() == 'fim':
        break

    # entrada para número
    try:
        nota = float(entrada)

        # verifica se a nota entre 0 e 10
        if 0 <= nota <= 10:
            notas.append(nota)  # adiciona a nota na lista
        else:
            print("Nota inválida, Digite um valor entre 0 e 10.")
    except:
        print("Entrada inválida, Digite um número ou 'fim'.")

# verifica se as notas foram inseridas 
if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
