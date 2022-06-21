import hashlib
import uuid

class HashValues:
    def __init__(self) -> None:
        self.seed = "gym-bud-app"

    def create_hash(self, value) -> str:
        m = hashlib.sha256()
        m.update(str(value).encode("utf-8"))
        m.update(self.seed.encode("utf-8"))
        hex_dig = m.hexdigest()

        return hex_dig

    def create_uuid(self) -> str:
        _uuid = uuid.uuid4()

        return str(_uuid)
