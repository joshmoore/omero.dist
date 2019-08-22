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
# Generated from file `TransmittanceRange.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy
import omero_model_IObject_ice
import omero_RTypes_ice
import omero_model_RTypes_ice
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

if 'Length' not in _M_omero.model.__dict__:
    _M_omero.model._t_Length = IcePy.declareClass('::omero::model::Length')
    _M_omero.model._t_LengthPrx = IcePy.declareProxy('::omero::model::Length')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if 'TransmittanceRange' not in _M_omero.model.__dict__:
    _M_omero.model.TransmittanceRange = Ice.createTempClass()
    class TransmittanceRange(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _cutIn=None, _cutOut=None, _cutInTolerance=None, _cutOutTolerance=None, _transmittance=None):
            if Ice.getType(self) == _M_omero.model.TransmittanceRange:
                raise RuntimeError('omero.model.TransmittanceRange is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._cutIn = _cutIn
            self._cutOut = _cutOut
            self._cutInTolerance = _cutInTolerance
            self._cutOutTolerance = _cutOutTolerance
            self._transmittance = _transmittance

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::IObject', '::omero::model::TransmittanceRange')

        def ice_id(self, current=None):
            return '::omero::model::TransmittanceRange'

        def ice_staticId():
            return '::omero::model::TransmittanceRange'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getCutIn(self, current=None):
            pass

        def setCutIn(self, theCutIn, current=None):
            pass

        def getCutOut(self, current=None):
            pass

        def setCutOut(self, theCutOut, current=None):
            pass

        def getCutInTolerance(self, current=None):
            pass

        def setCutInTolerance(self, theCutInTolerance, current=None):
            pass

        def getCutOutTolerance(self, current=None):
            pass

        def setCutOutTolerance(self, theCutOutTolerance, current=None):
            pass

        def getTransmittance(self, current=None):
            pass

        def setTransmittance(self, theTransmittance, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_TransmittanceRange)

        __repr__ = __str__

    _M_omero.model.TransmittanceRangePrx = Ice.createTempClass()
    class TransmittanceRangePrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.TransmittanceRange._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.TransmittanceRange._op_setVersion.end(self, _r)

        def getCutIn(self, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_getCutIn.invoke(self, ((), _ctx))

        def begin_getCutIn(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_getCutIn.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getCutIn(self, _r):
            return _M_omero.model.TransmittanceRange._op_getCutIn.end(self, _r)

        def setCutIn(self, theCutIn, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_setCutIn.invoke(self, ((theCutIn, ), _ctx))

        def begin_setCutIn(self, theCutIn, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_setCutIn.begin(self, ((theCutIn, ), _response, _ex, _sent, _ctx))

        def end_setCutIn(self, _r):
            return _M_omero.model.TransmittanceRange._op_setCutIn.end(self, _r)

        def getCutOut(self, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_getCutOut.invoke(self, ((), _ctx))

        def begin_getCutOut(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_getCutOut.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getCutOut(self, _r):
            return _M_omero.model.TransmittanceRange._op_getCutOut.end(self, _r)

        def setCutOut(self, theCutOut, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_setCutOut.invoke(self, ((theCutOut, ), _ctx))

        def begin_setCutOut(self, theCutOut, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_setCutOut.begin(self, ((theCutOut, ), _response, _ex, _sent, _ctx))

        def end_setCutOut(self, _r):
            return _M_omero.model.TransmittanceRange._op_setCutOut.end(self, _r)

        def getCutInTolerance(self, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_getCutInTolerance.invoke(self, ((), _ctx))

        def begin_getCutInTolerance(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_getCutInTolerance.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getCutInTolerance(self, _r):
            return _M_omero.model.TransmittanceRange._op_getCutInTolerance.end(self, _r)

        def setCutInTolerance(self, theCutInTolerance, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_setCutInTolerance.invoke(self, ((theCutInTolerance, ), _ctx))

        def begin_setCutInTolerance(self, theCutInTolerance, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_setCutInTolerance.begin(self, ((theCutInTolerance, ), _response, _ex, _sent, _ctx))

        def end_setCutInTolerance(self, _r):
            return _M_omero.model.TransmittanceRange._op_setCutInTolerance.end(self, _r)

        def getCutOutTolerance(self, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_getCutOutTolerance.invoke(self, ((), _ctx))

        def begin_getCutOutTolerance(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_getCutOutTolerance.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getCutOutTolerance(self, _r):
            return _M_omero.model.TransmittanceRange._op_getCutOutTolerance.end(self, _r)

        def setCutOutTolerance(self, theCutOutTolerance, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_setCutOutTolerance.invoke(self, ((theCutOutTolerance, ), _ctx))

        def begin_setCutOutTolerance(self, theCutOutTolerance, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_setCutOutTolerance.begin(self, ((theCutOutTolerance, ), _response, _ex, _sent, _ctx))

        def end_setCutOutTolerance(self, _r):
            return _M_omero.model.TransmittanceRange._op_setCutOutTolerance.end(self, _r)

        def getTransmittance(self, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_getTransmittance.invoke(self, ((), _ctx))

        def begin_getTransmittance(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_getTransmittance.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getTransmittance(self, _r):
            return _M_omero.model.TransmittanceRange._op_getTransmittance.end(self, _r)

        def setTransmittance(self, theTransmittance, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_setTransmittance.invoke(self, ((theTransmittance, ), _ctx))

        def begin_setTransmittance(self, theTransmittance, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TransmittanceRange._op_setTransmittance.begin(self, ((theTransmittance, ), _response, _ex, _sent, _ctx))

        def end_setTransmittance(self, _r):
            return _M_omero.model.TransmittanceRange._op_setTransmittance.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.TransmittanceRangePrx.ice_checkedCast(proxy, '::omero::model::TransmittanceRange', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.TransmittanceRangePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::TransmittanceRange'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_TransmittanceRangePrx = IcePy.defineProxy('::omero::model::TransmittanceRange', TransmittanceRangePrx)

    _M_omero.model._t_TransmittanceRange = IcePy.declareClass('::omero::model::TransmittanceRange')

    _M_omero.model._t_TransmittanceRange = IcePy.defineClass('::omero::model::TransmittanceRange', TransmittanceRange, -1, (), True, False, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt, False, 0),
        ('_cutIn', (), _M_omero.model._t_Length, False, 0),
        ('_cutOut', (), _M_omero.model._t_Length, False, 0),
        ('_cutInTolerance', (), _M_omero.model._t_Length, False, 0),
        ('_cutOutTolerance', (), _M_omero.model._t_Length, False, 0),
        ('_transmittance', (), _M_omero._t_RDouble, False, 0)
    ))
    TransmittanceRange._ice_type = _M_omero.model._t_TransmittanceRange

    TransmittanceRange._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RInt, False, 0), ())
    TransmittanceRange._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RInt, False, 0),), (), None, ())
    TransmittanceRange._op_getCutIn = IcePy.Operation('getCutIn', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Length, False, 0), ())
    TransmittanceRange._op_setCutIn = IcePy.Operation('setCutIn', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Length, False, 0),), (), None, ())
    TransmittanceRange._op_getCutOut = IcePy.Operation('getCutOut', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Length, False, 0), ())
    TransmittanceRange._op_setCutOut = IcePy.Operation('setCutOut', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Length, False, 0),), (), None, ())
    TransmittanceRange._op_getCutInTolerance = IcePy.Operation('getCutInTolerance', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Length, False, 0), ())
    TransmittanceRange._op_setCutInTolerance = IcePy.Operation('setCutInTolerance', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Length, False, 0),), (), None, ())
    TransmittanceRange._op_getCutOutTolerance = IcePy.Operation('getCutOutTolerance', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Length, False, 0), ())
    TransmittanceRange._op_setCutOutTolerance = IcePy.Operation('setCutOutTolerance', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Length, False, 0),), (), None, ())
    TransmittanceRange._op_getTransmittance = IcePy.Operation('getTransmittance', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    TransmittanceRange._op_setTransmittance = IcePy.Operation('setTransmittance', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())

    _M_omero.model.TransmittanceRange = TransmittanceRange
    del TransmittanceRange

    _M_omero.model.TransmittanceRangePrx = TransmittanceRangePrx
    del TransmittanceRangePrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
