# web_app/routes/home_routes.py
from flask import Blueprint, render_template, redirect, request, flash
from app.beer_finder import get_beer
import pandas as pd


results = get_beer(zip_code)
html = results.to_html()

print(html)