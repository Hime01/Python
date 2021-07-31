secs = int(input('Введите количество секунд, и я выведу время в формате чч:мм:сс: '))

hours = int(secs/3600)
secs = secs - hours * 3600
minutes = int(secs/60)
secs = secs - minutes * 60
if hours / 10 < 1:
    hours = '0' + str(hours)
if minutes / 10 < 1:
    minutes = '0' + str(minutes)
if secs / 10 < 1:
    secs = '0' + str(secs)

print(f'{hours}:{minutes}:{secs}')