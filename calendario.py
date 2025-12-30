from datetime import datetime, timedelta

WEEK = ["L", "M", "X", "J", "V", "S", "D"]

def get_weeks():
    hoy = datetime.now()
    # Encontramos el lunes de esta semana restando su número de día actual
    lunes_actual = hoy - timedelta(days=hoy.weekday())

    # Creamos una lista con los 14 días seguidos
    todos_los_dias = [lunes_actual + timedelta(days=i) for i in range(14)]

    # Partimos la lista en dos bloques de 7
    fila_uno = todos_los_dias[:7]
    fila_dos = todos_los_dias[7:]

    return [fila_uno, fila_dos]


if __name__ == "__main__":
    semanas = get_weeks()
    for semana in semanas:
        for dia in semana:
            print(WEEK[dia.weekday()], dia.day)
