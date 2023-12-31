import random

from abc import ABC, abstractmethod 

from exception import EmptyTextException

# Абстрактный класс не содержит всех реализаций методов, необходимых для полной работы, 
# это означает, что он содержит один или несколько абстрактных методов. 
# Абстрактный метод - это только объявление метода, без его подробной реализации.
class Cipher(ABC): 
    """
    Entity 
    Абстрактный класс, наследниками которого будут способы шифрования текста. 

    Методы
    ----------
    1) encrypt_text(text) 
        Метод, шифрующий текст. Должен возвращать строку
    """
    
    ALL_SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя !.?'
    LEN_SYMBOLS = len(ALL_SYMBOLS)

    @abstractmethod
    def encrypt_text(self, text) -> str: 
        pass


class CipherCaesar(Cipher):  
    def encrypt_text(self, text, key) -> str:

        if len(text) < 1: 
            raise EmptyTextException(f"len(text) = 0", 'Введён пустой текст')

        secret_message = ''

        for letter in text.strip(): 
            if letter in self.ALL_SYMBOLS: 
                new_index = (self.ALL_SYMBOLS.find(letter) + key) % self.LEN_SYMBOLS
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

        if len(text) < 1: 
            raise EmptyTextException(f"len(text) = 0", 'Введён пустой текст')

        secret_message = ''

        for letter in text: 
            if letter in self.key: 
                new_index = self.key.find(letter)
                secret_message += self.ALL_SYMBOLS[new_index]
            else: 
                secret_message += letter

        return secret_message


class AthenianCipher(Cipher):
    def encrypt_text(self, text, key) -> str:

        if len(text) < 1: 
            raise EmptyTextException(f"len(text) = 0", 'Введён пустой текст')

        secret_message = ''

        keyA = random.randint(1, key)
        keyB = random.randint(1, key)

        for letter in text: 
            if letter in self.ALL_SYMBOLS: 
                new_index = ((self.ALL_SYMBOLS.find(letter) * keyA) + keyB) % self.LEN_SYMBOLS
                secret_message += self.ALL_SYMBOLS[new_index]
            else: 
                secret_message += letter
                
        return secret_message   


if __name__ == '__main__': 
    t = CipherCaesar()
    r = t.encrypt_text('', 8)
    print(r)
    print(len(r))