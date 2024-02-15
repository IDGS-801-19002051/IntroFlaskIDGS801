from io import open
"""
archivo1=open("archivo.txt","a")
archivo1.write('\n saludo IDGS804 nuevo')
archivo1.close()
"""

archivo1=open("archivo.txt","r")
"""print(archivo1.read())
archivo1.seek(10)
print(archivo1.read())"""
#print(archivo1.readlines())
for datos in archivo1.readlines():
  print(datos.rstrip())
archivo1.close()