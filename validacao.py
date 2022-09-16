def invalid_name(name):
    for c in name:
        if c.upper() not in "ABÇCDEFGHIJKLMNOPQRSTUVWXYZ  ÁÃÀÂÍÎÌÓÕÔÒÚÙÛÉÊÈ":
            return True
    return False


def invalid_int(num):
    try:
        int(num)
        return False
    except:
        return True


def invalid_data(data):
    try:
        if data[2] != "/" or data[5] != "/":
            return True
    except:
        return True
    data = data.split("/")
    for d in data:
        if not d.isdigit():
            return True
    if not valida_data(int(data[1]), int(data[0]), int(data[2])):
        return True
    return False


def valida_data(month, day, year):
    if (month > 0 and month <= 12 and year > 0):
        if (month == 12 and day > 0 and day <= 31):
            return True
        elif (month == 11 and day > 0 and day <= 30):
            return True
        elif (month == 10 and day > 0 and day <= 31):
            return True
        elif (month == 9 and day > 0 and day <= 30):
            return True
        elif (month == 8 and day > 0 and day <= 31):
            return True
        elif (month == 7 and day > 0 and day <= 31):
            return True
        elif (month == 6 and day > 0 and day <= 30):
            return True
        elif (month == 5 and day > 0 and day <= 31):
            return True
        elif (month == 4 and day > 0 and day <= 30):
            return True
        elif (month == 3 and day > 0 and day <= 31):
            return True
        elif (month == 2 and day > 0 and day <= 28):
            return True
        elif (month == 1 and day > 0 and day <= 30):
            return True
        elif (month == 2 and day > 0 and day <= 29 and bis(year)):
            return True
    return False


def bis(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def invalid_hora(hora):
    if len(hora) != 5:
        return True
    if hora[2] != ":":
        return True
    horas = hora.split(":")
    for d in horas:
        if invalid_int(d):
            return True
    hora = int(horas[0])
    minutos = int(horas[1])
    if hora >= 8 and hora <= 11 or hora >= 13 and hora <= 17:
        if minutos >= 0 and minutos <= 60:
            return False
    return True


def validar_cpf(cpf):
    try:
        if cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":
            return False
        if "." in cpf and "-" in cpf and len(cpf) == 14:
            sep1 = cpf.split("-")
            sep2 = sep1[0].split('.')
            digits = sep2[0] + sep2[1] + sep2[2]
            if not digits.isdigit():
                return False
            v1 = int(digits[0]) * 10 + int(digits[1]) * 9 + int(
                digits[2]) * 8 + int(digits[3]) * 7 + int(digits[4]) * 6 + int(
                    digits[5]) * 5 + int(digits[6]) * 4 + int(
                        digits[7]) * 3 + int(digits[8]) * 2
            r1 = v1 * 10 % 11
            if r1 == 10:
                r1 = 0
            if r1 != int(sep1[1][0]):
                return False
            v2 = int(digits[0]) * 11 + int(digits[1]) * 10 + int(
                digits[2]) * 9 + int(digits[3]) * 8 + int(digits[4]) * 7 + int(
                    digits[5]) * 6 + int(digits[6]) * 5 + int(
                        digits[7]) * 4 + int(digits[8]) * 3 + int(
                            sep1[1][0]) * 2
            r2 = v2 * 10 % 11
            if r2 == 10:
                r2 = 0
            if r2 != int(sep1[1][1]):
                return False

            if digits[0] == digits[1] == digits[2] == digits[3] == digits[
                    4] == digits[5] == digits[6] == digits[7] == digits[
                        8] == sep1[1][1] == sep1[1][0]:
                return False

            return True

        else:
            return False
    except:
        return False
