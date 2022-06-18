class NotFoundError(Exception):
    entity_name: str
    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, user_id: {entity_id}")

class UserNotFoundError(NotFoundError):
    entity_name: str = "User"

class WorkoutNotFoundError(NotFoundError):
    entity_name: str = "Workout"

class PasswordNotFoundError(NotFoundError):
    entity_name: str = "Password"