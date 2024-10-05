diccionario = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "JUICIOSO": "Una persona responsable o que cumple con sus deberes",
            }
palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if palabra in diccionario.keys():
    print(diccionario[palabra])
else:
    print("Lo siento, la palabra que buscas no esta actualmente.")
