import bpy

class EnsiToolPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

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

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "rizom_path")
        layout.prop(self, "export_folder")
        layout.prop(self, "save_before_export")
        layout.prop(self, "forward_axis")
        layout.prop(self, "up_axis")

def register():
    bpy.utils.register_class(EnsiToolPreferences)

def unregister():
    bpy.utils.unregister_class(EnsiToolPreferences)
