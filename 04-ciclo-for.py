lista_etapas_lavado = ["Llenado", "Lavado", "Enguaje", "Drenado", "Listo"]

for elemento in lista_etapas_lavado:
    print(elemento)
    
    if elemento == "Llenado" or elemento == "Listo":
        print("Puedo abrir la tapa")
    else:
        print("No puede abrir la tapa, espere...")
    print("---------------")