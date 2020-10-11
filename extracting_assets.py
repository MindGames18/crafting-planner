import zipfile
import os

def extracting_assets(version):

    script_dir = os.path.dirname(__file__)
    sub_dir = '\\jar'
    path_dir = "\\" + version + '.jar'
    abs_file_path = script_dir + sub_dir + path_dir
    ext_dir = script_dir + sub_dir
    archive = zipfile.ZipFile(abs_file_path)
    
    for file in archive.namelist():
        if file.startswith('assets'):
            archive.extract(file, ext_dir)