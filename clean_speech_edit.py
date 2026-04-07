# -*- coding: utf-8 -*-
import customtkinter as ctk
from tkinter import filedialog


def run_app():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("CleanSpeechEdit")
    root.geometry("520x700")
    root.resizable(False, False)
    root.configure(fg_color="#0f172a")

    xml_path = {"value": None}
    audio_path = {"value": None}
    mode_var = ctk.StringVar(value="default")
    status_var = ctk.StringVar(value="Ожидание...")

    # --- callbacks ---
    def select_xml():
        path = filedialog.askopenfilename(title="Выбери XML")
        if path:
            xml_path["value"] = path
            xml_label.configure(text=path)

    def select_audio():
        path = filedialog.askopenfilename(title="Выбери аудио")
        if path:
            audio_path["value"] = path
            audio_label.configure(text=path)

    def generate():
        if not xml_path["value"] or not audio_path["value"]:
            status_var.set("❌ выбери файлы")
            return
        status_var.set("✅ Готово (демо)")

    # --- UI ---
    ctk.CTkLabel(root, text="CleanSpeechEdit", font=("Inter", 22, "bold")).pack(pady=(20, 12))

    ctk.CTkButton(root, text="📂 Выбрать XML", command=select_xml,
                  fg_color="#2b3b52", hover_color="#354a66",
                  font=("Inter", 14, "bold"), corner_radius=10, width=200).pack()
    xml_label = ctk.CTkLabel(root, text="XML не выбран", font=("Inter", 12), text_color="#94a3b8")
    xml_label.pack(pady=(4, 12))

    ctk.CTkButton(root, text="🎧 Выбрать аудио", command=select_audio,
                  fg_color="#2b3b52", hover_color="#354a66",
                  font=("Inter", 14, "bold"), corner_radius=10, width=200).pack()
    audio_label = ctk.CTkLabel(root, text="Аудио не выбрано", font=("Inter", 12), text_color="#94a3b8")
    audio_label.pack(pady=(4, 20))

    frame_modes = ctk.CTkFrame(root, fg_color="#182238", corner_radius=14)
    frame_modes.pack(fill="x", padx=18, pady=8)
    ctk.CTkRadioButton(frame_modes, text="Default (рекомендуется)", variable=mode_var, value="default",
                       font=("Inter", 15, "bold")).pack(anchor="w", padx=14, pady=(12, 4))
    ctk.CTkLabel(frame_modes, text="Лучший баланс: чисто, но сохраняет естественность речи",
                 font=("Inter", 12), text_color="#9aa0a6").pack(anchor="w", padx=14, pady=(0, 12))

    frame_soft = ctk.CTkFrame(root, fg_color="#182238", corner_radius=14)
    frame_soft.pack(fill="x", padx=18, pady=8)
    ctk.CTkRadioButton(frame_soft, text="Soft", variable=mode_var, value="soft",
                       font=("Inter", 15, "bold")).pack(anchor="w", padx=14, pady=(12, 4))
    ctk.CTkLabel(frame_soft, text="Минимальная чистка — если спикер говорит уже хорошо",
                 font=("Inter", 12), text_color="#9aa0a6").pack(anchor="w", padx=14, pady=(0, 12))

    frame_agg = ctk.CTkFrame(root, fg_color="#182238", corner_radius=14)
    frame_agg.pack(fill="x", padx=18, pady=8)
    ctk.CTkRadioButton(frame_agg, text="Aggressive", variable=mode_var, value="aggressive",
                       font=("Inter", 15, "bold")).pack(anchor="w", padx=14, pady=(12, 4))
    ctk.CTkLabel(frame_agg, text="Максимальная чистка — убирает повторы и весь мусор",
                 font=("Inter", 12), text_color="#9aa0a6").pack(anchor="w", padx=14, pady=(0, 12))

    ctk.CTkButton(root, text="▶ Генерировать", command=generate,
                  fg_color="#5b6bff", hover_color="#4b59e0",
                  font=("Inter", 15, "bold"), corner_radius=12, width=200, height=44).pack(pady=18)

    ctk.CTkLabel(root, textvariable=status_var, font=("Inter", 13), text_color="#9aa0a6").pack(pady=(0, 10))

    root.mainloop()


if __name__ == "__main__":
    run_app()
