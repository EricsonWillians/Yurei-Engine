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

from Yurei import core, geometry

class GameArea:
	
	def __init__(self):
		self.area = [
			geometry.YColorRect(core.VOID, core.VOID, 512, 32, core.YColor(core.WHITE)),
			geometry.YColorRect(core.VOID, core.VOID, 32, 768, core.YColor(core.WHITE)),
			geometry.YColorRect(512-32, core.VOID, 32, 768, core.YColor(core.WHITE)),
			geometry.YColorRect(core.VOID, 768-32, 512, 32, core.YColor(core.WHITE))
		]

	def __call__(self):
		return self.area

if __name__ == '__main__':
	w = core.YWindow()
	game_area = GameArea()
	r = core.Y2DRenderer(w, game_area(), core.TOP_LEFT_CORNER)
	w.set_renderer(r)

	w()
