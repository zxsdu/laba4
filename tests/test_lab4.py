import unittest
import sys
import os

# Додаємо шлях до папки src, щоб можна було імпортувати lab4
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab4 import (
    find_substring,
    replace_substring,
    split_text,
    format_string_f,
    format_string_method,
    extract_emails,
    validate_phone_number,
    extract_hashtags,
    extract_mentions,
    count_words,
    count_sentences,
    word_frequency,
    # Додайте сюди інші функції, які хочете протестувати
)

class TestTextAnalyzer(unittest.TestCase):

    def test_find_substring(self):
        """Тест для функції find_substring."""
        # TODO: Напишіть свій тест
        # self.assertEqual(find_substring("Hello, world!", "world"), 7)
        pass

    def test_replace_substring(self):
        """Тест для функції replace_substring."""
        # TODO: Напишіть свій тест
        # self.assertEqual(replace_substring("Hello, world!", "world", "Python"), "Hello, Python!")
        pass

    def test_split_text(self):
        """Тест для функції split_text."""
        # TODO: Напишіть свій тест
        # self.assertEqual(split_text("Hello, world!", ", "), ["Hello", "world!"])
        pass

    def test_format_string_f(self):
        """Тест для функції format_string_f."""
        # TODO: Напишіть свій тест
        # self.assertEqual(format_string_f("Alice", 30), "Мене звати Alice і мені 30 років.")
        pass

    def test_format_string_method(self):
        """Тест для функції format_string_method."""
        # TODO: Напишіть свій тест
        # self.assertEqual(format_string_method("Bob", 25), "Мене звати Bob і мені 25 років.")
        pass

    def test_extract_emails(self):
        """Тест для функції extract_emails."""
        text = "Contact us at info@example.com or support@test.com"
        expected = ["info@example.com", "support@test.com"]
        # TODO: Напишіть свій тест
        # self.assertEqual(extract_emails(text), expected)
        pass

    def test_validate_phone_number(self):
        """Тест для функції validate_phone_number."""
        # TODO: Напишіть свої тести для валідних і невалідних номерів
        # self.assertTrue(validate_phone_number("+380123456789"))
        # self.assertFalse(validate_phone_number("12345"))
        pass

    def test_extract_hashtags(self):
        """Тест для функції extract_hashtags."""
        text = "I love #Python and #Programming"
        expected = ["#Python", "#Programming"]
        # TODO: Напишіть свій тест
        # self.assertEqual(extract_hashtags(text), expected)
        pass

    def test_extract_mentions(self):
        """Тест для функції extract_mentions."""
        # TODO: Напишіть свій тест
        pass

    def test_count_words(self):
        """Тест для функції count_words."""
        # TODO: Напишіть свій тест
        pass

    def test_count_sentences(self):
        """Тест для функції count_sentences."""
        # TODO: Напишіть свій тест
        pass

    # === Додайте власні тести для інших функцій та варіантів ===


if __name__ == '__main__':
    # Запуск тестів
    unittest.main(verbosity=2)
