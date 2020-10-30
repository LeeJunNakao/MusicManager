from domain.music import InsertMusicDto
from adapters.repository import MusicRepository



def insert_music(**music: dict):
    
    dto = InsertMusicDto(**music)
    MusicRepository.create(**dto.dict())

    return dto.dict()
