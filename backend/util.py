import html
import json
import random
import re
from bs4 import BeautifulSoup
from typing import Any, Union, NamedTuple

import requests


class Recipe(NamedTuple):
    id: int
    name: str
    author: dict[str, str]
    cookTime: str
    prepTime: str
    totalTime: str
    description: str
    tags: list[str]
    image: str
    ingredients: list[str]
    instructions: list[dict[str, Any]]
    url: str


class KhansamaException(Exception):
    pass


class NoLDJSONException(KhansamaException):
    pass


def get_recipe_ldjson_from_url(url: str) -> dict:
    r = requests.get(url)
    r.raise_for_status()

    soup = BeautifulSoup(r.text)
    elements = soup.find_all("script", type="application/ld+json")

    ldjson = get_recipe_ldjson_from_list([el.string for el in elements])

    cookTime = ldjson.get("cookTime")
    if cookTime:
        cookTime = cookTime.lower()[2:]

    prepTime = ldjson.get("prepTime")
    if prepTime:
        prepTime = prepTime.lower()[2:]

    totalTime = ldjson.get("totalTime")
    if totalTime:
        totalTime = totalTime.lower()[2:]

    tags = []
    if "recipeCuisine" in ldjson:
        tags.append(ldjson["recipeCuisine"])

    if "cookingMethod" in ldjson:
        tags.append(ldjson["cookingMethod"])

    if "recipeCategory" in ldjson:
        tags.append(ldjson["recipeCategory"])

    image = ldjson.get("image")
    if isinstance(image, list):
        image = ldjson["image"][-1]

    khansified_recipe = {
        "url": url,
        "id": random.randint(10, 100),
        "name": ldjson["name"],
        "author": {
            "name": ldjson.get("author", {}).get("name"),
            "url": ldjson.get("author", {}).get("url"),
        },
        "cookTime": cookTime,
        "prepTime": prepTime,
        "totalTime": totalTime,
        "description": html.unescape(ldjson.get("description", "")),
        "tags": tags,
        "image": image,
        "ingredients": [
            html.unescape(ing) for ing in ldjson.get("recipeIngredient", [])
        ],
        "instructions": [
            {
                "step": i,
                "name": html.unescape(ins.get("name", "")),
                "text": html.unescape(ins.get("text", "")),
                "url": ins.get("url"),
            }
            for (i, ins) in enumerate(ldjson.get("recipeInstructions", []))
        ],
    }

    return khansified_recipe


def get_recipe_ldjson_from_list(
    elements: list[Union[str, dict, list]], raise_exc: bool = True
):
    result = None

    for element in elements:
        if isinstance(element, str):
            ldjson = json.loads(element)
        else:
            ldjson = element

        if is_recipe_type(ldjson):
            result = ldjson
            break

        elif "@type" not in ldjson and "@graph" in ldjson:
            graph = ldjson["@graph"]
            if not isinstance(graph, list):
                graph = [graph]

            result = get_recipe_ldjson_from_list(graph, raise_exc=False)
            if result is not None:
                break

    else:
        if raise_exc:
            raise NoLDJSONException("No ld+json with recipe type found!")

    return result


def is_recipe_type(ldjson: dict[str, Any]) -> bool:
    ldjson_type = ldjson.get("@type", "")

    if isinstance(ldjson_type, str):
        return ldjson_type.strip().lower() == "recipe"
    elif isinstance(ldjson_type, list):
        return "recipe" in map(lambda a: str(a).strip().lower(), ldjson_type)
    else:
        raise KhansamaException(f"@type is of unexpected type {type(ldjson_type)}")

    return False


# as per recommendation from @freylis, compile once only
CLEANR = re.compile("<.*?>")


def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, "", raw_html)
    return cleantext
