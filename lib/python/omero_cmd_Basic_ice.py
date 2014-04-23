# **********************************************************************
#
# Copyright (c) 2003-2013 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.5.1
#
# <auto-generated>
#
# Generated from file `Basic.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy
import omero_cmd_API_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Included module omero.cmd
_M_omero.cmd = Ice.openModule('omero.cmd')

# Start of module omero
__name__ = 'omero'

# Start of module omero.cmd
__name__ = 'omero.cmd'

if 'DoAll' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.DoAll = Ice.createTempClass()
    class DoAll(_M_omero.cmd.Request):
        def __init__(self, requests=None, contexts=None):
            _M_omero.cmd.Request.__init__(self)
            self.requests = requests
            self.contexts = contexts

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::DoAll', '::omero::cmd::Request')

        def ice_id(self, current=None):
            return '::omero::cmd::DoAll'

        def ice_staticId():
            return '::omero::cmd::DoAll'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_DoAll)

        __repr__ = __str__

    _M_omero.cmd.DoAllPrx = Ice.createTempClass()
    class DoAllPrx(_M_omero.cmd.RequestPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.DoAllPrx.ice_checkedCast(proxy, '::omero::cmd::DoAll', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.DoAllPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.cmd._t_DoAllPrx = IcePy.defineProxy('::omero::cmd::DoAll', DoAllPrx)

    _M_omero.cmd._t_DoAll = IcePy.declareClass('::omero::cmd::DoAll')

    _M_omero.cmd._t_DoAll = IcePy.defineClass('::omero::cmd::DoAll', DoAll, -1, (), False, False, _M_omero.cmd._t_Request, (), (
        ('requests', (), _M_omero.cmd._t_RequestList, False, 0),
        ('contexts', (), _M_omero.cmd._t_StringMapList, False, 0)
    ))
    DoAll._ice_type = _M_omero.cmd._t_DoAll

    _M_omero.cmd.DoAll = DoAll
    del DoAll

    _M_omero.cmd.DoAllPrx = DoAllPrx
    del DoAllPrx

if 'DoAllRsp' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.DoAllRsp = Ice.createTempClass()
    class DoAllRsp(_M_omero.cmd.OK):
        def __init__(self, responses=None, status=None):
            _M_omero.cmd.OK.__init__(self)
            self.responses = responses
            self.status = status

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::DoAllRsp', '::omero::cmd::OK', '::omero::cmd::Response')

        def ice_id(self, current=None):
            return '::omero::cmd::DoAllRsp'

        def ice_staticId():
            return '::omero::cmd::DoAllRsp'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_DoAllRsp)

        __repr__ = __str__

    _M_omero.cmd.DoAllRspPrx = Ice.createTempClass()
    class DoAllRspPrx(_M_omero.cmd.OKPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.DoAllRspPrx.ice_checkedCast(proxy, '::omero::cmd::DoAllRsp', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.DoAllRspPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.cmd._t_DoAllRspPrx = IcePy.defineProxy('::omero::cmd::DoAllRsp', DoAllRspPrx)

    _M_omero.cmd._t_DoAllRsp = IcePy.declareClass('::omero::cmd::DoAllRsp')

    _M_omero.cmd._t_DoAllRsp = IcePy.defineClass('::omero::cmd::DoAllRsp', DoAllRsp, -1, (), False, False, _M_omero.cmd._t_OK, (), (
        ('responses', (), _M_omero.cmd._t_ResponseList, False, 0),
        ('status', (), _M_omero.cmd._t_StatusList, False, 0)
    ))
    DoAllRsp._ice_type = _M_omero.cmd._t_DoAllRsp

    _M_omero.cmd.DoAllRsp = DoAllRsp
    del DoAllRsp

    _M_omero.cmd.DoAllRspPrx = DoAllRspPrx
    del DoAllRspPrx

if 'ListRequests' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.ListRequests = Ice.createTempClass()
    class ListRequests(_M_omero.cmd.Request):
        def __init__(self):
            _M_omero.cmd.Request.__init__(self)

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::ListRequests', '::omero::cmd::Request')

        def ice_id(self, current=None):
            return '::omero::cmd::ListRequests'

        def ice_staticId():
            return '::omero::cmd::ListRequests'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_ListRequests)

        __repr__ = __str__

    _M_omero.cmd.ListRequestsPrx = Ice.createTempClass()
    class ListRequestsPrx(_M_omero.cmd.RequestPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.ListRequestsPrx.ice_checkedCast(proxy, '::omero::cmd::ListRequests', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.ListRequestsPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.cmd._t_ListRequestsPrx = IcePy.defineProxy('::omero::cmd::ListRequests', ListRequestsPrx)

    _M_omero.cmd._t_ListRequests = IcePy.defineClass('::omero::cmd::ListRequests', ListRequests, -1, (), False, False, _M_omero.cmd._t_Request, (), ())
    ListRequests._ice_type = _M_omero.cmd._t_ListRequests

    _M_omero.cmd.ListRequests = ListRequests
    del ListRequests

    _M_omero.cmd.ListRequestsPrx = ListRequestsPrx
    del ListRequestsPrx

if 'ListRequestsRsp' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.ListRequestsRsp = Ice.createTempClass()
    class ListRequestsRsp(_M_omero.cmd.OK):
        def __init__(self, list=None):
            _M_omero.cmd.OK.__init__(self)
            self.list = list

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::ListRequestsRsp', '::omero::cmd::OK', '::omero::cmd::Response')

        def ice_id(self, current=None):
            return '::omero::cmd::ListRequestsRsp'

        def ice_staticId():
            return '::omero::cmd::ListRequestsRsp'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_ListRequestsRsp)

        __repr__ = __str__

    _M_omero.cmd.ListRequestsRspPrx = Ice.createTempClass()
    class ListRequestsRspPrx(_M_omero.cmd.OKPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.ListRequestsRspPrx.ice_checkedCast(proxy, '::omero::cmd::ListRequestsRsp', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.ListRequestsRspPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.cmd._t_ListRequestsRspPrx = IcePy.defineProxy('::omero::cmd::ListRequestsRsp', ListRequestsRspPrx)

    _M_omero.cmd._t_ListRequestsRsp = IcePy.declareClass('::omero::cmd::ListRequestsRsp')

    _M_omero.cmd._t_ListRequestsRsp = IcePy.defineClass('::omero::cmd::ListRequestsRsp', ListRequestsRsp, -1, (), False, False, _M_omero.cmd._t_OK, (), (('list', (), _M_omero.cmd._t_RequestList, False, 0),))
    ListRequestsRsp._ice_type = _M_omero.cmd._t_ListRequestsRsp

    _M_omero.cmd.ListRequestsRsp = ListRequestsRsp
    del ListRequestsRsp

    _M_omero.cmd.ListRequestsRspPrx = ListRequestsRspPrx
    del ListRequestsRspPrx

if 'PopStatus' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.PopStatus = Ice.createTempClass()
    class PopStatus(_M_omero.cmd.Request):
        def __init__(self, limit=0, include=None, exclude=None):
            _M_omero.cmd.Request.__init__(self)
            self.limit = limit
            self.include = include
            self.exclude = exclude

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::PopStatus', '::omero::cmd::Request')

        def ice_id(self, current=None):
            return '::omero::cmd::PopStatus'

        def ice_staticId():
            return '::omero::cmd::PopStatus'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_PopStatus)

        __repr__ = __str__

    _M_omero.cmd.PopStatusPrx = Ice.createTempClass()
    class PopStatusPrx(_M_omero.cmd.RequestPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.PopStatusPrx.ice_checkedCast(proxy, '::omero::cmd::PopStatus', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.PopStatusPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.cmd._t_PopStatusPrx = IcePy.defineProxy('::omero::cmd::PopStatus', PopStatusPrx)

    _M_omero.cmd._t_PopStatus = IcePy.defineClass('::omero::cmd::PopStatus', PopStatus, -1, (), False, False, _M_omero.cmd._t_Request, (), (
        ('limit', (), IcePy._t_int, False, 0),
        ('include', (), _M_omero.cmd._t_StateList, False, 0),
        ('exclude', (), _M_omero.cmd._t_StateList, False, 0)
    ))
    PopStatus._ice_type = _M_omero.cmd._t_PopStatus

    _M_omero.cmd.PopStatus = PopStatus
    del PopStatus

    _M_omero.cmd.PopStatusPrx = PopStatusPrx
    del PopStatusPrx

if 'PopStatusRsp' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.PopStatusRsp = Ice.createTempClass()
    class PopStatusRsp(_M_omero.cmd.OK):
        def __init__(self, list=None):
            _M_omero.cmd.OK.__init__(self)
            self.list = list

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::OK', '::omero::cmd::PopStatusRsp', '::omero::cmd::Response')

        def ice_id(self, current=None):
            return '::omero::cmd::PopStatusRsp'

        def ice_staticId():
            return '::omero::cmd::PopStatusRsp'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_PopStatusRsp)

        __repr__ = __str__

    _M_omero.cmd.PopStatusRspPrx = Ice.createTempClass()
    class PopStatusRspPrx(_M_omero.cmd.OKPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.PopStatusRspPrx.ice_checkedCast(proxy, '::omero::cmd::PopStatusRsp', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.PopStatusRspPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.cmd._t_PopStatusRspPrx = IcePy.defineProxy('::omero::cmd::PopStatusRsp', PopStatusRspPrx)

    _M_omero.cmd._t_PopStatusRsp = IcePy.declareClass('::omero::cmd::PopStatusRsp')

    _M_omero.cmd._t_PopStatusRsp = IcePy.defineClass('::omero::cmd::PopStatusRsp', PopStatusRsp, -1, (), False, False, _M_omero.cmd._t_OK, (), (('list', (), _M_omero.cmd._t_StatusList, False, 0),))
    PopStatusRsp._ice_type = _M_omero.cmd._t_PopStatusRsp

    _M_omero.cmd.PopStatusRsp = PopStatusRsp
    del PopStatusRsp

    _M_omero.cmd.PopStatusRspPrx = PopStatusRspPrx
    del PopStatusRspPrx

if 'FindHandles' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.FindHandles = Ice.createTempClass()
    class FindHandles(_M_omero.cmd.Request):
        def __init__(self, limit=0, include=None, exclude=None):
            _M_omero.cmd.Request.__init__(self)
            self.limit = limit
            self.include = include
            self.exclude = exclude

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::FindHandles', '::omero::cmd::Request')

        def ice_id(self, current=None):
            return '::omero::cmd::FindHandles'

        def ice_staticId():
            return '::omero::cmd::FindHandles'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_FindHandles)

        __repr__ = __str__

    _M_omero.cmd.FindHandlesPrx = Ice.createTempClass()
    class FindHandlesPrx(_M_omero.cmd.RequestPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.FindHandlesPrx.ice_checkedCast(proxy, '::omero::cmd::FindHandles', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.FindHandlesPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.cmd._t_FindHandlesPrx = IcePy.defineProxy('::omero::cmd::FindHandles', FindHandlesPrx)

    _M_omero.cmd._t_FindHandles = IcePy.defineClass('::omero::cmd::FindHandles', FindHandles, -1, (), False, False, _M_omero.cmd._t_Request, (), (
        ('limit', (), IcePy._t_int, False, 0),
        ('include', (), _M_omero.cmd._t_StateList, False, 0),
        ('exclude', (), _M_omero.cmd._t_StateList, False, 0)
    ))
    FindHandles._ice_type = _M_omero.cmd._t_FindHandles

    _M_omero.cmd.FindHandles = FindHandles
    del FindHandles

    _M_omero.cmd.FindHandlesPrx = FindHandlesPrx
    del FindHandlesPrx

if 'FindHandlesRsp' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.FindHandlesRsp = Ice.createTempClass()
    class FindHandlesRsp(_M_omero.cmd.OK):
        def __init__(self, handles=None):
            _M_omero.cmd.OK.__init__(self)
            self.handles = handles

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::FindHandlesRsp', '::omero::cmd::OK', '::omero::cmd::Response')

        def ice_id(self, current=None):
            return '::omero::cmd::FindHandlesRsp'

        def ice_staticId():
            return '::omero::cmd::FindHandlesRsp'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_FindHandlesRsp)

        __repr__ = __str__

    _M_omero.cmd.FindHandlesRspPrx = Ice.createTempClass()
    class FindHandlesRspPrx(_M_omero.cmd.OKPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.FindHandlesRspPrx.ice_checkedCast(proxy, '::omero::cmd::FindHandlesRsp', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.FindHandlesRspPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.cmd._t_FindHandlesRspPrx = IcePy.defineProxy('::omero::cmd::FindHandlesRsp', FindHandlesRspPrx)

    _M_omero.cmd._t_FindHandlesRsp = IcePy.defineClass('::omero::cmd::FindHandlesRsp', FindHandlesRsp, -1, (), False, False, _M_omero.cmd._t_OK, (), (('handles', (), _M_omero.cmd._t_HandleList, False, 0),))
    FindHandlesRsp._ice_type = _M_omero.cmd._t_FindHandlesRsp

    _M_omero.cmd.FindHandlesRsp = FindHandlesRsp
    del FindHandlesRsp

    _M_omero.cmd.FindHandlesRspPrx = FindHandlesRspPrx
    del FindHandlesRspPrx

if 'Timing' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.Timing = Ice.createTempClass()
    class Timing(_M_omero.cmd.Request):
        '''Diagnostic command which can be used to see the overhead
of callbacks. The number of steps and the simulated workload
can be specified.'''
        def __init__(self, steps=0, millisPerStep=0):
            _M_omero.cmd.Request.__init__(self)
            self.steps = steps
            self.millisPerStep = millisPerStep

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::Request', '::omero::cmd::Timing')

        def ice_id(self, current=None):
            return '::omero::cmd::Timing'

        def ice_staticId():
            return '::omero::cmd::Timing'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_Timing)

        __repr__ = __str__

    _M_omero.cmd.TimingPrx = Ice.createTempClass()
    class TimingPrx(_M_omero.cmd.RequestPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.TimingPrx.ice_checkedCast(proxy, '::omero::cmd::Timing', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.TimingPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.cmd._t_TimingPrx = IcePy.defineProxy('::omero::cmd::Timing', TimingPrx)

    _M_omero.cmd._t_Timing = IcePy.defineClass('::omero::cmd::Timing', Timing, -1, (), False, False, _M_omero.cmd._t_Request, (), (
        ('steps', (), IcePy._t_int, False, 0),
        ('millisPerStep', (), IcePy._t_int, False, 0)
    ))
    Timing._ice_type = _M_omero.cmd._t_Timing

    _M_omero.cmd.Timing = Timing
    del Timing

    _M_omero.cmd.TimingPrx = TimingPrx
    del TimingPrx

# End of module omero.cmd

__name__ = 'omero'

# End of module omero
