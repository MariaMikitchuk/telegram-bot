### Описание проекта
Описываем цель создания telegram-бота, какую проблему он решает для вас или пользователей.

### Как пользоваться
Описываем какие команды и какая логика заложена в вашем проекте.
В ТЗ говориться что должны быть базовые команды, их можно изменить по своему усмотрению
Главное показать какие endpoint API используются для каждой команды в вашем боте,
с какими параметрами и результатом ответа

#### custom command:

**/low** - минимальное, дописать описание

Запрос без параметров:

CURL GET https://exampleAPI.ru/v1/api/low/price

Пример ответ запроса:

```console
{"data":
    [
        {"depart_date":"2024-04-04",
        "origin":"MOW",
        "destination":"HKT",
        "gate":"Biletix",
        "return_date":"2024-04-08",
        "found_at":"2024-03-22T18:43:12Z",
        "trip_class":0,
        "value":67810,
        "number_of_changes":2,
        "duration":5585,
        "distance":7479,
        "show_to_affiliates":true,
        "actual":true},
        ...
        {"depart_date":"2024-04-03",
        "origin":"MOW",
        "destination":"HKT",
        "gate":"Kupi.com",
        "return_date":"2024-04-07",
        "found_at":"2024-03-24T11:16:30Z",
        "trip_class":0,"value":73340,
        "number_of_changes":3,"duration":2840,
        "distance":7479,
        "show_to_affiliates":true,
        "actual":true}
    ]
}
```

**/high** - максимально, дописать описание

Запрос без параметров:

CURL GET https://exampleAPI.ru/v1/api/high/price

Ответ запроса:
Аналогично показываем часть ответа для примера

**/custom** - произвольное\выборочное, дописать описание

Запрос с параметрами:
CURL POST https://exampleAPI.ru/v1/api/custom?min=1&max=10

Ответ запроса:
Аналогично показываем часть ответа для примера

Для запроса с параметрами используем всегда POST запрос к API



#### default command:

**/start** - старт, дописать описание

**/help** - помощь, дописать описание

### Как запустить
Описываем как запустить ваш проект на стороннем ПК, нужно описать процесс установки библиотек и сам запуск.
Можно показать скринами\картинками или текстовыми командами для консоли. 