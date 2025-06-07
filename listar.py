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
