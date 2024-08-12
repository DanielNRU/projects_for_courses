# Прогнозирование спроса на такси 

Компания «Чётенькое такси» собрала исторические данные о заказах такси в аэропортах. Цель проекта — построить модель, которая сможет прогнозировать количество заказов такси на следующий час, чтобы привлечь больше водителей в период пиковой нагрузки.

Для достижения этой цели необходимо:
1. Загрузить данные и выполнить их ресемплирование по одному часу.
2. Проанализировать данные.
3. Обучить различные модели с разными гиперпараметрами. Создать тестовую выборку размером 10% от исходных данных.
4. Проверить точность моделей на тестовой выборке и сделать выводы.

**Метрика:**
Значение метрики *RMSE* (Root Mean Squared Error) на тестовой выборке должно быть не больше 48.

**Данные:**
Файл с данными находится по пути `taxi.csv`. Основной столбец для анализа — `num_orders` (от англ. *number of orders*, «число заказов»).

## Используемые библиотеки

[![pandas](https://img.shields.io/badge/pandas-1.3.3-blue)](https://pandas.pydata.org/)
[![numpy](https://img.shields.io/badge/numpy-1.21.2-orange)](https://numpy.org/)
[![matplotlib](https://img.shields.io/badge/matplotlib-3.4.3-blue)](https://matplotlib.org/)
[![seaborn](https://img.shields.io/badge/seaborn-0.11.2-orange)](https://seaborn.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24.2-green)](https://scikit-learn.org/)
[![statsmodels](https://img.shields.io/badge/statsmodels-0.12.2-red)](https://www.statsmodels.org/)
