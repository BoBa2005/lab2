USER_SCHEME = ("id", "first_name", "second_name", "email", "password")
RECORD_SCHEME = ("id", "date", "content", "user_id", "title")
users = []
records = []
DATABASE = []

def parse_record(entity, record_str, entity_scheme):
    record_str = record_str.strip()
    if record_str.startswith(entity):
        record_str = record_str[len(entity):].strip()
    record_dict = {}
    for field in record_str.split(','):
        key, value = field.split('=')
        key = key.strip()
        value = value.strip()
        if key in entity_scheme:
            record_dict[key] = value
    return record_dict

def create_record(entity, record_str, entity_scheme, user_id):
    global DATABASE
    try:
        record_dict = parse_record(entity, record_str, entity_scheme)
        record_dict['user_id'] = user_id
        DATABASE.append(record_dict)
        print(f"{entity} створено успішно")
    except Exception as err:
        print(f"Помилка при створенні {entity}: {err}")

def search_entity_by_id(entity_name, entity_id):
    global DATABASE
    for entity in DATABASE:
        if str(entity.get('id')) == entity_id:
            print(f"Знайдено {entity_name}: {entity}")
            return
    print(f"{entity_name} з id {entity_id} не знайдено")

def search_entity_by_name(entity_name, entity_field, entity_value):
    global DATABASE
    found = False
    for entity in DATABASE:
        if entity.get(entity_field) == entity_value:
            print(f"Знайдено {entity_name}: {entity}")
            found = True
    if not found:
        print(f"{entity_name} з {entity_field} '{entity_value}' не знайдено")

def delete_entity_by_id(entity_name, entity_id):
    global DATABASE
    for idx, entity in enumerate(DATABASE):
        if str(entity.get('id')) == entity_id:
            del DATABASE[idx]
            print(f"{entity_name} з id {entity_id} видалено успішно")
            return
    print(f"{entity_name} з id {entity_id} не знайдено")

def main():
    global DATABASE
    while True:
        print("\nМеню:")
        print("1.Створити запис")
        print("2.Створити користувача")
        print("3.Пошук користувача за id")
        print("4.Пошук користувача за електронною адресою")
        print("5.Пошук запису за id")
        print("6.Пошук запису за назвою")
        print("7.Видалити запис за id")
        choice = input("Виберіть дію: ")
        if choice == "1":
            entity = "Record"
            record_str = input("Введіть дані для нового запису: ")
            user_id = input("Введіть id користувача для прив'язки запису: ")
            create_record(entity, record_str, RECORD_SCHEME, user_id)
        elif choice == "2":
            entity = "User"
            record_str = input("Введіть дані для нового користувача: ")
            create_record(entity, record_str, USER_SCHEME, "")
        elif choice == "3":
            entity_id = input("Введіть id користувача: ")
            search_entity_by_id("Користувач", entity_id)
        elif choice == "4":
            email = input("Введіть електронну адресу користувача: ")
            search_entity_by_name("Користувач", "email", email)
        elif choice == "5":
            entity_id = input("Введіть id запису: ")
            search_entity_by_id("Запис", entity_id)
        elif choice == "6":
            title = input("Введіть назву запису: ")
            search_entity_by_name("Запис", "title", title)
        elif choice == "7":
            entity_id = input("Введіть id запису для видалення: ")
            delete_entity_by_id("Запис", entity_id)
        else:
            print("Невідома цифра")

if __name__ == "__main__":
    for user in users:
        create_record("User", user, USER_SCHEME, "")
    for record in records:
        create_record("Record", record, RECORD_SCHEME, "")
    main()
