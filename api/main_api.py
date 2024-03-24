from api.core import url, headers, params
from api.utils import low_nutrient_api

from database.core import crud

db_write = crud.create()
db_read = crud.retrieve()

dish_low_protein = low_nutrient_api._get_min_value

# response = dish_low_protein("GET", url, headers, params, 1)
# response = response.json()
#
#
# titles = list(map(lambda x: x['title'], response))
# print(titles)
