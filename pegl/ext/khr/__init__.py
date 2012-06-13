#!/usr/bin/env python3

'''EGL Khronos (KHR) extension support.'''

# Copyright © 2012 Tim Pederick.
#
# This file is part of Pegl.
#
# Pegl is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pegl is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pegl. If not, see <http://www.gnu.org/licenses/>.

__all__ = ('locksurface', 'extensions')

extensions = {'EGL_KHR_lock_surface': 'locksurface',
              'EGL_KHR_lock_surface2': 'locksurface',
              'EGL_KHR_image_base': 'locksurface'}