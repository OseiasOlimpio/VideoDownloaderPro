import customtkinter as ctk
import threading
from downloader.ytdlp_service import download

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Video Downloader Pro")
        self.geometry("520x420")
        self.resizable(False, False)

        # ===== URL =====
        ctk.CTkLabel(self, text="Cole o link do vídeo").pack(pady=10)
        self.url_entry = ctk.CTkEntry(self, width=420)
        self.url_entry.pack()

        # ===== MODO =====
        self.mode = ctk.StringVar(value="video")
        ctk.CTkRadioButton(self, text="MP4 (Vídeo)", variable=self.mode, value="video").pack()
        ctk.CTkRadioButton(self, text="MP3 (Áudio)", variable=self.mode, value="mp3").pack()

        # ===== PRESET =====
        self.preset = ctk.StringVar(value="media")
        ctk.CTkOptionMenu(self, values=["alta", "media", "leve"], variable=self.preset).pack(pady=10)

        # ===== FRAME DE PROGRESSO =====
        self.progress_frame = ctk.CTkFrame(self)
        self.progress_frame.pack(pady=15)

        self.filename_label = ctk.CTkLabel(self.progress_frame, text="", text_color="gray")
        self.filename_label.pack(pady=4)

        self.progress = ctk.CTkProgressBar(self.progress_frame, width=400)
        self.progress.pack(pady=6)
        self.progress.set(0)

        self.percent_label = ctk.CTkLabel(self.progress_frame, text="")
        self.percent_label.pack()

        self.eta_label = ctk.CTkLabel(self.progress_frame, text="")
        self.eta_label.pack()

        # ===== STATUS =====
        self.status = ctk.CTkLabel(self, text="")
        self.status.pack(pady=5)

        # ===== BOTÃO =====
        self.download_button = ctk.CTkButton(
            self,
            text="Baixar",
            command=self.start_download
        )
        self.download_button.pack(pady=15)

    # ==========================
    # DOWNLOAD
    # ==========================
    def start_download(self):
        self.download_button.configure(state="disabled")
        self.status.configure(text="⏳ Preparando...")

        self.filename_label.configure(text="")
        self.percent_label.configure(text="0%")
        self.eta_label.configure(text="")
        self.progress.configure(mode="determinate")
        self.progress.set(0)

        url = self.url_entry.get()
        mode = self.mode.get()
        preset = self.preset.get()

        threading.Thread(
            target=download,
            args=(url, self.update_progress, mode, preset),
            daemon=True
        ).start()

    def update_progress(self, data):
        self.after(0, self._update_ui, data)

    def _update_ui(self, data):
        status = data["status"]

        if status == "downloading":
            percent = data["percent"]

            self.progress.configure(mode="determinate")
            self.progress.set(percent / 100)

            self.filename_label.configure(text=data.get("filename", ""))
            self.percent_label.configure(text=f"{percent:.1f}%")
            self.eta_label.configure(text=f"⏱️ {data.get('eta', '')}")
            self.status.configure(text="⬇️ Baixando...")

        elif status == "processing":
            self.progress.configure(mode="indeterminate")
            self.progress.start()
            self.status.configure(text="🔄 Convertendo / Comprimindo...")
            self.percent_label.configure(text="")
            self.eta_label.configure(text="")

        elif status == "finished":
            self.progress.stop()
            self.progress.set(1)

            self.status.configure(text="✅ Concluído")
            self.filename_label.configure(text=f"📁 Salvo em: {data.get('path')}")
            self.download_button.configure(state="normal")
            self.show_toast("Download concluído com sucesso 🎉")

        elif status == "error":
            self.progress.stop()
            self.status.configure(text="❌ Erro")
            self.download_button.configure(state="normal")
            
    # ==========================
    # TOAST
    # ==========================
    def show_toast(self, message):
        toast = ctk.CTkToplevel(self)
        toast.overrideredirect(True)
        toast.geometry("280x60+600+420")

        ctk.CTkLabel(toast, text=message).pack(expand=True)
        toast.after(3000, toast.destroy)