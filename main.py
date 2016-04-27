from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup 
from kivy.uix.label import Label
from kivy.lang import Builder
import abe1

#Loading the kv file with the Builder, it failed to load itself normally, so i have to force it
Builder.load_file('enginetable.kv')

#The home screen or Main screen
class HomeScreen(Screen):
    pass

#This screen lists all the departments available
class DepartmentsScreen(Screen):
    pass

#THis screen lists all the Level available
class Levels(Screen):
    pass

#Screen contains all the lecture days
class Days(Screen):
    pass

class DaySchedule(Screen):
    pass


#Screen Manager to name each screen
sm = ScreenManager()
sm.add_widget(HomeScreen(name='main'))
sm.add_widget(DepartmentsScreen(name='depts'))
sm.add_widget(Levels(name='levels'))
sm.add_widget(Days(name='days'))
sm.add_widget(abe1.Monday(name='abe1mon'))
sm.add_widget(DaySchedule(name='schedule'))


class EngineTableApp(App):
    def build(self):
        return sm
    
if __name__ == "__main__":
    EngineTableApp().run()