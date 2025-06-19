from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Character(BaseModel):
    name: str
    image: str

class SceneObject(BaseModel):
    src: str
    pos: str
    scale: float

class Scene(BaseModel):
    background: str
    objects: List[SceneObject]

class StoryPayload(BaseModel):
    title: str
    characters: List[Character]
    scenes: List[Scene]
    audio_url: str

@app.post("/render_story")
def render_story(payload: StoryPayload):
    print("🎬 Story Title:", payload.title)
    print("🎭 Characters:", payload.characters)
    print("🎞️ Scenes:", payload.scenes)
    print("🔊 Audio:", payload.audio_url)
    return { "status": "success", "video_url": "https://example.com/video.mp4" }
