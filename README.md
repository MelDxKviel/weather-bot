# weather-bot

## Описание 

Телеграм бот для получения текущей погоды по названию города


## Как запустить

Перед запуском необходимо задать переменные окружения в файле `.env` 

Имена переменных представлены в файле `.env.example`

### Docker

Создание образа
```bash
docker build --tag 'weather-bot' .
```

Запуск контейнера
```bash
docker run weather-bot
```

### Python

Создание виртуального окружения

```bash
python -m venv venv
```

Активация виртуального окружения

**Linux/MacOS**

```bash
source venv/bin/activate
```

**Windows**

```powershell
.\venv\Scripts\activate
```

Устанвока зависимостей

```bash
pip install -r requirements.txt
```

Запуск приложения

```bash
python main.py
```