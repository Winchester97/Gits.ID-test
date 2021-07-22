a = input('Email: ')

if '@' in a:
  print("format email dengan '@'",end='')
  indeks_titik = (a.index('@'))
  if indeks_titik <= 20:
    print(', Panjang Karakter',end='')
    if '.' in a[(indeks_titik+1):] :
      print(", format email dengan '.'", end='')
      if (a[:-6] == '.co.id') or (a[-3:] == '.id'):
        print(', dan Domain email sudah BENAR')
      else:
        print(' Benar, namun Domain salah')
    else:
      print(" Benar, namun letak '.' salah")
  else:
    print(' Benar, namun Karakter terlalu panjang')
else:
  print(" Format email tidak terdapat '@'")
