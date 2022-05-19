import sys
import re
from datetime import datetime

with open(sys.argv[1], 'r') as log_file:
    Lines = log_file.readlines()
    event_count = {}
    for line in Lines:
        # нормализуем строку, удалив более одного пробела подряд
        norm_line = re.sub('\s+',' ', line)
        # возьмём дату из строки
        event_datetime = datetime.strptime(norm_line[:21], "[%Y-%m-%d %H:%M:%S]")
        # сократим до минут
        event_datetime_minute = event_datetime.strftime("%Y-%m-%d %H:%M")
        if event_datetime_minute not in event_count:
            event_count[event_datetime_minute] = 1
        else:
            event_count[event_datetime_minute] += 1
    # выводим количество событий с NOK за каждую минуту
    for event_time, count in event_count.items():
        print(event_time, count, sep=' - NOK count - ')

