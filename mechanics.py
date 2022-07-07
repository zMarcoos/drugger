from file import *
from datetime import datetime, date

schedules = []
schedule_filename = 'schedules.txt'
past_schedules_filename = 'past_schedules.txt'

def load():
    try:
        file = open(schedule_filename, 'r', encoding='utf8')

        for line in file.readlines():
            schedules.append(read(line))
    except:
        print('Erro na função load')
    finally:
        file.close()

def has_same_schedule(timestamp: float):
    for schedule in schedules:
        if schedule['date'] == timestamp:
            return True
    return False

def save(schedule):
    schedules.append(schedule)
    write(schedule_filename, [schedule])

def confirm_alarm(schedule):
    write(past_schedules_filename, [schedule])
    schedules.remove(schedule)

    print('Parabéns! O alarme funcionou!!!!')

    input('Digite aqui para saber que você sabe que marcou o alarme: ')

def create_schedule():
    name = input('Digite um nome para o alarme: ')
    date = input('Digite a hora (d/m/aaaa) (HH:MM): ').split(' ')

    date_part_one = date[0].split('/')
    date_part_two = date[1].split(':')

    timestamp = datetime(
        day=int(date_part_one[0]),
        month=int(date_part_one[1]),
        year=int(date_part_one[2]),
        hour=int(date_part_two[0]),
        minute=int(date_part_two[1])
    ).timestamp()

    if has_same_schedule(timestamp):
        print('Já existe um alarme neste mesmo horário. Agende um que não esteja neste horário.')
    else:
        drugs_input = input('Informe os medicamentos separando-os por ";" (Medicamento dosagem medida; Medicamento dosagem medida): ').split(';')
        carer = input('Digite o nome do cuidador ou o seu próprio nome mesmo: ')
        description = input('Digite a descrição do alarme: ')

        drugs = []
        for drug in drugs_input:
            drugs.append(drug.strip())

        return {
            'name': name,
            'date': timestamp,
            'drugs': drugs,
            'carer': carer,
            'description': description
        }

def list_schedules():
    amount = len(schedules)
    if amount == 0:
        print('\nNão existem alarmes cadastrados!\n')
    else:
        print('\n')
        for index in range(amount):
            schedule = schedules[index]

            name = schedule['name']
            date = schedule['date']
            drugs = schedule['drugs']
            carer = schedule['carer']
            description = schedule['description']

            print(f'{index + 1}. {name} ({date})\n  - Autor: {carer}\n  - Medicamentos: {drugs}\n  - Descrição: {description}')
        print('\n')


def get_about():
    return """
     O Drugger foi pensado e projetado para atender melhor aos idosos e auxiliar seus
     cuidadores com o duro trabalho que é lembrar de todos os remédios para manter
     um bom atendimento e fazer essa ponte entre os eles (idosos e cuidadores) pela 
     saúde dos nossos queridos idosos! 

     Pensando nesse problema mal resolvido, surgimos-nos com essa solução e com
     essa inovação para solucionarmos esse impasse na vida de nossos velhinhos.

     Esse aplicativo tem o intuito secundáriode melhoria cognitiva de estímulos neuro-
     lógicos que faz os usuários aprimorarem sua lembrança de longo prazo em forma-
     tos de horários.

     Estamos na versão 1.0, mas logo estaremos fazendo atualizações. Curtam essa versão!
     """

