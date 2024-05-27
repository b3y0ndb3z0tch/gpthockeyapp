from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.app import MDApp

class MDBottomNavigationCustom(MDBottomNavigation):
    pass

class BottomNavigationItemStickhand(MDBottomNavigationItem):
    def on_tab_press(self):
        app = MDApp.get_running_app()
        app.root.ids.screen_manager.current = 'profile_stickhand'

class BottomNavigationItemForward(MDBottomNavigationItem):
    def on_tab_press(self):
        app = MDApp.get_running_app()
        app.root.ids.screen_manager.current = 'profile_forward'

class BottomNavigationItemDefense(MDBottomNavigationItem):
    def on_tab_press(self):
        app = MDApp.get_running_app()
        app.root.ids.screen_manager.current = 'profile_defense'

class BottomNavigationItemGoalie(MDBottomNavigationItem):
    def on_tab_press(self):
        app = MDApp.get_running_app()
        app.root.ids.screen_manager.current = 'profile_goalie'
