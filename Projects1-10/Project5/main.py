from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
Builder.load_file("design.kv")
from pathlib import Path
import random 
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


# Classes with the same names as the kivy file classes

class LoginScreen(Screen):

    def forgot_password(self):
        self.manager.current = "forgot_password_screen"

    def sign_up(self):
        self.manager.current = "sign_up_screen"
        self.ids.log_in_wrong.text = ""
    

    def check_user(self, usr, pas):
        with open("users.json") as file:
            users = json.load(file)
            if usr in users and users[usr]["password"] == pas:
                self.log_in()
            else: 
                self.ids.log_in_wrong.text = "Wrong username or password"

    def log_in(self):
        self.manager.current = "login_screen_success"
        self.ids.log_in_wrong.text = ""

class SignUpScreen(Screen):

    def add_user(self, usr, pas):
        
        with open("users.json") as file:
            users = json.load(file)

        users[usr] = {'username': usr, 'password': pas, 'created': datetime.now().strftime("%Y-%m-%d %H-%m-%S") }

        with open("users.json", "w") as file:
            json.dump(users, file)
        self.manager.transition.direction = "right"
        self.manager.current = "submit_screen"
    
    def go_back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class SubmitScreen(Screen):

    def go_back(self):
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):

    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    
    def display_quote(self, inp):
        inp = inp.lower()
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]   
        if inp in available_feelings:
            for feel in available_feelings:
                with open(f"quotes/{feel}.txt") as file:
                    quotes = file.readlines()
                    self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Choose a different feeling"

class ForgotPasswordScreen(Screen):
    def go_back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    
    def display_password(self, usr):
        with open("users.json") as file:
            users = json.load(file)
            if usr in users: #fixa input här
                pword = users[usr]["password"]
                self.ids.newpassword.text = f"The user: {usr} has the password: {pword}"
            else: 
                self.ids.newpassword.text = "We found no such user"

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

class ImageButton (ButtonBehavior, HoverBehavior, Image):
    pass
if __name__ == "__main__":
    MainApp().run()

