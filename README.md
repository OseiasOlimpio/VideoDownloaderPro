# 🎬 Video Downloader Pro

Aplicação desktop profissional para **download de vídeos e áudios da internet**, com interface gráfica moderna, progresso em tempo real e conversão/compressão usando FFmpeg.

> Projeto desenvolvido em Python com foco em **boas práticas**, **UX** e **distribuição em `.exe`** para Windows.

---

## ✨ Funcionalidades

* 📥 Download de vídeos em **MP4**
* 🎵 Extração de áudio em **MP3**
* 📊 Barra de progresso em tempo real
* 📈 Porcentagem, nome do arquivo e ETA
* 🎛️ Presets de qualidade (alta, média, leve)
* 🔄 Conversão e compressão automática
* 🖥️ Interface gráfica moderna (CustomTkinter)
* 📦 Geração de executável `.exe` (PyInstaller)

---

## 🖼️ Interface

Interface limpa, escura e responsiva, pensada para uso diário:

* Campo para link do vídeo
* Seleção de formato (MP4 / MP3)
* Preset de qualidade
* Área central de progresso
* Feedback visual de status

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11**
* **CustomTkinter** — Interface gráfica
* **yt-dlp** — Download de mídia
* **FFmpeg** — Conversão e compressão
* **Threading** — Execução sem travar a UI
* **PyInstaller** — Geração do `.exe`

---

## 📁 Estrutura do Projeto

```
video-downloader-pro/
│
├── app.py
│
├── ui/
│   └── main_window.py
│
├── downloader/
│   ├── ytdlp_service.py
│   └── ffmpeg_service.py
│
├── ffmpeg/
│   └── ffmpeg.exe
│
└── assets/
    └── icon.ico
```

---

## ▶️ Como Executar (Modo Desenvolvimento)

### 1️⃣ Clonar o repositório

```bash
https://github.com/OseiasOlimpio/VideoDownloaderPro
cd videodownloaderpro
```

### 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
venv\\Scripts\\activate
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o app

```bash
python app.py
```

---

## 🧱 Gerar Executável (.exe)

Com o ambiente ativo:

```bash
pyinstaller ^
--onefile ^
--windowed ^
--name VideoDownloaderPro ^
--add-binary "ffmpeg/ffmpeg.exe;ffmpeg" ^
app.py
```

O executável final estará em:

```
dist/VideoDownloaderPro.exe
```

---

## ⚠️ Observações Importantes

* O executável pode gerar **falso positivo em antivírus** (comum em apps Python)
* FFmpeg é distribuído apenas para uso do aplicativo
* O projeto é para fins **educacionais e demonstrativos**

---

## 👨‍💻 Autor

**Oseias**

* Desenvolvedor Web / Python
* Em busca de oportunidades como **freelancer** e **vaga júnior**

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!
