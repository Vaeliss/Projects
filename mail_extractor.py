import re
import pyperclip

my_regex = re.compile(r'''([a-zA-Z0-9._]+)
                      (@)
                      ([a-zA-Z0-9._]+)
                      (\.)
                      (com|it|net|org)''',
                      re.VERBOSE)
my_string = pyperclip.paste()
mail_list_divisa = my_regex.findall(my_string)
mail_list = []

for mail in mail_list_divisa:
    mail_list.append("".join(mail))

if len(mail_list) == 1:
    print("Trovato 1 indirizzo mail")
else:
    print(f"Trovati {len(mail_list)} indirizzi mail")
for mail in mail_list:
    print(mail)
