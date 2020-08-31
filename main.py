#! python3
# phoneAndEmail.py - находит телефонные номера и
# адреса электронной почты в буфее обмена

import pyperclip, re

# регулярное выражение для телефонов
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? 
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)  # территориальный код, разделителль, первые 3 цифры, разделитель, последние 4 цифры, добавочный номер

# регулярное выражение для адресов электронной почты
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z{2,4}])
)''', re.VERBOSE)  # имя пользователя, символ @, имя домена, остаьная часть адреса

# Поиск соответствия в тексте, содержащемся в буфере обмена
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# скопировать результаты в буфер обмена
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('/n'.join(matches))
else:
    print('Телефонные номера и адреса электронной почты'
          ' не обнаружены')
