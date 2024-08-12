# Обнаружение трещин на фотографиях бетона

## Описание проекта

Обнаружение трещин имеет жизненно важное значение для мониторинга и проверки состояния конструкций. В этой работе мы создадим классификатор с использованием предварительно обученной модели, который будет обнаруживать трещины на изображениях бетона. Для постановки задачи будем обозначать изображения бетона с трещинами как положительный класс, а изображения бетона без трещин — как отрицательный класс.

## Цель проекта

Использовать предварительно обученные модели ResNet50 и VGG16 для построения классификаторов изображений вместо создания модели с нуля.

## Используемые библиотеки

[![os](https://img.shields.io/badge/os-2.2.1-blue)](https://docs.python.org/3/library/os.html)
[![tensorflow](https://img.shields.io/badge/tensorflow-2.6.0-orange)](https://www.tensorflow.org/)
[![matplotlib](https://img.shields.io/badge/matplotlib-3.4.3-blue)](https://matplotlib.org/)
[![numpy](https://img.shields.io/badge/numpy-1.21.2-orange)](https://numpy.org/)
[![PIL](https://img.shields.io/badge/PIL-8.3.2-blue)](https://pillow.readthedocs.io/)
[![ResNet50](https://img.shields.io/badge/ResNet50-pretrained-blue)](https://keras.io/api/applications/resnet/)
[![VGG16](https://img.shields.io/badge/VGG16-pretrained-blue)](https://keras.io/api/applications/vgg/)
[![skillsnetwork](https://img.shields.io/badge/skillsnetwork-0.1.0-orange)](https://skills.network/)