s = input('Введите текст: ')
ans = ''
anscnt = 0
dct = {}
for now in s:
    if now not in dct:
        dct[now] = 0
    dct[now] = dct[now] + 1
for key in dct:
    if  dct[key] > anscnt:
        anscnt = dct[key]
        ans = key
print(ans)
#Код пока не работает