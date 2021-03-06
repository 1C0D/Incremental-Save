bl_info = {
    "name": "Incremental Save",
    "author": "1COD",
    "version": (1, 1, 0),
    "blender": (2, 80, 0),
    "location": "File menu",
    "warning": "",
    "description": "'Incremental Save', in F3 menu, assign shortcut from there",
    "category": "Developement"
}

"""
Read this:

search 'Incremental Save' in F3 menu, assign Ctrl+Alt+S shortcut, save your prefs

when the blend is not saved, it's doing a normal "save as": e.g:mysave.blend   
after, it will search the higher incrementation in this dir and increment of 1 > mysave1.blend
but if you had a higher incrementation, e.g mysave5.blend > mysave6.blend
if you physically delete files, after having saved, in the same session, it will get back to mysave.blend
if you want a new name, use the normal save as (ctrl+shift+S)    
"""

import bpy
import os
from itertools import takewhile

class Incremental_OP_save(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "wm.save_incremental"
    bl_label = "Incremental Save"

    def execute(self, context):

        if not bpy.data.is_saved:   #if not saved file
            bpy.ops.wm.save_as_mainfile('INVOKE_DEFAULT')
            return {'FINISHED'}

        #save incremental
        file = bpy.data.filepath
        ext_name= os.path.basename(file)
        name= os.path.splitext(ext_name)[0] #name without extension

        version=""
        letters=""        
        version = ''.join(list(takewhile(lambda c: c.isdigit(), name[::-1])))
        letters = name[:-len(version)] if version else name

        dir_name=os.path.dirname(file)
        same_name_list = [os.path.splitext(item)[0] #find higher incremented instances in dir
                            for item in sorted(os.listdir(dir_name)) 
                                if item.endswith('.blend') and letters in item]
        if same_name_list:
            version=""
            version = ''.join(list(takewhile(lambda c: c.isdigit(), name[::-1])))        
            if version:
                inc_version=int(version)+1 #increment the version
            else:
                inc_version=1
            inc_name=letters+str(inc_version)+".blend" #final name file
        else:
            inc_name=letters+".blend" #if no increment file before, add 1

        incrementedFile = os.path.join(dir_name, inc_name)
        bpy.ops.wm.save_as_mainfile(filepath=incrementedFile) #save as with the new path

        textReport = "Saved "+repr(inc_name)
        self.report({'INFO'},textReport)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(Incremental_OP_save)

def unregister():
    bpy.utils.unregister_class(Incremental_OP_save)

