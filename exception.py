class EmptyTextException(Exception): 
    """Исключение для ошибок во входных данных.
        Attributes:
            expression -- выражение, в котором произошла ошибка
            message -- объяснение ошибки
    """
    
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
