#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  widgets.py
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

class YLabel(pyglet.text.Label):
	
	def __init__(text='', font_name=None, font_size=None, bold=False, italic=False, color=(255, 255, 255, 255), x=0, y=0, width=None, height=None, anchor_x='left', anchor_y='baseline', align='left', multiline=False, dpi=None, batch=None, group=None):
		if isinstance(color, core.YColor):
			self.color = (color.r, color.g, color.b, color.a)
		else:
			self.color = color
		pyglet.text.Label.__init__(text, font_name, font_size, bold, italic, self.color, x, y, width, height, anchor_x, anchor_y, align, multiline, dpi, batch, group)
