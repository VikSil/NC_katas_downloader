from pathlib import Path

credentials = {'email': 'YOUR_EMAIL_HERE', 'password': 'YOUR_PASSWORD_HERE'}

root = Path.cwd()

timers = {'pageload': 7, 'pagesave': 10, 'hotkey': 2}

first_page_list = ['FIRST_URL', 'SECOND_URL', 'ETC_ETC']


replacements = {
            '+':' and ',
            '/': ' slash ',
            '|': ' or ',
            '\\': ' backslash ',
            '-':' - ',
            'â€“': ' - ',
            'Â£': '£',
            '?': '',
            '!': '',
            '%': '',
            '$': '',
            ',': '',
            '.': '',
            ';': '',
            ':': '',
            "'": '',
            '"': '',
        }
