from pythonforandroid.recipe import CythonRecipe

class PyjniusRecipe(CythonRecipe):
    version = '1.6.1'
    url = 'https://github.com/kivy/pyjnius/archive/{version}.zip'
    name = 'pyjnius'
    depends = ['python3']
    call_hostpython_via_targetpython = False
    cython_directives = {'language_level': '3'}

recipe = PyjniusRecipe()
