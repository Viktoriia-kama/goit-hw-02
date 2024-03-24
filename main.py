from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://viktoriia1kama:01112023gsuite@atlascluster.txkzlwo.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.ds02


# FUNCTIONS
# функція для виведення всіх записів із колекції
def get_all_info_from_collection():
    for i in list(db.cats.find()):
        print(i)


# функція, яка дозволяє user ввести ім'я кота та виводить інформацію про нього
def get_info_about_cat():
    cat_name = input("Введіть ім'я кота, інформацію про якого ви хочете отримати: ")
    print(db.cats.find_one({'name': cat_name}))


# функція, яка дозволяє користувачеві оновити вік кота за ім'ям
def update_year_by_name():
    cat_name = input("Введіть ім'я кота, вік якого ви хочете змінити: ")
    cat_new_age = int(input("Введіть вік кота: "))
    db.cats.update_one(
        {'name': cat_name},
        {
            '$set': {
                'age': cat_new_age
            }
        })
    print(f"The {cat_name}'s age was updated")


# функція, яка дозволяє додати нову характеристику до списку features кота за ім'ям
def update_features_by_name():
    cat_name = input("Введіть ім'я кота, характеристики якого ви хочете змінити: ")
    cat_new_feature = input("Введіть характеристику кота: ")
    db.cats.update_one(
        {'name': cat_name},
        {
            '$push': {
                'features':   cat_new_feature}
        })
    print(f"The {cat_name}'s feature was updated")


# функція для видалення запису з колекції за ім'ям тварини
def delete_info_by_name():
    cat_name = input("Введіть ім'я кота, інформацію про якого ви хочете видалити: ")
    db.cats.delete_one({'name': cat_name})
    print(f'The info about {cat_name} was deleted')


try:
#     db.cats.insert_one({
#         'name': 'barsik',
#         'age': 3,
#         'features': ['ходить в капці', 'дає себе гладити', 'рудий']
#     })
    
#     db.cats.insert_many([
#     {
#         'name': 'Lama',
#         'age': 2,
#         'features': ['ходить в лоток', 'не дає себе гладити', 'сірий'],
#     },
#     {
#         'name': 'Liza',
#         'age': 4,
#         'features': ['ходить в лоток', 'дає себе гладити', 'білий'],
#     },
#     {
#        ' name': 'Boris',
#         'age': 12,
#         'features': ['ходить в лоток', 'не дає себе гладити', 'сірий'],
#     },
#     {
#         'name': 'Murzik',
#         'age': 1,
#         'features': ['ходить в лоток', 'дає себе гладити', 'чорний'],
#     },
# ]) 
      
    get_all_info_from_collection()
    # get_info_about_cat()
    # update_year_by_name()
    # update_features_by_name()
    # db.cats.delete_many({})
    # delete_info_by_name()
except Exception as e:
    print(e)