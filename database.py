import sqlite3

class AnimeDatabase:
    def __init__(self, db_name="animehub.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Создаёт таблицу аниме, если её ещё нет"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS anime (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                banner TEXT,
                trailer TEXT,
                link TEXT
            )
        ''')
        self.connection.commit()

    def add_anime(self, title, description, banner, trailer, link):
        """Добавляет аниме в базу"""
        self.cursor.execute('''
            INSERT INTO anime (title, description, banner, trailer, link)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, banner, trailer, link))
        self.connection.commit()

    def get_all_anime(self):
        """Получает список всех аниме"""
        self.cursor.execute("SELECT * FROM anime")
        return self.cursor.fetchall()

    def close(self):
        """Закрывает соединение с базой данных"""
        self.connection.close()
