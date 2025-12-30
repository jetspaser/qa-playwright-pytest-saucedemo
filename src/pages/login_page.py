from playwright.sync_api import Page


class LoginPage:
    """
    Page Object для страницы логина SauceDemo.
    Инкапсулирует все действия и проверки,
    связанные со страницей авторизации.
    """

    # ====== ЛОКАТОРЫ ======
    USERNAME = "input#user-name"
    PASSWORD = "input#password"
    LOGIN_BTN = "input#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page) -> None:
        """
        Конструктор LoginPage.

        :param page: Объект Page Playwright (вкладка браузера)
        """
        self.page = page

    def open(self, base_url: str) -> None:
        """
        Открывает страницу логина.

        :param base_url: Базовый URL приложения
                         (например https://www.saucedemo.com/)
        """
        if not base_url:
            raise ValueError("base_url пустой. Проверь фикстуру base_url в conftest.py")

        self.page.goto(base_url, timeout=120_000)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию пользователя.

        :param username: Имя пользователя
        :param password: Пароль
        """
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BTN)

    def is_error_visible(self) -> bool:
        """
        Проверяет, отображается ли сообщение об ошибке.

        :return: True, если сообщение об ошибке видно
        """
        return self.page.locator(self.ERROR_MESSAGE).is_visible()

    def get_error_text(self) -> str | None:
        """
        Возвращает текст сообщения об ошибке.

        :return: Текст ошибки или None, если элемент отсутствует
        """
        return self.page.text_content(self.ERROR_MESSAGE)
