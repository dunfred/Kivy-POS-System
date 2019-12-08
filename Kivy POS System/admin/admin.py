from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):    
        super().__init__(**kwargs)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    def validate_and_run(self):
        username    = self.ids.username
        password    = self.ids.password
        course_link = self.ids.link
        info        = self.ids.head_info

        print(f"username {username.text}")
        print(f"password {password.text}")
        print(f"course_link {course_link.text}")
        print(f"info {info.text}")
        #Check if user wants to login using google account
        if self.ids.google.active == True:
            Google_mode = True
        else:
            Google_mode = False

        #Check if user has filled every field
        if username.text == "" or password.text == "" or course_link.text == "":
            info.text = "[color=ff3333]Please fill all fileds![/color]"
        else:
            info.text = "[color=00ee00]Successfully Validated[/color]"
            runtime_object = Automator(username.text, password.text, course_link.text, google_login_mode=Google_mode)
            runtime_object.goSkip()
    
    def exit(self):
        #App.get_running_app.stop()
        Window.close()

class AdminApp(App):
    def build(self):
        return AdminWindow()

if __name__ == "__main__":
    AdminApp().run()
