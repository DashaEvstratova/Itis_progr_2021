# Itis_progr_2021

Kazan Federal University Programming Course

Информатика и программирование 1 курс 1 семестр

Распределение баллов: 

            25 — Домашняя работа
            5 — Практика
            20 — Контрольные работы


Дедлайны домашних работ



 У домашек 2 дедлайна с прогрессивной шкалой максимальных баллов. Если студент не сдаёт задание до первого дедлайна, он получает,  максимум 50% от изначальных баллов за задание.     Если он не сдаёт до второго дедлайна, то он не получает ничего. 
 
 
Баллы выставляются за домашние задания. Каждое задание представляет собой спецификацию к программе, которую нужно реализовать. За каждое задание можно получить 1-3 баллов; в некоторых заданиях можно получить дополнительные баллы.

На выполнение каждого задания дается 3 попытки(3 коммита).

За копирование кода у других студентов выставляется оценка в 0 баллов без права на исправление и выдается индивидуальное задание.
 
  
   
  
  
  
#  Инструменты. Установка
 Git
 Sublime Text, Notepad++
  
## Windows
1. Перейдите по ссылке и скачайте установщик последней доступной версии Python 3 для Windows. https://www.python.org/downloads/

Запустите установщик. На первом экране обязательно отметьте галочкой опцию Add Python 3.6 to PATH – это сделает Python 3 доступным в командной строке. Далее следуйте инструкциям, в процессе установки не снимайте галочки у предлагаемых для установки компонентов.

2. Установить Sublime Text https://www.sublimetext.com/3 (Package Control -> Install Package -> SublimeRELP)
3. Настройка Sublime для Input

Устанавливаем плагин  SublimeRELP
Нстройки по ссылке https://www.youtube.com/watch?v=xMpr-i7YAsY

Идем Preferences – Key Bindings и  Вставляем код ниже 

{ "keys": ["ctrl+b"], "command": "repl_open", "caption": "Python - RUN current file", "id": "repl_python_run", "mnemonic": "d", "args": { "type": "subprocess", "encoding": "utf8", "cmd": ["python", "-i", "-u", "$file_basename"], "cwd": "$file_path", "syntax": "Packages/Python/Python.tmLanguage", "external_id": "python", "extend_env": {"PYTHONIOENCODING": "utf-8"} } }

Save+ Ctrl+B


# MacOS
Мы опишем 2 возможных способа установить Python 3 на MacOS.

Способ 1.
Перейдите по ссылке http://python.org/download/ и скачайте установщик последней доступной версии Python 3 для MacOS.

Запустите установщик, запустите его. Запустите Python.mpkg в открывшемся окне.

Во время установки вам нужно будет ввести административный пароль.

После установки в папке /Applications появится IDLE.

Способ 2.
С помощью утилиты brew: https://brew.sh/index_ru.html

Вам нужно установить brew, а затем набрать в терминале: #brew install python3
  После установки попробуйте запустить приложение Терминал (установлено по умолчанию) – и наберите python3 – должен запуститься интерактивный интерпретатор. Если команда python3 не запустила интерпретатор – попробуйте просто python.
  
# Процесс разработки. Настройка git

http://git-scm.com/book/ru/v2

Книга о распределённой системе контроля версий Git. Охватывает широкий спектр возможностей Git и поясняет всё на простых примерах. В версии на русском могут не открываться отдельные страницы, переключение языка в левом столбце.  
  
  
  
 
Part I
Использование GitHub
====================

Аккаунт и репозитории на github.com
-----------------------------------

В первую очередь необходимо установить и настроить клиент git, https://git-scm.com/download/win.


Затем надо зарегистрироваться на https://github.com/. После чего можно будет создавать свои репозитории. В ходе данного курса все необходимые репозитории для вашего кода будут создаваться автоматически при помощи GitHub Classrooms, но при желании или необходимости вы можете создавать их и самостоятельно.

Теперь пошагово разберем как получить задание, выполнить его и отправить на проверку.


Выполнение домашних заданий
---------------------------

Домашние задания выполняются на платформе GitHub Classrooms, которая обеспечивает автоматическое создание репозиториев для ваших решений. 

### Получение задания

Для получения задания необходимо пройти по https://classroom.github.com/a/cK4zQmbk и нажать кнопку "Accept this assignment"



После этого система создаст для вас новый репозиторий и выдаст его адрес. 



Перейдя по ссылке, вы окажетесь на сайте GitHub, и перед вами будет заготовка репозитория. В этом репозитории вы найдете описание задания, все необходимые информационные ресурсы и ссылки. 

