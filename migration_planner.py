# Copyright 2026 Google LLC
"""Selector app to choose between Exchange and Files migration planners."""

import os
import subprocess
import sys
import customtkinter as ctk

COLOR_BACKGROUND = "#F0F2F5"
COLOR_SURFACE = "#FFFFFF"
COLOR_PRIMARY = "#0B57D0"
COLOR_PRIMARY_HOVER = "#0842a0"
COLOR_TEXT_MAIN = "#1F1F1F"
FONT_HEADER_LARGE = ("Roboto", 24, "bold")
FONT_BODY_BOLD = ("Roboto", 14, "bold")


class SelectorApp(ctk.CTk):
  """Main application for workload selection."""

  def __init__(self):
    super().__init__()
    self.title("Migration Planner Selector")
    self.geometry("400x250")
    self.configure(fg_color=COLOR_BACKGROUND)

    ctk.CTkLabel(
        self,
        text="Select Workload",
        font=FONT_HEADER_LARGE,
        text_color=COLOR_TEXT_MAIN,
    ).pack(pady=(30, 20))

    self.options = ["Exchange", "Files"]
    self.combobox = ctk.CTkComboBox(
        self,
        values=self.options,
        width=250,
        height=40,
        corner_radius=20,
        font=FONT_BODY_BOLD,
    )
    self.combobox.set("Exchange")  # Set default
    self.combobox.pack(pady=10)

    self.btn_launch = ctk.CTkButton(
        self,
        text="Launch",
        width=250,
        height=40,
        corner_radius=20,
        font=FONT_BODY_BOLD,
        fg_color=COLOR_PRIMARY,
        hover_color=COLOR_PRIMARY_HOVER,
        command=self.launch_selected,
    )
    self.btn_launch.pack(pady=10)

  def launch_selected(self):
    selection = self.combobox.get()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if selection == "Exchange":
      module_name = "ui.exchange_online_ui"
    elif selection == "Files":
      module_name = "ui.files_ui"
    else:
      return
    subprocess.Popen([sys.executable, "-m", module_name], cwd=current_dir)
    self.destroy()


if __name__ == "__main__":
  app = SelectorApp()
  app.mainloop()