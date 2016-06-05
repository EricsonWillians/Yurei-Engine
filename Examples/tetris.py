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

pieces = {
	'I': [
		[1, 1, 1, 1]
	],
	'J': [
		[2, 2, 2],
		[0, 0, 2]
	],
	'L': [
		[3, 3, 3],
		[3, 0, 0]
	],
	'O': [
		[4, 4],
		[4, 4]
	],
	'S': [
		[0, 5, 5],
		[5, 5, 0]
	],
	'T': [
		[6, 6, 6],
		[0, 6, 0]
	],
	'Z': [
		[7, 7, 0],
		[0, 7, 7]
	]
}

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
	
	def __init__(self, renderer):
		self.r = renderer
		self.grid = []
		self.positions = []
		for y in range(PIECE_SIZE, GAME_AREA_HEIGHT, PIECE_SIZE):
			row = []
			row_pos = []
			for x in range(PIECE_SIZE, GAME_AREA_WIDTH, PIECE_SIZE):
				row.append(0)
				row_pos.append((x, y))
			self.grid.append(row)
			self.positions.append(row_pos)
	
	def draw(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if self.grid[i][j] == 1:
					pos = self.r.translate(self.positions[i][j][0], self.positions[i][j][1], PIECE_SIZE, PIECE_SIZE)
					geometry.YColorRect(pos[0], pos[1], PIECE_SIZE, PIECE_SIZE, core.YColor(core.CYAN)).draw()
				elif self.grid[i][j] == 2:
					pos = self.r.translate(self.positions[i][j][0], self.positions[i][j][1], PIECE_SIZE, PIECE_SIZE)
					geometry.YColorRect(pos[0], pos[1], PIECE_SIZE, PIECE_SIZE, core.YColor(core.BLUE)).draw()
				elif self.grid[i][j] == 3:
					pos = self.r.translate(self.positions[i][j][0], self.positions[i][j][1], PIECE_SIZE, PIECE_SIZE)
					geometry.YColorRect(pos[0], pos[1], PIECE_SIZE, PIECE_SIZE, core.YColor(core.ORANGE)).draw()
				elif self.grid[i][j] == 4:
					pos = self.r.translate(self.positions[i][j][0], self.positions[i][j][1], PIECE_SIZE, PIECE_SIZE)
					geometry.YColorRect(pos[0], pos[1], PIECE_SIZE, PIECE_SIZE, core.YColor(core.YELLOW)).draw()
				elif self.grid[i][j] == 5:
					pos = self.r.translate(self.positions[i][j][0], self.positions[i][j][1], PIECE_SIZE, PIECE_SIZE)
					geometry.YColorRect(pos[0], pos[1], PIECE_SIZE, PIECE_SIZE, core.YColor(core.LIME)).draw()
				elif self.grid[i][j] == 6:
					pos = self.r.translate(self.positions[i][j][0], self.positions[i][j][1], PIECE_SIZE, PIECE_SIZE)
					geometry.YColorRect(pos[0], pos[1], PIECE_SIZE, PIECE_SIZE, core.YColor(core.PURPLE)).draw()
				elif self.grid[i][j] == 7:
					pos = self.r.translate(self.positions[i][j][0], self.positions[i][j][1], PIECE_SIZE, PIECE_SIZE)
					geometry.YColorRect(pos[0], pos[1], PIECE_SIZE, PIECE_SIZE, core.YColor(core.RED)).draw()
					
	def __call__(self):
		return self.grid

if __name__ == '__main__':
	w = core.YWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	game_area = GameArea()
	r = core.Y2DRenderer(w, game_area(), core.TOP_LEFT_CORNER)
	grid = GameGrid(r)
	@w.event
	def on_draw():
		r.draw()
		grid.draw()
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
	
