num = input('Por favor, entre com o número de segundos que deseja converter: ')
im = int(num)

dia = im // (24*3600)
rdia = im % (24*3600)
hora = rdia // 3600
rhora = rdia % 3600
min = rhora // 60
rmin = rhora % 60


print(dia,'dias,',hora,'horas,',min,'minutos e',rmin,'segundos.')