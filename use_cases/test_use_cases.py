import datetime

from domain.models import User, Chirp
from repository.db import MockDb
from use_cases import ChirpHandler


# что делает этот тест

def test_create_chirp():
    now = datetime.datetime.now()
    user = User('tonnioo', 'Anton')
    chirp = Chirp(                    # сперва создает chirp, у него уже есть uuid
        author=user,
        text='Hello',
        replies=[],
        publish_date=now
    )

    uuid = chirp.uuid                   # получаем уникальный идентификатор

    db = MockDb()                      # создаем мокдб, базу данных для тестов
    chirp_handler = ChirpHandler(db)    # создаем класс handler в use_cases

    chirp_handler.create_chirp(chirp)
    chirp_from_db = db.read_chirp_from_db(uuid)  # читаем результат из db

    assert chirp_from_db.uuid == uuid   # проверяем все ли на месте
