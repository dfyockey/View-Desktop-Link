"""
# MIT License
#
# Copyright 2021 David Yockey
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__kupfer_name__ = _("View Desktop Link")
__kupfer_actions__ = ("ViewDesktopLink", )
__description__ = _("Opens a site specified by a .desktop file of Type=Link in the system's default web browser.\n")
__version__ = "1.0"
__author__ = "David Yockey (https://github.com/dfyockey)\n"

import xdg.DesktopEntry

from kupfer.objects import Action, FileLeaf
from kupfer import utils

class ViewDesktopLink (Action):
	"""
	    Adjust rank so this action appears as the default for valid items.
	    The value 100 was chosen because, for some reason, a ridiculously high
	    rank is needed when the action name begins with 'V', like 'View', as
	    opposed to something like 'Browse' that's closer to the beginning of
	    the alphabet.
	"""
	rank_adjust = 100
	
	de = None
	
	def __init__(self):
		super().__init__(_("View Desktop Link"))

	def item_types(self):
		yield FileLeaf

	def valid_for_item(self, fileobj):
		if fileobj.object.endswith(".desktop"):
			self.de = xdg.DesktopEntry.DesktopEntry(fileobj.object)
			if self.de.getType() == "Link" and self.de.getURL():
				return True
		return False

	def get_icon_name(self):
		return "go-jump"

	def activate(self, fileobj):
		utils.show_url(self.de.getURL())

