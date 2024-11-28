import csv

def leer_csv(nombre_archivo):
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        datos = list(lector_csv)
    return datos

def escribir_csv(nombre_archivo, datos, encabezados):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados)
        escritor_csv.writeheader()
        escritor_csv.writerows(datos)

def realizar_operaciones(datos):
    for fila in datos:
        operacion = fila['operation']
        op1 = float(fila['operand_1'])
        op2 = float(fila['operand_2'])
        if operacion == 'SUM':
            fila['correct_result'] = op1 + op2
        elif operacion == 'SUB':
            fila['correct_result'] = op1 - op2
        elif operacion == 'MUL':
            fila['correct_result'] = op1 * op2
        elif operacion == 'DIV':
            fila['correct_result'] = op1 / op2
        elif operacion == 'POW':
            fila['correct_result'] = op1 ** op2
    return datos

def main():
    nombre_archivo = 'data/math_operations.csv'
    datos = leer_csv(nombre_archivo)
    datos_actualizados = realizar_operaciones(datos)
    encabezados = datos[0].keys()
    escribir_csv(nombre_archivo, datos_actualizados, encabezados)
    print('Archivo CSV actualizado con los resultados correctos.')

if __name__ == '__main__':
    main()
