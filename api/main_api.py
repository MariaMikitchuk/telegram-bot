from api.utils import low_nutrient_api

from database.core import crud

db_write = crud.create()
db_read = crud.retrieve()

dish_low_nutrient = low_nutrient_api._get_min_value
dish_low_summary = low_nutrient_api._get_min_summary

