import csv
import json

# with open("users.txt", "r+", newline="") as users:
    # escribir como lista
    # writer = csv.writer(users)

    # writer.writerow(["name", "id", "username", "posts"])
    # writer.writerow(["tania", "4", "tanntani", "4"])
    # writer.writerow(["ken-ken", "5", "kk101297", "2"])

    # fieldnames = ['name', 'id', 'username', 'posts']
    # escribir como diccionario
    # writer = csv.DictWriter(users, fieldnames=fieldnames)

    # writer.writeheader()
    # writer.writerow({"name": "tania", "id":"4", "username":"tanntani", "posts":"4"})
    # writer.writerow({"name": "kkk21312", "id":"67", "username":"tansvd", "posts":"24"})

    # users.seek(0)

    # leer como diccionario
    # reader = csv.DictReader(users)
    # leer como lista
    # reader = csv.reader(users)

    # print("lista de todo el archivo:")
    # for row in reader:
    #     print(row)



new_data = {
        "name":"asd",
        "id":"234",
        "username":"kwnzcxzcmos",
        "post":"7",
    }

with open("users.json", "w", newline="") as users:
    json.dump(new_data,users, indent=4)
    
with open("users.json", "r+", newline="") as users:
	data = json.load(users)
	print(data) # { json con la data }

