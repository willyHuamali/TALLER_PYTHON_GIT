curso={'matematicas':5, 'fisica':2, 'quimica':7}
total_credito=0
for asignatura,credito in curso.items():
    print(asignatura, "tiene ", credito, 'creditos')
    total_credito +=credito
print('numero total de creditos de los cursos es:' ,total_credito)