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
