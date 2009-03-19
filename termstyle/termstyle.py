#!/usr/bin/env python
import sys

class Style(object):
	prefix='\x1b['
	suffix='m'
	enabled = True
	
	def __init__(self, on_codes, off_codes = 0):
		self._on = self.sequence(on_codes)
		self._off = self.sequence(off_codes)
	
	def _get_on(self): return self._on if self.enabled else ''
	def _get_off(self): return self._off if self.enabled else ''
	on = property(_get_on)
	off = property(_get_off)
		
	@classmethod
	def sequence(cls, codes):
		wrap_single = lambda code: "%s%s%s" % (cls.prefix, code, cls.suffix)
		try:
			return ''.join([wrap_single(code) for code in codes])
		except TypeError:
			return wrap_single(codes)
			
	def __str__(self):
		if self.disabled:
			return ''
		return self.on
	
	def __call__(self, *args):
		contents = ''.join([self.on + str(arg) for arg in args])
		return "%s%s" % (contents, self.off)
		

def auto():
	"""set colouring on if STDOUT is a terminal device, off otherwise"""
	Style.enabled = sys.stdout.isatty()

def enable():
	"""force coloured output"""
	Style.enabled = True

def disable():
	"""disable coloured output"""
	Style.enabled = False
	
reset = Style(0)

black = Style(30)
red = Style(31)
green = Style(32)
yellow = Style(33)
blue = Style(34)
magenta = Style(35)
cyan = Style(36)
white = Style(37)

bg_black = Style(40)
bg_red = Style(41)
bg_green = Style(42)
bg_yellow = Style(43)
bg_blue = Style(44)
bg_magenta = Style(45)
bg_cyan = Style(46)
bg_white = Style(47)

bold = Style(1)
underscore = Style(2)
inverted = Style(7)

