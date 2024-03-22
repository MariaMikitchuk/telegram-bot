import json

from api.utils import low_nutrient_api
from core import url, headers, params
from database.core import crud

db_write = crud.create()
db_read = crud.retrieve()

dish_low_protein = low_nutrient_api._get_min_protein

response = dish_low_protein("GET", url, headers, params, 2)
response = response.json()


titles = list(map(lambda x: x['title'], response))
print(titles)
