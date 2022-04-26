# Инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
class TestParam:
    link = "https://stepik.org/lesson/25969/step/8"

    def test_use_links(self, firefox):
        firefox.get(self.link)
