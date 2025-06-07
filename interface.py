# --- Interface de Console ---
# Interface de usuário, de acordo com os número apresentados as ações de Cadastro, Registro de nota, Listagem de alunos, Consulta de notas e Calculo de média podem ser 
# realizadas
# Contendo consigo a opção de menu de saída a qual encerra o programa
# Todos listados por meio de números as quais as opções requeridas devem ser escolhidas e inseridas ao executar o código 


def exibir_menu():
    """Exibe o menu principal."""
    print("\n--- Sistema de Notas ---")
    print("1. Cadastrar Aluno")
    print("2. Registrar Nota")
    print("3. Listar Alunos")
    print("4. Consultar Notas de Aluno")
    print("5. Calcular Média de Aluno em Disciplina")
    print("0. Sair")
    print("-------------------------------------")

def obter_opcao() -> int:
    """Obtém a opção do usuário."""  
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            print("Erro: Por favor, insira um número.")
