# Классификация комментариев с использованием BERT

Интернет-магазин «Викишоп» запускает новый сервис, позволяющий пользователям редактировать и дополнять описания товаров, подобно вики-сообществам. Клиенты могут предлагать свои правки и комментировать изменения других. Магазин нуждается в инструменте для автоматического поиска токсичных комментариев и их отправки на модерацию.

**Цель проекта:**
Необходимо обучить модель, которая будет классифицировать комментарии как позитивные или негативные. Метрика качества *F1* должна быть не меньше 0.75.

**Описание данных:**
Данные находятся в файле `toxic_comments.csv`.

- **text** — текст комментария.
- **toxic** — целевой признак (токсичный комментарий: 1 — да, 0 — нет).

## Используемые библиотеки

[![pandas](https://img.shields.io/badge/pandas-1.3.3-blue)](https://pandas.pydata.org/)
[![numpy](https://img.shields.io/badge/numpy-1.21.2-orange)](https://numpy.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24.2-green)](https://scikit-learn.org/)
[![transformers](https://img.shields.io/badge/transformers-4.24.0-blue)](https://huggingface.co/transformers/)
[![torch](https://img.shields.io/badge/torch-1.12.1-orange)](https://pytorch.org/)
[![tqdm](https://img.shields.io/badge/tqdm-4.64.1-green)](https://tqdm.github.io/)
[![nltk](https://img.shields.io/badge/nltk-3.6.3-red)](https://www.nltk.org/)
