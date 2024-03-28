class User:
    def __init__(self, id, first_name, second_name, email, password):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = password

class Record:
    def __init__(self, id, date, content, user, title):
        self.id = id
        self.date = date
        self.content = content
        self.user = user
        self.title = title

class Database:
    def __init__(self):
        self.users = []
        self.records = []

    def add_user(self, user):
        self.users.append(user)

    def add_record(self, record):
        self.records.append(record)

    def search_user_by_id(self, user_id):
        for user in self.users:
            if str(user.id) == user_id:
                return user
        return None

    def search_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def search_record_by_id(self, record_id):
        for record in self.records:
            if str(record.id) == record_id:
                return record
        return None

    def search_record_by_title(self, title):
        for record in self.records:
            if record.title == title:
                return record
        return None

def main():
    database = Database()

    while True:
        print("\nМеню:")
        print("1.Створити запис")
        print("2.Створити користувача")
        print("3.Пошук користувача за id")
        print("4.Пошук користувача за електронною адресою")
        print("5.Пошук запису за id")
        print("6.Пошук запису за назвою")
        choice = input("Виберіть дію: ")

        if choice == "1":
            record_data = input("Введіть дані для нового запису (id, date, content, user, title): ")
            record = Record(*record_data.split(', '))
            database.add_record(record)
            print("Запис створено успішно")

        elif choice == "2":
            user_data = input("Введіть дані для нового користувача (id, first_name, second_name, email, password): ")
            user = User(*user_data.split(', '))
            database.add_user(user)
            print("Користувача створено успішно")

        elif choice == "3":
            user_id = input("Введіть id користувача: ")
            user = database.search_user_by_id(user_id)
            if user:
                print(f"Знайдено користувача: {user.__dict__}")
            else:
                print(f"Користувача з id {user_id} не знайдено")

        elif choice == "4":
            email = input("Введіть електронну адресу користувача: ")
            user = database.search_user_by_email(email)
            if user:
                print(f"Знайдено користувача: {user.__dict__}")
            else:
                print(f"Користувача з електронною адресою {email} не знайдено")

        elif choice == "5":
            record_id = input("Введіть id запису: ")
            record = database.search_record_by_id(record_id)
            if record:
                print(f"Знайдено запис: {record.__dict__}")
            else:
                print(f"Запис з id {record_id} не знайдено")

        elif choice == "6":
            title = input("Введіть назву запису: ")
            record = database.search_record_by_title(title)
            if record:
                print(f"Знайдено запис: {record.__dict__}")
            else:
                print(f"Запис з назвою {title} не знайдено")

        else:
            print("Невідома цифра")

if __name__ == "__main__":
    main()
