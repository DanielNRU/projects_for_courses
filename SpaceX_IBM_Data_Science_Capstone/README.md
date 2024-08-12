# SpaceX IBM Data Science Capstone

# Прогноз посадки первой ступени ракеты SpaceX Falcon 9

## Описание проекта

В этом проекте мы будем предсказывать, успешно ли сядет первая ступень ракеты Falcon 9. SpaceX рекламирует запуски ракеты Falcon 9 на своем веб-сайте по цене 62 миллиона долларов, тогда как другие поставщики требуют от 165 миллионов долларов за каждый запуск. Большая часть экономии заключается в том, что SpaceX может повторно использовать первую ступень. Поэтому, если мы сможем предсказать успешность посадки первой ступени, мы сможем определить стоимость запуска. Эта информация может быть полезна компаниям, которые хотят конкурировать с SpaceX за запуск ракеты.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_1_L2/images/Falcon9_rocket_family.svg)

Пример успешного Falcon 9 приземления первой ступени ракеты

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/landing_1.gif)

Здесь показаны несколько примеров неудачных посадок:

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/crash.gif)

## Используемые библиотеки

[![requests](https://img.shields.io/badge/requests-2.26.0-blue)](https://docs.python-requests.org/)
[![pandas](https://img.shields.io/badge/pandas-1.3.3-blue)](https://pandas.pydata.org/)
[![numpy](https://img.shields.io/badge/numpy-1.21.2-orange)](https://numpy.org/)
[![datetime](https://img.shields.io/badge/datetime-4.3.0-blue)](https://docs.python.org/3/library/datetime.html)
[![sys](https://img.shields.io/badge/sys-3.10.0-blue)](https://docs.python.org/3/library/sys.html)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.9.3-orange)](https://www.crummy.com/software/BeautifulSoup/)
[![re](https://img.shields.io/badge/re-2.2.1-blue)](https://docs.python.org/3/library/re.html)
[![unicodedata](https://img.shields.io/badge/unicodedata-2.2.1-blue)](https://docs.python.org/3/library/unicodedata.html)
[![matplotlib](https://img.shields.io/badge/matplotlib-3.4.3-blue)](https://matplotlib.org/)
[![seaborn](https://img.shields.io/badge/seaborn-0.11.2-orange)](https://seaborn.pydata.org/)
[![sql](https://img.shields.io/badge/sql-3.10.0-blue)](https://docs.python.org/3/library/sql.html)
[![csv](https://img.shields.io/badge/csv-1.0.5-blue)](https://docs.python.org/3/library/csv.html)
[![sqlite3](https://img.shields.io/badge/sqlite3-3.35.5-orange)](https://www.sqlite.org/)
[![folium](https://img.shields.io/badge/folium-0.12.1-blue)](https://python-visualization.github.io/folium/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24.2-orange)](https://scikit-learn.org/stable/)
[![warnings](https://img.shields.io/badge/warnings-3.10.0-blue)](https://docs.python.org/3/library/warnings.html)
