from fastapi import FastAPI

app = FastAPI(title='АС УЗСВ', version='0.1.0')

# Проверка работоспособности без обращений к PostgreSQL
@app.get('/health/live')
def live():
    return {'status': 'live'}