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
# Generated from file `EventLog.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy
import omero_model_IObject_ice
import omero_RTypes_ice
import omero_System_ice
import omero_Collections_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Start of module omero
__name__ = 'omero'

# Start of module omero.model
__name__ = 'omero.model'

if 'Event' not in _M_omero.model.__dict__:
    _M_omero.model._t_Event = IcePy.declareClass('::omero::model::Event')
    _M_omero.model._t_EventPrx = IcePy.declareProxy('::omero::model::Event')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if 'EventLog' not in _M_omero.model.__dict__:
    _M_omero.model.EventLog = Ice.createTempClass()
    class EventLog(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _entityId=None, _entityType=None, _action=None, _event=None):
            if Ice.getType(self) == _M_omero.model.EventLog:
                raise RuntimeError('omero.model.EventLog is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._entityId = _entityId
            self._entityType = _entityType
            self._action = _action
            self._event = _event

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::EventLog', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::EventLog'

        def ice_staticId():
            return '::omero::model::EventLog'
        ice_staticId = staticmethod(ice_staticId)

        def getEntityId(self, current=None):
            pass

        def setEntityId(self, theEntityId, current=None):
            pass

        def getEntityType(self, current=None):
            pass

        def setEntityType(self, theEntityType, current=None):
            pass

        def getAction(self, current=None):
            pass

        def setAction(self, theAction, current=None):
            pass

        def getEvent(self, current=None):
            pass

        def setEvent(self, theEvent, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_EventLog)

        __repr__ = __str__

    _M_omero.model.EventLogPrx = Ice.createTempClass()
    class EventLogPrx(_M_omero.model.IObjectPrx):

        def getEntityId(self, _ctx=None):
            return _M_omero.model.EventLog._op_getEntityId.invoke(self, ((), _ctx))

        def begin_getEntityId(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.EventLog._op_getEntityId.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getEntityId(self, _r):
            return _M_omero.model.EventLog._op_getEntityId.end(self, _r)

        def setEntityId(self, theEntityId, _ctx=None):
            return _M_omero.model.EventLog._op_setEntityId.invoke(self, ((theEntityId, ), _ctx))

        def begin_setEntityId(self, theEntityId, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.EventLog._op_setEntityId.begin(self, ((theEntityId, ), _response, _ex, _sent, _ctx))

        def end_setEntityId(self, _r):
            return _M_omero.model.EventLog._op_setEntityId.end(self, _r)

        def getEntityType(self, _ctx=None):
            return _M_omero.model.EventLog._op_getEntityType.invoke(self, ((), _ctx))

        def begin_getEntityType(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.EventLog._op_getEntityType.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getEntityType(self, _r):
            return _M_omero.model.EventLog._op_getEntityType.end(self, _r)

        def setEntityType(self, theEntityType, _ctx=None):
            return _M_omero.model.EventLog._op_setEntityType.invoke(self, ((theEntityType, ), _ctx))

        def begin_setEntityType(self, theEntityType, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.EventLog._op_setEntityType.begin(self, ((theEntityType, ), _response, _ex, _sent, _ctx))

        def end_setEntityType(self, _r):
            return _M_omero.model.EventLog._op_setEntityType.end(self, _r)

        def getAction(self, _ctx=None):
            return _M_omero.model.EventLog._op_getAction.invoke(self, ((), _ctx))

        def begin_getAction(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.EventLog._op_getAction.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getAction(self, _r):
            return _M_omero.model.EventLog._op_getAction.end(self, _r)

        def setAction(self, theAction, _ctx=None):
            return _M_omero.model.EventLog._op_setAction.invoke(self, ((theAction, ), _ctx))

        def begin_setAction(self, theAction, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.EventLog._op_setAction.begin(self, ((theAction, ), _response, _ex, _sent, _ctx))

        def end_setAction(self, _r):
            return _M_omero.model.EventLog._op_setAction.end(self, _r)

        def getEvent(self, _ctx=None):
            return _M_omero.model.EventLog._op_getEvent.invoke(self, ((), _ctx))

        def begin_getEvent(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.EventLog._op_getEvent.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getEvent(self, _r):
            return _M_omero.model.EventLog._op_getEvent.end(self, _r)

        def setEvent(self, theEvent, _ctx=None):
            return _M_omero.model.EventLog._op_setEvent.invoke(self, ((theEvent, ), _ctx))

        def begin_setEvent(self, theEvent, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.EventLog._op_setEvent.begin(self, ((theEvent, ), _response, _ex, _sent, _ctx))

        def end_setEvent(self, _r):
            return _M_omero.model.EventLog._op_setEvent.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.EventLogPrx.ice_checkedCast(proxy, '::omero::model::EventLog', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.EventLogPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_EventLogPrx = IcePy.defineProxy('::omero::model::EventLog', EventLogPrx)

    _M_omero.model._t_EventLog = IcePy.declareClass('::omero::model::EventLog')

    _M_omero.model._t_EventLog = IcePy.defineClass('::omero::model::EventLog', EventLog, -1, (), True, False, _M_omero.model._t_IObject, (), (
        ('_entityId', (), _M_omero._t_RLong, False, 0),
        ('_entityType', (), _M_omero._t_RString, False, 0),
        ('_action', (), _M_omero._t_RString, False, 0),
        ('_event', (), _M_omero.model._t_Event, False, 0)
    ))
    EventLog._ice_type = _M_omero.model._t_EventLog

    EventLog._op_getEntityId = IcePy.Operation('getEntityId', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RLong, False, 0), ())
    EventLog._op_setEntityId = IcePy.Operation('setEntityId', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RLong, False, 0),), (), None, ())
    EventLog._op_getEntityType = IcePy.Operation('getEntityType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    EventLog._op_setEntityType = IcePy.Operation('setEntityType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    EventLog._op_getAction = IcePy.Operation('getAction', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    EventLog._op_setAction = IcePy.Operation('setAction', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    EventLog._op_getEvent = IcePy.Operation('getEvent', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Event, False, 0), ())
    EventLog._op_setEvent = IcePy.Operation('setEvent', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Event, False, 0),), (), None, ())

    _M_omero.model.EventLog = EventLog
    del EventLog

    _M_omero.model.EventLogPrx = EventLogPrx
    del EventLogPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
