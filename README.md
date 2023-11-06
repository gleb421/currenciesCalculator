# Currencies Calculator

# Общее описание решения

### Программа, которая помогает переводить значение различных валют в рубли

## Описание работы программы currencies.py


###В нем находятся словарь Constants, в котором находятся коэффициенты различных валют к рублю

## Описание работы программы currencies_calculator.py
### 1) Выводит все коды валют, указанные в файле currencies.py, чтобы пользователь корректно ввел данные
### 2)Описание работы функции currenciesCalc
### Параметры функции:
 - chislo - количество иностранной валюты
 - val - курс определенной валюты к рулблю
### Результат выполнения функции:
-Вылавливает, в каких местах и при каких условиях будут появляться различные ошибки и определяет, какое сообщение об ошибке увидит пользователь.
 Возвращает итоговый результат, равный chislo * Constants.currenc[val]
### Пример работы функции:

- input -> 5, 'USD'
- return 5 * 93.0351
- output -> 465,1755

## Описание работы программы Unit_tests.py

### 1) Описание работы функции test_res(self)
Проверяет, сходятся ли результаты работы currencies_calculator при вводе адекватных значений, за счет того, что мы можем просчитать итоговый результат самостоятельно. Берем в пример 3 ввода данных
### 2)Описание работы функции test_zero_mul(self)
Проверяет, является ли 0 результатом работы программы currencies_calculator, если chislo = 0. Берем в пример 3 ввода данных
### 3)Описание работы функции test_types(self)
Рассматривает 3 ввода данных, при которых должна появиться ошибка TypeError, и проверяет, адекватно-ли работает наша программа в этих случаях. Выводит сообщение об ошибке пользователю 
### 4)Описание работы функции test_wrongcode(self)
Проверяет как работает программа currencies_calculator, если val является строкой, но не соответствует ни одному из кодов 

### 5)Описание работы функции test_values(self)
Проверяет как работает программа currencies_calculator, если chislo < 0. Выводит сообщение об ошибке пользователю.


### Результат выполнения всех функций в Unit_tests.py:

- Функции проверяют адекватно ли работает currencies_calculator во всех случаях

# История изменения проекта с хэшами коммитов
commit e3def356710f892c6b0689b476ac0a7479f8fc4e (origin/UnitTests)
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 02:00:39 2023 +0300

    Были исправлены ошибки, связанные с ValueError

    Выводилось неверное значение при вводе отрицательной переменной, после изменений при вводе отрицательной переменной появляется ValueError

commit 378f3b899df84232bf7299cb0589a24c7beb4ba8
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:57:14 2023 +0300

    Добавлена функция для проверки ValueError

    Это ошибка появляется при вводе отрицательного числа

commit dc6a172553b203b301fd3ffcc69af708fb91dd27
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:54:56 2023 +0300

    Добавлено сообщение для KeyError

commit cc83907393e979004ed3a6b88220b059f5ba01bd
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:52:51 2023 +0300

    Добавлена проверка KeyError с выводом пользователю

commit 1c6a05e4b35e32577b6715cd780d604c3ba1c429
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:51:42 2023 +0300

    Вывод сообщения об ошибке

commit a391aa7dd38dbe248ee981e17a25285119abb19b
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:50:28 2023 +0300

    Добавлены сообщения, которые будет видеть пользователь при TypeError

commit d3436c6ee3226b176f1308fdfe190eb2f73c0aa8
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:41:37 2023 +0300

    Была добавлена функция для проверки TypeError

    функция test_types  проверяет, корректно-ли работает программа при вводе переменных неправильного типа данных

commit 35763d36110d083176b1185ae49bd216a0e0930e
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:37:03 2023 +0300

    Создание файла с unit тестами

    В начале добавлены функции, которые проверят работу программы при адекватных значениях и которые проверят работу при нулевой переменной

commit 2ded0467a0d8f73496b71c9e7b9ed2aae3b7fbb3
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:30:56 2023 +0300

    Программа, которая конвертирует значение разных валют в рубли

:
commit d133f76a2a9824c5a5b48db1107fd42ad14e01b3 (HEAD -> main, origin/main, origin/HEAD)
Merge: 2ded046 e3def35
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 02:02:05 2023 +0300

    Merge pull request #1 from gleb421/UnitTests

    Создание файла с unit тестами

commit e3def356710f892c6b0689b476ac0a7479f8fc4e (origin/UnitTests)
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 02:00:39 2023 +0300

    Были исправлены ошибки, связанные с ValueError

    Выводилось неверное значение при вводе отрицательной переменной, после изменений при вводе отрицательной переменной появляется ValueError

commit 378f3b899df84232bf7299cb0589a24c7beb4ba8
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:57:14 2023 +0300

    Добавлена функция для проверки ValueError

    Это ошибка появляется при вводе отрицательного числа

commit dc6a172553b203b301fd3ffcc69af708fb91dd27
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:54:56 2023 +0300

    Добавлено сообщение для KeyError

commit cc83907393e979004ed3a6b88220b059f5ba01bd
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:52:51 2023 +0300

    Добавлена проверка KeyError с выводом пользователю

commit 1c6a05e4b35e32577b6715cd780d604c3ba1c429
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:51:42 2023 +0300

    Вывод сообщения об ошибке

commit a391aa7dd38dbe248ee981e17a25285119abb19b
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:50:28 2023 +0300

    Добавлены сообщения, которые будет видеть пользователь при TypeError

commit d3436c6ee3226b176f1308fdfe190eb2f73c0aa8
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:41:37 2023 +0300

    Была добавлена функция для проверки TypeError

    функция test_types  проверяет, корректно-ли работает программа при вводе переменных неправильного типа данных

commit 35763d36110d083176b1185ae49bd216a0e0930e
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:37:03 2023 +0300

    Создание файла с unit тестами

    В начале добавлены функции, которые проверят работу программы при адекватных значениях и которые проверят работу при нулевой переменной

commit 2ded0467a0d8f73496b71c9e7b9ed2aae3b7fbb3
Author: gleb421 <94608946+gleb421@users.noreply.github.com>
Date:   Tue Nov 7 01:30:56 2023 +0300

    Программа, которая конвертирует значение разных валют в рубли

