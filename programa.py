import requests
import json
from cnpj import cnpjs

opcao = int(input("\nEscolha a opção desejada:\n\n1 - Listar os CNPJs cadastrados\n2 - Importar dados de CNPJ\n0 - Sair\n"))

while opcao != 0:

    if opcao == 1:
        lista = cnpjs()
        print(lista.listarCNPJ())

    elif opcao == 2:

        cnpjDesejado = input("\nDigite o CNPJ desejado: ")
        req = requests.get("https://www.receitaws.com.br/v1/cnpj/%s" % cnpjDesejado)

        if req.status_code == requests.codes.ok:
            j = json.loads(req.text)

            cnpjSelecionado = cnpjs()

            cnpjSelecionado.cnpj = j['cnpj']
            cnpjSelecionado.razaoSocial = j['nome']
            cnpjSelecionado.email = j['email']
            
            cnpjSelecionado.salvar()

            print("CNPJ", cnpjDesejado, "cadastrado com sucesso!")

    else:
        print("\nOpção inválida, tente novamente\n")
    
    opcao = int(input("\nEscolha a opção desejada\n1 - Listar os CNPJs cadastrados\n2 - Importar dados de CNPJ\n0 - Sair\n"))