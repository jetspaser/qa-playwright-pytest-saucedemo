import pytest


@pytest.mark.api  # маркируем тест как API
def test_status_is_ok(api_client):
    """
    Проверяем, что публичный API работает корректно.
    В данном примере: GET /todos/1
    """

    # Отправляем GET-запрос:
    # api_client сам сформирует URL вида:
    # https://jsonplaceholder.typicode.com/todos/1
    response = api_client.get("todos/1")

    # Проверяем HTTP-статус 200 (успех)
    assert response.status_code == 200, "API должен вернуть 200 OK"

    # Преобразуем тело ответа в JSON
    data = response.json()

    # Проверяем, что вернулся правильный объект с id=1
    assert data["id"] == 1, "Ожидали id=1 в ответе"
