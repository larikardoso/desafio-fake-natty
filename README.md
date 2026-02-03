# 🎙️ Text to Speech App com Python

Aplicação em Python que transforma texto em áudio utilizando **IA (Text-to-Speech)**, com interface gráfica simples e intuitiva.  
O usuário digita um texto, gera o áudio, escuta o resultado e decide se deseja salvar ou não o arquivo gerado.

Projeto desenvolvido com foco em **boas práticas**, **experiência do usuário** e **testes automatizados**, ideal para portfólio.

---

## 🖥️ Demonstração (fluxo)

1. O aplicativo abre uma janela com a pergunta:  
   **“O que você deseja transcrever hoje?”**
2. O usuário digita o texto
3. O áudio é gerado automaticamente
4. Após a geração:
   - O áudio pode ser reproduzido
   - Um botão **Salvar áudio** aparece
5. O usuário escolhe onde salvar o arquivo `.mp3`
6. Arquivos temporários são limpos ao fechar o app

---

## 🚀 Funcionalidades

- ✅ Interface gráfica com **Tkinter**
- ✅ Conversão de texto para áudio (Text-to-Speech)
- ✅ Reprodução de áudio no próprio app
- ✅ Botão de salvar exibido **somente após gerar o áudio**
- ✅ Uso de arquivos temporários
- ✅ Limpeza automática de arquivos temporários ao fechar o app
- ✅ Testes automatizados com **pytest**
- ✅ Estrutura organizada para facilitar manutenção

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Tkinter** – Interface gráfica
- **gTTS** – Geração de áudio (Text-to-Speech)
- **pygame** – Reprodução de áudio
- **pytest** – Testes automatizados
- **uuid / tempfile / os** – Gerenciamento de arquivos temporários

---

## 📁 Estrutura do Projeto

```text
desafio_fake_natty/
│
├── project.py               # Interface gráfica e fluxo principal
├── audio_service.py         # Lógica de geração e limpeza de áudio
├── __init__.py
│
├── tests/
│   ├── __init__.py
│   └── test_audio.py        # Testes automatizados
│
├── README.md
└── requirements.txt
````

## ⚙️ Como Rodar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/larikardoso/desafio_fake_natty.git
cd desafio_fake_natty
````

### 2️⃣ Criar ambiente virtual (recomendado)
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows (Git Bash)
````

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
````

### 4️⃣ Executar o aplicativo
```bash
python project.py
````

## 🧪 Rodando os Testes Automatizados

Execute os testes a partir da raiz do projeto:

```bash
pytest
````

### ✔️ O que os testes cobrem
- Criação de arquivos de áudio temporários
- Existência do arquivo gerado
- Limpeza correta dos arquivos temporários
- Garantia de que não ficam resíduos no sistema

### 🧹 Gerenciamento de Arquivos Temporários
- O áudio é gerado inicialmente como um arquivo temporário
- O arquivo só é salvo permanentemente se o usuário escolher
- Ao fechar o aplicativo:
    - Todos os arquivos temporários são removidos automaticamente

### Isso evita:
- Erros como WinError 32
- Acúmulo de arquivos no sistema
