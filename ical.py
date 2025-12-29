# import requests
# from ics import Calendar
# from datetime import datetime, timedelta, timezone
# from LOCAL import CALENDAR_URL
#
#
# def format_events():
#     url = CALENDAR_URL
#     response = requests.get(url)
#     calendar = Calendar(response.text)
#
#     now = datetime.now(timezone.utc)
#     start_range = now - timedelta(days=7)
#     end_range = now + timedelta(days=14)
#     list = []
#     for event in calendar.events:
#         if event.begin and start_range <= event.begin <= end_range:
#             evento = {"day": event.begin.date().day,
#                       "month": event.begin.date().month,
#                       "name": event.name,
#                       "time": event.begin.strftime("%H:%M")
#                       }
#             list.append(evento)
#     return list
#
#
# if __name__ == "__main__":
#     events = format_events()
#     for event in events:
#         # print(f'Evento: {event["name"]}, el {event["day"]} del {event["month"]} a las {event["time"]}')
#         print(event)

import requests
from ics import Calendar
from datetime import datetime, timedelta, timezone
from LOCAL import CALENDAR_URL


def format_events():
    url = CALENDAR_URL
    response = requests.get(url)
    calendar = Calendar(response.text)

    now = datetime.now(timezone.utc)
    # Rango de visualización (útil para tu e-Paper de 7.5")
    start_range = now - timedelta(days=7)
    end_range = now + timedelta(days=14)

    event_list = []

    for event in calendar.events:
        if event.begin and start_range <= event.begin <= end_range:
            # Guardamos el objeto 'begin' completo para poder ordenar fácilmente
            evento = {
                "begin": event.begin,  # Objeto datetime para ordenar
                "day": event.begin.date().day,
                "month": event.begin.date().month,
                "name": event.name,
                "time": event.begin.strftime("%H:%M")
            }
            event_list.append(evento)

    # ORDENACIÓN: Usamos el campo 'begin' (que incluye fecha y hora)
    event_list.sort(key=lambda x: x["begin"])

    return event_list


if __name__ == "__main__":
    events = format_events()
    for event in events:
        # Ahora aparecerán en orden: del más antiguo al más futuro
        print(f'{event["day"]}/{event["month"]} {event["time"]} - {event["name"]}')