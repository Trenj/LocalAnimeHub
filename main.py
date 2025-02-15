from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

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
        
        # Кнопка добавления аниме
        self.add_anime_btn = Button(text='+', size_hint_y=None, height=50)
        self.add_anime_btn.bind(on_press=self.add_anime)
        self.root_layout.add_widget(self.add_anime_btn)
        
        return self.root_layout
    
    def add_anime(self, instance):
        # Заглушка для добавления аниме (в будущем откроем форму)
        self.anime_list.add_widget(Label(text='Добавлено аниме', size_hint_y=None, height=40))

if __name__ == '__main__':
    AnimeHubApp().run()
