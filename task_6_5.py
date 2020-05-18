class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки. Используем {self.title}.")

class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисую {self.title[0:4]}ой.")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисую {self.title}ом.")

class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисую {self.title}ом.")

a = Stationery("Канцтовары")
pen = Pen("Ручка")
pencil = Pencil("Карандаш")
marker = Handle("Маркер")
a.draw()
pen.draw()
pencil.draw()
marker.draw()
