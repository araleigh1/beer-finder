# web_app/routes/weather_routes.py

import os
from flask import Blueprint, render_template, request
import pandas as pd
from app.beer_finder import get_beer

beer_routes = Blueprint("beer_routes", __name__)

@beer_routes.route("/zip_form")
def zip_form():
    return render_template("zip_form.html")

@beer_routes.route("/beer_ranking", methods=["GET", "POST"])
def zip_forecast():

    if request.method == "POST":
        zip_code = request.form["zip_code"]
    elif request.method == "GET":
        zip_code = request.args["zip_code"] #> {'zip_code': '20057'}

    results = get_beer(zip_code)
    
    results.to_html(header = "true", table_id = "table",formatters={'Website':lambda x:f'<a href="{x}">{x}</a>'}, escape=False)
    return render_template("beer_ranking.html", zip_code=zip_code, tables=[results.to_html(classes='table table-striped table-hover thead-light')], titles=results.columns.values)
    