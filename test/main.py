#! python3
# phoneAndEmail.py - находит телефонные номера и
# адреса электронной почты в буфее обмена

import pyperclip
import re

# регулярное выражение для телефонов
phoneRegex1 = re.compile(r'''
((\+7|7|8))?
([\s\-])?
(\(?[489][0-9]{2}\))?
([\s\-])?
([0-9]{3})
([\s\-])?
([0-9]{2})
([\s\-])?
([0-9]{2})''')



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
print(phoneRegex1.findall(text))

for groups in phoneRegex1.findall(text):
    #phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)
print(emailRegex.findall(text))
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# скопировать результаты в буфер обмена
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса электронной почты'
          ' не обнаружены')
