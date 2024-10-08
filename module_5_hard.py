"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №5.hard
Дополнительное практическое задание по модулю: "Классы и объекты."
"""

import time

class User:
    """
    Класс пользователя, содержащий атрибуты: имя пользователя, пароль, возраст
    """
    def __init__(self, username, password, age):
        self.username = username
        self.password = hash(password)
        self.age = age

    # Задание специального "магического" метода "Свойства в строке" класса
    def __str__(self):
        return f'Пользователь: {self.username}, возраст: {self.age}'


class Video:
    """
    Класс видеороликов, содержащий атрибуты: заголовок, продолжительность, секунда остановки,
    ограничение по возрасту
    """
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    # Задание специального "магического" метода "Свойства в строке" класса
    def __str__(self):
        return f'название: {self.title}, продолжительность: {self.duration}, 18+: {self.adult_mode}'


class UrTube:
    """
    Класс платформы, содержащий атрибуты: список объектов User, список объектов Video, текущий пользователь
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    # Регистрация нового пользователя в системе
    def register(self, nickname, password, age):
        exist = False # Флаг наличия пользователя в списке
        for item in self.users:
            if nickname == item.username:
                exist = True
        if not exist:
            self.current_user = User(nickname, password, age)
            self.users.append(self.current_user)
            print(f'Пользователь {nickname} успешно зарегистрирован')
        else:
            print(f'Пользователь {nickname} уже существует')

    # Аутентификация пользователя в системе
    def log_in(self, nickname, password):
        hash_pass = hash(password) # Получение хэша пароля кандидата в пользователи
        exist = False # Флаг наличия пользователя в списке
        for item in self.users:
            if nickname == item.username and hash_pass == item.password:
                self.current_user = item
                print(f'Вход пользователя "{nickname}" успешно выполнен!')
                exist = True
                break
        if not exist: print(f'Ошибка имени пользователя или пароля!')

    # Выход пользователя из системы
    def log_out(self):
        print(f'Текущий {self.current_user} сброшен')
        self.current_user = None

    # Добавление в список системы 'неограниченного количества' записей видео
    def add(self, *args):
        for arg in args:
            exist = False  # Флаг наличия видео в списке
            for item in self.videos:
                if arg.title == item.title:
                    exist = True
                    break
            if not exist:
                self.videos.append(arg)
                print(f'Видео "{arg.title}" добавлено в список')

    # Поиск видеороликов по фразе
    def get_videos(self, find_str:str):
        print('Найдены видеозаписи:')
        for item in self.videos:
            if find_str.lower() in item.title.lower(): print(item)

    # Просмотр видео
    def watch_video(self, video:str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for item in self.videos:
            if video.lower() in item.title.lower():
                if item.adult_mode and self.current_user.age <= 17:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                else: # все ограничения соблюдены - показываем видео:
                    for item.time_now in range(1, item.duration + 1):
                        print(item.time_now, end = ' ')
                        time.sleep(1)
                    item.time_now = 0
                    print('Конец видео')

# Запуск
if __name__ == '__main__':
    ur = UrTube() # Инициализация платформы "UrTube"

    # Команды к системе "UrTube":
    ur.register('vasya_pupkin', 'lolkekcheburek', 18) # Пользователь vasya_pupkin успешно зарегистрирован
    ur.register('prosto_pupkin', 'prostocheburek', 13) # Пользователь prosto_pupkin успешно зарегистрирован
    ur.register('vasya_pupkin', 'lolkekcheburek', 18) # Пользователь vasya_pupkin уже существует

    ur.log_in('prosto_pupki', 'prostocheburek') # Ошибка имени пользователя или пароля!
    ur.log_in('prosto_pupkin', 'prostochebure') # Ошибка имени пользователя или пароля!
    ur.log_in('prosto_pupkin', 'prostocheburek') # Вход пользователя "prosto_pupkin" успешно выполнен!

    ur.log_out() # Текущий Пользователь: prosto_pupkin, возраст: 13 сброшен
    print(ur.current_user) # 'None' Пользователь "сброшен"

    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    ur.add(v1, v2)
    # Видео "Лучший язык программирования 2024 года" добавлено в список
    # Видео "Для чего девушкам парень программист?" добавлено в список

    v3 = Video('Лучший язык программирования 2024 года', 200)
    v4 = Video('Для чего козе баян?', 7)
    ur.add(v3, v4) # Видео "Для чего козе баян?" добавлено в список
    # v3 не добавляется в список Videos (т.к. уже там есть)

    ur.get_videos('для чего')
    # Найдены видеозаписи:
    # название: Для чего девушкам парень программист?, продолжительность: 10, 18+: True
    # название: Для чего козе баян?, продолжительность: 7, 18+: False

    ur.watch_video('Для чего девушкам парень программист?') # Войдите в аккаунт, чтобы смотреть видео
    ur.log_in('prosto_pupkin', 'prostocheburek') # Вход пользователя "prosto_pupkin" успешно выполнен!
    ur.watch_video('Для чего девушкам парень программист?') # Вам нет 18 лет, пожалуйста покиньте страницу
    ur.log_in('vasya_pupkin', 'lolkekcheburek') # Вход пользователя "vasya_pupkin" успешно выполнен!
    ur.watch_video('Для чего девушкам парень программист?') # 1 2 3 4 5 6 7 8 9 10 Конец видео