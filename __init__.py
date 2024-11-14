# Informations sur l'add-on
bl_info = {
    "name": "ENSI Tool Addon",
    "author": "Renaux Alexandre",
    "version": (0, 1, 0),
    "blender": (4, 2, 1),
    "location": "View3D > Sidebar > ENSI Tool",
    "tracker_url": "https://github.com/Ecole-des-Nouvelles-Images",
    "category": "Import-Export",
}


# Importation des modules nécessaires

import bpy
import os
from bpy.utils import register_class, unregister_class
from . import et_ruv



# Classe pour les préférences de l'add-on
class EnsiToolPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    # Propriété pour stocker le chemin d'accès à RizomUV
    rizom_path: bpy.props.StringProperty(
        name="Rizom Path",
        subtype="FILE_PATH",
        description="Path to the RizomUV executable"
    )

    export_folder: bpy.props.StringProperty(
        name="Export Folder",
        subtype="DIR_PATH",
        description="Path to the export folder"
    )

    save_before_export: bpy.props.BoolProperty(
        name="Save Before Export",
        description="Save the file before exporting",
        default=True
    )

    forward_axis: bpy.props.EnumProperty(
        name="Forward Axis",
        description="Forward axis for the FBX export",
        items=[
            ("X", "X", "X"),
            ("Y", "Y", "Y"),
            ("Z", "Z", "Z"),
            ("-X", "-X", "-X"),
            ("-Y", "-Y", "-Y"),
            ("-Z", "-Z", "-Z"),
        ],
        default="-Z"
    )
    # Ajouter une propriété pour l'axe up
    up_axis: bpy.props.EnumProperty(
        name="Up Axis",
        description="Up axis for the FBX export",
        items=[
            ("X", "X", "X"),
            ("Y", "Y", "Y"),
            ("Z", "Z", "Z"),
            ("-X", "-X", "-X"),
            ("-Y", "-Y", "-Y"),
            ("-Z", "-Z", "-Z"),
        ],
        default="Y"
    )

    # Méthode pour dessiner l'interface des préférences
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "rizom_path")
        layout.prop(self, "export_folder")
        layout.prop(self, "save_before_export")
        layout.prop(self, "forward_axis")
        layout.prop(self, "up_axis")


# Classe pour le panneau personnalisé
class VIEW3D_PT_ensi_tool(bpy.types.Panel):
    bl_space_type = "VIEW_3D"  # Dans la zone de la vue 3D
    bl_region_type = "UI"  # Dans la région de la barre latérale
    bl_label = "ENSI Tool"  # Titre du panneau
    bl_category = "ENSI Tool"  # Catégorie du panneau

    # Méthode pour dessiner l'interface du panneau
    def draw(self, context):
        layout = self.layout
        prefs = context.preferences.addons[__name__].preferences
        layout.prop(prefs, "rizom_path")
        layout.prop(prefs, "export_folder")
        layout.prop(prefs, "forward_axis")
        layout.prop(prefs, "up_axis")
        row = layout.row()
        row.operator("et_ruv.export", text="Export to RizomUV")
        row = layout.row()
        row.operator("wm.url_open", text="Infos").url = "https://github.com/Ecole-des-Nouvelles-Images"


# Fonction pour enregistrer les classes de l'add-on
def register():
    bpy.utils.register_class(EnsiToolPreferences)
    bpy.utils.register_class(VIEW3D_PT_ensi_tool)
    bpy.types.Scene.rizom_path = bpy.props.StringProperty(
        name="Rizom Path",
        subtype="FILE_PATH",
        description="Path to the RizomUV executable"
    )


# Fonction pour désenregistrer les classes de l'add-on
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_ensi_tool)
    bpy.utils.unregister_class(EnsiToolPreferences)
    del bpy.types.Scene.rizom_path


# Point d'entrée principal du script
if __name__ == "__main__":
    register()
