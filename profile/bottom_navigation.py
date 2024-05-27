from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.properties import ObjectProperty

class MDBottomNavigationCustom(MDBottomNavigation):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class BottomNavigationItemStickhand(MDBottomNavigationItem):
    def on_tab_press(self):
        self.screen_manager.current = 'profile_stickhand'

class BottomNavigationItemForward(MDBottomNavigationItem):
    def on_tab_press(self):
        self.screen_manager.current = 'profile_forward'

class BottomNavigationItemDefense(MDBottomNavigationItem):
    def on_tab_press(self):
        self.screen_manager.current = 'profile_defense'

class BottomNavigationItemGoalie(MDBottomNavigationItem):
    def on_tab_press(self):
        self.screen_manager.current = 'profile_goalie'
