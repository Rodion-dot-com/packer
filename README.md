# Проект Хакатон от Yandex.Market & Yandex.Practicum

## Стек технологий:
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
## Наша команда:

### Project-manager: 
* Каримов Артур Ильсурович.
 
### [DS](https://github.com/ivanoff-sd/bestpack_repo): 
* Степанова Екатерина Николаевна, 
* Ушаев Евгений Викторович, 
* Иванов Сергей Дмитриевич.

### [Frontend-разработчики](https://github.com/nidoveralis/product-packing-react):
* Дьякова Алина Эдуардовна, 
* Мантусова Мария Андреевна.



### Backend-разработчики: 
[Эмулятор внешних данных для сервиса упаковщика Яндекс Маркета](https://github.com/Proforg77/yama_serv_emul)
[Backend проекта](https://github.com/Rodion-dot-com/packer)
* Шляпцев Пётр Александрович, 
* Прошляков Родион Александрович.

### Дизайн:  
* Громова Кристина Андреевна, 
* Лопаткина Юлия Александровна.

## Наша цель: 

* Необходимо придумать способ подсказывать пользователю информацию о выборе упаковочного материала, а также разработать интерфейс для упаковщика.

## Ссылка на GH-pages

* [Кликай сюда](https://nidoveralis.github.io/product-packing-react/)


## Инструкция по локальному запуску проекта:
* Создайте файл .env с переменными окружения в директории infra:
Шаблон наполнения env-файла
```
SECRET_KEY=some-kind-of-key # установите ваш секретный ключ 
DB_ENGINE=django.db.backends.sqlite3 # указываем, что работаем с sqlite3
DB_NAME=db.sqlite3 # имя базы данных
```
* Перейдите в директорию с файлом docker-compose.yaml
```
cd infra/
```
* Соберите контейнеры и запустите их
```
docker-compose up
```
- Основной функционал готов, проверить работу можно [тут](http://localhost/) 
- Чтобы остановить и удалить контейнеры выполните команду
```
docker-compose down -v
```