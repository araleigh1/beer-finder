# web_app/routes/weather_routes.py

import os
from flask import Blueprint, render_template, request
import pandas as pd
from app.beer_finder import get_beer

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/form")
def weather_form():
    print("VISITED THE WEATHER FORM...")
    return render_template("weather_form.html")

CSV_FILENAME = "data.csv"
csv_filepath = os.path.join("data",CSV_FILENAME)
df2 = pd.read_csv(csv_filepath, encoding='latin1')
df2.to_html(header = "true", table_id = "table")

@weather_routes.route("/weather/forecast", methods=["GET", "POST"])
def weather_forecast():
    print("GENERATING A WEATHER FORECAST...")

    if request.method == "POST":
        zip_code = request.form["zip_code"]
    elif request.method == "GET":
        zip_code = request.args["zip_code"] #> {'zip_code': '20057'}

    results = get_beer(zip_code)
    #print(results.keys())
    return render_template("weather_forecast.html", zip_code=zip_code, tables=[df2.to_html(classes='data')], titles=df2.columns.values)