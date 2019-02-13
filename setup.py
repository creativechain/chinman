from setuptools import setup

import shutil
import os

setup(name="chinman",
      version          = __import__('chinman').__version__,
      description      = "Testnet management scripts.",
      url              = "https://github.com/creativechain/chinman",
      author           = "Creary",
      packages         = ["chinman", "simple_crea_client"],
      install_requires = ["flask", "wtforms"],
      entry_points     = {"console_scripts" : [
                          "chinman=chinman.main:sys_main",
                         ]}
    )

template_source = 'templates'
template_target = '/tmp/chinman-templates'
static_source = 'static'
static_target = '/tmp/chinman-static'

if os.path.exists(template_target):
    shutil.rmtree(template_target)

shutil.copytree(template_source, template_target)

if os.path.exists(static_target):
    shutil.rmtree(static_target)

shutil.copytree(static_source, static_target)
