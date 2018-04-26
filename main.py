import sys
from plugin_manager import PluginManager
from plugin_manager import __ALLMODEL__

if __name__ == '__main__':
    PluginManager.LoadAllPlugin()

    for SingleModel in __ALLMODEL__:
        plugins = SingleModel.GetPluginObject()
        for item in plugins:
            item.Start()