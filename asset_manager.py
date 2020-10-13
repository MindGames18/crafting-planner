import zipfile
import constants
import os
import stat
import shutil

'''
    All the Assets Related methods go here
'''


def extracting_assets(version):

    path_dir = "\\" + version + '.jar'

    abs_file_path = constants.script_dir + constants.jar_dir + path_dir
    ext_dir = constants.script_dir + constants.jar_dir

    archive = zipfile.ZipFile(abs_file_path)

    for file in archive.namelist():
        if file.startswith('assets'):
            archive.extract(file, ext_dir)


def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)


def delete_assets():
    asset_dir = "\\jar\\assets"
    abs_dir_path = constants.script_dir + asset_dir
    # os.remove(abs_dir_path)
    shutil.rmtree(abs_dir_path, onerror=remove_readonly)
