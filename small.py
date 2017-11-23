from kivy.clock import Clock
import threading
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
    toaster = ToastNotifier()

    def __inti__(self, **kwargs):
        super(TimerLayout, self).__init__(**kwargs)
        Clock.shedule_interval(self.stopWatch, .1)
        self.stopWatch(0)
        self.endTime = 0

    def onPress(self):
        startTime   = int(time.time())
        self.endTime     = startTime + 1500
        
        Clock.unschedule(self.stopWatch)
        Clock.schedule_interval(self.stopWatch, .1)

    def stopWatch(self, dt):
        timeLeft = int(self.endTime - time.time())
        self.time = str(self.parseTime(timeLeft))

        if(timeLeft == 0):
            Clock.unschedule(self.stopWatch)
            t = threading.Thread(target = self.toaster.show_toast,
                    args = ("Pomodoro",
                    "Session ended! Time to break.",
                    "stopwatch.ico",
                    10))
            t.start()

    def parseTime(self, seconds):
        minutes = seconds // 60
        secLeft = seconds % 60

        return str(minutes) + ":" + str(secLeft)

pomodoro = PomodoroApp()
pomodoro.run()


