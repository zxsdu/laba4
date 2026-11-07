"""Лабораторна робота №4. Обробка рядків та регулярні вирази.

Базові операції з рядками, форматування (f-strings та .format()),
регулярні вирази, аналіз тексту та консольне меню.
"""
import re
from collections import Counter


def _check_str(value, name="text"):
    """Перевіряє, що значення є рядком, інакше викидає TypeError."""
    if not isinstance(value, str):
        raise TypeError(
            f"Параметр '{name}' має бути рядком, отримано {type(value).__name__}"
        )


# ---------------------------------------------------------------------------
# 1. Базові операції з рядками
# ---------------------------------------------------------------------------
def find_substring(text, substring):
    """Пошук підрядка в тексті (індекс першого входження або -1)."""
    _check_str(text, "text")
    _check_str(substring, "substring")
    return text.find(substring)


def replace_substring(text, old, new):
    """Заміна підрядка в тексті."""
    _check_str(text, "text")
    _check_str(old, "old")
    _check_str(new, "new")
    return text.replace(old, new)


def split_text(text, delimiter=' '):
    """Розділення тексту за роздільником."""
    _check_str(text, "text")
    _check_str(delimiter, "delimiter")
    if delimiter == '':
        raise ValueError("Роздільник не може бути порожнім рядком")
    return text.split(delimiter)


def format_string_f(name, age):
    """Форматування рядка з використанням f-string."""
    return f"Мене звати {name} і мені {age} років."


def format_string_method(name, age):
    """Форматування рядка з використанням методу .format()."""
    return "Мене звати {} і мені {} років.".format(name, age)


# ---------------------------------------------------------------------------
# 2. Регулярні вирази
# ---------------------------------------------------------------------------
EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
PHONE_PATTERN = r'^(?:\+?38)?0\d{9}$'


def extract_emails(text):
    """Витяг email адрес з тексту."""
    _check_str(text)
    return re.findall(EMAIL_PATTERN, text)


def validate_phone_number(number):
    """Валідація українського телефонного номера (+380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX)."""
    _check_str(number, "number")
    return bool(re.match(PHONE_PATTERN, number.strip()))


def validate_email(email):
    """Валідація email адреси."""
    _check_str(email, "email")
    return bool(re.fullmatch(EMAIL_PATTERN, email.strip()))


def extract_hashtags(text):
    """Витяг хештегів з тексту."""
    _check_str(text)
    return re.findall(r'#\w+', text)


def extract_mentions(text):
    """Витяг згадувань користувачів з тексту."""
    _check_str(text)
    return re.findall(r'(?<![\w.])@\w+', text)


# ---------------------------------------------------------------------------
# 3. Аналіз тексту
# ---------------------------------------------------------------------------
def count_words(text):
    """Підрахунок кількості слів у тексті."""
    _check_str(text)
    return len(re.findall(r'\w+', text))


def count_sentences(text):
    """Підрахунок кількості речень у тексті.

    Роздільник речення - група знаків . ! ? після якої йде пробіл або кінець
    тексту (тому крапки всередині email чи чисел речення не розривають).
    """
    _check_str(text)
    parts = re.split(r'[.!?]+(?:\s+|$)', text)
    return len([p for p in parts if p.strip()])


def word_frequency(text):
    """Підрахунок частоти слів у тексті (без урахування регістру)."""
    _check_str(text)
    return Counter(re.findall(r'\w+', text.lower()))


def analyze_text(text):
    """Комплексний аналіз тексту."""
    _check_str(text)
    if not text.strip():
        raise ValueError("Текст для аналізу порожній")
    return {
        'word_count': count_words(text),
        'sentence_count': count_sentences(text),
        'word_frequency': word_frequency(text).most_common(5),
        'emails': extract_emails(text),
        'hashtags': extract_hashtags(text),
        'mentions': extract_mentions(text),
    }


def analyze_file(path):
    """Аналіз текстового файлу (UTF-8)."""
    _check_str(path, "path")
    with open(path, encoding='utf-8') as file:
        return analyze_text(file.read())


def format_analysis_results(results):
    """Форматування результатів аналізу."""
    def joined(items):
        return ', '.join(items) if items else '—'

    output = "Результати аналізу тексту:\n\n"
    output += f"Кількість слів: {results['word_count']}\n"
    output += f"Кількість речень: {results['sentence_count']}\n\n"

    output += "Топ-5 найчастіших слів:\n"
    for word, count in results['word_frequency']:
        output += f"{word}: {count}\n"

    output += f"\nЗнайдені email адреси: {joined(results['emails'])}\n"
    output += f"Знайдені хештеги: {joined(results['hashtags'])}\n"
    output += f"Знайдені згадування: {joined(results['mentions'])}\n"
    return output


# ---------------------------------------------------------------------------
# 4. Інтерфейс користувача
# ---------------------------------------------------------------------------
MENU = (
    "\nОберіть опцію:\n"
    "1. Аналіз тексту\n"
    "2. Валідація телефону\n"
    "3. Аналіз файлу\n"
    "4. Вихід\n"
    "Ваш вибір: "
)


def main():
    print("Ласкаво просимо до аналізатора тексту!")
    while True:
        try:
            choice = input(MENU).strip()

            if choice == '1':
                text = input("Введіть текст для аналізу: ")
                print(format_analysis_results(analyze_text(text)))
            elif choice == '2':
                phone = input("Введіть номер телефону для валідації: ")
                if validate_phone_number(phone):
                    print("Номер телефону валідний.")
                else:
                    print("Номер телефону невалідний.")
            elif choice == '3':
                path = input("Введіть шлях до текстового файлу: ").strip()
                print(format_analysis_results(analyze_file(path)))
            elif choice == '4':
                print("Дякуємо за використання аналізатора!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")
        except (EOFError, KeyboardInterrupt):
            print("\nРоботу перервано користувачем.")
            break
        except FileNotFoundError:
            print("Помилка: файл не знайдено.")
        except (TypeError, ValueError, OSError) as e:
            print(f"Виникла помилка: {e}")


if __name__ == '__main__':
    main()
