import sys
from kivy.app import App
from fivearow import *

class TouchInput(main):
    def on_touch_down(self, touch):
        print(touch)

class fivearow(main):
    def build(slef):
        return TouchInput()

if _name_ == "__main__":
    fivearow.main()