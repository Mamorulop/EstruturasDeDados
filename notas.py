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
