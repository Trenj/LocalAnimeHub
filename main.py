from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.graphics import Color, RoundedRectangle
from add_anime_form import AddAnimeForm  # Импорт формы
from database import AnimeDatabase


class AnimeHubApp(App):
    def build(self):
        self.db = AnimeDatabase()  # Подключаем базу данных

        self.root_layout = BoxLayout(orientation='vertical')

        # Заголовок
        self.root_layout.add_widget(Label(text='Список добавленных тайтлов', size_hint_y=None, height=50))

        # Область списка аниме
        self.scroll_view = ScrollView()
        self.anime_list = GridLayout(cols=1, size_hint_y=None)
        self.anime_list.bind(minimum_height=self.anime_list.setter('height'))
        self.scroll_view.add_widget(self.anime_list)
        self.root_layout.add_widget(self.scroll_view)

        # Загружаем сохранённые аниме
        self.load_anime()

        # Контейнер для кнопки
        btn_layout = BoxLayout(size_hint=(None, None), size=(60, 60), pos_hint={'right': 1, 'bottom': 1})

        # Кнопка добавления аниме
        self.add_anime_btn = Button(text='+', size_hint=(None, None), size=(60, 60))
        self.add_anime_btn.bind(on_press=self.open_add_anime_form)

        # Скругление углов кнопки
        with self.add_anime_btn.canvas.before:
            Color(0.2, 0.6, 1, 1)  # Цвет кнопки
            self.rounded_rect = RoundedRectangle(pos=self.add_anime_btn.pos, size=self.add_anime_btn.size, radius=[20])

        # Обновление позиции скругления при изменении размеров кнопки
        self.add_anime_btn.bind(pos=self.update_rounded_rect, size=self.update_rounded_rect)

        btn_layout.add_widget(self.add_anime_btn)
        self.root_layout.add_widget(btn_layout)

        return self.root_layout

    def load_anime(self):
        """Загружает сохранённые аниме в интерфейс"""
        for anime in self.db.get_all_anime():
            anime_id, title, description, banner, trailer, link = anime  # Распаковка данных
            self.anime_list.add_widget(Label(text=f"{title}: {description}", size_hint_y=None, height=40))

    def add_anime(self, title, description, banner, trailer, link):
        """Добавляет аниме в базу и в интерфейс"""
        self.db.add_anime(title, description, banner, trailer, link)  # Запись в БД
        self.anime_list.add_widget(Label(text=f"{title}: {description}", size_hint_y=None, height=40))
        self.popup.dismiss()  # Закрываем окно формы

    def update_rounded_rect(self, instance, value):
        """Обновляет положение и размер скругленного фона кнопки"""
        self.rounded_rect.pos = instance.pos
        self.rounded_rect.size = instance.size

    def open_add_anime_form(self, instance):
        """Открывает форму добавления аниме"""
        self.popup = Popup(title='Добавить аниме', content=AddAnimeForm(self), size_hint=(0.8, 0.8))
        self.popup.open()


if __name__ == '__main__':
    AnimeHubApp().run()
