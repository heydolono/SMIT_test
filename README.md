# SMIT тестовое задание

### Это проект REST API сервиса, который рассчитывает стоимость страхования от типа груза и объявленной стоимости

## Установка и запуск

### 1. Клонирование репозитория

```
git clone https://github.com/heydolono/SMIT_test.git
cd SMIT_test
```

### 2. Установка зависимостей

```
pip install -r requirements.txt
```

### 3. Установка переменных окружения
Переименуйте файл example.env в .env

### 4. Запуск Docker контейнеров

```
docker-compose up --build
```

## API

### POST rate/load-rate
# Загрузка JSON
Загрузите database.json

### GET rate/calculate-value

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
