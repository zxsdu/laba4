import os
import tempfile
import unittest

from text_analyzer import *


class TestTextAnalyzer(unittest.TestCase):
    def test_find_substring(self):
        self.assertEqual(find_substring("Hello, world!", "world"), 7)
        self.assertEqual(find_substring("Hello, world!", "xyz"), -1)

    def test_replace_substring(self):
        self.assertEqual(replace_substring("Hello, world!", "world", "Python"), "Hello, Python!")

    def test_split_text(self):
        self.assertEqual(split_text("Hello, world!", ", "), ["Hello", "world!"])
        self.assertEqual(split_text("a b c"), ["a", "b", "c"])

    def test_format_string_f(self):
        self.assertEqual(format_string_f("Alice", 30), "Мене звати Alice і мені 30 років.")

    def test_format_string_method(self):
        self.assertEqual(format_string_method("Bob", 25), "Мене звати Bob і мені 25 років.")

    def test_extract_emails(self):
        self.assertEqual(
            extract_emails("Contact us at info@example.com or support@test.com"),
            ["info@example.com", "support@test.com"])

    def test_validate_phone_number(self):
        self.assertTrue(validate_phone_number("+380123456789"))
        self.assertTrue(validate_phone_number("380663331133"))
        self.assertTrue(validate_phone_number("0663331133"))
        self.assertFalse(validate_phone_number("12345"))
        self.assertFalse(validate_phone_number("+3802222"))

    def test_validate_email(self):
        self.assertTrue(validate_email("user@example.com"))
        self.assertFalse(validate_email("user@@example"))

    def test_extract_hashtags(self):
        self.assertEqual(extract_hashtags("I love #Python and #Programming"),
                         ["#Python", "#Programming"])

    def test_extract_mentions(self):
        self.assertEqual(extract_mentions("Hello @user1 and @user2"), ["@user1", "@user2"])
        self.assertEqual(extract_mentions("mail me: a@b.com"), [])

    def test_count_words(self):
        self.assertEqual(count_words("This is a test sentence."), 5)

    def test_count_sentences(self):
        self.assertEqual(count_sentences("This is one. This is two! Is this three?"), 3)
        self.assertEqual(count_sentences("Write to info@example.com now. Thanks..."), 2)

    def test_word_frequency(self):
        self.assertEqual(word_frequency("a A b").most_common(1), [("a", 2)])

    def test_analyze_text(self):
        result = analyze_text("Hi #tag @user a@b.com. Bye!")
        self.assertEqual(result['sentence_count'], 2)
        self.assertEqual(result['hashtags'], ['#tag'])
        self.assertEqual(result['mentions'], ['@user'])
        self.assertEqual(result['emails'], ['a@b.com'])

    def test_format_analysis_results(self):
        text = format_analysis_results(analyze_text("Hello world. Hello!"))
        self.assertIn("Кількість слів: 3", text)
        self.assertIn("hello: 2", text)

    # --- обробка помилок ---
    def test_type_errors(self):
        with self.assertRaises(TypeError):
            find_substring(123, "a")
        with self.assertRaises(TypeError):
            extract_emails(None)
        with self.assertRaises(TypeError):
            validate_phone_number(380663331133)

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            split_text("abc", "")
        with self.assertRaises(ValueError):
            analyze_text("   ")

    def test_analyze_file(self):
        with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write("Привіт, світе! #hello")
            path = f.name
        try:
            self.assertEqual(analyze_file(path)['word_count'], 3)
        finally:
            os.remove(path)
        with self.assertRaises(FileNotFoundError):
            analyze_file("no_such_file.txt")


if __name__ == '__main__':
    unittest.main(verbosity=2)
