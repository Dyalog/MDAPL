"""
Preprocessing script to keep specified resources up to date.
"""

import os
import os.path
import shutil

MIGRATE_EXTS = (
    ".dws",
)

UPDATING = "updating... {}"
COPYING  = "copying.... {}"
FROM = "res"
NEWROOT = "book"

hits = 0

print(f"Migrating resources from `{FROM}` to `{os.path.join(NEWROOT, FROM)}`.")
for root, _, files in os.walk(FROM):
    newroot = os.path.join(NEWROOT, root)
    for filename in files:
        name, ext = os.path.splitext(filename)
        if ext.lower() not in MIGRATE_EXTS:
            continue
        # We want to migrate this file.
        if not os.path.exists(newroot):
            os.makedirs(newroot)
        fullpath = os.path.join(newroot, filename)
        oldpath = os.path.join(root, filename)
        exists = os.path.exists(fullpath)
        if (not exists or os.path.getmtime(oldpath) != os.path.getmtime(fullpath)):
            shutil.copy2(oldpath, fullpath)
            hits += 1
            if exists:
                print(UPDATING.format(oldpath))
            else:
                print(COPYING.format(oldpath))
print("finished... {} files modified.".format(hits))
