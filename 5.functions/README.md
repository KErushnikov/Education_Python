# Домашнее задание к лекции 5.«Функции — использование встроенных и создание собственных»

# Решение

https://github.com/KErushnikov/Education_Python/blob/main/5.functions/homework.py

Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:

```
      documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
```    
Перечень полок, на которых находятся документы хранится в следующем виде:

```
      directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }
```

## Задача №1
Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

* `p` – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
* `s` – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;  
*Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ*.
* `l`– list – команда, которая выведет список всех документов в формате `passport "2207 876234" "Василий Гупкин"`;
* `a` – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. *Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку*.

**Внимание**: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

## Задача №2
* `d` – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. *Предусмотрите сценарий, когда пользователь вводит несуществующий документ*;
* `m` – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. *Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку*;
* `as` – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. *Предусмотрите случай, когда пользователь добавляет полку, которая уже существует*.;

## Задача №3
Почитать про lambda-функции. И что такое `*args` и `**kwargs`.

## Задача №4
Для подготовки к следующей лекции прочитайте про [классы](https://pythonworld.ru/osnovy/obektno-orientirovannoe-programmirovanie-obshhee-predstavlenie.html).

---
Инструкция по выполнению домашнего задания:

1. Зарегистрируйтесь на сайте [Repl.IT](https://repl.it/).
2. Перейдите в раздел **my repls**.
3. Нажмите кнопку **Start coding now!**, если приступаете впервые, или **New Repl**, если у вас уже есть работы.
4. В списке языков выберите Python.
5. Код пишите в левой части окна.
6. Посмотреть результат выполнения файла можно, нажав на кнопку **Run**. Результат появится в правой части окна.


*Никаких файлов прикреплять не нужно.*