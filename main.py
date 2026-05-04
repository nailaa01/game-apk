from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class GameApp(App):
    def build(self):
        self.pilihan = ["Batu", "Gunting", "Kertas"]

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(text="Pilih salah satu!", font_size=24)
        layout.add_widget(self.label)

        for p in self.pilihan:
            btn = Button(text=p, font_size=20)
            btn.bind(on_press=self.main_game)
            layout.add_widget(btn)

        return layout

    def main_game(self, instance):
        komputer = random.choice(self.pilihan)
        player = instance.text

        if player == komputer:
            hasil = "SERI 🤝"
        elif (player == "Batu" and komputer == "Gunting") or \
             (player == "Gunting" and komputer == "Kertas") or \
             (player == "Kertas" and komputer == "Batu"):
            hasil = "MENANG 🎉"
        else:
            hasil = "KALAH 😢"

        self.label.text = f"Kamu: {player}\nKomputer: {komputer}\n{hasil}"

GameApp().run()
