import calendar
from datetime import datetime, timedelta

WEEK = ["L", "M", "X", "J", "V", "S", "D"]
YEAR = datetime.now().year
MONTH = datetime.now().month


def get_weeks():
    hoy = datetime.now()
    semanas = []
    fila_uno = []
    fila_dos = []
    if hoy.weekday() == 0:
        for i in range(7):
            fila_uno.append(hoy + timedelta(days=i))
        for i in range(7):
            fila_dos.append(fila_uno[-1] + timedelta(days=i))
    elif hoy.weekday() == 1:
        for i in range(1):
            fila_uno.append(hoy - timedelta(days=i + 1))
        fila_uno.reverse()
        for i in range(6):
            fila_uno.append(hoy + timedelta(days=i))
        for i in range(1, 8):
            fila_dos.append(fila_uno[-1] + timedelta(days=i))
    elif hoy.weekday() == 2:
        for i in range(2):
            fila_uno.append(hoy - timedelta(days=i + 1))
        fila_uno.reverse()
        for i in range(5):
            fila_uno.append(hoy + timedelta(days=i))
        for i in range(1, 8):
            fila_dos.append(fila_uno[-1] + timedelta(days=i))
    elif hoy.weekday() == 3:
        for i in range(3):
            fila_uno.append(hoy - timedelta(days=i + 1))
        fila_uno.reverse()
        for i in range(4):
            fila_uno.append(hoy + timedelta(days=i))
        for i in range(1, 8):
            fila_dos.append(fila_uno[-1] + timedelta(days=i))
    elif hoy.weekday() == 4:
        for i in range(4):
            fila_uno.append(hoy - timedelta(days=i + 1))
        fila_uno.reverse()
        for i in range(3):
            fila_uno.append(hoy + timedelta(days=i))
        for i in range(1, 8):
            fila_dos.append(fila_uno[-1] + timedelta(days=i))
    elif hoy.weekday() == 5:
        for i in range(4):
            fila_uno.append(hoy - timedelta(days=i + 1))
        fila_uno.reverse()
        for i in range(2):
            fila_uno.append(hoy + timedelta(days=i))
        for i in range(1, 8):
            fila_dos.append(fila_uno[-1] + timedelta(days=i))
    elif hoy.weekday() == 6:
        for i in range(6):
            fila_uno.append(hoy - timedelta(days=i + 1))
        fila_uno.reverse()
        for i in range(1):
            fila_uno.append(hoy + timedelta(days=i))
        for i in range(1, 8):
            fila_dos.append(fila_uno[-1] + timedelta(days=i))
    semanas.append(fila_uno)
    semanas.append(fila_dos)
    return semanas


if __name__ == "__main__":
    semanas = get_weeks()
    for semana in semanas:
        for dia in semana:
            print(WEEK[dia.weekday()], dia.day)
