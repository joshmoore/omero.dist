# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.4
#
# <auto-generated>
#
# Generated from file `SystemF.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import omero_RTypes_ice
import Ice_BuiltinSequences_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module omero
__name__ = 'omero'

# Start of module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')
__name__ = 'omero.sys'

if '_t_LongList' not in _M_omero.sys.__dict__:
    _M_omero.sys._t_LongList = IcePy.defineSequence('::omero::sys::LongList', (), IcePy._t_long)

if '_t_IntList' not in _M_omero.sys.__dict__:
    _M_omero.sys._t_IntList = IcePy.defineSequence('::omero::sys::IntList', (), IcePy._t_int)

if '_t_CountMap' not in _M_omero.sys.__dict__:
    _M_omero.sys._t_CountMap = IcePy.defineDictionary('::omero::sys::CountMap', (), IcePy._t_long, IcePy._t_long)

if '_t_ParamMap' not in _M_omero.sys.__dict__:
    _M_omero.sys._t_ParamMap = IcePy.defineDictionary('::omero::sys::ParamMap', (), IcePy._t_string, _M_omero._t_RType)

if '_t_IdByteMap' not in _M_omero.sys.__dict__:
    _M_omero.sys._t_IdByteMap = IcePy.defineDictionary('::omero::sys::IdByteMap', (), IcePy._t_long, _M_Ice._t_ByteSeq)

if 'EventContext' not in _M_omero.sys.__dict__:
    _M_omero.sys._t_EventContext = IcePy.declareClass('::omero::sys::EventContext')
    _M_omero.sys._t_EventContextPrx = IcePy.declareProxy('::omero::sys::EventContext')

# End of module omero.sys

__name__ = 'omero'

# End of module omero
