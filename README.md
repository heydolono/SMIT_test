# SMIT тестовое задание

### Это проект REST API сервиса, который рассчитывает стоимость страхования от типа груза и объявленной стоимости

## Установка и запуск

### 1. Клонирование репозитория

```
git clone https://github.com/heydolono/SMIT_test.git
cd SMIT_test/app
```

### 2. Установка зависимостей

```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

### 3. Установка переменных окружения
Переименуйте файл example.env в .env

### 4. Запуск Docker контейнеров

```
docker-compose up
```

## API
Документация доступна по 
```
http://127.0.0.1:8000/docs
```
### POST rate/load-rate
### Загрузка JSON
Загрузите database.json

### POST rate/calculate-value

Пример запроса:
```
{
  "date": "2020-06-01",
  "cargo_type": "Glass",
  "declared_value": 1000
}
```
Пример ответа:
```
{
  "calculate_value": 40
}
```
