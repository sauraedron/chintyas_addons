# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#  Contributors : Saurabh Wankhade
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Chintya's Tools",
    "author": "Saurabh Wankhade",
    "version": (0, 1, 1),
    "blender": (2, 70),
    "description": "Easing workflow",
    "warning": "",
    "category": "3D View"}
import bpy


class CTon(bpy.types.Operator):
    """Chintya's tools"""      
    bl_idname = "toggle.on"    
    bl_label = "Toggle Hair on"
    bl_options = {'REGISTER'}  

    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.visible_objects
        object = bpy.ops.object
        for obj in selected:
            scene.objects.active =obj
            for mod in obj.modifiers:
                if mod.type == "PARTICLE_SYSTEM":
                    mod.show_viewport = True

        return {'FINISHED'}
    
class CToff(bpy.types.Operator):
    """Chintya's tools"""      
    bl_idname = "toggle.off"    
    bl_label = "Toggle Hair off"
    bl_options = {'REGISTER'}  

    def execute(self, context):        
        scene = bpy.context.scene
        selected = bpy.context.visible_objects
        object = bpy.ops.object


        for obj in selected:
            scene.objects.active =obj
            for mod in obj.modifiers:
                if mod.type == "PARTICLE_SYSTEM":
                    mod.show_viewport = False

        return {'FINISHED'}

class DrawPanel(bpy.types.Panel):
    bl_label = "Chintya's panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Hair Togglers")
        split = layout.split()
        col = split.column()
        col.operator("toggle.on",text="Viewport ON")
        col.operator("toggle.off",text="Viewport OFF")

def register():
    bpy.utils.register_class(DrawPanel)
    bpy.utils.register_class(CToff)
    bpy.utils.register_class(CTon)
    

def unregister():
    bpy.utils.unregister_class(CTon)
    bpy.utils.unregister_class(CToff)
    bpy.utils.unregister_class(DrawPanel)



if __name__ == "__main__":
    register()








                         

