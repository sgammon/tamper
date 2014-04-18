# -*- coding: utf-8 -*-

'''

  tamper for python: setup

'''

# stdlib + setuptools
import os, setuptools

# package
import tamper, tamper.packs, test_tamper


setuptools.setup(name="tamper",
      version=".".join(map(unicode, tamper.__version__)),
      author=" ".join(tamper.__author__.split(" ")[0:-1]),
      author_email=tamper.__author__.split(" ")[-1].replace('<', '').replace('>', ''),
      packages=(tamper.__name__, tamper.packs.__name__, test_tamper.__name__),
      scripts=["tamp"],
      tests_require=["nose", "coverage"],
      description="Tamper is a serialization protocol for categorical data. It allows you to quickly and efficently transfer bulk datasets from server to browser.",
      url="https://github.com/sgammon/tamper"
)
