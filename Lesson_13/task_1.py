class ProjectException(Exception):
    pass


class LevelError(ProjectException):
    def __init__(self, user_lvl, lvl):
        self.user_lvl = user_lvl
        self.lvl = lvl

    def __str__(self):
        return f'Уровень пользователя ниже необходимого: требуется {self.lvl}, получен {self.user_lvl}'


class AccessError(ProjectException):
    def __init__(self, name, idx):
        self.name = name
        self.idx = idx

    def __str__(self):
        return f'Отказано в доступе: пользователь с именем {self.name} и индексом {self.idx} не найден'