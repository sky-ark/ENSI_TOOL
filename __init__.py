bl_info = {
    "name": "ENSI Tool Addon",
    "description": "A simple tool to export objects to RizomUV",
    "author": "Renaux Alexandre",
    "version": (0, 1, 0),
    "blender": (4, 2, 1),
    "category": "Import-Export",
    "location": "View3D > Sidebar",
    "doc_url": "https://github.com/sky-ark/ENSI_TOOL/tree/master",
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
