import os


def build_abs_local_path(path):
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, path.replace('./', '')).replace('\\', '/')