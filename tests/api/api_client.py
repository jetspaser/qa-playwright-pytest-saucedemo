import requests  # библиотека для HTTP-запросов


class APIClient:
    """
    Простой универсальный API-клиент.
    Его задача: удобно отправлять GET/POST/PUT/DELETE запросы.
    """

    def __init__(self, base_url):
        # базовый URL, например: "https://jsonplaceholder.typicode.com"
        # rstrip("/") убирает лишний слэш на конце
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint, **kwargs):
        # GET-запрос на base_url/endpoint
        # endpoint = "todos/1" → полный URL будет "base_url/todos/1"
        return requests.get(f"{self.base_url}/{endpoint}", **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        # POST-запрос
        # data — form-data
        # json — JSON-объект
        return requests.post(f"{self.base_url}/{endpoint}", data=data, json=json, **kwargs)

    def put(self, endpoint, json=None, **kwargs):
        # PUT — обновление ресурса
        return requests.put(f"{self.base_url}/{endpoint}", json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        # DELETE — удаление ресурса
        return requests.delete(f"{self.base_url}/{endpoint}", **kwargs)
