import random
import string
from faker import Faker

fake = Faker()

def generate_user_data():
    # Генерируем случайную строку для гарантии уникальности email
    random_digits = "".join(random.choices(string.digits, k=6))
    
    return {
        "email": f"sultan_test_{random_digits}@yandex.ru",
        "password": fake.password(length=8),
        "name": fake.first_name()
    }