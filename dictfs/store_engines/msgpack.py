"""
Author: Liran Funaro <liran.funaro@gmail.com>

Copyright (C) 2006-2021 Liran Funaro

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import msgpack


def write(f, obj):
    msgpack.pack(obj, f, use_bin_type=True)


def read(f):
    try:
        return msgpack.unpack(f, raw=False)
    except msgpack.exceptions.ExtraData:
        f.seek(0)
        return list(msgpack.Unpacker(f, raw=False))