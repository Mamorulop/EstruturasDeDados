# -*- coding: utf-8 -*-
"""Sistema Gerenciamento de Notas Escolares"""

import sys

# Estrutura de dados principal: Dicionário de alunos
# Formato: alunos[matricula] = {"nome": nome, "notas": {disciplina: [nota1, nota2, ...]}}
alunos = {}
# -Funções de Gerenciamento-
# Cadastra aluno, escreva o nome do aluno e adicione o número de matrícula podendo conter apenas números ou números com a adição de letras

def cadastrar_aluno(matricula: str, nome: str):
    """Cadastra um novo aluno no dicionário 'alunos'."""
    if not matricula or not nome:
        print("Erro: Matrícula e nome não podem ser vazios.")
        return
    if matricula in alunos:
        print(f"Erro: Matrícula ")
    else:
        alunos[matricula] = {"nome": nome, "notas": {}}
        print(f"Aluno ")

# Após aluno resgistrado adicione uma disciplina de acordo com o número de matrícula do aluno e uma nota 
# Pode ser adicionado mais de uma matéria e valores de nota mediante a disciplina escolhida

def registrar_nota(matricula: str, disciplina: str, nota: float):
    """Registra uma nota para um aluno em uma disciplina."""
    if matricula not in alunos:
        print(f"Erro: Aluno com matrícula {matricula} não encontrado.")
        return
    if not disciplina:
        print("Erro: Nome da disciplina não pode ser vazio.")
        return
    try:
        nota_float = float(nota)
        if nota_float < 0:
             raise ValueError("Nota não pode ser negativa.")

        # Se a disciplina ainda não existe para o aluno, cria a lista de notas
        if disciplina not in alunos[matricula]["notas"]:
            alunos[matricula]["notas"][disciplina] = []

        # Adiciona a nota à lista da disciplina
        alunos[matricula]["notas"][disciplina].append(nota_float)
        print(f"Nota {nota_float:.2f} registrada para {alunos[matricula]['nome']} em {disciplina}.")

    except ValueError as e:
        print(f"Erro: Valor da nota inválido ou negativo ({e}). Use números (ex: 7.5).")

# Listagem de alunos mediante ao cadastro feito e aos alunos já inseridos no código 

def listar_alunos():
    """Lista todos os alunos cadastrados."""
    print("\n--- Lista de Alunos Cadastrados ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        # Ordena pela matrícula para exibição consistente
        for matricula in sorted(alunos.keys()):
            print(f"- Matrícula: {matricula}, Nome: {alunos[matricula]['nome']}")
    print("-----------------------------------")

# Ao consultar os alunos é exigido o número de matrícula, apenas um aluno é mostrado por vez 
# Nome e número de matrícula é listado juntamente com as notas do mesmo de acordo com a disciplina adicionada e escolhida pelo usuário 

def consultar_notas_aluno(matricula: str):
    """Consulta e exibe as notas de um aluno específico."""
    if matricula not in alunos:
        print(f"Erro: Aluno com matrícula {matricula} não encontrado.")
        return

    aluno = alunos[matricula]
    print(f"\n--- Notas de {aluno['nome']} ({matricula}) ---")
    if not aluno["notas"]:
        print("Nenhuma nota registrada para este aluno.")
    else:
        # Ordena as disciplinas pelo nome antes de imprimir
        for disciplina in sorted(aluno["notas"].keys()):
            notas_disciplina = aluno["notas"][disciplina]
            notas_str = ", ".join([f"{n:.2f}" for n in notas_disciplina])
            print(f"  - {disciplina}: {notas_str}")
    print("------------------------------------------")

# Calculo da média das disciplinas por meio das notas adicionadas 
# Caso apenas um valor seja adicionado o mesmo será considerado a média do aluno 

def calcular_media_disciplina(matricula: str, disciplina: str):
    """Calcula e exibe a média de um aluno em uma disciplina."""
    if matricula not in alunos:
        print(f"Erro: Aluno com matrícula {matricula} não encontrado.")
        return

    aluno = alunos[matricula]
    if disciplina not in aluno["notas"] or not aluno["notas"][disciplina]:
        print(f"Nenhuma nota encontrada para {aluno['nome']} na disciplina {disciplina}.")
        return

    notas_disciplina = aluno["notas"][disciplina]
    media = sum(notas_disciplina) / len(notas_disciplina)
    print(f"\n--- Média de {aluno['nome']} em {disciplina} ---")
    print(f"Média: {media:.2f}")
    print("-------------------------------------------------")

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

# Loop principal devido a ser um sistema de Gerenciamento de notas, possui uma repetição de ações 
# Cadastro de alunos, Matrícula, Disciplinas, Listagem, Notas e Média de Notas

def main():
    """Loop principal do programa."""
    # Dados iniciais (opcional)
    cadastrar_aluno("M1", "Maurício")
    cadastrar_aluno("M2", "Senhor das Trevas")
    registrar_nota("M1", "Python", 8.0)
    registrar_nota("M1", "Python", 9.5)
    registrar_nota("M2", "Python", 7.0)
    registrar_nota("M1", "Algoritmos", 6.5)
    print("\nDados iniciais carregados.")

    while True:
        exibir_menu()
        opcao = obter_opcao()

        if opcao == 1:
            mat = input("Matrícula: ").strip()
            nome = input("Nome: ").strip()
            cadastrar_aluno(mat, nome)
        elif opcao == 2:
            mat = input("Matrícula do Aluno: ").strip()
            disc = input("Disciplina: ").strip()
            while True:
                nota_str = input("Nota: ").strip().replace(",", ".")
                try:
                    nota_val = float(nota_str)
                    break
                except ValueError:
                    print("Nota inválida. Digite um número.")
            registrar_nota(mat, disc, nota_val)
        elif opcao == 3:
            listar_alunos()
        elif opcao == 4:
            mat = input("Matrícula do Aluno: ").strip()
            consultar_notas_aluno(mat)
        elif opcao == 5:
            mat = input("Matrícula do Aluno: ").strip()
            disc = input("Disciplina: ").strip()
            calcular_media_disciplina(mat, disc)
        elif opcao == 0:
            print("Obrigado e Tamo junto! Encerra aqui")
            sys.exit()
        else:
            print("Opção inválida.")

        input("\nEnter para continuar...")

if __name__ == "__main__":
    main()

#AAAAAAAAAAAAAA EXPLICAÇÃO