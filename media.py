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
