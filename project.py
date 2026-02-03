import tkinter as tk
from tkinter import messagebox, filedialog
from gtts import gTTS
import pygame
import uuid
import os
import shutil
from audio_service import (
    gerar_audio_temporario,
    tocar_audio,
    limpar_temporario
)


# variável global para guardar o último áudio gerado
audio_gerado = None


def gerar_audio():
    global audio_gerado

    texto = entrada_texto.get("1.0", tk.END).strip()

    if not texto:
        messagebox.showwarning("Aviso", "Digite algum texto para transcrever.")
        return

    try:
        nome_arquivo = f"temp_audio_{uuid.uuid4()}.mp3"
        audio_gerado = nome_arquivo

        tts = gTTS(text=texto, lang="pt-br")
        tts.save(nome_arquivo)

        tocar_audio(nome_arquivo)

        # Mostra o botão de salvar depois de gerar o áudio
        botao_salvar.pack(pady=10)

        messagebox.showinfo("Pronto", "Áudio gerado com sucesso 🎧")

    except Exception as e:
        messagebox.showerror("Erro", str(e))


def salvar_audio():
    global audio_gerado

    if not audio_gerado or not os.path.exists(audio_gerado):
        messagebox.showwarning("Aviso", "Nenhum áudio disponível para salvar.")
        return

    caminho = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("Arquivo de Áudio", "*.mp3")],
        title="Salvar áudio como"
    )

    if not caminho:
        return

    try:
        shutil.copy(audio_gerado, caminho)
        messagebox.showinfo("Sucesso", "Áudio salvo com sucesso 💾")

        limpar_audio_temp()

        botao_salvar.pack_forget()

    except Exception as e:
        messagebox.showerror("Erro", str(e))

def tocar_audio(caminho):
    pygame.mixer.init()
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

def limpar_audio_temp():
    global audio_gerado

    try:
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
    except Exception:
        pass

    if audio_gerado and os.path.exists(audio_gerado):
        try:
            os.remove(audio_gerado)
        except PermissionError:
            pass  # garante que o app não quebre

    audio_gerado = None

def ao_fechar_app():
    limpar_audio_temp()
    janela.destroy()

# 🪟 Janela principal
janela = tk.Tk()
janela.title("🤖 Bot Text-to-Speech")
janela.geometry("520x400")

label = tk.Label(
    janela,
    text="🤖 O que você deseja transcrever hoje?",
    font=("Arial", 12, "bold")
)
label.pack(pady=10)

entrada_texto = tk.Text(janela, height=8, width=58)
entrada_texto.pack(pady=10)

botao_gerar = tk.Button(
    janela,
    text="🔊 Gerar Áudio",
    command=gerar_audio,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11)
)
botao_gerar.pack(pady=15)

# Botão começa escondido
botao_salvar = tk.Button(
    janela,
    text="💾 Salvar Áudio",
    command=salvar_audio,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11)
)

janela.mainloop()
