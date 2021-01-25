import bpy

bl_info = {
    "name": "sample addon",
    "author": "ymg",
    "version": (1,0),
    "blender": (2,91,2),
    "location": "",
    "description": "firstcommit",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

def register():
    print("sample addon was enabled")

def unregister():
    print("sample addon was disable")

if __name__ == "__main__":
    register()