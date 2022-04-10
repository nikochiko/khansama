from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from util import get_recipe_ldjson_from_url


app = Flask("khansama")

db = SQLAlchemy(app)

recipes = []


@app.route("/khansify")
def khansify():
    url = request.args.get("url")

    if not url:
        return jsonify({"message": "URL query parameter is required!"}), 400

    for r in recipes:
        if r["url"] == url:
            recipe = r
            break
    else:
        recipe = get_recipe_ldjson_from_url(url)

        recipes.append(recipe)

    response = jsonify(recipe)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/recipes")
def get_recipes():
    response = jsonify(recipes)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/recipes/<int:id>")
def get_recipe(id):
    for recipe in recipes:
        if recipe["id"] == id:
            response = jsonify(recipe)
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response

    return "not found", 404
