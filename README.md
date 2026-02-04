### Hexlet tests and linter status:
[![Actions Status](https://github.com/DashaChizh/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DashaChizh/python-project-50/actions)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=DashaChizh_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=DashaChizh_python-project-50)
[![Python CI](https://github.com/DashaChizh/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/DashaChizh/python-project-50/actions/workflows/pyci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=DashaChizh_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=DashaChizh_python-project-50)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=DashaChizh_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=DashaChizh_python-project-50)

### Описание 
Вычислитель отличий (gendiff) - это программа, которая находит отличия между двумя файлами. 
Поддерживает входные типы файлов: `*.json` , `*.yml` , `*.yaml`.
Возвращает результат в одном из трех форматов: `stylish` , `plain` , `json`.

## Требования
* Python 3.9 или выше
* PyYAML 6.0 или выше
* [uv](https://docs.astral.sh/uv/)

### Установка

1. Клонируйте репозиторий по ссылке:
    ```sh
    git clone 
    git@github.com:DashaChizh/python-project-50.git
    ```

2. Перейдите в директорию проекта:
    ```sh
    cd python-project-50
    ```

3. Установите пакет:
    ```sh
    make install
    make build
    make package-install
    ```
---

## Работа с программой
Из командной строки:
* `$ gendiff -h` вывод справки по программе
* `$ gendiff file1.json file2.json` вывод различий в формате `stylish` (по умолчанию)
* `$ gendiff file1.json file2.yaml -f plain` вывод различий в формате `plain`
* `$ gendiff file1.yaml file2.yaml -f json` вывод различий в формате `json`

## Пример
[![asciicast](https://asciinema.org/a/gqZpLfsfMCQtk9Br.svg)](https://asciinema.org/a/gqZpLfsfMCQtk9Br)