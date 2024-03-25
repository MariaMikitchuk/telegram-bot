from typing import Dict

import requests

def _make_response(method: str , url: str, headers: Dict, params: Dict, timeout: int = 10, success=200):

    response = requests.request(
        method,
        url,
        headers=headers,
        params=params,
        timeout=timeout
    )

    status_code = response.status_code

    if status_code == success:
        return response

    return status_code

def _get_min_value(method: str, url: str, headers: Dict, params: Dict, min_value: str, nutrient: str, timeout: int = 10, func=_make_response):
    if nutrient == 'protein':
        params["minProtein"] = min_value
    elif nutrient == 'carbs':
        params["minCarbs"] = min_value
    elif nutrient == 'calcium':
        params["minCalcium"] = min_value
    elif nutrient == 'phosphorus':
        params["minPhosphorus"] = min_value
    print(params)

    response = func(method=method, url=url, headers=headers, params=params, timeout=timeout).json()
    max_dishes = min(10, len(response))
    titles = [f"{i + 1}. {dish['title']}" for i, dish in enumerate(response[:max_dishes])]
    id_list = list(map(lambda x: x['id'], response[:max_dishes]))
    id_dict = {index + 1: dish_id for index, dish_id in enumerate(id_list)}
    return response, titles, id_dict, max_dishes


def _get_min_summary(method: str, url: str, headers: Dict, timeout: int = 10, func=_make_response):
    response = func(method=method, url=url, headers=headers, params=params, timeout=timeout).json()
    summary = response["summary"]
    link = response["sourceUrl"]
    return summary, link


class SiteApiInterface():

    @staticmethod
    def get_min_nutr():
        return _get_min_value

    @staticmethod
    def get_min_dish():
        return _get_min_summary

if __name__ == '__main__':
    _make_response()
    _get_min_value()
    _get_min_summary

    SiteApiInterface()