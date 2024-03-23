import psycopg2
from faker import Faker
import random

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="mysecretpassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


# Функція для створення випадкових даних
def generate_fake_data(fake, number_users, number_tasks, unique_status_values):
    users = []
    tasks = []
    statuses = unique_status_values

    # Заповнення таблиці users
    for _ in range(number_users):
        fullname = fake.name()
        email = fake.email()
        users.append((fullname, email))

    # Заповнення таблиці tasks
    for _ in range(number_tasks):
        title = fake.sentence()
        description = fake.text()
        status_id = random.randint(1, len(statuses))
        user_id = random.randint(1, number_users)
        tasks.append((title, description, status_id, user_id))

    return users, tasks, statuses


# Задання кількості користувачів, завдань та унікальних статусів
NUMBER_USERS = 10
NUMBER_TASKS = 30
UNIQUE_STATUS_VALUES = ['new', 'in progress', 'completed']

# Створення об'єкта Faker
fake = Faker()

# Генерація випадкових даних
users, tasks, statuses = generate_fake_data(fake, NUMBER_USERS, NUMBER_TASKS, UNIQUE_STATUS_VALUES)

# Додавання користувачів до таблиці users
for user in users:
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", user)

# Додавання статусів до таблиці status
for status in statuses:
    cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))

# Додавання завдань до таблиці tasks
for task in tasks:
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", task)

# Збереження змін до бази даних
conn.commit()

# Закриття з'єднання
cur.close()
conn.close()
