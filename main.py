from mechanics import *

load()

while True:
    print('\n')
    print('(1) Agendar')
    print('(2) - Listar alarmes')
    print('(3) - Sobre')
    print('(0) - Sair')
    print('\n')

    option = input('Selecione: ').lower()
    if option == '1':
        schedule = create_schedule()
        if schedule is None:
            print('\nNão foi possível agendar o alarme. Ocorreu algo inesperado.\n')
        else:
            print('\nAlarme agendado com sucesso!\n')
    elif option == '2':
        list_schedules()
    elif option == '3':
        print(get_about())
    elif option == '0':
        break
    elif option == 'voltar':
        print('Voltando...\n')
    else:
        print('Opção inválida!')
        continue
