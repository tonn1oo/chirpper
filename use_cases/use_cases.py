from domain.models import Chirp
from repository.db import AbstractDatabase


class ChirpHandler:                              #
    def __init__(self, db: AbstractDatabase, ):
        self.db = db

    def create_chirp(self, chirp: Chirp):   # вызываем create_chirp,
        self.db.save_chirp_to_db(chirp)     # который зависит от db и вызывает метод save_chirp_to_db
