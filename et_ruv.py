import bpy, math
import os
from bpy.utils import register_class, unregister_class
from subprocess import Popen
from os import system, path, makedirs


def get_ruv_export_path():
    _export_path = bpy.path.abspath('//') + bpy.context.preferences.addons[__package__].preferences.export_folder + '\\'
    if not path.exists(_export_path):
        makedirs(_export_path)
    return _export_path


def ruv_filename(self, context):
    _object_name = bpy.context.active_object.name
    _export_path = get_ruv_export_path()
    _export_file = _export_path + _object_name + '_ruv.fbx'

    if bpy.context.preferences.addons[__package__].option_save_before_export:
        bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)

    return _export_file


def ruv_fbx_export(self, context):
    _export_file = ruv_filename(self, context)
    prefs = bpy.context.preferences.addons[__package__].preferences
    bpy.ops.export_scene.fbx(filepath=_export_file, use_selection=True, axis_forward=prefs.forward_axis,
                             axis_up=prefs.up_axis,  filter_glob="*.fbx", global_scale=1.0, apply_unit_scale=True,
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
    bl_label = "RizomUV"
    bl_description = "Export the selected object to RizomUV"

    def execute(self, context):
        _export_file = ruv_fbx_export(self, context)
        _rizom_path = bpy.context.preferences.addons[__package__].preferences.rizom_path

        Popen([_rizom_path, _export_file])
        return {'FINISHED'}

#class ruv_import(bpy.types.Operator):

classes = (
    ruv_fbx_export_execute,
    ruv_fbx_export,
)
def register():
    for cls in classes:
        register_class(cls)

def unregister():
    for cls in reversed(classes):
        unregister_class(cls)