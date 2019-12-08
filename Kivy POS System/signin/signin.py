from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_filed
        info = self.ids.info

        user_name = user.text
        password = pwd.text
        #Empty fields
        if user_name == "" or password == "":
            info.text = "[color=#FF0000]Username and/or password required![/color]"                
        else:
            #Correct info
            if user_name == "admin" and password == "mega":
                info.text = "[color=#00FF00]Logged in successfully!![/color]"
            #Wrong info
            else:
                info.text = "[color=#FF0000]Wrong combination of Username and Password, try again[/color]"

class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__ == "__main__":
    sa = SigninApp()
    sa.run()


