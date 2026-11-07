import unittest

from variant5 import extract_measurements, extract_eco_domes


class TestVariant5(unittest.TestCase):
    def test_measurements_basic(self):
        result = extract_measurements("Швидкість 1200 км/год, потужність 50 ТВт.")
        self.assertEqual([(m['value'], m['unit']) for m in result],
                         [(1200.0, 'км/год'), (50.0, 'ТВт')])

    def test_measurements_decimal_and_percent(self):
        result = extract_measurements("Рівень 0,01% та температура 22.5 °C")
        self.assertEqual([(m['value'], m['unit']) for m in result],
                         [(0.01, '%'), (22.5, '°C')])

    def test_measurements_thousands_separator(self):
        result = extract_measurements("Відстань 1 250 км")
        self.assertEqual(result[0]['value'], 1250.0)

    def test_measurements_ignore_non_units(self):
        self.assertEqual(extract_measurements("5 мільйонів жителів у 2150 році"), [])
        self.assertEqual(extract_measurements("Модель HL-500 та NT3K-78901-XZ"), [])

    def test_eco_domes(self):
        text = "Куполи EC-Dome-7, EC-Dome-12 і знову EC-Dome-7; не EC-Dome-X та XEC-Dome-3"
        self.assertEqual(extract_eco_domes(text), ["EC-Dome-7", "EC-Dome-12"])

    def test_empty_and_invalid(self):
        self.assertEqual(extract_measurements(""), [])
        self.assertEqual(extract_eco_domes(""), [])
        with self.assertRaises(TypeError):
            extract_measurements(None)
        with self.assertRaises(TypeError):
            extract_eco_domes(42)


if __name__ == '__main__':
    unittest.main(verbosity=2)
