from typing import Dict

import requests

def _make_response(method: str, url: str, headers: Dict, params: Dict, timeout: int, success=200):

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

def _get_min_protein(method: str, url: str, headers: Dict, params: Dict, min_protein, timeout: int = 5, func=_make_response):
    params["minProtein"] = min_protein

    respons = func(method, url, headers=headers, params=params, timeout=timeout)
    return respons

class SiteApiInterface():

    @staticmethod
    def get_min_protein():
        return _get_min_protein

if __name__ == '__main__':
    _make_response()
    _get_min_protein()

    SiteApiInterface()