Чтобы приступить к выполнению, вам будет необходимо склонировать этот репозиторий на свой жесткий диск используя git-клиент.
Если вы установили GitHub Desktop, то для этого достаточно нажать кнопку Clone or download и выбрать Open in desktop (если не произошел автоматический запуск программы, то перезапустите браузер):

После клонирования вы сможете открыть репозиторий в проводнике Windows нажав на ссылку "open this repository":


После этого переходим к выполнению задания.

### Выполнение задания

Для выполнения задания необходимо создать проект в среде разработки внутри только что склонированного репозитория (можно прямо в его корне). Этот пункт обязателен, если вы создадите проект в другом месте, то не сможете отправить его на проверку.



### Сохранение изменений

После того как вы создали проект, и написали какой-то код, вы можете зафиксировать свои изменения, для того, чтобы иметь возможность вернуться к предыдущей версии кода, если вдруг у вас что-то пошло не так. 


### Если что-то не получается

Если при решении задания вы уже сломали себе (и своему соседу) голову, то не стесняйтесь задавать вопросы мне. В разделе Контакты указаны... мои контакты, если не отвечаю сразу, значит немного занят, но обязательно отвечу когда будет время. Для того, чтобы мне было проще вам помочь, заранее выложите все ваши текущие наработки на GitHub, даже если ничего не компилируется и не работает.

### Отправка решения на проверку

После того, как вы решили ваш вариант задания, и уверены, что все решено правильно (или не уверены, но дедлайн уже пришел), то изменения нужно выложить на GitHub и отправить на проверку.

Для этого необходимо в клиенте Git открыть репозиторий задания и закоммитить все изменения. Окно коммита должно выглядеть следующим образом (в списке файлов у вас могут быть другие файлы, больше или меньше):



В поле Summary нужно ввести текст сообщения, например, "Задание выполнено". А в поле Description можно оставить пустым, или указать какие известные недостатки есть на текущий момент. После чего нажимаем кнопку Commit to master и создается новый **локальный** коммит. Затем отправляем все изменения на GitHub нажатием кнопки "Push origin".


### Ручная проверка

После того как вы отправили задание на проверку может пройти несколько дней, как правило я проверяю на выходных. Если у меня не будет замечаний, то я закрою Issue, и вам придет уведомление. Если же будут какие-то замечания, то я отвечу комментарием к этому Issue и напишу что мне не нравится, вам так же придет об этом уведомление.




 # Литература, источники
 
   Документация Python https://docs.python.org/3/
   
   Есть утилита autopep8, которая позволяет автоматически приводить код к виду, соответствующему PEP 8. https://pypi.org/project/autopep8/
   
   Библиотеки, написанные сообществом, находятся на ресурсе PyPI (Python Package Index). https://pypi.org/

    Именно с этого ресурса будут устанавливаться внешние пакеты, когда вы будете устанавливать их с помощью утилиты pip. Лучший способ найти библиотеку для решения той или иной       задачи – постараться загуглить ее – часто поиск Google выдает наиболее релевантный вариант. На GitHub есть коллекция хороших библиотек для решения всевозможных задач.
   
      Habrahabr.ru
      
      Большая база вопросов и ответов по Python сосредоточена на ресурсе Stack Overflow – вы будете часто натыкаться на него, когда будете искать решение в непонятных ситуациях.

      https://stackoverflow.com/
      
      
      На русском https://ru.stackoverflow.com/questions/tagged/python
      
      
      https://github.com/bayandin/awesome-awesomeness
      
      Хорошие ресурсы для новичков в Python на русском языке:
      
      https://pythonworld.ru/samouchitel-python
      
      https://metanit.com/python/tutorial/
      
      
      КНижки:
      
      Федоров Д. Ю. Программирование на языке высокого уровня Python : учеб. пособие. — М. : Издательство Юрайт, 2019. — 161 с.
      
      Tagliaferri L. How To Code in Python 3.- DigitalOcean, New York City, New York, USA.- ISBN 978-0-9997730-1-7
      
      Хеллман Д. Стандартная библиотека Python 3: справочник с примерами, 2-е изд. : Пер. с англ. — СПб. : ООО “Диалектика”, 2019. — 1376 с. : ил. LSBN 978-5-6040043-8-8 (рус.)
      
      Копец Д. Классические задачи Computer Science на языке Python. - СПб.: Питер, 2020. 256 с.: ил. - (Серия «Библиотека программиста).ISBN 978-5-4461-1428-3
      
      Марк Саммерфилд - Программирование на Python 3. Подробное руководство
      
      Марк Лутц - Изучаем Python, 4-е издание
      
      
Курсы https://stepik.org/course/3356/syllabus
Курсы яндекс
