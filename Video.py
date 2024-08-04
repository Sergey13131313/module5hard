class Video:
    def __init__(self, title, duration, timeNow = 0, adultMode = False):
        self.title = title
        self.duration = duration
        if duration < timeNow:
            self.timeNow = duration
        else:
            self.timeNow = timeNow
        self.adultMode = adultMode

    def __eq__(self, other):
        return self.title == other

    def __str__(self):
        return (f'Название - {self.title},'
                f' продолжительность - {self.duration},'
                f' возростное ограничение - {'до 18 лет' if self.adultMode else 'старше 18 лет до 18 лет'}')




if __name__ == '__main__':

    track1 = Video('Video1', 120, 130)
    print(track1)

    a = 10