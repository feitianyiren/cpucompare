#!/usr/bin/env python2
##
#     Project: CPUCompare
# Description: A GTK+ application to make comparisons between CPU models
#      Author: Fabio Castelli <muflone@vbsimple.net>
#   Copyright: 2013-2017 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

from cpucompare.ui import CPUCompareUI
from cpucompare.database import SQLite3Connection
from cpucompare.constants import *
import os.path

if __name__ == '__main__':
  database = SQLite3Connection()
  database.open(os.path.join(DIR_DATA, 'cpucompare.db'))

  gui = CPUCompareUI(database)
  gui.run()
