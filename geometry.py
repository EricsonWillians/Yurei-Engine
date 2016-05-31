#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  geometry.py
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
from Yurei import core
import pyglet


class YRect:

	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

class YColorRect(YRect):

	def __init__(self, x, y, w, h, c: core.YColor):
		YRect.__init__(self, x, y, w, h)
		self.c = core.ycheck(c, core.YColor, "Error: The color object must be an instance of YColor.")		

	def draw(self):
		pyglet.gl.glTranslatef(self.x, self.y, 0)
		pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
									 [0, 1, 2, 0, 2, 3],
									 ("v2i", (
										 0,
										 0,
										 0,
										 self.h,
										 self.w,
										 self.h,
										 self.w,
										 0)
									  ),
									 ("c4B", (
										 self.c.r,
										 self.c.g,
										 self.c.b,
										 self.c.a,
										 self.c.r,
										 self.c.g,
										 self.c.b,
										 self.c.a,
										 self.c.r,
										 self.c.g,
										 self.c.b,
										 self.c.a,
										 self.c.r,
										 self.c.g,
										 self.c.b,
										 self.c.a)
									  )
									 )

class YImageRect(YRect):

	def __init__(self, x, y, w, h, path):
		YRect.__init__(self, x, y, w, h)
		self.path = path	
		self.image = pyglet.image.load(self.path)
		# self.vlist = pyglet.graphics.vertex_list(4, ('v2f', [-x, -y, x, -y, -x, y, x, y]), ('t2f', [0, 0, 1, 0, 0, 1, 1, 1]))

	def draw(self):
		pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
		pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
		pyglet.gl.glEnable(pyglet.gl.GL_TEXTURE_2D)
		pyglet.gl.glBindTexture(pyglet.gl.GL_TEXTURE_2D, self.image.get_texture().id)
		pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_LINEAR)
		pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_LINEAR)
