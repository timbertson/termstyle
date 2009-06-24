#!/usr/bin/env python

from setuptools import *

try:
	readme = open('readme.rst').read()
except StandardError:
	readme = 'see readme.rst'

setup(
	name='termstyle',
	version='0.1.5',
	description='a dirt-simple terminal-colour library',
	author='Tim Cuthbertson',
	author_email='tim3d.junk+termstyle@gmail.com',
	url='http://github.com/gfxmonk/termstyle/tree',
	packages=find_packages(exclude=["test"]),
	
	long_description=readme,
	classifiers=[
		"License :: OSI Approved :: BSD License",
		"Programming Language :: Python",
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
	],
	keywords='console ansi color colour terminal xterm',
	license='BSD',
	install_requires=[
		'setuptools',
	],
)
