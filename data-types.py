# LIST
# almacena cualquier tipo de dato
# se puede agregar, eliminar y modificar el elemento de cada lista por su indice
# Puedes eliminar elementos con del, remove(), o pop().

list = [12, "jonaanw", 1.062, False]
list[3] = True
list[1] = "jonaa"
list.remove(True)

# print(list)
# print(list[3])

pizzas = [
    {
        "calories": 4202,
        "name": "family",
    },
    {
        "calories": 3700,
        "name": "big",
    },
    {
        "calories": 3102,
        "name": "medium",
    },
]

# print(pizzas[2])
# ------------

# ------------
# TUPLES
# son inmutables.

tuplee = (12,324.5,534,53, "jonjonjon")

# print(tuplee)
# error doesn't modifiquied tuplee = ("jojo")
# ------------


# ------------
# DICTIONARYS
# funcionan con CLAVE - VALOR
# en un diccionario de Python, las claves pueden ser de varios tipos, no solo cadenas (strings). Las claves deben ser hashables, lo que significa que deben ser inmutables. Esto incluye strings, int, float, tuples, boolean

persons = {
    2:{
        "age": 19,
        "fv-food": "pizza",
        "in-job": False,
    },
    "joseph":{
        "age": 19,
        "fv-food": "kfc",
        "in-job": True,
    },
    True:{
        "age": 22,
        "fv-food": "lasagna",
        "in-job": True,
    },
    ("sao", 123):{
        "age": 9999,
        "fv-food": "lasagna",
        "in-job": False,
    }
}

# print(persons)
# print(persons["jon"])


# ------------
# SETS
# Almacena solo valores únicos, sin duplicados, y no tiene un orden específico. No se utilizan claves.

dictionary = {"jonjon", 1.65, "single", True}

# print(dictionary)

first_set = {1,2,3,4,5}
second_set = {"jjon", "sedsc", 231, False}

# print(second_set)