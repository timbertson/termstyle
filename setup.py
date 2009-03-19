#!/usr/bin/env python

from setuptools import *

setup(
	name='termstyle',
	version='0.1',
	description='a dirt-simple terminal-colour library',
	author='Tim Cuthbertson',
	author_email='tim3d.junk+termstyle@gmail.com',
	url='http://github.com/gfxmonk/termstyle/tree',
	packages=find_packages(exclude=["test"]),
	
	long_description="""\
	termstyle is a simple library for adding coloured output to
	terminal (console) programs.
	
	Standard Usage:
	
		from termstyle import *
		print "%s:%s" % (red('Hey'), green('how are you?'))
		print blue('How ', bold('you'), ' doin?')
	
	or, you can use a colour just as a string
		print "%sBlue!%s" % (blue, reset)
	
	Styles:
		reset (no colour / style)

		# colour:
		black
		red
		green
		yellow
		blue
		magenta
		cyan
		white

		# background colour:
		bg_black
		bg_red
		bg_green
		bg_yellow
		bg_blue
		bg_magenta
		bg_cyan
		bg_white

		# weight:
		bold
		underscore
		inverted
	
	Controls:
		auto() - sets colouring on only if sys.stdout is a terminal
		disabe() - disable colours
		enable() - enable colours
	
	""",
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
