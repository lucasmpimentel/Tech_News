import sys


# Requisito 12
def analyzer_menu():
    entrada = input(
        """
    Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
    """
    )

    resposta = [
        "Digite quantas notícias serão buscadas:",
        "Digite o título:",
        "Digite a data no formato aaaa-mm-dd:",
        "Digite a tag:",
        "Digite a categoria:"
    ]

    try:
        opcao = int(entrada)

        if 0 <= int(entrada) <= 7:
            if 0 <= int(entrada) <= 4:
                print(resposta[opcao])
        else:
            raise ValueError
    except ValueError:
        print("Opção inválida", file=sys.stderr)
