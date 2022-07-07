import os
from time import sleep
from file import *
from datetime import datetime
from threading import Thread
from playsound import playsound

schedules = []
schedule_filename = 'schedules.txt'

def in_time(schedule):
    now = datetime.timestamp(datetime.now())
    alarm_timestamp = schedule['date'] - now
    return alarm_timestamp > 0

def has_same_schedule(timestamp: float):
    for schedule in schedules:
        if schedule['date'] == timestamp:
            return True
    return False

def save():
    write(schedule_filename, schedules)

def confirm_alarm(schedule):
    if schedule in schedules:
        schedules.remove(schedule)

    save()

    print('Digite "voltar" confirmar o alarme e voltar para o menu principal: ', end='')

def set_alarm(schedule):
    if in_time(schedule) > 0:
        sleep(int(schedule['date'] - datetime.timestamp(datetime.now())))

        print(f'\n\nALARME TOCANDO!!\n\nAlarme: {schedule["name"]}\nHorário: {datetime.fromtimestamp(schedule["date"])}\nRemédios: {", ".join(schedule["drugs"])}\nDescrição: {schedule["description"]}\n')

        audio_file = os.path.dirname(__file__) + '\\note.mp3'
        playsound(audio_file)

    confirm_alarm(schedule)

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
        
        schedule = {
            'name': name,
            'date': timestamp,
            'drugs': drugs,
            'carer': carer,
            'description': description
        }

        schedules.append(schedule)
        save()

        Thread(target=set_alarm, args=(schedule, )).start()
        
        return schedule

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

            print(f'{index + 1}. {name} ({datetime.fromtimestamp(date)})\n  - Autor: {carer}\n  - Medicamentos: {drugs}\n  - Descrição: {description}')
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

def load():
    try:
        file = open(schedule_filename, 'r', encoding='utf8')

        for line in file.readlines():
            schedules.append(read(line))
    except:
        print('Erro na função load')
    finally:
        file.close()

    for schedule in schedules:
        if not in_time(schedule):
            schedules.remove(schedule)
            save()

            print('Alarme removido porque não estava no horário.')
            continue

        Thread(target=set_alarm, args=(schedule, )).start()
