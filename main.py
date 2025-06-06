from flask import Flask, render_template
from datetime import datetime
import random
from calendario import get_weeks
from ical import format_events
from weather import get_weather

app = Flask("__main__")

#
@app.route("/")
def calendario():
    events = format_events()
    MONTHS = ["Enero",
              "Febrero",
              "Marzo",
              "Abril",
              "Mayo",
              "Junio",
              "Julio",
              "Agosto",
              "Septiembre",
              "Octubre",
              "Noviembre",
              "Diciembre"
              ]

    WEEK = [("L","🍏"), ("M","🥛"), ("X","🍏"),( "J","🥪"), ("V","🍏"), ("S",""), ("D","")]
    TODAY = datetime.now().day
    MONTH = int(datetime.now().month)-1
    semanas = get_weeks()
    weather = get_weather()
    img = random.randint(1,31)
    return render_template("calendar.html",
                           week=WEEK,
                           semanas=semanas,
                           events=events,
                           today=int(TODAY),
                           month=MONTHS[MONTH],
                           weather=weather,
                           img=img)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
