import shutil
from distutils.core import setup
from distutils.cmd import Command
from distutils.extension import Extension

from setuptools import setup, find_packages
from os.path import join
import os

import py2app
from py2app.build_app import py2app

APP = [os.path.join('apaf', 'run.py')]
APP_ICO = os.path.join(os.getcwd(), 'vidalia.icns')
class APAFClean(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print "Removing old build directory..."
        try:
            shutil.rmtree('build')
        except:
            pass
        print "Removing old dist directory..."
        try:
            shutil.rmtree('dist')
        except:
            pass

class APAFBuild(py2app):
    description = "Creates an OSX installation of APAF"

    user_options = py2app.user_options

    boolean_options = py2app.boolean_options

    def setup_distribution(self):
        self.distribution.app = APP
        #self.distribution.ext_modules = list()
        #self.distribution.ext_modules.append()
        self.iconfile = APP_ICO

    def finalize_options(self):
        py2app.finalize_options(self)
        self.setup_distribution()

    def run(self):
        print "Building APAF application!"
        py2app.run(self)


# static files
DATA_FILES = [(root, [join(root, file) for file in files])
              for root, _, files in os.walk(join('apaf', 'panel', 'static'))]
# binary files
DATA_FILES += [(root, [join(root, file) for file in files])
               for root, _, files in os.walk(join('contrib'))]


OPTIONS_PY2APP = dict(
    argv_emulation = True,
#    modules=['_psutil_osx'],
)

OPTIONS_PY2EXE = dict(
    packages = 'twisted.web'
)



setup( app=APP,
        data_files=DATA_FILES,
        options=dict(py2app=OPTIONS_PY2APP,
                 py2exe=OPTIONS_PY2EXE,
        ),
        packages=find_packages(),
        cmdclass={
          'clean': APAFClean,
          'py2app': APAFBuild
          } )

