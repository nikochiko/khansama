from flask import Flask, jsonify, request

from util import get_recipe_ldjson_from_url


app = Flask("khansama")

# TODO: setup database


@app.route("/khansify")
def khansify():
    url = request.args.get("url")
    if not url:
        return jsonify({"message": "URL query parameter is required!"}), 400

    recipe = get_recipe_ldjson_from_url(url)
    return jsonify(recipe)
