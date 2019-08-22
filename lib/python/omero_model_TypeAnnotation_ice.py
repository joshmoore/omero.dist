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
# Generated from file `TypeAnnotation.ice'
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
import omero_model_Annotation_ice

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

if 'TypeAnnotation' not in _M_omero.model.__dict__:
    _M_omero.model.TypeAnnotation = Ice.createTempClass()
    class TypeAnnotation(_M_omero.model.Annotation):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _ns=None, _name=None, _description=None, _annotationLinksSeq=None, _annotationLinksLoaded=False, _annotationLinksCountPerOwner=None):
            if Ice.getType(self) == _M_omero.model.TypeAnnotation:
                raise RuntimeError('omero.model.TypeAnnotation is an abstract class')
            _M_omero.model.Annotation.__init__(self, _id, _details, _loaded, _version, _ns, _name, _description, _annotationLinksSeq, _annotationLinksLoaded, _annotationLinksCountPerOwner)

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Annotation', '::omero::model::IObject', '::omero::model::TypeAnnotation')

        def ice_id(self, current=None):
            return '::omero::model::TypeAnnotation'

        def ice_staticId():
            return '::omero::model::TypeAnnotation'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_TypeAnnotation)

        __repr__ = __str__

    _M_omero.model.TypeAnnotationPrx = Ice.createTempClass()
    class TypeAnnotationPrx(_M_omero.model.AnnotationPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.TypeAnnotationPrx.ice_checkedCast(proxy, '::omero::model::TypeAnnotation', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.TypeAnnotationPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::TypeAnnotation'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_TypeAnnotationPrx = IcePy.defineProxy('::omero::model::TypeAnnotation', TypeAnnotationPrx)

    _M_omero.model._t_TypeAnnotation = IcePy.declareClass('::omero::model::TypeAnnotation')

    _M_omero.model._t_TypeAnnotation = IcePy.defineClass('::omero::model::TypeAnnotation', TypeAnnotation, -1, (), True, False, _M_omero.model._t_Annotation, (), ())
    TypeAnnotation._ice_type = _M_omero.model._t_TypeAnnotation

    _M_omero.model.TypeAnnotation = TypeAnnotation
    del TypeAnnotation

    _M_omero.model.TypeAnnotationPrx = TypeAnnotationPrx
    del TypeAnnotationPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
