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

if __name__ == '__main__':
	w = core.YWindow()
	a = geometry.YColorRect(0, 0, 200, 200, core.YColor(core.RED))
	i = geometry.YImageRect(0, 0, 400, 400, "GFX/brick.jpg")
	r = core.Y2DRenderer(w, [a], core.BOTTOM_LEFT_CORNER)
	w.set_renderer(r)
		
	w + (2, (lambda x: print("yep")))
	w()
