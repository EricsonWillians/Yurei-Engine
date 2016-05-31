#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  core.py
#  
#  Copyright 2016 Ericson Willians (Rederick Deathwill) <EricsonWRP@ERICSONWRP-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
import json
import pyglet
import os

# CFG
# ======================================================== #

GRAPHICS_PATH = "GFX"
SOUNDS_PATH = "SFX"
MUSIC_PATH = "SFX"
DEFAULT_CFG_PATH = "conf.yur"
DEFAULT_OPTIONS_PATH = "options.yur"
DEFAULT_HIGHSCORE_PATH = "highscore.yur"

# CONSTANTS
# ======================================================== #

ON = True
OFF = False

# Directional Constants:
# -------------------------------------------------------------------------------------------------------

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

# Coordenate Constants:
# -------------------------------------------------------------------------------------------------------

TOP_LEFT_CORNER = 0
TOP_RIGHT_CORNER = 1
BOTTOM_LEFT_CORNER = 2
BOTTOM_RIGHT_CORNER = 3

# Color Constants:
# -------------------------------------------------------------------------------------------------------

VIVID = 255
VOID = 0

AQUA = (VOID, VIVID, VIVID)
BLACK = (VOID, VOID, VOID)
BLUE = (VOID, VOID, VIVID)
CORNFLOWER_BLUE = (100, 149, 237)
FUCHSIA = (VIVID, VOID, VIVID)
GRAY = (128, 128, 128)
GREEN = (VOID, 128, VOID)
LIME = (VOID, VIVID, VOID)
MAROON = (128, VOID, VOID)
NAVY_BLUE = (VOID, VOID, 128)
OLIVE = (128, 128, VOID)
PURPLE = (128, VOID, 128)
RED = (VIVID, VOID, VOID)
SILVER = (192, 192, 192)
TEAL = (VOID , 128, 128)
WHITE = (VIVID, VIVID, VIVID)
YELLOW = (VIVID, VIVID, VOID)

COLORS = [
	AQUA, 
	BLACK, 
	BLUE, 
	CORNFLOWER_BLUE, 
	FUCHSIA, 
	GRAY, 
	GREEN, 
	LIME, 
	MAROON, 
	NAVY_BLUE, 
	OLIVE, 
	PURPLE, 
	RED, 
	SILVER, 
	TEAL, 
	WHITE, 
	YELLOW
]
	
# Alpha Constants:
# -------------------------------------------------------------------------------------------------------

SOLID = 255
TRANSPARENT = 125
BARELY_VISIBLE = 25
 
# Thickness Constants:
# -------------------------------------------------------------------------------------------------------
 
FILLED = 0
 
# Trigger Constants:
# -------------------------------------------------------------------------------------------------------

ENDLESS = 0
ONCE = 1
TWICE = 2
THRICE = 3

# Delay Constants:
# -------------------------------------------------------------------------------------------------------

NO_DELAY = 0

# Core Classes
# ======================================================== #

def ycheck(arg, obj, msg):
	if isinstance(arg, obj):
		return arg
	else:
		print(msg)
		sys.exit()

class YSerializable:
    def __init__(self):
        self._file = None

    def serialize(self, path, mode, data):
        try:
            with open(path, mode) as outfile:
                self._file = outfile
                self._file.write(json.dumps(data))
        except:
            raise FileNotFoundError()


class YData(YSerializable):
    def __init__(self, data_name):
        YSerializable.__init__(self)
        self.data_name = data_name
        if os.path.isfile(self.data_name):
            self.data = self.load(self.data_name)
        else:
            self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        for x in self.data:
            yield x

    def get_data(self):
        return self.data

    def write(self, path):
        self.serialize(path, 'w', self.get_data())

    def load(self, path):
        with open(path, 'r') as _file:
            return json.load(_file)

class YColor:
	
	def __init__(self, *args):
		if len(args) == 1:
			self.r = args[0][0]
			self.g = args[0][1]
			self.b = args[0][2]
		elif len(args) >= 3:
			self.r = args[0]
			self.g = args[1]
			self.b = args[2]
		if len(args) == 4:
			self.a = args[3]
		else:
			self.a = 255

class YWindow(YData, pyglet.window.Window):

	def __init__(self, screen_width=1024, screen_height=768, fullscreen=False, locked_mouse=False):
		YData.__init__(self, "config.yur")
		if not self.data:
			self.data = {
					"SCREEN_WIDTH": screen_width,
					"SCREEN_HEIGHT": screen_height,
					"FULLSCREEN": fullscreen,
					"LOCKED_MOUSE": locked_mouse}
		self.write(self.data_name)
		pyglet.window.Window.__init__(self, self.data["SCREEN_WIDTH"], self.data["SCREEN_HEIGHT"], fullscreen=self.data["FULLSCREEN"])
		if self.data["LOCKED_MOUSE"]:
			self.set_exclusive_mouse()
		self.renderer = None
		self.procedures = {}
	
	def __add__(self, other):
		if len(other) == 2:
			self.procedures[other[0]] = other[1]
		else:
			print("The argument for __add__ must be a tuple with 2 elements in the following format: (dt, f)")
			sys.exit()
		
	def __call__(self):
		for p in self.procedures:
			pyglet.clock.schedule_interval(self.procedures[p], p)
		pyglet.app.run()
		

	def set_renderer(self, r):
		self.renderer = r

	def on_draw(self):
		self.clear()
		if self.renderer:
			self.renderer.draw()
		else:
			print("The app has no renderer associated with it.")
			sys.exit()

	def on_key_press(self, key, modifiers):
		if key == pyglet.window.key.UP or key == pyglet.window.key.W:
			print("Yep!")
		elif key == pyglet.window.key.DOWN or key == pyglet.window.key.S:
			pass
		elif key == pyglet.window.key.LEFT or key == pyglet.window.key.A:
			pass
		elif key == pyglet.window.key.RIGHT or key == pyglet.window.key.D:
			pass

class Y2DRenderer:
	
	def __init__(self, window, yobject_list, point_of_origin=TOP_LEFT_CORNER):
		self.screen_width = window.data["SCREEN_WIDTH"]
		self.screen_height = window.data["SCREEN_HEIGHT"]
		self.yobject_list = yobject_list
		self.point_of_origin = point_of_origin
		
	def draw(self):
		for o in self.yobject_list:
			if self.point_of_origin == TOP_LEFT_CORNER:
				o.y = o.y + (self.screen_height - o.h)
			elif self.point_of_origin == TOP_RIGHT_CORNER:
				o.y = o.y + (self.screen_height - o.h)
				o.x = o.x + (self.screen_width - o.w)
			elif self.point_of_origin == BOTTOM_LEFT_CORNER:
				pass
			elif self.point_of_origin == BOTTOM_RIGHT_CORNER:
				o.x = o.x + (self.screen_width - o.w)
			o.draw()
