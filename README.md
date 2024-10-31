# LESSON-4. Space photos

Данный проект может скачивать изображения от NASA(EPIC и APOD) и SpaceX. А ещё он может постить их в группе в Telegram.

## Установка скрипта

Прежде чем запускать код необходимо установить некоторые библиотеки. Их всех с нужными версиями можно найти в файле `requirements.txt`, а для установки используйте команду:
```
pip install -r requirements.txt
```
Чтобы ваш проект работал вам нужно создать файл `.env`, а после добавить туда ключи токена телеграма и NASA. Ваш телеграм-токен вам выдаст (BotFather)[https://t.me/BotFather]. И не забудьте предать ID вашего чата! А токен для NASA вы можите получить (здесь)[https://api.nasa.gov/]. Собственно, на этом же сайте есть вся необходимая информация для получения своего токена.
```
NASA_API_KEY = ваш токен
TELEGRAM_TOKEN = ваш токен

```

## Как скачать изображения

1. Для  скачивания изображений с SpaceX запустите код:
    ```
    python spaceX_photos.py
    ```
    Ещё для `spaceX_photos.py` есть необязательный аргумент `--ID`. Благодаря ему можно передавать ID определённых изображений с сайта SpaceX. Для этого запустите код:
    ```
    python spaceX_photos.py --ID 
    ```
    И после "--ID" запишите нужный вам ID.

2. Для  скачивания изображений с  NASA EPIC запустите код:
    ```
    python NASA_EPIC_photos.py
    ```

3. Для скачивания изображений с NASA APOD запустите код:
    ```
    python NASA_photos.py 
    ```
## Отправка сообщений в группу Telegram

**Перед тем как начинать отправку в Telegram скачайте несколько изображений**
Чтобы начать отправку изображений в группу, запустите код:
```
python telegram_bot.py
```
После того как вы запустите код, бот начнёт отправлять изображения в группу. По умолчанию он будет это делать раз в 14400 секунд, что равняется четырём часам. Этот временной промежуток можно изменить. Для этого используйте необязательный аргумент `--frequence`. Чтобы всё заработало запустите код:
```
python telegram_bot.py --frequence=x
```
Где 'x' - необходимое вам число. Важно ещё то, что писать время нужно в секундах.

## Цель проекта 

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).