from pythonforandroid.recipes.python3 import Python3Recipe as BaseRecipe

class PatchedPython3Recipe(BaseRecipe):
    patches = [
        'patches/pyconfig_detection.patch',
        'patches/reproducible-buildinfo.diff',
        'patches/cpython-311-ctypes-find-library.patch',
        # 'patches/3.14_armv7l_fix.patch',  # removed
    ]

recipe = PatchedPython3Recipe()
