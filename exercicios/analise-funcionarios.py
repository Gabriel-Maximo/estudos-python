funcionarios = [
    ('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6),
    ('SP', 10), ('MG', 4), ('ES', 9), ('ES', 7),
    ('ES', 12), ('SP', 7), ('SP', 11), ('MG', 8),
    ('ES', 8), ('SP', 9), ('RJ', 13), ('MG', 5),
    ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7),
    ('ES', 14), ('SP', 10), ('MG', 12)
]

estados = [estado for estado, valor in funcionarios]

estados_unicos = set(estados)

funcionarios_estado = {
    estado: [valor for estado_tupla, valor in funcionarios if estado_tupla == estado]
    for estado in estados_unicos
}

total_funcionarios = {
    estado: sum(valores)
    for estado, valores in funcionarios_estado.items()
}

print(funcionarios_estado)
print(total_funcionarios)
