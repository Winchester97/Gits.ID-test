h = input('Input jam: ')
m = input('Input Menit: ')
s = input('Input Detik: ')
0
ket = input('Input keterangan ("AM/PM"): ')

#h, m, s, ket = '12','00','00','AM'

if ket == 'AM':
  if h == '12':
    h = '00'

print()
print(h,m, sep=':')
