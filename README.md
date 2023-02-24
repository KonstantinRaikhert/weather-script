# weather-script

![versions](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue)
Этот скрипт позволяет с консоли Unix систем узнать погоду в Вашем городе

### Подготовка к использованию:

* Скопируйте репозиторий к себе:

`git clone https://github.com/KonstantinRaikhert/weather-script.git`

* В каталоге найдите исполняемый скрипт `weather` и задайте ему соответсвующие права:

  `chmod +x weather`

* Для удобства создайте точку входа в приложение:

  `sudo ln -s $(pwd)/weather /usr/local/bin/`

* Получите API ключ с бесплатного сайта [OpenWeather](https://openweathermap.org/) , создайте файл в корневом каталоге `.env` и задайте переменную:

  `OPEN_WEATHER_API_KEY=<Ваш API ключ>`

  Так же необходимо добавить в environments:
  
  ```bash
  set -a
  source .env
  set +a
  ```

### Использование:

Запустите `weather` в консоли и получите примерно такой ответ:

```bash
Москва, температура -4°C, Снег
Восход: 07:34
Закат: 17:51
```
