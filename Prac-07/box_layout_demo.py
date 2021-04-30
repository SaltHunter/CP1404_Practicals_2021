from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Boxlayoutdemo is an app which is used to greet the user"""
    def build(self):
        """Build the GUI"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle Greeting"""
        print('greet')
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        """Handle Clearing of user input"""
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
