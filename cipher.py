import random

class Cipher(): 
    """
    Entity 
    Абстрактный класс, наследниками которого будут способы шифрования текста. 

    Методы
    ----------
    1) encrypt_text(text) 
        Метод, шифрующий текст. Должен возвращать строку
    """
    def encrypt_text(self, text) -> str: 
        raise NotImplementedError('Создайте encrypt_text')



class CipherCaesar(Cipher):
    def __init__(self) -> None:
        self.ALL_SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя !.?'
    
    def encrypt_text(self, text, key) -> str:
        secret_message = ''

        for letter in text: 
            if letter in self.ALL_SYMBOLS: 
                new_index = (self.ALL_SYMBOLS.find(letter) + key) % len(self.ALL_SYMBOLS)
                secret_message += self.ALL_SYMBOLS[new_index]
            else: 
                secret_message += letter
                
        return secret_message   


class CipherSimpleSubstitution(Cipher):

    def __init__(self) -> None:
        self.ALL_SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.key = list(self.ALL_SYMBOLS)
        random.shuffle(self.key)
        self.key = ''.join(self.key)


    def encrypt_text(self, text) -> str:
        secret_message = ''

        for letter in text: 
            if letter in self.key: 
                new_index = self.key.find(letter)
                secret_message += self.ALL_SYMBOLS[new_index]
            else: 
                secret_message += letter

        return secret_message


class AthenianCipher(Cipher):

    def __init__(self) -> None:
        self.ALL_SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя !.?'
    
    def encrypt_text(self, text, key) -> str:
        secret_message = ''

        keyA = random.randint(1, key)
        keyB = random.randint(1, key)

        for letter in text: 
            if letter in self.ALL_SYMBOLS: 
                new_index = ((self.ALL_SYMBOLS.find(letter) * keyA) + keyB) % len(self.ALL_SYMBOLS)
                secret_message += self.ALL_SYMBOLS[new_index]
            else: 
                secret_message += letter
                
        return secret_message   


if __name__ == '__main__': 
    t = AthenianCipher()
    print(t.encrypt_text('АБРИКОСОВЫЙ', 8))