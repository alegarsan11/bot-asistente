import csv

archivo_entrada = 'tester-test-performance;2023-05-15T11.50.11.555.csv'
archivo_salida = 'datos_modificados1.csv'
caracter_a_reemplazar = ','
caracter_reemplazo = ';'

with open(archivo_entrada, 'r') as archivo_lectura, open(archivo_salida, 'w', newline='') as archivo_escritura:
    lector_csv = csv.reader(archivo_lectura)
    escritor_csv = csv.writer(archivo_escritura)
    for fila in lector_csv:
        fila_modificada = [valor.replace('"', "") for valor in fila]
        escritor_csv.writerow(fila_modificada)

print('Archivo CSV modificado generado exitosamente.')