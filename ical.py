import requests
from ics import Calendar
from datetime import datetime, timedelta, timezone
from LOCAL import CALENDAR_URL


def format_events():
    url = CALENDAR_URL
    response = requests.get(url)
    calendar = Calendar(response.text)

    now = datetime.now(timezone.utc)
    start_range = now - timedelta(days=7)
    end_range = now + timedelta(days=14)

    event_dict = {event.begin.date().day: [] for event in calendar.events}

    for event in calendar.events:
        if event.begin and start_range <= event.begin <= end_range:
            evento = {
                "begin": event.begin,
                "day": event.begin.date().day,
                "month": event.begin.date().month,
                "name": event.name,
                "time": event.begin.strftime("%H:%M")
            }
            event_dict[evento["day"]].append(evento)

    for day in event_dict:
        event_dict[day].sort(key=lambda x: x["begin"])


    return event_dict


if __name__ == "__main__":
    events = format_events()
    # for event in events:
    #     # Ahora aparecerán en orden: del más antiguo al más futuro
    #     print(f'{event["day"]}/{event["month"]} {event["time"]} - {event["name"]}')
    for event in events:
        print(f'{event}: {events[event]}')

