# Incremental-Save
to do incremental .blend saves

search 'Incremental Save' in F3 menu, assign Ctrl+Alt+S shortcut, save your prefs

when the blend is not saved, it's doing a normal "save as": e.g:mysave.blend   
after, it will search the higher incrementation in this dir and increment of 1 > mysave1.blend   
but if you had a higher incrementation, e.g mysave5.blend > mysave6.blend   
if you physically delete files, after having saved, in the same session, it will get back to mysave.blend   
if you want a new name, use the normal save as (ctrl+shift+S)    
