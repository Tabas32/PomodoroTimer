import time
from win10toast import ToastNotifier

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty

class PomodoroApp(App):
    def build(self):
        return TimerLayout()

class TimerLayout(FloatLayout):
    time = StringProperty()

    def onPress(self):
        startTime   = int(time.time())
        endTime     = startTime + 10#1500

        for i in range(10):
            self.time = str(i)
            time.sleep(1)

#toaster = ToastNotifier()
#toaster.show_toast("Pomodoro",
#              "Session started!",
#              duration=10)

#time.sleep(30)
#toaster.show_toast("Pomodoro",
#              "Session ended! Time to break.",
#              duration=10)
pomodoro = PomodoroApp()
pomodoro.run()


