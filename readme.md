# Name
Nutrecipes Bot

## Description
This Bot has been created to develop programming skills in Python within the Skillbox diploma project.<br>The main functionality of this Bot 
embedded in its name - Nutrecipes Bot which contains two words - *Nutrients* and *Recipes*. So the Bot will help you find the recipe of a dish 
which contains definite nutrients range of nutrients.<br>This Bot will help you eat healthy and various. It is free and convenient because it 
contains a lot of 
tips and hints by suggesting you buttons that will think over the next action for you.

### How to use
After the Bot greets you? you will be asked to choose one of the following commands: 
- low;
- high;

For the **low** command https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByNutrients endpoint is used.<br> 
**Low** command means that you should choose one of the offered nutrients(protein, carbs, calcium, phosphorus) and then enter a minimum quantity of 
the 
chosen nutrient in grams. After that the Bot will suggest you the list of maximum 10 dishes which correspond this value. Then you should type a 
sequence 
number of the dish you want to learn more about. Finally, the Bot will send you a short description of the dish and the link with dish's recipe. 
For the final step the Bot uses https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{}/information endpoint where "{}" contains id 
of the recipe.

For the **high** command the same endpoint is used.<br> 
**High** command means that you should choose one of the offered nutrients(suger, fat, cholesterol, carbs) and then enter a maximum quantity of the 
chosen nutrient in grams. After that the Bot will suggest you the list of maximum 10 dishes which correspond this value. Then you should type a 
sequence 
number of the dish you want to learn more about. Finally, the Bot will send you a short description of the dish and the link with dish's recipe. 
For the dish's summary the same endpoint as in the low command is used.

### custom commands

**/low** - minimum quantity of the chosen nutrient in the dish:
You should send one chosen parameter: minProtein, minCarbs, minCalcium, minPhosphorus).

*request:*<br>
CURL GET https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByNutrients

*response:*<br>
```
[
    {
        "id": 112134,
        "title": "Baked Cauliflower Cheese Soup",
        "image": "https://img.spoonacular.com/recipes/112134-312x231.jpg",
        "imageType": "jpg",
        "calories": 515,
        "protein": "24g",
        "fat": "40g",
        "carbs": "14g"
    }, ...
]
```

For getting dish's summary and recipe link you should use the following *request* where "112134" is an id of the dish:

*You don't have to send params.*

CURL GET https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/112134/information

*response:*<br>
```
{
    "vegetarian": false,
    "vegan": false,
    "glutenFree": false,
    "dairyFree": false,
    "veryHealthy": false,
    "cheap": false,
    "veryPopular": false,
    "sustainable": false,
    "lowFodmap": false,
    "weightWatcherSmartPoints": 19,
    "gaps": "no",
    "preparationMinutes": 30,
    "cookingMinutes": 30,
    "aggregateLikes": 0,
    "healthScore": 12,
    "creditsText": "Food.com",
    "sourceName": "Food.com",
    "pricePerServing": 325.51,
    "extendedIngredients": [
        {
            "id": 2004,
            "aisle": "Produce",
            "image": "bay-leaves.jpg",
            "consistency": "SOLID",
            "name": "bay leaf",
            ...
```

**/high** - maximum quantity of the chosen nutrient in the dish.

It uses the same endpoint but for getting a list with dishes you should pass one of the other parameters:
- maxSugar;
- maxFat;
- maxCholesterol;
- maxCarbs.


#### default command:
**/start** - to start Bot.
It sends greetings, asks to greet and then offers to choose one of the custom commands.

**/help** - to show the list of default commands.

**/echo** - to send echo reply when there is no definite state.

## Installation

To run this project on your PC you should clone the following repository from https://gitlab.skillbox.ru/mariia_mikitchuk/python_basic_diploma/-/tree/master.

To do this with SHH key use the following command in the terminal:
```commandline
git clone git@gitlab.skillbox.ru:mariia_mikitchuk/python_basic_diploma.git
```

To do this with HTTPS use the following command in the terminal:
```commandline
git clone https://gitlab.skillbox.ru/mariia_mikitchuk/python_basic_diploma.git
```

Then create personal virtual environment by entring the following command in the terminal:
- for windows:
```commandline
python -m venv name_of_your_virtual_environment
name_of_your_virtual_environment\Scripts\activate
```

- for Unix or MacOS:
```commandline
python -m venv name_of_your_virtual_environment
source name_of_your_virtual_environment/bin/activate
```

Now you should install all the packages:
```commandline
pip install -r requirements.txt
```

Finally, you should find file main.py in the root of the project and run it.

To use this Bot in telegram you just need to find it in the telegram by its name - Nutrecipes Bot or by following the link [Nutrecipes Bot](t.me/NutrecipesBot)

## Development
You may join the development or to give piece of advice on improvement issues. For this purpose please contact [Mariya](mailto:6742517@gmail.com)

## Members

- Mariya Mikitchuk - developer
- Alexander Olkhovik - superviser

