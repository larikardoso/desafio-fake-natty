import os
import uuid
from gtts import gTTS
import pygame

TEMP_PREFIX = "temp_audio_"


def gerar_audio_temporario(texto: str) -> str:
    if not texto.strip():
        raise ValueError("Texto vazio")

    nome_arquivo = f"{TEMP_PREFIX}{uuid.uuid4()}.mp3"

    tts = gTTS(text=texto, lang="pt-br")
    tts.save(nome_arquivo)

    return nome_arquivo


def tocar_audio(caminho: str):
    pygame.mixer.init()
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()


def liberar_audio():
    if pygame.mixer.get_init():
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()


def limpar_temporario(caminho: str):
    liberar_audio()
    if caminho and os.path.exists(caminho):
        os.remove(caminho)
