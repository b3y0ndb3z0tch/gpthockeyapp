# profile/profile.py
# This file defines the ProfileScreen class used for managing the user profile.
# It includes methods for loading and saving profile data to a JSON file.

from kivy.uix.screenmanager import Screen  # Import Screen from Kivy
from kivy.properties import StringProperty  # Import StringProperty for managing string properties
import json  # Import JSON module for reading and writing JSON files
import os  # Import OS module to handle file paths

class ProfileScreen(Screen):  # Define the ProfileScreen class inheriting from Screen
    position = StringProperty('')  # Define a StringProperty to hold the position
    shooting_hand = StringProperty('')  # Define a StringProperty to hold the shooting hand
    height = StringProperty('')  # Define a StringProperty to hold the height
    weight = StringProperty('')  # Define a StringProperty to hold the weight
    age = StringProperty('')  # Define a StringProperty to hold the age
    experience_level = StringProperty('')  # Define a StringProperty to hold the experience level
    preferred_rinks = StringProperty('')  # Define a StringProperty to hold the preferred rinks
    favorite_team = StringProperty('')  # Define a StringProperty to hold the favorite team
    biography = StringProperty('')  # Define a StringProperty to hold the biography

    def on_enter(self):
        """
        This method is called when the screen is entered.
        It loads the user profile data from the JSON file.
        """
        user_data = self.load_user_data()
        if user_data:
            self.position = user_data.get('position', '')
            self.shooting_hand = user_data.get('shooting_hand', '')
            self.height = user_data.get('height', '')
            self.weight = user_data.get('weight', '')
            self.age = user_data.get('age', '')
            self.experience_level = user_data.get('experience_level', '')
            self.preferred_rinks = user_data.get('preferred_rinks', '')
            self.favorite_team = user_data.get('favorite_team', '')
            self.biography = user_data.get('biography', '')

    def save_profile(self):
        """
        Save the user profile data to a JSON file.
        """
        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        os.makedirs(data_directory, exist_ok=True)
        file_path = os.path.join(data_directory, 'user_data.json')

        # Load existing data
        user_data = self.load_user_data() or {}

        # Update with profile data
        user_data['position'] = self.position
        user_data['shooting_hand'] = self.shooting_hand
        user_data['height'] = self.height
        user_data['weight'] = self.weight
        user_data['age'] = self.age
        user_data['experience_level'] = self.experience_level
        user_data['preferred_rinks'] = self.preferred_rinks
        user_data['favorite_team'] = self.favorite_team
        user_data['biography'] = self.biography

        # Write data back to file
        with open(file_path, 'w') as f:
            json.dump(user_data, f)

    def load_user_data(self):
        """
        Load user data from the JSON file.
        """
        data_directory = os.path.join(os.path.dirname(__file__), '../data')
        file_path = os.path.join(data_directory, 'user_data.json')

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return None
        return None
