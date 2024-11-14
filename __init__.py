bl_info = {
    "name": "ENSI Tool Addon",
    "author": "Renaux Alexandre",
    "version": (0, 1, 0),
    "blender": (4, 2, 1),
    "category": "Object",
}

import bpy
from . import operators, panels, preferences

def register():
    operators.register()
    panels.register()
    preferences.register()

def unregister():
    operators.unregister()
    panels.unregister()
    preferences.unregister()

if __name__ == "__main__":
    register()
