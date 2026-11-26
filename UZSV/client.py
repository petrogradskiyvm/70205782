import httpx

class ClientError(Exception):
    pass

# Хранение клиентом настроек доверия и токена активного сеанса
class HttpClient:
    def __init__(self,url,verify=True):
        self.url = url.rstrip('/')
        self.verify = verify
        self.token = None

    def call(self,method,path,data=None):
        headers = {'Authorization': f'Bearer {self.token}'} if self.token else {}
        try:
            # Тайм-аут для ограничения ожидания
            with httpx.Client(timeout=3.0, verify=self.verify, trust_env=False) as session:
                response = session.request(method, self.url + path, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        # Коды API превращаются в читабельные для пользователя сообщения
        except httpx.HTTPStatusError as exc:
            messages = {
                401: 'Проверьте введеные данные и попробуйте авторизоваться снова.',
                403: 'Для этого действия необходимы другие права.',
                404: 'Запись не найдена.',
                409: 'Запрашиваемое изменение конфликтует с активным состоянием.',
                422: 'Проверьте значение полей.',
                429: 'Превышен лимит попыток входа в систему.'
            }
            status = exc.response.status_code
            raise ClientError(messages.get(status, f'Ошибка API {status}')) from exc
        except (httpx.RequestError, ValueError) as exc:
            raise ClientError('Сервер не доступен или TLS-проверка не пройдена.') from exc