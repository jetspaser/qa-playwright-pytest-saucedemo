class LoginPage:
    USERNAME = "input#user-name"
    PASSWORD = "input#password"
    LOGIN_BTN = "input#login-button"

    def __init__(self, page):
        self.page = page

    def open(self, base_url):
        self.page.goto(base_url)

    def login(self, username, password):
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BTN)
