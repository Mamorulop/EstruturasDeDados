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
