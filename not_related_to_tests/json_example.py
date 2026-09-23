import json

# Десериализация JSON as dict
json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)  # Преобразуем JSON-строку в Python-объект (dict)

print(parsed_data["name"])


# Cериализация dict as JSON
data = {
    "name": "Мария",
    "age": 25,
    "is_student": True
}

json_string = json.dumps(data, indent=4, ensure_ascii=False)  # Преобразуем Python-объект в JSON-строку
print(json_string)


# Чтение (JSON file  as dict)
with open("test.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Загружаем JSON из файла
    print(f" JSON as dict {data}")


# Запись (dict as jSON file)
with open("json_from_dict.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)  # Сохраняем JSON в файл

