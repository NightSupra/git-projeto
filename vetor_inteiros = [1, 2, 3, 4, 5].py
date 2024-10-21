class Aluno:
    def _init_(self, nome):
        self.nome = nome
        self.notas = []
        self.recuperacao = 0
        self.media = 0

    def adicionar_notas(self, notas):
        self.notas = notas
        self.calcular_media()

    def calcular_media(self):
        if self.notas:
            self.media = sum(self.notas) / len(self.notas)

    def calcular_recuperacao(self):
        if self.media < 6:
            self.recuperacao = (self.media + self.recuperacao) / 2

def listar_alunos(alunos):
    for i, aluno in enumerate(alunos):
        print(f"{i + 1}. {aluno.nome} - Notas: {aluno.notas} - Média: {aluno.media:.2f} - Recuperação: {aluno.recuperacao:.2f}")

def main():
    alunos = [
        Aluno("Alice"),
        Aluno("Bruno"),
        Aluno("Carlos"),
        Aluno("Daniela"),
        Aluno("Eduardo"),
        Aluno("Fernanda"),
        Aluno("Gustavo"),
        Aluno("Helena"),
        Aluno("Igor"),
        Aluno("Julia"),
    ]

    # Adicionando notas para os alunos
    for aluno in alunos:
        notas = []
        for i in range(4):
            nota = float(input(f"Digite a nota {i + 1} de {aluno.nome}: "))
            notas.append(nota)
        aluno.adicionar_notas(notas)

    # Listar alunos e suas médias
    print("\nLista de Alunos:")
    listar_alunos(alunos)

    # Selecionar aluno para recuperação
    escolha = int(input("\nEscolha o número do aluno para calcular a recuperação: ")) - 1
    if 0 <= escolha < len(alunos):
        aluno_selecionado = alunos[escolha]
        aluno_selecionado.recuperacao = float(input("Digite a nota de recuperação: "))
        aluno_selecionado.calcular_recuperacao()
        print(f"\nMédia final de {aluno_selecionado.nome}: {aluno_selecionado.media:.2f} (Recuperação: {aluno_selecionado.recuperacao:.2f})")
    else:
        print("Escolha inválida.")

if __name__ == "_main_":
    main()