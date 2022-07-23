import datetime

from models import Chirp, User


def test_create_chirp():
    now = datetime.datetime.now()
    user = User('tonnioo', 'Anton')
    chirp = Chirp(

        author=user,
        text='Hello',
        replies=[],
        publish_date=now

    )

    assert chirp.author == user
    assert chirp.text == 'Hello'
    assert chirp.replies == []
    assert chirp.publish_date == now


def test_create_user():
    user = User('tonnioo', 'Anton')
    assert user.login == 'tonnioo'
    assert user.name == 'Anton'
