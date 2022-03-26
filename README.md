# docker_compose_test
Разворачивание проекта обработки статистической информации по API в Docker-compose

Реализован API, принимающий данные пользователя и возвращающий rорреляцию по Пирсону и ковариацию

Скачать проект с репозитория:
git@github.com:AndrewFekl/docker_compose_test.git

Запуск пректа:
docker-compose up

    API
    POST http://127.0.0.1:8000/api/calculate
    Принимает входные данные в JSON-формате, вычисляет и сохраняет метрики в базу данных

    
        {
            "user_id": int,
            "data": {
                "x_data_type": str,
                "y_data_type": str,
                "x": [
                    {
                        "date": YYYY-MM-DD,
                        "value": float,
                    },
                    ...
                ],
                "y": [
                    {
                        "date": YYYY-MM-DD,
                        "value": float,
                    },
                    ...
                ]
            }
        }
    GET http://127.0.0.1:8000/api/correlation?x_data_type=str&y_data_type=str&user_id=int

Отдает посчитанную метрику для конкретного пользователя и конкретных типов данных
Если для данной комбинации рассчитанных данных нет - возвращает 404
    Формат ответа в случае HTTP 200:

   {
       "user_id": int,
       "x_data_type": str,
       "y_data_type": str,
       "correlation": {
           "value": float,
           "p_value": float,
       }
   }


POST http://127.0.0.1:8000/users/token

Получение токена для аторизации.
В теле запроса необходимо передать логин и пароль зарегистрированного пользователя:

    {
    "username": "admin",
    "password": "coder74"
}

    
http://127.0.0.1:8000/users/register

Регистрация новых пользователей
