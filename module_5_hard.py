# Дополнительное практическое задание по модулю: "Классы и объекты."
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.
# Задание "Свой YouTube":
import time
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self. current_user = None # текущий пользователь
    def log_in(self, nickname: str, password: str): # Поиск пользователя с таким же логином и паролем
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                return user
    def register(self, nickname, password, age): #Регистрация
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user) # добавление нового пользователя
            self.current_user = new_user # авто_вход
        else:
            print(f"Пользователь {nickname} уже существует")
    def log_out(self): # Для сброса текущего пользователя
        self.current_user = None
    def add(self, *args):
       for video in args:
           if video.title not in self.videos:
               self.videos.append(video)
    def get_videos(self, words:str):
        list_video = []
        for video1 in self.videos:
            if words.upper() in video1.title.upper():
                list_video.append(video1.title)
                return list_video
    def watch_video(self, movie):
            if self.current_user is None:
                print('Войдите в аккаунт, чтобы посмотреть видео')
                return
            if self.current_user and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
            elif self.current_user:
                for video in self.videos:
                    if movie in video.title:
                        for i in range(1, video.duration + 1):
                            print(i)
                            time.sleep(1) # Пауза между выводами секунд
                        print('Конец видео')
    def __str__(self):
        return self.videos

class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title #заголовок
        self.duration = duration #продолжительность
        self.time_now = 0 #секунда остановки
        self.adult_mode = adult_mode #ограничение по возрасту
    def __eq__(self, other):
        return self.title == other.title
    def __contains__(self, item):
        return item in self.title

class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname # имя пользователя
        self.password = password # пароль
        self.age = age # возраст
    def __str__(self):
        return self.nickname


if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
