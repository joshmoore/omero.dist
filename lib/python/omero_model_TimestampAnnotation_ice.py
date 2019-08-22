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
# Generated from file `TimestampAnnotation.ice'
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
import omero_model_BasicAnnotation_ice

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

if 'AnnotationAnnotationLink' not in _M_omero.model.__dict__:
    _M_omero.model._t_AnnotationAnnotationLink = IcePy.declareClass('::omero::model::AnnotationAnnotationLink')
    _M_omero.model._t_AnnotationAnnotationLinkPrx = IcePy.declareProxy('::omero::model::AnnotationAnnotationLink')

if 'Annotation' not in _M_omero.model.__dict__:
    _M_omero.model._t_Annotation = IcePy.declareClass('::omero::model::Annotation')
    _M_omero.model._t_AnnotationPrx = IcePy.declareProxy('::omero::model::Annotation')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if 'TimestampAnnotation' not in _M_omero.model.__dict__:
    _M_omero.model.TimestampAnnotation = Ice.createTempClass()
    class TimestampAnnotation(_M_omero.model.BasicAnnotation):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _ns=None, _name=None, _description=None, _annotationLinksSeq=None, _annotationLinksLoaded=False, _annotationLinksCountPerOwner=None, _timeValue=None):
            if Ice.getType(self) == _M_omero.model.TimestampAnnotation:
                raise RuntimeError('omero.model.TimestampAnnotation is an abstract class')
            _M_omero.model.BasicAnnotation.__init__(self, _id, _details, _loaded, _version, _ns, _name, _description, _annotationLinksSeq, _annotationLinksLoaded, _annotationLinksCountPerOwner)
            self._timeValue = _timeValue

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Annotation', '::omero::model::BasicAnnotation', '::omero::model::IObject', '::omero::model::TimestampAnnotation')

        def ice_id(self, current=None):
            return '::omero::model::TimestampAnnotation'

        def ice_staticId():
            return '::omero::model::TimestampAnnotation'
        ice_staticId = staticmethod(ice_staticId)

        def getTimeValue(self, current=None):
            pass

        def setTimeValue(self, theTimeValue, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_TimestampAnnotation)

        __repr__ = __str__

    _M_omero.model.TimestampAnnotationPrx = Ice.createTempClass()
    class TimestampAnnotationPrx(_M_omero.model.BasicAnnotationPrx):

        def getTimeValue(self, _ctx=None):
            return _M_omero.model.TimestampAnnotation._op_getTimeValue.invoke(self, ((), _ctx))

        def begin_getTimeValue(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TimestampAnnotation._op_getTimeValue.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getTimeValue(self, _r):
            return _M_omero.model.TimestampAnnotation._op_getTimeValue.end(self, _r)

        def setTimeValue(self, theTimeValue, _ctx=None):
            return _M_omero.model.TimestampAnnotation._op_setTimeValue.invoke(self, ((theTimeValue, ), _ctx))

        def begin_setTimeValue(self, theTimeValue, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TimestampAnnotation._op_setTimeValue.begin(self, ((theTimeValue, ), _response, _ex, _sent, _ctx))

        def end_setTimeValue(self, _r):
            return _M_omero.model.TimestampAnnotation._op_setTimeValue.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.TimestampAnnotationPrx.ice_checkedCast(proxy, '::omero::model::TimestampAnnotation', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.TimestampAnnotationPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::TimestampAnnotation'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_TimestampAnnotationPrx = IcePy.defineProxy('::omero::model::TimestampAnnotation', TimestampAnnotationPrx)

    _M_omero.model._t_TimestampAnnotation = IcePy.declareClass('::omero::model::TimestampAnnotation')

    _M_omero.model._t_TimestampAnnotation = IcePy.defineClass('::omero::model::TimestampAnnotation', TimestampAnnotation, -1, (), True, False, _M_omero.model._t_BasicAnnotation, (), (('_timeValue', (), _M_omero._t_RTime, False, 0),))
    TimestampAnnotation._ice_type = _M_omero.model._t_TimestampAnnotation

    TimestampAnnotation._op_getTimeValue = IcePy.Operation('getTimeValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RTime, False, 0), ())
    TimestampAnnotation._op_setTimeValue = IcePy.Operation('setTimeValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RTime, False, 0),), (), None, ())

    _M_omero.model.TimestampAnnotation = TimestampAnnotation
    del TimestampAnnotation

    _M_omero.model.TimestampAnnotationPrx = TimestampAnnotationPrx
    del TimestampAnnotationPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
