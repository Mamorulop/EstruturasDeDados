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
