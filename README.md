# Робот пылесос 

### О приложении
Необходимо написать консольное интерактивное приложение, 
принимающее простой набор команд для управления роботом (точкой на поле)
в рамках некоторого поля произвольного размера

### Установка
Для установки необходимых пакетов выполните команду в нужной директории

pip install -r requirements.txt

Для Windows также необходима библиотека curses:

python -m pip install windows-curses
### Запуск

Для запуска используйте следующую команду:

python3 main_robot.py -wd 60 -lg 80 -n 100

или

python3 main_robot.py --width 60 --length 80 --num_hurdles 100

При запуске без аргументов будут использованны значения по умолчанию:
--width 100 --length 100 --num_hurdles 100



где width - ширина карты, length - длинна, num_hurdles - количество препятсвий.
Все параметры должны быть целочисленными.

### Управление

Для управления роботом используйте коммандные клавишы: UP/ DOWN/ LEFT/ RIGHT.
Для поворота робота по часовой стрелки нажмите F2, против часовой F1.
Для выхода из приложения нажмите любую другую клавишу.

### Структура проекта 
Проект содержит в себе четыре файла:

* main_robot.py - запуск приложения, отрисовка окон, карты и объектов
* body.py - содержит класс для создания объектов, которые можно нанести на карту
* map_constructor.py - создает карту с препятствиями 
* robot.py - содержит класс, определяющий поведение робота 