"""Варіант 5.

1. Обробка наукових даних: витяг числових значень та одиниць вимірювання.
2. Назви екокуполів (наприклад, EC-Dome-7).
"""
import re
import sys

# Одиниці вимірювання (довші записи стоять першими, щоб "км/год" не
# розпізнавалось як "км").
UNITS = [
    'км/год', 'м/с', 'км', 'м', 'см', 'мм',
    'кг', 'г', 'т',
    'кВт', 'МВт', 'ГВт', 'ТВт', 'Вт',
    'кДж', 'МДж', 'Дж',
    'кГц', 'МГц', 'ГГц', 'ТГц', 'Гц',
    'КБ', 'МБ', 'ГБ', 'ТБ', 'ПБ',
    'петабайтів', 'петабайти', 'петабайт',
    '°C', '°F', '%',
]
_UNITS_RE = '|'.join(re.escape(u) for u in sorted(UNITS, key=len, reverse=True))

# число (з пробілом як роздільником тисяч та десятковою крапкою/комою),
# необов'язковий пробіл і одиниця вимірювання
MEASUREMENT_PATTERN = re.compile(
    r'(?<![\w.,-])'
    r'(?P<value>\d+(?:[ \u00A0]\d{3})*(?:[.,]\d+)?)'
    r'[ \u00A0]?'
    r'(?P<unit>' + _UNITS_RE + r')'
    r'(?!\w)'
)

# Назва екокуполу: EC-Dome-<номер>
ECO_DOME_PATTERN = re.compile(r'\bEC-Dome-\d+\b')


def _check_str(text):
    if not isinstance(text, str):
        raise TypeError(f"Текст має бути рядком, отримано {type(text).__name__}")


def extract_measurements(text):
    """Повертає список словників: вихідний фрагмент, число та одиниця."""
    _check_str(text)
    result = []
    for match in MEASUREMENT_PATTERN.finditer(text):
        raw_value = match.group('value')
        number = float(raw_value.replace(' ', '').replace('\u00A0', '').replace(',', '.'))
        result.append({
            'text': match.group(0),
            'value': number,
            'unit': match.group('unit'),
        })
    return result


def extract_eco_domes(text):
    """Повертає унікальні назви екокуполів у порядку появи."""
    _check_str(text)
    return list(dict.fromkeys(ECO_DOME_PATTERN.findall(text)))


def format_results(measurements, domes):
    lines = ["Знайдені числові значення та одиниці вимірювання:"]
    if measurements:
        for m in measurements:
            lines.append(f"  {m['value']:g} {m['unit']}   (фрагмент: «{m['text']}»)")
    else:
        lines.append("  не знайдено")
    lines.append("")
    lines.append("Знайдені назви екокуполів:")
    if domes:
        lines.extend(f"  {d}" for d in domes)
    else:
        lines.append("  не знайдено")
    return "\n".join(lines)


def main(path='neoterra.txt'):
    try:
        with open(path, encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return 1
    except UnicodeDecodeError:
        print(f"Помилка: файл '{path}' має бути в кодуванні UTF-8.")
        return 1

    print(format_results(extract_measurements(text), extract_eco_domes(text)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'neoterra.txt'))
