class ResultDto:
    def __init__(self, id: int, success: bool, message: str) -> None:
        self.id = id
        self.success = success
        self.message = message
