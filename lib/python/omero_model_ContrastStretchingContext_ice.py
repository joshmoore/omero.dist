# **********************************************************************
#
# Copyright (c) 2003-2011 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.4.2
#
# <auto-generated>
#
# Generated from file `ContrastStretchingContext.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy, __builtin__
import omero_model_IObject_ice
import omero_RTypes_ice
import omero_model_RTypes_ice
import omero_System_ice
import omero_Collections_ice
import omero_model_CodomainMapContext_ice

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

if not _M_omero.model.__dict__.has_key('RenderingDef'):
    _M_omero.model._t_RenderingDef = IcePy.declareClass('::omero::model::RenderingDef')
    _M_omero.model._t_RenderingDefPrx = IcePy.declareProxy('::omero::model::RenderingDef')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('ContrastStretchingContext'):
    _M_omero.model.ContrastStretchingContext = Ice.createTempClass()
    class ContrastStretchingContext(_M_omero.model.CodomainMapContext):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _renderingDef=None, _xstart=None, _ystart=None, _xend=None, _yend=None):
            if __builtin__.type(self) == _M_omero.model.ContrastStretchingContext:
                raise RuntimeError('omero.model.ContrastStretchingContext is an abstract class')
            _M_omero.model.CodomainMapContext.__init__(self, _id, _details, _loaded, _version, _renderingDef)
            self._xstart = _xstart
            self._ystart = _ystart
            self._xend = _xend
            self._yend = _yend

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::CodomainMapContext', '::omero::model::ContrastStretchingContext', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::ContrastStretchingContext'

        def ice_staticId():
            return '::omero::model::ContrastStretchingContext'
        ice_staticId = staticmethod(ice_staticId)

        def getXstart(self, current=None):
            pass

        def setXstart(self, theXstart, current=None):
            pass

        def getYstart(self, current=None):
            pass

        def setYstart(self, theYstart, current=None):
            pass

        def getXend(self, current=None):
            pass

        def setXend(self, theXend, current=None):
            pass

        def getYend(self, current=None):
            pass

        def setYend(self, theYend, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_ContrastStretchingContext)

        __repr__ = __str__

    _M_omero.model.ContrastStretchingContextPrx = Ice.createTempClass()
    class ContrastStretchingContextPrx(_M_omero.model.CodomainMapContextPrx):

        def getXstart(self, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_getXstart.invoke(self, ((), _ctx))

        def begin_getXstart(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_getXstart.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getXstart(self, _r):
            return _M_omero.model.ContrastStretchingContext._op_getXstart.end(self, _r)

        def setXstart(self, theXstart, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_setXstart.invoke(self, ((theXstart, ), _ctx))

        def begin_setXstart(self, theXstart, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_setXstart.begin(self, ((theXstart, ), _response, _ex, _sent, _ctx))

        def end_setXstart(self, _r):
            return _M_omero.model.ContrastStretchingContext._op_setXstart.end(self, _r)

        def getYstart(self, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_getYstart.invoke(self, ((), _ctx))

        def begin_getYstart(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_getYstart.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getYstart(self, _r):
            return _M_omero.model.ContrastStretchingContext._op_getYstart.end(self, _r)

        def setYstart(self, theYstart, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_setYstart.invoke(self, ((theYstart, ), _ctx))

        def begin_setYstart(self, theYstart, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_setYstart.begin(self, ((theYstart, ), _response, _ex, _sent, _ctx))

        def end_setYstart(self, _r):
            return _M_omero.model.ContrastStretchingContext._op_setYstart.end(self, _r)

        def getXend(self, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_getXend.invoke(self, ((), _ctx))

        def begin_getXend(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_getXend.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getXend(self, _r):
            return _M_omero.model.ContrastStretchingContext._op_getXend.end(self, _r)

        def setXend(self, theXend, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_setXend.invoke(self, ((theXend, ), _ctx))

        def begin_setXend(self, theXend, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_setXend.begin(self, ((theXend, ), _response, _ex, _sent, _ctx))

        def end_setXend(self, _r):
            return _M_omero.model.ContrastStretchingContext._op_setXend.end(self, _r)

        def getYend(self, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_getYend.invoke(self, ((), _ctx))

        def begin_getYend(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_getYend.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getYend(self, _r):
            return _M_omero.model.ContrastStretchingContext._op_getYend.end(self, _r)

        def setYend(self, theYend, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_setYend.invoke(self, ((theYend, ), _ctx))

        def begin_setYend(self, theYend, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ContrastStretchingContext._op_setYend.begin(self, ((theYend, ), _response, _ex, _sent, _ctx))

        def end_setYend(self, _r):
            return _M_omero.model.ContrastStretchingContext._op_setYend.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.ContrastStretchingContextPrx.ice_checkedCast(proxy, '::omero::model::ContrastStretchingContext', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.ContrastStretchingContextPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_ContrastStretchingContextPrx = IcePy.defineProxy('::omero::model::ContrastStretchingContext', ContrastStretchingContextPrx)

    _M_omero.model._t_ContrastStretchingContext = IcePy.declareClass('::omero::model::ContrastStretchingContext')

    _M_omero.model._t_ContrastStretchingContext = IcePy.defineClass('::omero::model::ContrastStretchingContext', ContrastStretchingContext, (), True, _M_omero.model._t_CodomainMapContext, (), (
        ('_xstart', (), _M_omero._t_RInt),
        ('_ystart', (), _M_omero._t_RInt),
        ('_xend', (), _M_omero._t_RInt),
        ('_yend', (), _M_omero._t_RInt)
    ))
    ContrastStretchingContext._ice_type = _M_omero.model._t_ContrastStretchingContext

    ContrastStretchingContext._op_getXstart = IcePy.Operation('getXstart', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    ContrastStretchingContext._op_setXstart = IcePy.Operation('setXstart', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())
    ContrastStretchingContext._op_getYstart = IcePy.Operation('getYstart', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    ContrastStretchingContext._op_setYstart = IcePy.Operation('setYstart', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())
    ContrastStretchingContext._op_getXend = IcePy.Operation('getXend', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    ContrastStretchingContext._op_setXend = IcePy.Operation('setXend', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())
    ContrastStretchingContext._op_getYend = IcePy.Operation('getYend', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    ContrastStretchingContext._op_setYend = IcePy.Operation('setYend', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())

    _M_omero.model.ContrastStretchingContext = ContrastStretchingContext
    del ContrastStretchingContext

    _M_omero.model.ContrastStretchingContextPrx = ContrastStretchingContextPrx
    del ContrastStretchingContextPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
