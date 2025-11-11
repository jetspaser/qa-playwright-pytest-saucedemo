class LoginPage:
    # ====== ЛОКАТОРЫ (селекторы) элементов страницы ======
    # Поле ввода логина
    USERNAME = "input#user-name"
    # Поле ввода пароля
    PASSWORD = "input#password"
    # Кнопка "Login"
    LOGIN_BTN = "input#login-button"
    # Сообщение об ошибке (появляется при неправильных данных)
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page):
        """
        Конструктор страницы.
        В него передаётся объект page (страница браузера),
        который предоставляет Playwright.

        self.page — ссылка на открытую вкладку браузера.
        Через неё мы взаимодействуем с элементами.
        """
        self.page = page

    def open(self, base_url):
        self.page.goto(base_url, timeout=120000)  # 120s
        """
        Открываем страницу логина.
        base_url передаётся из фикстуры (conftest.py),
        чтобы в будущем можно было легко переключать окружения.
        """
        self.page.goto(base_url)

    def login(self, username, password):
        """
        Выполняем авторизацию:
        1. Вводим логин
        2. Вводим пароль
        3. Нажимаем кнопку Login

        Этот метод скрывает детали Selenium/Playwright
        и делает тест читабельным: login_page.login("user", "pass")
        """
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BTN)

    def is_error_visible(self):
        """
        Проверяем, появилось ли сообщение об ошибке.
        Используется в негативных тестах.
        Возвращает True/False.

        Если завтра селектор сменится — меняем его здесь,
        тесты НЕ придётся трогать.
        """
        return self.page.is_visible(self.ERROR_MESSAGE)

    def get_error_text(self):
        """
        Возвращает ТЕКСТ сообщения об ошибке.
        Это важно для точного сравнения:
        например, проверять конкретный текст ошибки,
        а не просто факт её отображения.

        Возвращает строку или None, если элемента нет.
        """
        return self.page.text_content(self.ERROR_MESSAGE)



