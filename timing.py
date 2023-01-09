def targetTime(dataAlvo, horaAlvo):
    from datetime import date, datetime

    data = date.today().strftime('%d-%m-%Y').split('-')
    hora = datetime.now().strftime('%H:%M:%S').split(':')

    dataAlvo = dataAlvo.split('-')
    horaAlvo = horaAlvo.split(':')

    if int(data[2]) > int(dataAlvo[2]):
        return True
    elif int(data[1]) > int(dataAlvo[1]) and int(data[2]) == int(dataAlvo[2]):
        return True
    elif int(data[0]) > int(dataAlvo[0]) and int(data[1]) == int(dataAlvo[1]) and int(data[2]) == int(dataAlvo[2]):
        return True
    elif int(hora[0]) > int(horaAlvo[0]) and int(data[0]) == int(dataAlvo[0]) and int(data[1]) == int(dataAlvo[1]) and int(data[2]) == int(dataAlvo[2]):
        return True
    elif int(hora[1]) > int(horaAlvo[1]) and int(hora[0]) == int(horaAlvo[0]) and int(data[0]) == int(dataAlvo[0]) and int(data[1]) == int(dataAlvo[1]) and int(data[2]) == int(dataAlvo[2]):
        return True
    elif int(hora[2]) > int(horaAlvo[2]) and int(hora[1]) == int(horaAlvo[1]) and int(hora[0]) == int(horaAlvo[0]) and int(data[0]) == int(dataAlvo[0]) and int(data[1]) == int(dataAlvo[1]) and int(data[2]) == int(dataAlvo[2]):
        return True
    else:
        return False

print(targetTime('08-01-2023','12:15:00'))
