from use_case_encrypt import UseCaseEncrypt
from text import Text

def main(): 
    
    print("""
    Шифрование текста!
    Как ввести текст? 
    1 - В консоль 
    2 - Указать имя файла .txt
    """)

    answer = int(input())
    text = Text()
    use_case = UseCaseEncrypt()

    if answer == 1: 
        text.add_text_in_console()   
    else: 
        file_name = input('Введите имя файла - ')
        text.add_text_in_file(file_name)

    print("""
    Какой вариант шифрования выбрать!
    1 - Шифр Цезаря
    2 - Афинный шифр
    3 - Шифр подстановки
    
    """)

    answer = int(input())

    if answer == 1: 
        key = int(input('Введите ключ - '))
        secret_text = use_case.encrypt_cezar(text.get_text(), key)
    elif answer == 2:
        key = int(input('Введите ключ - '))
        secret_text = use_case.encrypt_athenian_cipher(text.get_text(), key)
    else: 
        secret_text = use_case.encrypt_simple_substitution(text.get_text())
    
    print(secret_text)

if __name__ == '__main__':
    main()