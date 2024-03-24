from typing import Dict

import requests

def _make_response(method: str , url: str, headers: Dict, params: Dict, timeout: int = 1, success=200):

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

def _get_min_value(method: str, url: str, headers: Dict, params: Dict, min_value, nutrient, timeout: int = 5, func=_make_response):
    if nutrient == 'protein':
        params["minProtein"] = min_value
    elif nutrient == 'carbs':
        params["minCarbs"] = min_value
    elif nutrient == 'calcium':
        params["minCalcium"] = min_value
    elif nutrient == 'phosphorus':
        params["minPhosphorus"] = min_value
    print(params)

    respons = func(method=method, url=url, headers=headers, params=params, timeout=timeout)
    return respons

class SiteApiInterface():

    @staticmethod
    def get_min_protein():
        return _get_min_value

if __name__ == '__main__':
    _make_response()
    _get_min_value()

    SiteApiInterface()