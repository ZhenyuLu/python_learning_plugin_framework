from PluginManager import Model_ParamPanelObj, Model_Component

class Plugin3(Model_ParamPanelObj):
    def __init__(self):
        pass

    def Start(self):
        print("I am plugin3 , I am a ParamPanel!")


class Plugin4(Model_Component):
    def __init__(self):
        pass

    def Start(self):
        print("I am plugin4 , I am a Component!")