import os, stat
import shutil

def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

def delete_assets() :
    script_dir = os.path.dirname(__file__)
    asset_dir = "\\jar\\assets"
    abs_dir_path = script_dir + asset_dir
    #os.remove(abs_dir_path)
    shutil.rmtree(abs_dir_path, onerror=remove_readonly)