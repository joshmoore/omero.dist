# **********************************************************************
#
# Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.2
#
# <auto-generated>
#
# Generated from file `API.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy
import omero_RTypes_ice
import omero_ServerErrors_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Start of module omero
__name__ = 'omero'

# Start of module omero.cmd
_M_omero.cmd = Ice.openModule('omero.cmd')
__name__ = 'omero.cmd'
_M_omero.cmd.__doc__ = """Simplified API that is intended for passing"""

if '_t_StringMap' not in _M_omero.cmd.__dict__:
    _M_omero.cmd._t_StringMap = IcePy.defineDictionary('::omero::cmd::StringMap', (), IcePy._t_string, IcePy._t_string)

if '_t_StringMapList' not in _M_omero.cmd.__dict__:
    _M_omero.cmd._t_StringMapList = IcePy.defineSequence('::omero::cmd::StringMapList', (), _M_omero.cmd._t_StringMap)

if 'State' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.State = Ice.createTempClass()
    class State(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    State.ALL = State("ALL", 0)
    State.ACTIVE = State("ACTIVE", 1)
    State.INACTIVE = State("INACTIVE", 2)
    State.SUCCESS = State("SUCCESS", 3)
    State.FAILURE = State("FAILURE", 4)
    State.CANCELLED = State("CANCELLED", 5)
    State._enumerators = { 0:State.ALL, 1:State.ACTIVE, 2:State.INACTIVE, 3:State.SUCCESS, 4:State.FAILURE, 5:State.CANCELLED }

    _M_omero.cmd._t_State = IcePy.defineEnum('::omero::cmd::State', State, (), State._enumerators)

    _M_omero.cmd.State = State
    del State

if '_t_StateList' not in _M_omero.cmd.__dict__:
    _M_omero.cmd._t_StateList = IcePy.defineSequence('::omero::cmd::StateList', (), _M_omero.cmd._t_State)

if 'Handle' not in _M_omero.cmd.__dict__:
    _M_omero.cmd._t_Handle = IcePy.declareClass('::omero::cmd::Handle')
    _M_omero.cmd._t_HandlePrx = IcePy.declareProxy('::omero::cmd::Handle')

if 'Status' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.Status = Ice.createTempClass()
    class Status(Ice.Object):
        def __init__(self, source=None, category='', name='', flags=None, parameters=None, currentStep=0, steps=0, startTime=0, stepStartTimes=None, stepStopTimes=None, stopTime=0):
            self.source = source
            self.category = category
            self.name = name
            self.flags = flags
            self.parameters = parameters
            self.currentStep = currentStep
            self.steps = steps
            self.startTime = startTime
            self.stepStartTimes = stepStartTimes
            self.stepStopTimes = stepStopTimes
            self.stopTime = stopTime

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::Status')

        def ice_id(self, current=None):
            return '::omero::cmd::Status'

        def ice_staticId():
            return '::omero::cmd::Status'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_Status)

        __repr__ = __str__

    _M_omero.cmd.StatusPrx = Ice.createTempClass()
    class StatusPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.StatusPrx.ice_checkedCast(proxy, '::omero::cmd::Status', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.StatusPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::cmd::Status'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.cmd._t_StatusPrx = IcePy.defineProxy('::omero::cmd::Status', StatusPrx)

    _M_omero.cmd._t_Status = IcePy.defineClass('::omero::cmd::Status', Status, -1, (), False, False, None, (), (
        ('source', (), _M_omero.cmd._t_HandlePrx, False, 0),
        ('category', (), IcePy._t_string, False, 0),
        ('name', (), IcePy._t_string, False, 0),
        ('flags', (), _M_omero.cmd._t_StateList, False, 0),
        ('parameters', (), _M_omero.cmd._t_StringMap, False, 0),
        ('currentStep', (), IcePy._t_int, False, 0),
        ('steps', (), IcePy._t_int, False, 0),
        ('startTime', (), IcePy._t_long, False, 0),
        ('stepStartTimes', (), _M_Ice._t_LongSeq, False, 0),
        ('stepStopTimes', (), _M_Ice._t_LongSeq, False, 0),
        ('stopTime', (), IcePy._t_long, False, 0)
    ))
    Status._ice_type = _M_omero.cmd._t_Status

    _M_omero.cmd.Status = Status
    del Status

    _M_omero.cmd.StatusPrx = StatusPrx
    del StatusPrx

if '_t_StatusList' not in _M_omero.cmd.__dict__:
    _M_omero.cmd._t_StatusList = IcePy.defineSequence('::omero::cmd::StatusList', (), _M_omero.cmd._t_Status)

if 'Request' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.Request = Ice.createTempClass()
    class Request(Ice.Object):
        def __init__(self):
            pass

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::Request')

        def ice_id(self, current=None):
            return '::omero::cmd::Request'

        def ice_staticId():
            return '::omero::cmd::Request'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_Request)

        __repr__ = __str__

    _M_omero.cmd.RequestPrx = Ice.createTempClass()
    class RequestPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.RequestPrx.ice_checkedCast(proxy, '::omero::cmd::Request', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.RequestPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::cmd::Request'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.cmd._t_RequestPrx = IcePy.defineProxy('::omero::cmd::Request', RequestPrx)

    _M_omero.cmd._t_Request = IcePy.defineClass('::omero::cmd::Request', Request, -1, (), False, False, None, (), ())
    Request._ice_type = _M_omero.cmd._t_Request

    _M_omero.cmd.Request = Request
    del Request

    _M_omero.cmd.RequestPrx = RequestPrx
    del RequestPrx

if '_t_RequestList' not in _M_omero.cmd.__dict__:
    _M_omero.cmd._t_RequestList = IcePy.defineSequence('::omero::cmd::RequestList', (), _M_omero.cmd._t_Request)

if 'Response' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.Response = Ice.createTempClass()
    class Response(Ice.Object):
        def __init__(self):
            pass

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::Response')

        def ice_id(self, current=None):
            return '::omero::cmd::Response'

        def ice_staticId():
            return '::omero::cmd::Response'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_Response)

        __repr__ = __str__

    _M_omero.cmd.ResponsePrx = Ice.createTempClass()
    class ResponsePrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.ResponsePrx.ice_checkedCast(proxy, '::omero::cmd::Response', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.ResponsePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::cmd::Response'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.cmd._t_ResponsePrx = IcePy.defineProxy('::omero::cmd::Response', ResponsePrx)

    _M_omero.cmd._t_Response = IcePy.defineClass('::omero::cmd::Response', Response, -1, (), False, False, None, (), ())
    Response._ice_type = _M_omero.cmd._t_Response

    _M_omero.cmd.Response = Response
    del Response

    _M_omero.cmd.ResponsePrx = ResponsePrx
    del ResponsePrx

if 'OK' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.OK = Ice.createTempClass()
    class OK(_M_omero.cmd.Response):
        def __init__(self):
            _M_omero.cmd.Response.__init__(self)

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::OK', '::omero::cmd::Response')

        def ice_id(self, current=None):
            return '::omero::cmd::OK'

        def ice_staticId():
            return '::omero::cmd::OK'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_OK)

        __repr__ = __str__

    _M_omero.cmd.OKPrx = Ice.createTempClass()
    class OKPrx(_M_omero.cmd.ResponsePrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.OKPrx.ice_checkedCast(proxy, '::omero::cmd::OK', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.OKPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::cmd::OK'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.cmd._t_OKPrx = IcePy.defineProxy('::omero::cmd::OK', OKPrx)

    _M_omero.cmd._t_OK = IcePy.defineClass('::omero::cmd::OK', OK, -1, (), False, False, _M_omero.cmd._t_Response, (), ())
    OK._ice_type = _M_omero.cmd._t_OK

    _M_omero.cmd.OK = OK
    del OK

    _M_omero.cmd.OKPrx = OKPrx
    del OKPrx

if 'ERR' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.ERR = Ice.createTempClass()
    class ERR(_M_omero.cmd.Response):
        def __init__(self, category='', name='', parameters=None):
            _M_omero.cmd.Response.__init__(self)
            self.category = category
            self.name = name
            self.parameters = parameters

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::ERR', '::omero::cmd::Response')

        def ice_id(self, current=None):
            return '::omero::cmd::ERR'

        def ice_staticId():
            return '::omero::cmd::ERR'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_ERR)

        __repr__ = __str__

    _M_omero.cmd.ERRPrx = Ice.createTempClass()
    class ERRPrx(_M_omero.cmd.ResponsePrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.ERRPrx.ice_checkedCast(proxy, '::omero::cmd::ERR', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.ERRPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::cmd::ERR'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.cmd._t_ERRPrx = IcePy.defineProxy('::omero::cmd::ERR', ERRPrx)

    _M_omero.cmd._t_ERR = IcePy.defineClass('::omero::cmd::ERR', ERR, -1, (), False, False, _M_omero.cmd._t_Response, (), (
        ('category', (), IcePy._t_string, False, 0),
        ('name', (), IcePy._t_string, False, 0),
        ('parameters', (), _M_omero.cmd._t_StringMap, False, 0)
    ))
    ERR._ice_type = _M_omero.cmd._t_ERR

    _M_omero.cmd.ERR = ERR
    del ERR

    _M_omero.cmd.ERRPrx = ERRPrx
    del ERRPrx

if 'Unknown' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.Unknown = Ice.createTempClass()
    class Unknown(_M_omero.cmd.ERR):
        def __init__(self, category='', name='', parameters=None):
            _M_omero.cmd.ERR.__init__(self, category, name, parameters)

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::ERR', '::omero::cmd::Response', '::omero::cmd::Unknown')

        def ice_id(self, current=None):
            return '::omero::cmd::Unknown'

        def ice_staticId():
            return '::omero::cmd::Unknown'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_Unknown)

        __repr__ = __str__

    _M_omero.cmd.UnknownPrx = Ice.createTempClass()
    class UnknownPrx(_M_omero.cmd.ERRPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.UnknownPrx.ice_checkedCast(proxy, '::omero::cmd::Unknown', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.UnknownPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::cmd::Unknown'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.cmd._t_UnknownPrx = IcePy.defineProxy('::omero::cmd::Unknown', UnknownPrx)

    _M_omero.cmd._t_Unknown = IcePy.defineClass('::omero::cmd::Unknown', Unknown, -1, (), False, False, _M_omero.cmd._t_ERR, (), ())
    Unknown._ice_type = _M_omero.cmd._t_Unknown

    _M_omero.cmd.Unknown = Unknown
    del Unknown

    _M_omero.cmd.UnknownPrx = UnknownPrx
    del UnknownPrx

if '_t_ResponseList' not in _M_omero.cmd.__dict__:
    _M_omero.cmd._t_ResponseList = IcePy.defineSequence('::omero::cmd::ResponseList', (), _M_omero.cmd._t_Response)

if 'CmdCallback' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.CmdCallback = Ice.createTempClass()
    class CmdCallback(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_omero.cmd.CmdCallback:
                raise RuntimeError('omero.cmd.CmdCallback is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::CmdCallback')

        def ice_id(self, current=None):
            return '::omero::cmd::CmdCallback'

        def ice_staticId():
            return '::omero::cmd::CmdCallback'
        ice_staticId = staticmethod(ice_staticId)

        def step(self, complete, total, current=None):
            """Notifies clients that the given number of steps
            from the total is complete. This method will not
            necessarily be called for every step.
            Arguments:
            complete -- 
            total -- 
            current -- The Current object for the invocation."""
            pass

        def finished(self, rsp, s, current=None):
            """Called when the command has completed in any fashion
            including cancellation. The Status#flags list will
            contain information about whether or not the process
            was cancelled.
            Arguments:
            rsp -- 
            s -- 
            current -- The Current object for the invocation."""
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_CmdCallback)

        __repr__ = __str__

    _M_omero.cmd.CmdCallbackPrx = Ice.createTempClass()
    class CmdCallbackPrx(Ice.ObjectPrx):

        """Notifies clients that the given number of steps
        from the total is complete. This method will not
        necessarily be called for every step.
        Arguments:
        complete -- 
        total -- 
        _ctx -- The request context for the invocation."""
        def step(self, complete, total, _ctx=None):
            return _M_omero.cmd.CmdCallback._op_step.invoke(self, ((complete, total), _ctx))

        """Notifies clients that the given number of steps
        from the total is complete. This method will not
        necessarily be called for every step.
        Arguments:
        complete -- 
        total -- 
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation."""
        def begin_step(self, complete, total, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.cmd.CmdCallback._op_step.begin(self, ((complete, total), _response, _ex, _sent, _ctx))

        """Notifies clients that the given number of steps
        from the total is complete. This method will not
        necessarily be called for every step.
        Arguments:
        complete -- 
        total -- """
        def end_step(self, _r):
            return _M_omero.cmd.CmdCallback._op_step.end(self, _r)

        """Called when the command has completed in any fashion
        including cancellation. The Status#flags list will
        contain information about whether or not the process
        was cancelled.
        Arguments:
        rsp -- 
        s -- 
        _ctx -- The request context for the invocation."""
        def finished(self, rsp, s, _ctx=None):
            return _M_omero.cmd.CmdCallback._op_finished.invoke(self, ((rsp, s), _ctx))

        """Called when the command has completed in any fashion
        including cancellation. The Status#flags list will
        contain information about whether or not the process
        was cancelled.
        Arguments:
        rsp -- 
        s -- 
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation."""
        def begin_finished(self, rsp, s, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.cmd.CmdCallback._op_finished.begin(self, ((rsp, s), _response, _ex, _sent, _ctx))

        """Called when the command has completed in any fashion
        including cancellation. The Status#flags list will
        contain information about whether or not the process
        was cancelled.
        Arguments:
        rsp -- 
        s -- """
        def end_finished(self, _r):
            return _M_omero.cmd.CmdCallback._op_finished.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.CmdCallbackPrx.ice_checkedCast(proxy, '::omero::cmd::CmdCallback', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.CmdCallbackPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::cmd::CmdCallback'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.cmd._t_CmdCallbackPrx = IcePy.defineProxy('::omero::cmd::CmdCallback', CmdCallbackPrx)

    _M_omero.cmd._t_CmdCallback = IcePy.defineClass('::omero::cmd::CmdCallback', CmdCallback, -1, (), True, False, None, (), ())
    CmdCallback._ice_type = _M_omero.cmd._t_CmdCallback

    CmdCallback._op_step = IcePy.Operation('step', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)), (), None, ())
    CmdCallback._op_finished = IcePy.Operation('finished', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.cmd._t_Response, False, 0), ((), _M_omero.cmd._t_Status, False, 0)), (), None, ())

    _M_omero.cmd.CmdCallback = CmdCallback
    del CmdCallback

    _M_omero.cmd.CmdCallbackPrx = CmdCallbackPrx
    del CmdCallbackPrx

if 'Handle' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.Handle = Ice.createTempClass()
    class Handle(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_omero.cmd.Handle:
                raise RuntimeError('omero.cmd.Handle is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::Handle')

        def ice_id(self, current=None):
            return '::omero::cmd::Handle'

        def ice_staticId():
            return '::omero::cmd::Handle'
        ice_staticId = staticmethod(ice_staticId)

        def addCallback(self, cb, current=None):
            """Add a callback for notifications.
            Arguments:
            cb -- 
            current -- The Current object for the invocation."""
            pass

        def removeCallback(self, cb, current=None):
            """Remove callback for notifications.
            Arguments:
            cb -- 
            current -- The Current object for the invocation."""
            pass

        def getRequest(self, current=None):
            """Returns the request object that was used to
            initialize this handle. Never null.
            Arguments:
            current -- The Current object for the invocation."""
            pass

        def getResponse(self, current=None):
            """Returns a response if this handle has finished
            execution, otherwise returns null.
            Arguments:
            current -- The Current object for the invocation."""
            pass

        def getStatus(self, current=None):
            """Returns a status object for the current execution.
            This will likely be the same object that would be
            returned as a component of the Response value.
            Never null.
            Arguments:
            current -- The Current object for the invocation."""
            pass

        def cancel(self, current=None):
            """Attempts to cancel execution of this Request. Returns
            true if cancellation was successful. Returns false if not,
            in which case likely this request will run to completion.
            Arguments:
            current -- The Current object for the invocation."""
            pass

        def close(self, current=None):
            """Closes this handle. If the request is running, then a
            cancellation will be attempted first. All uses of a handle
            should be surrounded by a try/finally close block.
            Arguments:
            current -- The Current object for the invocation."""
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_Handle)

        __repr__ = __str__

    _M_omero.cmd.HandlePrx = Ice.createTempClass()
    class HandlePrx(Ice.ObjectPrx):

        """Add a callback for notifications.
        Arguments:
        cb -- 
        _ctx -- The request context for the invocation."""
        def addCallback(self, cb, _ctx=None):
            return _M_omero.cmd.Handle._op_addCallback.invoke(self, ((cb, ), _ctx))

        """Add a callback for notifications.
        Arguments:
        cb -- 
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation."""
        def begin_addCallback(self, cb, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.cmd.Handle._op_addCallback.begin(self, ((cb, ), _response, _ex, _sent, _ctx))

        """Add a callback for notifications.
        Arguments:
        cb -- """
        def end_addCallback(self, _r):
            return _M_omero.cmd.Handle._op_addCallback.end(self, _r)

        """Remove callback for notifications.
        Arguments:
        cb -- 
        _ctx -- The request context for the invocation."""
        def removeCallback(self, cb, _ctx=None):
            return _M_omero.cmd.Handle._op_removeCallback.invoke(self, ((cb, ), _ctx))

        """Remove callback for notifications.
        Arguments:
        cb -- 
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation."""
        def begin_removeCallback(self, cb, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.cmd.Handle._op_removeCallback.begin(self, ((cb, ), _response, _ex, _sent, _ctx))

        """Remove callback for notifications.
        Arguments:
        cb -- """
        def end_removeCallback(self, _r):
            return _M_omero.cmd.Handle._op_removeCallback.end(self, _r)

        """Returns the request object that was used to
        initialize this handle. Never null.
        Arguments:
        _ctx -- The request context for the invocation."""
        def getRequest(self, _ctx=None):
            return _M_omero.cmd.Handle._op_getRequest.invoke(self, ((), _ctx))

        """Returns the request object that was used to
        initialize this handle. Never null.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation."""
        def begin_getRequest(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.cmd.Handle._op_getRequest.begin(self, ((), _response, _ex, _sent, _ctx))

        """Returns the request object that was used to
        initialize this handle. Never null.
        Arguments:"""
        def end_getRequest(self, _r):
            return _M_omero.cmd.Handle._op_getRequest.end(self, _r)

        """Returns a response if this handle has finished
        execution, otherwise returns null.
        Arguments:
        _ctx -- The request context for the invocation."""
        def getResponse(self, _ctx=None):
            return _M_omero.cmd.Handle._op_getResponse.invoke(self, ((), _ctx))

        """Returns a response if this handle has finished
        execution, otherwise returns null.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation."""
        def begin_getResponse(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.cmd.Handle._op_getResponse.begin(self, ((), _response, _ex, _sent, _ctx))

        """Returns a response if this handle has finished
        execution, otherwise returns null.
        Arguments:"""
        def end_getResponse(self, _r):
            return _M_omero.cmd.Handle._op_getResponse.end(self, _r)

        """Returns a status object for the current execution.
        This will likely be the same object that would be
        returned as a component of the Response value.
        Never null.
        Arguments:
        _ctx -- The request context for the invocation."""
        def getStatus(self, _ctx=None):
            return _M_omero.cmd.Handle._op_getStatus.invoke(self, ((), _ctx))

        """Returns a status object for the current execution.
        This will likely be the same object that would be
        returned as a component of the Response value.
        Never null.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation."""
        def begin_getStatus(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.cmd.Handle._op_getStatus.begin(self, ((), _response, _ex, _sent, _ctx))

        """Returns a status object for the current execution.
        This will likely be the same object that would be
        returned as a component of the Response value.
        Never null.
        Arguments:"""
        def end_getStatus(self, _r):
            return _M_omero.cmd.Handle._op_getStatus.end(self, _r)

        """Attempts to cancel execution of this Request. Returns
        true if cancellation was successful. Returns false if not,
        in which case likely this request will run to completion.
        Arguments:
        _ctx -- The request context for the invocation."""
        def cancel(self, _ctx=None):
            return _M_omero.cmd.Handle._op_cancel.invoke(self, ((), _ctx))

        """Attempts to cancel execution of this Request. Returns
        true if cancellation was successful. Returns false if not,
        in which case likely this request will run to completion.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation."""
        def begin_cancel(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.cmd.Handle._op_cancel.begin(self, ((), _response, _ex, _sent, _ctx))

        """Attempts to cancel execution of this Request. Returns
        true if cancellation was successful. Returns false if not,
        in which case likely this request will run to completion.
        Arguments:"""
        def end_cancel(self, _r):
            return _M_omero.cmd.Handle._op_cancel.end(self, _r)

        """Closes this handle. If the request is running, then a
        cancellation will be attempted first. All uses of a handle
        should be surrounded by a try/finally close block.
        Arguments:
        _ctx -- The request context for the invocation."""
        def close(self, _ctx=None):
            return _M_omero.cmd.Handle._op_close.invoke(self, ((), _ctx))

        """Closes this handle. If the request is running, then a
        cancellation will be attempted first. All uses of a handle
        should be surrounded by a try/finally close block.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation."""
        def begin_close(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.cmd.Handle._op_close.begin(self, ((), _response, _ex, _sent, _ctx))

        """Closes this handle. If the request is running, then a
        cancellation will be attempted first. All uses of a handle
        should be surrounded by a try/finally close block.
        Arguments:"""
        def end_close(self, _r):
            return _M_omero.cmd.Handle._op_close.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.HandlePrx.ice_checkedCast(proxy, '::omero::cmd::Handle', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.HandlePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::cmd::Handle'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.cmd._t_HandlePrx = IcePy.defineProxy('::omero::cmd::Handle', HandlePrx)

    _M_omero.cmd._t_Handle = IcePy.defineClass('::omero::cmd::Handle', Handle, -1, (), True, False, None, (), ())
    Handle._ice_type = _M_omero.cmd._t_Handle

    Handle._op_addCallback = IcePy.Operation('addCallback', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.cmd._t_CmdCallbackPrx, False, 0),), (), None, ())
    Handle._op_removeCallback = IcePy.Operation('removeCallback', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.cmd._t_CmdCallbackPrx, False, 0),), (), None, ())
    Handle._op_getRequest = IcePy.Operation('getRequest', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.cmd._t_Request, False, 0), ())
    Handle._op_getResponse = IcePy.Operation('getResponse', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.cmd._t_Response, False, 0), ())
    Handle._op_getStatus = IcePy.Operation('getStatus', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.cmd._t_Status, False, 0), ())
    Handle._op_cancel = IcePy.Operation('cancel', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_bool, False, 0), (_M_omero._t_LockTimeout,))
    Handle._op_close = IcePy.Operation('close', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())

    _M_omero.cmd.Handle = Handle
    del Handle

    _M_omero.cmd.HandlePrx = HandlePrx
    del HandlePrx

if '_t_HandleList' not in _M_omero.cmd.__dict__:
    _M_omero.cmd._t_HandleList = IcePy.defineSequence('::omero::cmd::HandleList', (), _M_omero.cmd._t_HandlePrx)

if 'Session' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.Session = Ice.createTempClass()
    class Session(_M_Glacier2.Session):
        """Starting point for all command-based OMERO.blitz interaction."""
        def __init__(self):
            if Ice.getType(self) == _M_omero.cmd.Session:
                raise RuntimeError('omero.cmd.Session is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::Session', '::Ice::Object', '::omero::cmd::Session')

        def ice_id(self, current=None):
            return '::omero::cmd::Session'

        def ice_staticId():
            return '::omero::cmd::Session'
        ice_staticId = staticmethod(ice_staticId)

        def submit_async(self, _cb, req, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_Session)

        __repr__ = __str__

    _M_omero.cmd.SessionPrx = Ice.createTempClass()
    class SessionPrx(_M_Glacier2.SessionPrx):

        def submit(self, req, _ctx=None):
            return _M_omero.cmd.Session._op_submit.invoke(self, ((req, ), _ctx))

        def begin_submit(self, req, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.cmd.Session._op_submit.begin(self, ((req, ), _response, _ex, _sent, _ctx))

        def end_submit(self, _r):
            return _M_omero.cmd.Session._op_submit.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.SessionPrx.ice_checkedCast(proxy, '::omero::cmd::Session', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.SessionPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::cmd::Session'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.cmd._t_SessionPrx = IcePy.defineProxy('::omero::cmd::Session', SessionPrx)

    _M_omero.cmd._t_Session = IcePy.defineClass('::omero::cmd::Session', Session, -1, (), True, False, None, (_M_Glacier2._t_Session,), ())
    Session._ice_type = _M_omero.cmd._t_Session

    Session._op_submit = IcePy.Operation('submit', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_omero.cmd._t_Request, False, 0),), (), ((), _M_omero.cmd._t_HandlePrx, False, 0), ())

    _M_omero.cmd.Session = Session
    del Session

    _M_omero.cmd.SessionPrx = SessionPrx
    del SessionPrx

# End of module omero.cmd

__name__ = 'omero'

# End of module omero
