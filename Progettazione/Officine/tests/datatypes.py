from code.datatypes import Targa


targa1 = "1294"
targa2 = "AZ 1246"
targa3_err = ""
targa4_err = "ZAZHATT"

targhe = [targa1, targa2, targa3_err, targa4_err]

for test in targhe:
  t = Targa(test)
  print(t)

