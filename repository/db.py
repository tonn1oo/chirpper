from abc import ABC


class AbstractDatabase(ABC):
    def read_chirp_from_db(self, uuid):
        raise NotImplementedError

    def save_chirp_to_db(self, chirp):
        raise NotImplementedError


class MockDb(AbstractDatabase):
    def __init__(self):
        self.chirps = {}           # сохраняет переданные туда chirp

    def read_chirp_from_db(self, uuid):
        return self.chirps[uuid]

    def save_chirp_to_db(self, chirp):
        self.chirps[chirp.uuid] = chirp     # происходит сохранение в db , положили в словарь chirp
