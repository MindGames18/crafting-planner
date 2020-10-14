import zipfile
import constants
import os
import stat
import shutil
import PIL.Image
import io
import base64
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


def convert_to_bytes(file_or_bytes, resize=None):
    '''
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    '''
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize(
            (128, 128), resample=PIL.Image.NEAREST)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()
