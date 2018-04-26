from PluginManager import Model_MenuObj, Model_ToolBarObj

class Plugin1(Model_MenuObj):
    def __init__(self):
        pass

    def Start(self):
        print("I am plugin1 , I am a menu!")

class Plugin2(Model_ToolBarObj):
    def __init__(self):
        pass

    def Start(self):
        print("I am plugin2 , I am a ToolBar!")