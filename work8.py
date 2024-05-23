import sqlite3

# Создание базы данных и таблиц
def create_tables():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Создание таблицы countries
    cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL
                    )''')

    # Создание таблицы cities
    cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        area REAL DEFAULT 0,
                        country_id INTEGER,
                        FOREIGN KEY (country_id) REFERENCES countries(id)
                    )''')

    # Создание таблицы students
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        city_id INTEGER,
                        FOREIGN KEY (city_id) REFERENCES cities(id)
                    )''')

    conn.commit()
    conn.close()

# Добавление записей в таблицы
def insert_data():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Добавление записей в таблицу countries
    cursor.executemany("INSERT INTO countries (title) VALUES (?)", [("Kyrgyzstan",), ("Germany",), ("China",)])

    # Добавление записей в таблицу cities
    cursor.executemany("INSERT INTO cities (title, country_id) VALUES (?, ?)", [
        ("Bishkek", 1), ("Osh", 1), ("Berlin", 2), ("Beijing", 3), ("Moscow", 2), ("New York", 2), ("Paris", 2)])

    conn.commit()
    conn.close()

# Отображение списка городов
def display_cities():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cursor.execute("SELECT title FROM cities")
    cities = cursor.fetchall()

    print("Список городов из вашей базы данных:")
    for city in cities:
        print(city[0])

    conn.close()

# Отображение информации о студентах в выбранном городе
def display_students(city_id):
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
                    FROM students
                    INNER JOIN cities ON students.city_id = cities.id
                    INNER JOIN countries ON cities.country_id = countries.id
                    WHERE cities.id = ?''', (city_id,))
    students = cursor.fetchall()

    print("Имя\tФамилия\tСтрана\tГород\tПлощадь города")
    for student in students:
        print("\t".join(str(elem) for elem in student))

    conn.close()

if __name__ == "__main__":
    create_tables()
    insert_data()

    while True:
        print("\nВы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
        display_cities()
        city_id = input("Введите id города: ")

        if city_id == '0':
            print("Программа завершена.")
            break

        try:
            city_id = int(city_id)
            display_students(city_id)
        except ValueError:
            print("Ошибка: Некорректный ввод. Пожалуйста, введите целое число.")
