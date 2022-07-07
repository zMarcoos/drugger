from mechanics import *

load()

while True:
    print('(1) Agendar')
    print('(2) - Listar alarmes')
    print('(3) - Sobre')
    print('(0) - Sair')

    option = input('Selecione: ')
    if option == '1':
        schedule = create_schedule()
        if schedule is None:
            print('Não foi possível agendar o alarme. Ocorreu algo inesperado.')
        else:
            save(schedule)
            print('Alarme agendado com sucesso!')
    elif option == '2':
        list_schedules()
    elif option == '3':
        print(get_about())
    elif option == '0':
        break
    else:
        print('Opção inválida!')
