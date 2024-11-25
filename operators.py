import bpy
import os
from subprocess import Popen
from os import path, makedirs

def get_ruv_export_path():
    export_folder = bpy.context.preferences.addons[__package__].preferences.export_folder
    if not export_folder:
        self.report({'ERROR'}, "Export folder is not set.")
        return None

    _export_path = bpy.path.abspath(export_folder)
    if not path.exists(_export_path):
        makedirs(_export_path)
    return _export_path

def ruv_filename(self, context):
    _object_name = bpy.context.active_object.name
    _export_path = get_ruv_export_path()
    if not _export_path:
        return None

    _export_file = os.path.join(_export_path, _object_name + '_ruv.fbx')

    if bpy.context.preferences.addons[__package__].preferences.save_before_export:
        if not bpy.data.is_saved:
            self.report({'ERROR'}, "Please save the file before exporting.")
            return None
        try:
            bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
        except Exception as e:
            self.report({'ERROR'}, f"Failed to save the file: {e}")
            return None

    return _export_file

def ruv_fbx_export(self, context):
    _export_file = ruv_filename(self, context)
    if not _export_file:
        return None

    prefs = bpy.context.preferences.addons[__package__].preferences
    bpy.ops.export_scene.fbx(filepath=_export_file, use_selection=True, axis_forward=prefs.forward_axis,
                             axis_up=prefs.up_axis, filter_glob="*.fbx", global_scale=1.0, apply_unit_scale=True,
                             bake_space_transform=False, object_types={'MESH'}, use_mesh_modifiers=True,
                             mesh_smooth_type='OFF', use_mesh_edges=False, use_tspace=False, use_custom_props=False,
                             add_leaf_bones=False, primary_bone_axis='Y', secondary_bone_axis='X',
                             use_armature_deform_only=False, bake_anim=True, bake_anim_use_all_bones=True,
                             bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True,
                             bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0,
                             path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True,
                             use_metadata=True)
    return _export_file

class ruv_fbx_export_execute(bpy.types.Operator):
    bl_idname = "et_ruv.export"
    bl_label = "RizomUVexport"
    bl_description = "Export the selected object to RizomUV"

    def execute(self, context):
        _export_file = ruv_fbx_export(self, context)
        if not _export_file:
            return {'CANCELLED'}

        _rizom_path = bpy.context.preferences.addons[__package__].preferences.rizom_path

        try:
            Popen([_rizom_path, _export_file])
        except Exception as e:
            self.report({'ERROR'}, f"Failed to open RizomUV: {e}")
            return {'CANCELLED'}

        return {'FINISHED'}

class ruv_fbx_import(bpy.types.Operator):
    bl_idname = "et_ruv.import"
    bl_label = "RizomUVimport"
    bl_description = "Import from RizomUV"

    def execute(self, context):
        obj_selected = bpy.context.object
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
        prefs = bpy.context.preferences.addons[__package__].preferences
        bpy.ops.import_scene.fbx(filepath=ruv_filename(self, context))

        obj_imported = bpy.context.selected_objects[0]

        obj_imported.select_set(True)
        obj_selected.select_set(True)
        bpy.context.view_layer.objects.active = obj_imported

        bpy.ops.object.join_uvs()

        obj_selected.select_set(False)

        bpy.ops.object.delete()

        bpy.context.view_layer.objects.active = obj_selected
        obj_selected.select_set(True)

        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        bpy.ops.uv.seams_from_islands(mark_seams=True, mark_sharp=False)
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(ruv_fbx_export_execute)
    bpy.utils.register_class(ruv_fbx_import)

def unregister():
    bpy.utils.unregister_class(ruv_fbx_export_execute)
    bpy.utils.unregister_class(ruv_fbx_import)