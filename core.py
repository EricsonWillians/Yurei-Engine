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

import json
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

ORIGIN = 0

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

# DATA
# ======================================================== #

class Serializable:
	
	def __init__(self):
		
		self.file = None
		
	def serialize(self, path, mode):	
		try:
			self.file = open(path, mode)
		except:
			raise FileNotFoundError()
		if self.file is not None:
			return self.file
			self.file.close()

class Data(Serializable):

	def __init__(self):
		
		Serializable.__init__(self)
		self.data = {}
		
	def __setitem__(self, key, value):
		self.data[key] = value
		
	def __getitem__(self, key):
		return self.data[key]
		
	def get_data(self):
		return self.data
		
	def write(self, path):
		self.serialize(path, "w").write(json.dumps(self.get_data()))
		
	def load(self, path):
		json_data = open(path, "r")
		self.data = json.load(json_data)
		json_data.close()
		return self.data

