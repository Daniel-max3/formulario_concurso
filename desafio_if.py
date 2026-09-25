print("  SISTEMA DE INSCRIÇÃO - CONCURSO  ")

nome = input("Seu nome completo: ")
idade = int(input("Sua idade: "))
cpf = input("Seu CPF: ")

status_inscricao = "INSCRIÇÃO APROVADA"
documento_adicional = "Nenhum" 

if idade > 18:
    print("Idade adequada")
else:
    print("Inscrição não permitida: Candidato menor de 18 anos.")
    exit()

#Escolaridade

print("\n ---Escolaridade-=-")
print("1 - Ensino Médio \n2 - Ensino Superior \n3 - Pós-graduação")
opcao_escolaridade = int(input("Escolha a opção (1, 2 ou 3): "))

if opcao_escolaridade == "1":
    escolaridade = "Ensino Médio"
elif opcao_escolaridade == "2":
    escolaridade = "Ensino Superior"
elif opcao_escolaridade == "3":
    escolaridade = "Pós-graduação"
else:
    escolaridade = "Opção invalida"

#Documentos

print("\n ---Sexo--- ")
sexo = input("Digite M para Masculino ou F para Feminino: ")

if sexo == "M":
    documento_adicional = "Certificado de Reservista Obrigatorio"
elif sexo == "F":
    documento_adicional = "Não a necessidade de documento militar"
else:
    documento_adicional = "Valor de sexo invalido"

print("1 - Administração \n2 - Tecnologia da Informação \n3 - Educação")
opcao_area = input("Escolha a opção (1, 2 ou 3): ")

#Área profissional

if opcao_area == "1":
    area_profisional = "Administração"
    cargo = "Analista Administrativo"
elif opcao_area == "2":
    area_profisional = "Tecnologia da Informação"
    cargo = "Analista de Sistemas"
elif opcao_area == "3":
    area_profisional = "Educação"
    cargo = "Professor"
else:
    area_profisional = ""
    cargo = "Não definido"

print("Resumo da inscrição")
print(f"Nome do candidato: {nome}")
print(f"CPF informado: {cpf}")
print(f"Idade: {idade}")
print(f"Escolaridade escolhida: {escolaridade}")
print(f"Área profissional selecionada: {area_profisional}")
print(f"Documento adicional necessário: {documento_adicional}")
print(f"\nStatus da inscrição: {status_inscricao}")

if idade >= 18 and escolaridade and sexo in ["M", "F"]:
    print("\nSITUAÇÃO: INSCRIÇÃO APROVADA!")
else:
    print("\nSITUAÇÃO: INSCRIÇÃO COM PENDÊNCIAS!")