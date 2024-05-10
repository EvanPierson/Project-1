import tkinter as tk
from logic import *


class GUI:
    def __init__(self) -> None:
        """
        Creates the GUI application that is to be used
        """
        self.tv = Television()

        self.window = tk.Tk()
        self.window.title("TV Remote")

        self.power_button = tk.Button(self.window, text="Power", command=self.toggle_power)
        self.power_button.pack()

        self.channel_label = tk.Label(self.window, text="Channel: ")
        self.channel_label.pack()

        self.volume_label = tk.Label(self.window, text="Volume: ")
        self.volume_label.pack()

        self.channel_up_button = tk.Button(self.window, text="Channel Up", command=self.channel_up)
        self.channel_up_button.pack()

        self.channel_down_button = tk.Button(self.window, text="Channel Down", command=self.channel_down)
        self.channel_down_button.pack()

        self.volume_up_button = tk.Button(self.window, text="Volume Up", command=self.volume_up)
        self.volume_up_button.pack()

        self.volume_down_button = tk.Button(self.window, text="Volume Down", command=self.volume_down)
        self.volume_down_button.pack()

        self.mute_button = tk.Button(self.window, text="Mute", command=self.toggle_mute)
        self.mute_button.pack()

        self.update_labels()

    def toggle_power(self) -> None:
        """
        Function used to turn on and off the remote
        """
        self.tv.power()
        self.update_labels()

    def toggle_mute(self) -> None:
        """
        Function used to set the volume to zero
        """
        self.tv.mute()
        self.update_labels()

    def channel_up(self) -> None:
        """
        Function used to increase the channel label
        """
        self.tv.channel_up()
        self.update_labels()

    def channel_down(self) -> None:
        """
        Function used to decrease the channel label
        """
        self.tv.channel_down()
        self.update_labels()

    def volume_up(self) -> None:
        """
        Function used to increase the volume label
        """
        self.tv.volume_up()
        self.update_labels()

    def volume_down(self) -> None:
        """
        Function used to decrease the volume label
        """
        self.tv.volume_down()
        self.update_labels()

    def update_labels(self) -> str:
        """
        Function used to update all the labels as well as disable the buttons when power is False
        """
        self.channel_label.config(text=f"Channel: {self.tv._Television__channel}")
        self.volume_label.config(text=f"Volume: {self.tv._Television__volume}")

        if self.tv._Television__muted:
            self.volume_label.config(text=f"Volume: {Television.MIN_VOLUME} (Muted)")

        # Disable all buttons except the power button
        if self.tv._Television__status:
            self.channel_up_button.config(state=tk.NORMAL)
            self.channel_down_button.config(state=tk.NORMAL)
            self.volume_up_button.config(state=tk.NORMAL)
            self.volume_down_button.config(state=tk.NORMAL)
            self.mute_button.config(state=tk.NORMAL)
        else:
            self.channel_up_button.config(state=tk.DISABLED)
            self.channel_down_button.config(state=tk.DISABLED)
            self.volume_up_button.config(state=tk.DISABLED)
            self.volume_down_button.config(state=tk.DISABLED)
            self.mute_button.config(state=tk.DISABLED)

    def run(self) -> None:
        """
        Function that runs the application
        """
        self.window.mainloop()


tv_remote_gui = GUI()
tv_remote_gui.run()
