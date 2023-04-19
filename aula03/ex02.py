print("Programa de emprestimos ## Selecione: (0 - Não e 1 - Sim)")

negativo = int(input("Você possui o nome negativado? "))

if negativo == 1:
    print("Não é possível realizar o empréstimo.")
else:
    carteira = int(input("Você possui carteira assinada? "))
    if carteira == 0:
        print("Não é possível realizar o empréstimo.")
    else:
        casaPropria = int(input("Você possui casa própria? "))
        if casaPropria == 0:
            print("Não é possível realizar o empréstimo.")
        else:
            print("É possível conceder empréstimo")