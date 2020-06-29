# web_app/routes/weather_routes.py

from flask import Blueprint, render_template, request

from app.beer_finder import get_beer

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/form")
def weather_form():
    print("VISITED THE WEATHER FORM...")
    return render_template("weather_form.html")

@weather_routes.route("/weather/forecast", methods=["GET", "POST"])
def weather_forecast():
    print("GENERATING A WEATHER FORECAST...")

    if request.method == "POST":
        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        zip_code = request.form["zip_code"]
    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        zip_code = request.args["zip_code"] #> {'zip_code': '20057'}

    results = get_beer(zip_c=zip_code)
    print(results.keys())
    return render_template("weather_forecast.html", zip_code=zip_code, results=results)