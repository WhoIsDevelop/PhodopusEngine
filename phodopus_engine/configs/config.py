
class ConfigEngine:
    def __init__(self):
        self.debug = ConfigDebug()
        self.interface = ConfigInterface()
        self.render = ConfigRender()
        self.project = ConfigProject()
        self.inputs = ConfigInputs()

class ConfigDebug:
    def __init__(self):
        self.show_type = 1 # 0 - none, 1 - with main graphic, 2 - only debug graphic
        self.show_fps = True
        self.show_text = False
        self.show_objects = False
        self.show_static = False
        self.show_sprites = False

class ConfigRender:
    def __init__(self):
        self.render_type = 0 # 0 - pygame
        self.width = 800
        self.height = 600
        self.postprocessing_enabled = True
        self.max_fps = False
        self.MAX_FPS = 240


class ConfigProject:
    def __init__(self):
        self.window_name = 'Phodopus Engine'


class ConfigInputs:
    def __init__(self):
        self.enabled = True

class ConfigInterface:
    def __init__(self):
        self.enabled = True
        self.visible = True