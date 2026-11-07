import re
from collections import Counter

# === Функції для базових операцій з рядками ===

def find_substring(text, substring):
    """
    Пошук підрядка в тексті.
    Повертає індекс першого входження або -1, якщо підрядок не знайдено.
    """
    # TODO: Реалізуйте функцію
    pass

def replace_substring(text, old, new):
    """
    Заміна підрядка в тексті.
    """
    # TODO: Реалізуйте функцію
    pass

def split_text(text, delimiter=' '):
    """
    Розділення тексту за роздільником.
    """
    # TODO: Реалізуйте функцію
    pass

def format_string_f(name, age):
    """
    Форматування рядка з використанням f-string.
    Приклад: "Мене звати [name] і мені [age] років."
    """
    # TODO: Реалізуйте функцію
    pass

def format_string_method(name, age):
    """
    Форматування рядка з використанням методу .format().
    Приклад: "Мене звати [name] і мені [age] років."
    """
    # TODO: Реалізуйте функцію
    pass

# === Функції для роботи з регулярними виразами ===

def extract_emails(text):
    """
    Витяг email адрес з тексту.
    """
    # TODO: Реалізуйте функцію
    pass

def validate_phone_number(number):
    """
    Валідація українського телефонного номера.
    Формат: +380xxxxxxxxx
    """
    # TODO: Реалізуйте функцію
    pass

def extract_hashtags(text):
    """
    Витяг хештегів з тексту.
    """
    # TODO: Реалізуйте функцію
    pass

def extract_mentions(text):
    """
    Витяг згадувань користувачів з тексту (напр. @user).
    """
    # TODO: Реалізуйте функцію
    pass

# === Функції для аналізу тексту ===

def count_words(text):
    """
    Підрахунок кількості слів у тексті.
    """
    # TODO: Реалізуйте функцію
    pass

def count_sentences(text):
    """
    Підрахунок кількості речень у тексті.
    """
    # TODO: Реалізуйте функцію
    pass

def word_frequency(text):
    """
    Підрахунок частоти слів у тексті.
    Повертає об'єкт Counter.
    """
    # TODO: Реалізуйте функцію
    pass

def analyze_text(text):
    """
    Комплексний аналіз тексту.
    Повертає словник з результатами аналізу.
    """
    # TODO: Реалізуйте цю функцію, викликаючи інші ваші функції.
    # Приклад результату:
    # {
    #     'word_count': ...,
    #     'sentence_count': ...,
    #     'word_frequency': [...],
    #     'emails': [...],
    #     ...
    # }
    return {}

def format_analysis_results(results):
    """
    Форматування результатів аналізу для зручного виведення.
    """
    # TODO: Реалізуйте функцію
    output = "Результати аналізу тексту:\n"
    # Додайте форматування для кожного елементу в `results`
    return output

# === Функція для вилучення даних за варіантом ===

def extract_variant_data(text, variant_pattern):
    """
    Вилучає дані з тексту за допомогою патерну, специфічного для варіанту.
    """
    # TODO: Реалізуйте функцію
    pass

# === Головна частина програми ===

def read_file_content(filepath):
    """
    Читає вміст файлу.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом {filepath}")
        return None

def main():
    """
    Головна функція, що керує виконанням програми.
    """
    print("Ласкаво просимо до аналізатора тексту!")

    # Шлях до файлу з текстом
    text_filepath = 'src/data/neoterra_text.txt'

    # Читання тексту з файлу
    text_to_analyze = read_file_content(text_filepath)
    if not text_to_analyze:
        return # Завершити, якщо файл не прочитано

    while True:
        try:
            print("\nОберіть опцію:")
            print("1. Аналіз тексту 'NeoTerra 3000'")
            print("2. Валідація телефонного номера")
            print("3. Вилучення даних за варіантом")
            print("4. Вихід")
            choice = input("Ваш вибір: ")

            if choice == '1':
                results = analyze_text(text_to_analyze)
                print(format_analysis_results(results))

            elif choice == '2':
                phone = input("Введіть номер телефону для валідації: ")
                if validate_phone_number(phone):
                    print("Номер телефону валідний.")
                else:
                    print("Номер телефону невалідний.")

            elif choice == '3':
                variant = input("Введіть номер вашого варіанту (1-30): ")
                # TODO: Визначте патерн для вашого варіанту
                # Наприклад, для варіанту 1 (квантові комп'ютери):
                # pattern = r'\b[A-Z]{2}-\d{4}\b'
                # variant_data = extract_variant_data(text_to_analyze, pattern)
                # print(f"Знайдені дані: {variant_data}")
                print("Цю частину необхідно реалізувати самостійно згідно вашого варіанту.")

            elif choice == '4':
                print("Дякуємо за використання аналізатора!")
                break

            else:
                print("Невірний вибір. Спробуйте ще раз.")

        except Exception as e:
            print(f"Виникла помилка: {e}")

if __name__ == '__main__':
    main()
