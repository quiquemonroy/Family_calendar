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
    list = []
    for event in calendar.events:
        if event.begin and start_range <= event.begin <= end_range:
            evento = {"day": event.begin.date().day,
                      "month": event.begin.date().month,
                      "name": event.name,
                      "time": event.begin.strftime("%H:%M")
                      }
            list.append(evento)
    return list


if __name__ == "__main__":
    events = format_events()
    for event in events:
        print(event["name"])
