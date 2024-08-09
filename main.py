# lista de notas
notas = []

# loop
while True:
    # exibir menu
    print('1 - Inserir nota.')
    print('2 - Calcular media das notas.')
    print('3 - Sair do programa.')

    # usuario informa opção desejada
    opcao = input('opção desejada: ')

    # verifica a opção escolhida
    match opcao:

        case '1':
            # usuario informa a nova nota
            nova_nota = str (input('Informe nova nota de 0 a 10: ')).replace(',', '.')

            # insere a nova nota ou retorna erro
            try:
                # converter a nova nota para float
                nova_nota = float(nova_nota)

                # verificar se a nota é maior que 0 e menor que 10
                if nova_nota >= 0 and nova_nota <= 10:
                    notas.append(nova_nota)
                    print(f'Nota {nova_nota} inserida com sucesso')
                else:
                    print('Nota invalida')
            except:
                print('Não foi possivel inserir a nova nota.')
            finally:
                continue
        case '2':
            # calcular A MEDIA OU RETORNA ERRO
            try:
                media = sum(notas) / len(notas)
                print(f' A media do aluno é {media:,.2f}.')
            except:
                print('Nao foi possivel calcular a media')
            finally:
                continue
        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('Opção invalida.')
            continue









