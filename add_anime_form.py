from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class AddAnimeForm(Popup):
    def __init__(self, add_callback, **kwargs):
        super().__init__(**kwargs)
        self.title = "Добавить аниме"
        self.size_hint = (0.8, 0.7)
        
        self.add_callback = add_callback  # Функция для обработки добавления
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Поля ввода
        self.title_input = TextInput(hint_text="Название аниме")
        self.description_input = TextInput(hint_text="Описание", multiline=True)
        self.banner_input = TextInput(hint_text="Ссылка на баннер")
        self.trailer_input = TextInput(hint_text="Ссылка на трейлер")
        self.watch_link_input = TextInput(hint_text="Ссылка на просмотр")
        
        layout.add_widget(Label(text="Название:"))
        layout.add_widget(self.title_input)
        layout.add_widget(Label(text="Описание:"))
        layout.add_widget(self.description_input)
        layout.add_widget(Label(text="Ссылка на баннер:"))
        layout.add_widget(self.banner_input)
        layout.add_widget(Label(text="Ссылка на трейлер:"))
        layout.add_widget(self.trailer_input)
        layout.add_widget(Label(text="Ссылка на просмотр:"))
        layout.add_widget(self.watch_link_input)
        
        # Кнопки
        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        add_button = Button(text="Добавить", on_press=self.on_add)
        cancel_button = Button(text="Отмена", on_press=self.dismiss)
        
        button_layout.add_widget(add_button)
        button_layout.add_widget(cancel_button)
        
        layout.add_widget(button_layout)
        
        self.content = layout

    def on_add(self, instance):
        anime_data = {
            "title": self.title_input.text,
            "description": self.description_input.text,
            "banner": self.banner_input.text,
            "trailer": self.trailer_input.text,
            "watch_link": self.watch_link_input.text
        }
        self.add_callback(anime_data)  # Передаем данные в основное приложение
        self.dismiss()
