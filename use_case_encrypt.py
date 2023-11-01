from cipher import CipherCaesar, CipherSimpleSubstitution, AthenianCipher
from exception import EmptyTextException

class UseCaseEncrypt():
    """
    Класс-фасад. 
    Один метод - один способ зашифровать текст
    """

    def encrypt_cezar(self, text, key): 
        # Шифрование методо Цезаря
        t = CipherCaesar()
        try: 
            return t.encrypt_text(text, key)
        except EmptyTextException as e: 
            print(e.expression)
            print(e.message)
            

    def encrypt_simple_substitution(self, text):
        # Шифрование методом простой подстановки
        t = CipherSimpleSubstitution()
        return t.encrypt_text(text)


    def encrypt_athenian_cipher(self, text, key): 
        # Шифрование афинным шифром 
        t = AthenianCipher()
        return t.encrypt_text(text, key)



if __name__ == '__main__': 
    t = UseCaseEncrypt()
    t.encrypt_cezar('', 8)