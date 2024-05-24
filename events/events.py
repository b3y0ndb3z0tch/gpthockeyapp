import os
import json
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton


class EventScreen(Screen):
    def open_create_event_dialog(self):
        self.dialog = MDDialog(
            title="Create Event",
            type="custom",
            content_cls=EventDialogContent(),
            buttons=[
                MDRaisedButton(
                    text="CANCEL",
                    on_release=self.close_dialog
                ),
                MDRaisedButton(
                    text="CREATE",
                    on_release=self.create_event
                ),
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def create_event(self, *args):
        event_details = self.dialog.content_cls.ids
        event_name = event_details.event_name.text
        event_date = event_details.event_date.text
        event_start_time = event_details.event_start_time.text
        event_end_time = event_details.event_end_time.text

        event_data = {
            "event_name": event_name,
            "event_date": event_date,
            "event_start_time": event_start_time,
            "event_end_time": event_end_time
        }

        self.save_event(event_data)
        self.close_dialog()

    def save_event(self, event_data):
        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_events.json')

        if not os.path.exists(data_directory):
            os.makedirs(data_directory)

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                try:
                    events = json.load(f)
                except json.JSONDecodeError:
                    events = []
        else:
            events = []

        events.append(event_data)

        with open(file_path, 'w') as f:
            json.dump(events, f, indent=4)

        print(f"Event saved: {event_data}")


class EventDialogContent(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        return EventScreen()


if __name__ == '__main__':
    MainApp().run()
