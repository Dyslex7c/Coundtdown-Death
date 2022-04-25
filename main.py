from random import randint
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader

years = randint(0, 100)
days = randint(0, 364)
hours = randint(0, 23)
minutes = randint(0, 59)
seconds = randint(0, 59)
time_difference = 0


class Layout(BoxLayout):
    pass


class MyPopup(BoxLayout):
    pass


tmp = SoundLoader.load('countdown.mp3')
tmp.play()


class ClockLabel(Label):
    def __init__(self, **kwargs):
        super(ClockLabel, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        global hours, minutes, seconds, years, days, time_difference
        time_difference += 1
        if int(hours) < 10 and len(str(hours)) == 1:
            hours = '0' + str(hours)
        if int(minutes) < 10 and len(str(minutes)) == 1:
            minutes = '0' + str(minutes)
        if int(seconds) < 10 and len(str(seconds)) == 1:
            seconds = '0' + str(seconds)
        self.text = f"{('{years}yrs {days}d, {hours}:{minutes}:{seconds}'.format(years=years, days=days, hours=hours, minutes=minutes, seconds=seconds))}"
        seconds = int(seconds) - 1
        if seconds < 0:
            minutes = int(minutes) - 1
            seconds = 59
        if int(minutes) < 0:
            hours = int(hours) - 1
            minutes = 59
        if int(hours) < 0:
            days = int(days) - 1
            hours = 23
        if int(days) < 0:
            years = int(years) - 1
            days = 364
        if int(years) < 0:
            self.text = "Congrats! You've made it to the end!"
            end_screen()
        if time_difference == 10:
            tmp.play()
            time_difference = 0


class CountdownDeathApp(App):
    def build(self):
        return Layout()


def end_screen():
    end = Popup(
        title="Congrats! You've made it to the end! Thank you for enduring with us for such a plethora of time!\n\nBased on a 2019 American supernatural horror film called 'Countdown' directed and written by Justin Dec")
    end.open()


clock = CountdownDeathApp()
clock.run()
