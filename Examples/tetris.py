#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tetris.py
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

import pyglet
from Yurei import core, geometry

# 480 / 10 = 48
# 736 / 16 = 46

SCREEN_WIDTH = 768
SCREEN_HEIGHT = 768
GAME_AREA_BORDER = 16
GAME_AREA_WIDTH = 368
GAME_AREA_HEIGHT = 752
GAME_AREA_CENTER = 184
PIECE_SIZE = 16
HEIGHT_LIMIT = 47
LINE_SIZE = 23

class GameArea:
	
	def __init__(self):
		self.area = [
			geometry.YColorRect(core.VOID, core.VOID, 384, GAME_AREA_BORDER, core.YColor(core.WHITE)),
			geometry.YColorRect(core.VOID, core.VOID, GAME_AREA_BORDER, 768, core.YColor(core.WHITE)),
			geometry.YColorRect(384-GAME_AREA_BORDER, core.VOID, GAME_AREA_BORDER, 768, core.YColor(core.WHITE)),
			geometry.YColorRect(core.VOID, 768-GAME_AREA_BORDER, 384, GAME_AREA_BORDER, core.YColor(core.WHITE))
		]

	def __call__(self):
		return self.area

class GameGrid:
	
	def __init__(self):
		pass
		
class GamePiece:
	
	def __init__(self, piece):
		if piece == 'I':
			self.data = [
				geometry.YColorRect(GAME_AREA_CENTER, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.CYAN)),
				geometry.YColorRect(GAME_AREA_CENTER, PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, core.YColor(core.CYAN)),
				geometry.YColorRect(GAME_AREA_CENTER, PIECE_SIZE*3, PIECE_SIZE, PIECE_SIZE, core.YColor(core.CYAN)),
				geometry.YColorRect(GAME_AREA_CENTER, PIECE_SIZE*4, PIECE_SIZE, PIECE_SIZE, core.YColor(core.CYAN))
			]
		elif piece == 'J':
			self.data = [
				geometry.YColorRect(GAME_AREA_CENTER, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.BLUE)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.BLUE)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.BLUE)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE*2, PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, core.YColor(core.BLUE))
			]
		elif piece == 'L':
			self.data = [
				geometry.YColorRect(GAME_AREA_CENTER, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.ORANGE)),
				geometry.YColorRect(GAME_AREA_CENTER, PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, core.YColor(core.ORANGE)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.ORANGE)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.ORANGE))
			]
		elif piece == 'O':
			self.data = [
				geometry.YColorRect(GAME_AREA_CENTER, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.YELLOW)),
				geometry.YColorRect(GAME_AREA_CENTER, PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, core.YColor(core.YELLOW)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.YELLOW)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE, PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, core.YColor(core.YELLOW))
			]
		elif piece == 'S':
			self.data = [
				geometry.YColorRect(GAME_AREA_CENTER, PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, core.YColor(core.LIME)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.LIME)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE, PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, core.YColor(core.LIME)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.LIME))
			]
		elif piece == 'T':
			self.data = [
				geometry.YColorRect(GAME_AREA_CENTER, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.PURPLE)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.PURPLE)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.PURPLE)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE, PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, core.YColor(core.PURPLE))
			]
		elif piece == 'Z':
			self.data = [
				geometry.YColorRect(GAME_AREA_CENTER, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.RED)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, core.YColor(core.RED)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE, PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, core.YColor(core.RED)),
				geometry.YColorRect(GAME_AREA_CENTER + PIECE_SIZE*2, PIECE_SIZE*2, PIECE_SIZE, PIECE_SIZE, core.YColor(core.RED))
			]

	def __call__(self):
		return self.data

if __name__ == '__main__':
	w = core.YWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	game_area = GameArea()
	i = GamePiece('Z')
	r = core.Y2DRenderer(w, game_area(), core.TOP_LEFT_CORNER)
	[r + p for p in i()]
	w.set_renderer(r)
	w()
"""
	@w.event
	def on_key_press(key, modifiers):
		if key == pyglet.window.key.UP or key == pyglet.window.key.W:
			print("Yep!")
		elif key == pyglet.window.key.DOWN or key == pyglet.window.key.S:
			pass
		elif key == pyglet.window.key.LEFT or key == pyglet.window.key.A:
			pass
		elif key == pyglet.window.key.RIGHT or key == pyglet.window.key.D:
			pass
"""
	
