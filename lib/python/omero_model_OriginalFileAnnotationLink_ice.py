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
# Generated from file `OriginalFileAnnotationLink.ice'
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

if not _M_omero.model.__dict__.has_key('OriginalFile'):
    _M_omero.model._t_OriginalFile = IcePy.declareClass('::omero::model::OriginalFile')
    _M_omero.model._t_OriginalFilePrx = IcePy.declareProxy('::omero::model::OriginalFile')

if not _M_omero.model.__dict__.has_key('Annotation'):
    _M_omero.model._t_Annotation = IcePy.declareClass('::omero::model::Annotation')
    _M_omero.model._t_AnnotationPrx = IcePy.declareProxy('::omero::model::Annotation')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('OriginalFileAnnotationLink'):
    _M_omero.model.OriginalFileAnnotationLink = Ice.createTempClass()
    class OriginalFileAnnotationLink(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _parent=None, _child=None):
            if __builtin__.type(self) == _M_omero.model.OriginalFileAnnotationLink:
                raise RuntimeError('omero.model.OriginalFileAnnotationLink is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._parent = _parent
            self._child = _child

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::IObject', '::omero::model::OriginalFileAnnotationLink')

        def ice_id(self, current=None):
            return '::omero::model::OriginalFileAnnotationLink'

        def ice_staticId():
            return '::omero::model::OriginalFileAnnotationLink'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getParent(self, current=None):
            pass

        def setParent(self, theParent, current=None):
            pass

        def getChild(self, current=None):
            pass

        def setChild(self, theChild, current=None):
            pass

        def link(self, theParent, theChild, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_OriginalFileAnnotationLink)

        __repr__ = __str__

    _M_omero.model.OriginalFileAnnotationLinkPrx = Ice.createTempClass()
    class OriginalFileAnnotationLinkPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.OriginalFileAnnotationLink._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.OriginalFileAnnotationLink._op_setVersion.end(self, _r)

        def getParent(self, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_getParent.invoke(self, ((), _ctx))

        def begin_getParent(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_getParent.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getParent(self, _r):
            return _M_omero.model.OriginalFileAnnotationLink._op_getParent.end(self, _r)

        def setParent(self, theParent, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_setParent.invoke(self, ((theParent, ), _ctx))

        def begin_setParent(self, theParent, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_setParent.begin(self, ((theParent, ), _response, _ex, _sent, _ctx))

        def end_setParent(self, _r):
            return _M_omero.model.OriginalFileAnnotationLink._op_setParent.end(self, _r)

        def getChild(self, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_getChild.invoke(self, ((), _ctx))

        def begin_getChild(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_getChild.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getChild(self, _r):
            return _M_omero.model.OriginalFileAnnotationLink._op_getChild.end(self, _r)

        def setChild(self, theChild, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_setChild.invoke(self, ((theChild, ), _ctx))

        def begin_setChild(self, theChild, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_setChild.begin(self, ((theChild, ), _response, _ex, _sent, _ctx))

        def end_setChild(self, _r):
            return _M_omero.model.OriginalFileAnnotationLink._op_setChild.end(self, _r)

        def link(self, theParent, theChild, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_link.invoke(self, ((theParent, theChild), _ctx))

        def begin_link(self, theParent, theChild, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLink._op_link.begin(self, ((theParent, theChild), _response, _ex, _sent, _ctx))

        def end_link(self, _r):
            return _M_omero.model.OriginalFileAnnotationLink._op_link.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.OriginalFileAnnotationLinkPrx.ice_checkedCast(proxy, '::omero::model::OriginalFileAnnotationLink', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.OriginalFileAnnotationLinkPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_OriginalFileAnnotationLinkPrx = IcePy.defineProxy('::omero::model::OriginalFileAnnotationLink', OriginalFileAnnotationLinkPrx)

    _M_omero.model._t_OriginalFileAnnotationLink = IcePy.declareClass('::omero::model::OriginalFileAnnotationLink')

    _M_omero.model._t_OriginalFileAnnotationLink = IcePy.defineClass('::omero::model::OriginalFileAnnotationLink', OriginalFileAnnotationLink, (), True, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt),
        ('_parent', (), _M_omero.model._t_OriginalFile),
        ('_child', (), _M_omero.model._t_Annotation)
    ))
    OriginalFileAnnotationLink._ice_type = _M_omero.model._t_OriginalFileAnnotationLink

    OriginalFileAnnotationLink._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    OriginalFileAnnotationLink._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())
    OriginalFileAnnotationLink._op_getParent = IcePy.Operation('getParent', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_OriginalFile, ())
    OriginalFileAnnotationLink._op_setParent = IcePy.Operation('setParent', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_OriginalFile),), (), None, ())
    OriginalFileAnnotationLink._op_getChild = IcePy.Operation('getChild', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_Annotation, ())
    OriginalFileAnnotationLink._op_setChild = IcePy.Operation('setChild', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_Annotation),), (), None, ())
    OriginalFileAnnotationLink._op_link = IcePy.Operation('link', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_OriginalFile), ((), _M_omero.model._t_Annotation)), (), None, ())

    _M_omero.model.OriginalFileAnnotationLink = OriginalFileAnnotationLink
    del OriginalFileAnnotationLink

    _M_omero.model.OriginalFileAnnotationLinkPrx = OriginalFileAnnotationLinkPrx
    del OriginalFileAnnotationLinkPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
