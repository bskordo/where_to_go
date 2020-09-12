# Where to go — attractive places in Moscow

Site about attractive places in Moscow if you want to spend your free time by discovering Moscow.
Sample running site you can find here  [http://aspire.pythonanywhere.com/](http://aspire.pythonanywhere.com/).


## How to Use

* Download the code
* Install virtual env and activate it
* Install modules from requirements
* You can download more place from https://github.com/devmanorg/where-to-go-places
* Run a server

## Example of launch on Linux, Python 3.6:

```bash
$ python3 -m venv myvenv
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py load_place https://github.com/devmanorg/where-to-go-places/tree/master/places
$ python manage.py runserver
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

