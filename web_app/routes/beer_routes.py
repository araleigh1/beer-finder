# web_app/routes/weather_routes.py

import os
from flask import Blueprint, render_template, request
import pandas as pd
from app.beer_finder import get_beer

beer_routes = Blueprint("beer_routes", __name__)

@beer_routes.route("/zip_form")
def zip_form():
    print("-----------------------------------------------------------------------")
    print("SEARCHING LOCAL BARS, RESTAURANTS, AND STORES...")
    print("-----------------------------------------------------------------------")
    return render_template("zip_form.html")

#df2 = get_beer(zip_code)


#CSV_FILENAME = "data.csv"
#csv_filepath = os.path.join("data",CSV_FILENAME)
#df2 = pd.read_csv(csv_filepath, encoding='latin1')
#df2.to_html(header = "true", table_id = "table")

@beer_routes.route("/beer_ranking", methods=["GET", "POST"])
def zip_forecast():

    if request.method == "POST":
        zip_code = request.form["zip_code"]
    elif request.method == "GET":
        zip_code = request.args["zip_code"] #> {'zip_code': '20057'}

    results = get_beer(zip_code)
    results.to_html(header = "true", table_id = "table")
    return render_template("beer_ranking.html", zip_code=zip_code, tables=[results.to_html(classes='data')], titles=results.columns.values)