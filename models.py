from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    nickname: str
    joined_games: list[str] = []
    active_game: str | None = None

class Game(BaseModel):
    id: str
    name: str
    participants: list[int] = []
    target_cycle: dict[str, str] = {}
