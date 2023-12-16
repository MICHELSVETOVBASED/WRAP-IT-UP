import sys

# Считываем строки из входного потока и удаляем начальные и конечные пробелы
lst_in = list(map(str.strip, sys.stdin.readlines()))

# Преобразуем пробелы в дефисы для каждой строки
result_urls = []
for url in lst_in:
    replaced_url = '-'.join(url.split())
    result_urls.append(replaced_url)

# Выводим результат
for result_url in result_urls:
    print(result_url)
