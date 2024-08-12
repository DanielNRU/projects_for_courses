# Оценка стоимости автомобилей

## Описание проекта

Сервис по продаже автомобилей с пробегом «Не бит, не крашен» разрабатывает приложение для привлечения новых клиентов. В нем пользователи смогут быстро узнать рыночную стоимость своего автомобиля. Для этого необходимо построить модель, которая будет оценивать стоимость автомобилей на основе исторических данных о технических характеристиках, комплектациях и ценах.

При разработке модели важны следующие аспекты:

- **Качество предсказания**
- **Скорость предсказания**
- **Время обучения**

## Описание данных

Данные для анализа находятся в файле `/datasets/autos.csv`.

Признаки:

- **DateCrawled** — дата скачивания анкеты из базы.
- **VehicleType** — тип автомобильного кузова.
- **RegistrationYear** — год регистрации автомобиля.
- **Gearbox** — тип коробки передач.
- **Power** — мощность (л. с.).
- **Model** — модель автомобиля.
- **Kilometer** — пробег (км).
- **RegistrationMonth** — месяц регистрации автомобиля.
- **FuelType** — тип топлива.
- **Brand** — марка автомобиля.
- **Repaired** — была ли машина в ремонте или нет.
- **DateCreated** — дата создания анкеты.
- **NumberOfPictures** — количество фотографий автомобиля.
- **PostalCode** — почтовый индекс владельца анкеты (пользователя).
- **LastSeen** — дата последней активности пользователя.

## Используемые библиотеки

[![pandas](https://img.shields.io/badge/pandas-1.3.3-blue)](https://pandas.pydata.org/)
[![re](https://img.shields.io/badge/re-2.2.1-blue)](https://docs.python.org/3/library/re.html)
[![os](https://img.shields.io/badge/os-2.2.1-blue)](https://docs.python.org/3/library/os.html)
[![numpy](https://img.shields.io/badge/numpy-1.21.2-orange)](https://numpy.org/)
[![matplotlib](https://img.shields.io/badge/matplotlib-3.4.3-blue)](https://matplotlib.org/)
[![seaborn](https://img.shields.io/badge/seaborn-0.11.2-orange)](https://seaborn.pydata.org/)
[![scipy](https://img.shields.io/badge/scipy-1.7.1-green)](https://scipy.org/)
[![time](https://img.shields.io/badge/time-3.10.0-blue)](https://docs.python.org/3/library/time.html)
[![phik](https://img.shields.io/badge/phik-0.12.0-orange)](https://phik.readthedocs.io/)
[![lightgbm](https://img.shields.io/badge/lightgbm-3.3.2-blue)](https://lightgbm.readthedocs.io/)
[![catboost](https://img.shields.io/badge/catboost-1.1.1-orange)](https://catboost.ai/)
