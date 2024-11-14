﻿import bpy

class VIEW3D_PT_ensi_tool(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "ENSI Tool"
    bl_category = "ENSI Tool"

    def draw(self, context):
        layout = self.layout
        prefs = context.preferences.addons[__package__].preferences
        layout.prop(prefs, "rizom_path")
        layout.prop(prefs, "export_folder")
        layout.prop(prefs, "forward_axis")
        layout.prop(prefs, "up_axis")
        row = layout.row()
        row.operator("et_ruv.export", text="Export to RizomUV")
        row = layout.row()
        row.operator("wm.url_open", text="Infos").url = "https://github.com/Ecole-des-Nouvelles-Images"

def register():
    bpy.utils.register_class(VIEW3D_PT_ensi_tool)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_ensi_tool)