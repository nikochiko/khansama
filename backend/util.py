import json
from bs4 import BeautifulSoup
from typing import Any, Union

import requests


class KhansamaException(Exception):
    pass


class NoLDJSONException(KhansamaException):
    pass


def get_recipe_ldjson_from_url(url: str) -> dict:
    r = requests.get(url)
    r.raise_for_status()

    soup = BeautifulSoup(r.text)
    elements = soup.find_all("script", type="application/ld+json")

    return get_recipe_ldjson_from_list([el.string for el in elements])


def get_recipe_ldjson_from_list(
        elements: list[Union[str, dict, list]], raise_exc: bool = True):
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

            result = get_recipe_ldjson_from_list(
                    graph, raise_exc=False)
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
        raise KhansamaException(
            f"@type is of unexpected type {type(ldjson_type)}")

    return False
