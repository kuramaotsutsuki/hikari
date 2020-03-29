#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © Nekokatt 2019-2020
#
# This file is part of Hikari.
#
# Hikari is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hikari is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Hikari. If not, see <https://www.gnu.org/licenses/>.
"""Various utilities used internally within this API.

These are not bound to the versioning contact, and are considered to be
implementation detail that could change at any time, so should not be
used outside this library.
"""
from hikari._internal import assertions
from hikari._internal import cdn
from hikari._internal import conversions
from hikari._internal import marshaller
from hikari._internal import meta
from hikari._internal import more_asyncio
from hikari._internal import more_collections
from hikari._internal import more_logging