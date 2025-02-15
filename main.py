from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.graphics import Color, RoundedRectangle
from add_anime_form import AddAnimeForm  # Импорт формы

class AnimeHubApp(App):
    def build(self):
        self.root_layout = BoxLayout(orientation='vertical')
        
        # Заголовок
        self.root_layout.add_widget(Label(text='Список добавленных тайтлов', size_hint_y=None, height=50))
        
        # Область списка аниме
        self.scroll_view = ScrollView()
        self.anime_list = GridLayout(cols=1, size_hint_y=None)
        self.anime_list.bind(minimum_height=self.anime_list.setter('height'))
        self.scroll_view.add_widget(self.anime_list)
        self.root_layout.add_widget(self.scroll_view)
        
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
    
    def update_rounded_rect(self, instance, value):
        self.rounded_rect.pos = instance.pos
        self.rounded_rect.size = instance.size
    
    def open_add_anime_form(self, instance):
        self.popup = Popup(title='Добавить аниме', content=AddAnimeForm(self), size_hint=(0.8, 0.8))
        self.popup.open()
    
    def add_anime(self, anime_data):
        # Добавление нового тайтла в список
        self.anime_list.add_widget(Label(text=anime_data['title'], size_hint_y=None, height=40))
        self.popup.dismiss()

if __name__ == '__main__':
    AnimeHubApp().run()
