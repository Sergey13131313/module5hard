import User as us
import Video as v
import time as t


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.currentUser = None

    def logIn(self, nick, password):
        if [nick, hash(password)] in self.users:
            self.currentUser = [nick, hash(password)]

    def register(self, nick, password, age):
        for x in self.users:
            if x.nickname == nick:
                print(f'Пользователь {x.nickname} уже существует')
                return

        self.users.append(us.User(nick, password, age))
        self.currentUser = self.users[-1]

    def logOut(self, user):
        self.currentUser = None

    def addVideo(self, *listVideo):
        for x in listVideo:
            if x not in self.videos:
                self.videos.append(x)

    def getVideos(self, searchWord):
        searchList = []
        for x in self.videos:
            if searchWord.upper() in x.title.upper():
                searchList.append(x.title)
        return searchList

    def watchVideo(self, nameFilm):

        if self.currentUser != None:
            film = None
            try:
                film = self.videos[self.videos.index(nameFilm)]
                if (film.adultMode == True) and (self.currentUser.age < 18):
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                for i in range(film.timeNow + 1, film.duration + 1):
                    print(i, end=' ')
                    t.sleep(1)
                print('Конец видео')
            except ValueError:
                print('Такого видео нет!')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = v.Video('Лучший язык программирования 2024 года', 200)
    v2 = v.Video('Для чего девушкам парень программист?', 10, adultMode=True)
    # Добавление видео
    ur.addVideo(v1, v2)

    print(ur.getVideos('лучший'))
    print(ur.getVideos('ПРОГ'))

    ur.watchVideo('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watchVideo('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watchVideo('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.currentUser)
    ur.watchVideo('Лучший язык программирования 2024 года!')


