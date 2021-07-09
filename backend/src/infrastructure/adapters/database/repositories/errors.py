
class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id: int) -> None:
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")

