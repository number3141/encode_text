from cipher import CipherCaesar, CipherSimpleSubstitution, AthenianCipher

class UseCaseEncrypt():
    """
    Класс-фасад. 
    Один метод - один способ зашифровать текст
    """

    def encrypt_cezar(self, text, key): 
        # Шифрование методо Цезаря
        t = CipherCaesar()
        return t.encrypt_text(text, key)

    
    def encrypt_simple_substitution(self, text):
        # Шифрование методом простой подстановки
        t = CipherSimpleSubstitution()
        return t.encrypt_text(text)


    def encrypt_athenian_cipher(self, text, key): 
        # Шифрование афинным шифром 
        t = AthenianCipher()
        return t.encrypt_text(text, key)

