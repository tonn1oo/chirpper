from abc import ABC

from domain.models import Chirp


class AbstractDatabase(ABC):
    def read_chirp_from_db(self, uuid):
        raise NotImplementedError

    def save_chirp_to_db(self, chirps: list[Chirp]):
        raise NotImplemented


class MockDb(AbstractDatabase):
    def __init__(self):
        self.chirps = {}  # сохраняет переданные туда chirp

    def read_chirp_from_db(self, uuid) -> Chirp:
        return self.chirps[uuid]

    def save_chirp_to_db(self, chirps: list[Chirp]):
        for chirp in chirps:
            self.chirps[chirp.uuid] = chirp  # происходит сохранение в db , положили в словарь chirp
