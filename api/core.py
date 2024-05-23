from api.utils.nutrient_api import SiteApiInterface
from config_data.config import RAPID_API_HOST, RAPID_API_KEY

headers = {"X-RapidAPI-Key": RAPID_API_KEY, "X-RapidAPI-Host": RAPID_API_HOST}

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes" \
      "/findByNutrients"
url_dish = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{" \
           "}/information"

params_dish = {"": ""}

params = {"limitLicense": "false", "minProtein": "0", "minVitaminC": "0",
          "minSelenium": "0", "maxFluoride": "50", "maxVitaminB5": "50",
          "maxVitaminB3": "50", "maxIodine": "50", "minCarbs": "0",
          "maxCalories": "250", "minAlcohol": "0", "maxCopper": "50",
          "maxCholine": "50", "maxVitaminB6": "50", "minIron": "0",
          "maxManganese": "50", "minSodium": "0", "minSugar": "0", "maxFat": "20",
          "minCholine": "0", "maxVitaminC": "50", "maxVitaminB2": "50",
          "minVitaminB12": "0", "maxFolicAcid": "50", "minZinc": "0", "offset": "0",
          "maxProtein": "100", "minCalories": "0", "minCaffeine": "0",
          "minVitaminD": "0", "maxVitaminE": "50", "minVitaminB2": "0", "minFiber": "0",
          "minFolate": "0", "minManganese": "0", "maxPotassium": "50", "maxSugar": "50",
          "maxCaffeine": "50", "maxCholesterol": "50", "maxSaturatedFat": "50",
          "minVitaminB3": "0", "maxFiber": "50", "maxPhosphorus": "50",
          "minPotassium": "0", "maxSelenium": "50", "maxCarbs": "100",
          "minCalcium": "0", "minCholesterol": "0", "minFluoride": "0",
          "maxVitaminD": "50", "maxVitaminB12": "50", "minIodine": "0", "maxZinc": "50",
          "minSaturatedFat": "0", "minVitaminB1": "0", "maxFolate": "50",
          "minFolicAcid": "0", "maxMagnesium": "50", "minVitaminK": "0",
          "maxSodium": "50", "maxAlcohol": "50", "maxCalcium": "50",
          "maxVitaminA": "50", "maxVitaminK": "50", "minVitaminB5": "0",
          "maxIron": "50", "minCopper": "0", "maxVitaminB1": "50", "number": "10",
          "minVitaminA": "0", "minPhosphorus": "0", "minVitaminB6": "0", "minFat": "5",
          "minVitaminE": "0"}

site_api = SiteApiInterface()

if __name__ == "__main__":
    site_api()
