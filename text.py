class Text(): 
    def __init__(self, text = '') -> None:
        self.text = text

    
    def add_text_in_file(self, file_name): 
        with open(file_name, 'r', encoding = 'UTF-8') as f: 
            self.text = f.read()


    def add_text_in_console(self):
        self.text = input('Введите текст - ')


    def get_text(self):
        return self.text