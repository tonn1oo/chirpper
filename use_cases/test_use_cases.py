import datetime

from domain.models import User, Chirp
from repository.db import MockDb
from use_cases.use_cases import ChirpHandler


# что делает этот тест

def test_create_chirp():
    now = datetime.datetime.now()
    user = User('tonnioo', 'Anton')
    chirp = Chirp(  # сперва создает chirp, у него уже есть uuid
        author=user,
        text='Hello',
        replies=[],
        publish_date=now
    )

    uuid = chirp.uuid  # получаем уникальный идентификатор

    db = MockDb()  # создаем мокдб, базу данных для тестов
    chirp_handler = ChirpHandler(db)  # создаем класс handler в use_cases

    chirp_handler.create_chirp(chirp)
    chirp_from_db = db.read_chirp_from_db(uuid)  # читаем результат из db

    assert chirp_from_db.uuid == uuid  # проверяем все ли на месте


def test_reply_chirp():  # проверяет работоспособность метода , который создает комментарий
    now = datetime.datetime.now()
    user = User('tonnioo', 'Anton')
    chirp1 = Chirp(
        author=user,
        text='Hello',
        replies=[],
        publish_date=now
    )                           # Создает 2 chirp
    chirp2 = Chirp(
        author=user,
        text='Hello',
        replies=[],
        publish_date=now
    )
    uuid1 = chirp1.uuid         # с уникальными идентификаторами
    uuid2 = chirp2.uuid

    db = MockDb()
    chirp_handler = ChirpHandler(db)

    # выполняет метод reply.chirp, который превращает один chirp в комментарий к другому chirp
    chirp_handler.reply_chirp(chirp1, chirp2)

    # считываем исходный chirp и комментарий из bd по заранее собранным uuid
    chirp_from_db1 = db.read_chirp_from_db(uuid1)
    chirp_from_db2 = db.read_chirp_from_db(uuid2)

    # проверяем является ли второй chirp одним из комментариев к первому
    assert chirp_from_db2 in chirp_from_db1.replies

    # проверяем явояется ли chirp_from_db2.parent родительским chirp для chirp_from_db2
    assert chirp_from_db2.parent == chirp_from_db1
