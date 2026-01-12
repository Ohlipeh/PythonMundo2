nome = str(input("Qual é seu nome? "))
if nome == "André":
    print("Que nome lindo você tem!")
elif nome == "Maria" or nome == "Pedro" or nome == "Paulo":
    print("Seu nome é bem popular no Brasil.")
else:
    print("Seu nome é tão normal!")
print(f"Tenha um bom dia, {nome}!")
