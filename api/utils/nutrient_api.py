from typing import Dict, Optional, Tuple, List
from bs4 import BeautifulSoup

import requests


def remove_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()


def _make_response(method: str, url: str, headers: Dict, params: Dict,
                   timeout: int = 10, success=200):
    response = requests.request(method, url, headers=headers, params=params,
                                timeout=timeout)

    status_code = response.status_code

    if status_code == success:
        return response

    return status_code


# def _get_min_value(method: str, url: str, headers: Dict, params: Dict, min_value: str,
#                    nutrient: str, timeout: int = 10, func=_make_response):
#     updated_params = {}
#     if nutrient == 'protein':
#         updated_params["minProtein"] = min_value
#     elif nutrient == 'carbs':
#         updated_params["minCarbs"] = min_value
#     elif nutrient == 'calcium':
#         updated_params["minCalcium"] = min_value
#     elif nutrient == 'phosphorus':
#         updated_params["minPhosphorus"] = min_value
#
#     response = func(method=method, url=url, headers=headers, params=updated_params,
#                     timeout=timeout).json()
#     max_dishes = min(10, len(response))
#     titles = [f"{i + 1}. {dish['title']}" for i, dish in
#               enumerate(response[:max_dishes])]
#     id_list = list(map(lambda x: x['id'], response[:max_dishes]))
#     id_dict = {index + 1: dish_id for index, dish_id in enumerate(id_list)}
#     return response, titles, id_dict, max_dishes
#
#
# def _get_max_value(method: str, url: str, headers: Dict, params: Dict, min_value: str,
#                    nutrient: str, timeout: int = 10, func=_make_response):
#     updated_params = {}
#     if nutrient == 'sugar':
#         updated_params["maxSugar"] = min_value
#     elif nutrient == 'fat':
#         updated_params["maxFat"] = min_value
#     elif nutrient == 'cholesterol':
#         updated_params["maxCholesterol"] = min_value
#     elif nutrient == 'carbs':
#         updated_params["maxCarbs"] = min_value
#
#     response = func(method=method, url=url, headers=headers, params=updated_params,
#                     timeout=timeout).json()
#     max_dishes = min(10, len(response))
#     titles = [f"{i + 1}. {dish['title']}" for i, dish in
#               enumerate(response[:max_dishes])]
#     id_list = list(map(lambda x: x['id'], response[:max_dishes]))
#     id_dict = {index + 1: dish_id for index, dish_id in enumerate(id_list)}
#     return response, titles, id_dict, max_dishes


def _make_response_and_process(method: str, url: str, headers: Dict, params: Dict,
                               nutrient_param: Optional[str] = None,
                               value: Optional[str] = None, timeout: int = 10,
                               func=_make_response) -> Tuple[List, List, Dict, int]:
    updated_params = {}
    if nutrient_param and value:
        updated_params[nutrient_param] = value

    response = func(method=method, url=url, headers=headers, params=updated_params,
                    timeout=timeout).json()
    max_dishes = min(10, len(response))
    titles = [f"{i + 1}. {dish['title']}" for i, dish in
              enumerate(response[:max_dishes])]
    id_list = list(map(lambda x: x['id'], response[:max_dishes]))
    id_dict = {index + 1: dish_id for index, dish_id in enumerate(id_list)}
    return response, titles, id_dict, max_dishes


def _get_min_value(method: str, url: str, headers: Dict, params: Dict, min_value: str,
                   nutrient: str, timeout: int = 10, func=_make_response) -> \
        Tuple[List, List, Dict, int]:
    nutrient_param = None
    if nutrient == 'protein':
        nutrient_param = "minProtein"
    elif nutrient == 'carbs':
        nutrient_param = "minCarbs"
    elif nutrient == 'calcium':
        nutrient_param = "minCalcium"
    elif nutrient == 'phosphorus':
        nutrient_param = "minPhosphorus"

    return _make_response_and_process(method, url, headers, params, nutrient_param,
                                      min_value, timeout, func)


def _get_max_value(method: str, url: str, headers: Dict, params: Dict, min_value: str,
                   nutrient: str, timeout: int = 10, func=_make_response) -> \
        Tuple[List, List, Dict, int]:
    nutrient_param = None
    if nutrient == 'sugar':
        nutrient_param = "maxSugar"
    elif nutrient == 'fat':
        nutrient_param = "maxFat"
    elif nutrient == 'cholesterol':
        nutrient_param = "maxCholesterol"
    elif nutrient == 'carbs':
        nutrient_param = "maxCarbs"

    return _make_response_and_process(method, url, headers, params, nutrient_param,
                                      min_value, timeout, func)


def _get_summary(method: str, url: str, headers: Dict, params: Dict, timeout: int = 10,
                 func=_make_response):
    response = func(method=method, url=url, headers=headers, params=params,
                    timeout=timeout).json()
    summary = response["summary"]
    cleared_summary = remove_html_tags(summary)
    link = response["sourceUrl"]
    return cleared_summary, link


class SiteApiInterface():

    @staticmethod
    def get_min_nutr():
        return _get_min_value()

    @staticmethod
    def get_max_nutr():
        return _get_max_value()

    @staticmethod
    def get_min_dish():
        return _get_summary()



if __name__ == '__main__':
    _make_response()
    _make_response_and_process()
    _get_min_value()
    _get_max_value()
    _get_summary()

    SiteApiInterface()
