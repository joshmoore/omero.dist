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
# Generated from file `Detector.ice'
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

if 'ElectricPotential' not in _M_omero.model.__dict__:
    _M_omero.model._t_ElectricPotential = IcePy.declareClass('::omero::model::ElectricPotential')
    _M_omero.model._t_ElectricPotentialPrx = IcePy.declareProxy('::omero::model::ElectricPotential')

if 'DetectorType' not in _M_omero.model.__dict__:
    _M_omero.model._t_DetectorType = IcePy.declareClass('::omero::model::DetectorType')
    _M_omero.model._t_DetectorTypePrx = IcePy.declareProxy('::omero::model::DetectorType')

if 'Instrument' not in _M_omero.model.__dict__:
    _M_omero.model._t_Instrument = IcePy.declareClass('::omero::model::Instrument')
    _M_omero.model._t_InstrumentPrx = IcePy.declareProxy('::omero::model::Instrument')

if 'DetectorAnnotationLink' not in _M_omero.model.__dict__:
    _M_omero.model._t_DetectorAnnotationLink = IcePy.declareClass('::omero::model::DetectorAnnotationLink')
    _M_omero.model._t_DetectorAnnotationLinkPrx = IcePy.declareProxy('::omero::model::DetectorAnnotationLink')

if 'Annotation' not in _M_omero.model.__dict__:
    _M_omero.model._t_Annotation = IcePy.declareClass('::omero::model::Annotation')
    _M_omero.model._t_AnnotationPrx = IcePy.declareProxy('::omero::model::Annotation')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if '_t_DetectorAnnotationLinksSeq' not in _M_omero.model.__dict__:
    _M_omero.model._t_DetectorAnnotationLinksSeq = IcePy.defineSequence('::omero::model::DetectorAnnotationLinksSeq', (), _M_omero.model._t_DetectorAnnotationLink)

if '_t_DetectorLinkedAnnotationSeq' not in _M_omero.model.__dict__:
    _M_omero.model._t_DetectorLinkedAnnotationSeq = IcePy.defineSequence('::omero::model::DetectorLinkedAnnotationSeq', (), _M_omero.model._t_Annotation)

if 'Detector' not in _M_omero.model.__dict__:
    _M_omero.model.Detector = Ice.createTempClass()
    class Detector(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _manufacturer=None, _model=None, _lotNumber=None, _serialNumber=None, _voltage=None, _gain=None, _offsetValue=None, _zoom=None, _amplificationGain=None, _type=None, _instrument=None, _annotationLinksSeq=None, _annotationLinksLoaded=False, _annotationLinksCountPerOwner=None):
            if Ice.getType(self) == _M_omero.model.Detector:
                raise RuntimeError('omero.model.Detector is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._manufacturer = _manufacturer
            self._model = _model
            self._lotNumber = _lotNumber
            self._serialNumber = _serialNumber
            self._voltage = _voltage
            self._gain = _gain
            self._offsetValue = _offsetValue
            self._zoom = _zoom
            self._amplificationGain = _amplificationGain
            self._type = _type
            self._instrument = _instrument
            self._annotationLinksSeq = _annotationLinksSeq
            self._annotationLinksLoaded = _annotationLinksLoaded
            self._annotationLinksCountPerOwner = _annotationLinksCountPerOwner

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Detector', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::Detector'

        def ice_staticId():
            return '::omero::model::Detector'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getManufacturer(self, current=None):
            pass

        def setManufacturer(self, theManufacturer, current=None):
            pass

        def getModel(self, current=None):
            pass

        def setModel(self, theModel, current=None):
            pass

        def getLotNumber(self, current=None):
            pass

        def setLotNumber(self, theLotNumber, current=None):
            pass

        def getSerialNumber(self, current=None):
            pass

        def setSerialNumber(self, theSerialNumber, current=None):
            pass

        def getVoltage(self, current=None):
            pass

        def setVoltage(self, theVoltage, current=None):
            pass

        def getGain(self, current=None):
            pass

        def setGain(self, theGain, current=None):
            pass

        def getOffsetValue(self, current=None):
            pass

        def setOffsetValue(self, theOffsetValue, current=None):
            pass

        def getZoom(self, current=None):
            pass

        def setZoom(self, theZoom, current=None):
            pass

        def getAmplificationGain(self, current=None):
            pass

        def setAmplificationGain(self, theAmplificationGain, current=None):
            pass

        def getType(self, current=None):
            pass

        def setType(self, theType, current=None):
            pass

        def getInstrument(self, current=None):
            pass

        def setInstrument(self, theInstrument, current=None):
            pass

        def unloadAnnotationLinks(self, current=None):
            pass

        def sizeOfAnnotationLinks(self, current=None):
            pass

        def copyAnnotationLinks(self, current=None):
            pass

        def addDetectorAnnotationLink(self, target, current=None):
            pass

        def addAllDetectorAnnotationLinkSet(self, targets, current=None):
            pass

        def removeDetectorAnnotationLink(self, theTarget, current=None):
            pass

        def removeAllDetectorAnnotationLinkSet(self, targets, current=None):
            pass

        def clearAnnotationLinks(self, current=None):
            pass

        def reloadAnnotationLinks(self, toCopy, current=None):
            pass

        def getAnnotationLinksCountPerOwner(self, current=None):
            pass

        def linkAnnotation(self, addition, current=None):
            pass

        def addDetectorAnnotationLinkToBoth(self, link, bothSides, current=None):
            pass

        def findDetectorAnnotationLink(self, removal, current=None):
            pass

        def unlinkAnnotation(self, removal, current=None):
            pass

        def removeDetectorAnnotationLinkFromBoth(self, link, bothSides, current=None):
            pass

        def linkedAnnotationList(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Detector)

        __repr__ = __str__

    _M_omero.model.DetectorPrx = Ice.createTempClass()
    class DetectorPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.Detector._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.Detector._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.Detector._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.Detector._op_setVersion.end(self, _r)

        def getManufacturer(self, _ctx=None):
            return _M_omero.model.Detector._op_getManufacturer.invoke(self, ((), _ctx))

        def begin_getManufacturer(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getManufacturer.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getManufacturer(self, _r):
            return _M_omero.model.Detector._op_getManufacturer.end(self, _r)

        def setManufacturer(self, theManufacturer, _ctx=None):
            return _M_omero.model.Detector._op_setManufacturer.invoke(self, ((theManufacturer, ), _ctx))

        def begin_setManufacturer(self, theManufacturer, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setManufacturer.begin(self, ((theManufacturer, ), _response, _ex, _sent, _ctx))

        def end_setManufacturer(self, _r):
            return _M_omero.model.Detector._op_setManufacturer.end(self, _r)

        def getModel(self, _ctx=None):
            return _M_omero.model.Detector._op_getModel.invoke(self, ((), _ctx))

        def begin_getModel(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getModel.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getModel(self, _r):
            return _M_omero.model.Detector._op_getModel.end(self, _r)

        def setModel(self, theModel, _ctx=None):
            return _M_omero.model.Detector._op_setModel.invoke(self, ((theModel, ), _ctx))

        def begin_setModel(self, theModel, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setModel.begin(self, ((theModel, ), _response, _ex, _sent, _ctx))

        def end_setModel(self, _r):
            return _M_omero.model.Detector._op_setModel.end(self, _r)

        def getLotNumber(self, _ctx=None):
            return _M_omero.model.Detector._op_getLotNumber.invoke(self, ((), _ctx))

        def begin_getLotNumber(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getLotNumber.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getLotNumber(self, _r):
            return _M_omero.model.Detector._op_getLotNumber.end(self, _r)

        def setLotNumber(self, theLotNumber, _ctx=None):
            return _M_omero.model.Detector._op_setLotNumber.invoke(self, ((theLotNumber, ), _ctx))

        def begin_setLotNumber(self, theLotNumber, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setLotNumber.begin(self, ((theLotNumber, ), _response, _ex, _sent, _ctx))

        def end_setLotNumber(self, _r):
            return _M_omero.model.Detector._op_setLotNumber.end(self, _r)

        def getSerialNumber(self, _ctx=None):
            return _M_omero.model.Detector._op_getSerialNumber.invoke(self, ((), _ctx))

        def begin_getSerialNumber(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getSerialNumber.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getSerialNumber(self, _r):
            return _M_omero.model.Detector._op_getSerialNumber.end(self, _r)

        def setSerialNumber(self, theSerialNumber, _ctx=None):
            return _M_omero.model.Detector._op_setSerialNumber.invoke(self, ((theSerialNumber, ), _ctx))

        def begin_setSerialNumber(self, theSerialNumber, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setSerialNumber.begin(self, ((theSerialNumber, ), _response, _ex, _sent, _ctx))

        def end_setSerialNumber(self, _r):
            return _M_omero.model.Detector._op_setSerialNumber.end(self, _r)

        def getVoltage(self, _ctx=None):
            return _M_omero.model.Detector._op_getVoltage.invoke(self, ((), _ctx))

        def begin_getVoltage(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getVoltage.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVoltage(self, _r):
            return _M_omero.model.Detector._op_getVoltage.end(self, _r)

        def setVoltage(self, theVoltage, _ctx=None):
            return _M_omero.model.Detector._op_setVoltage.invoke(self, ((theVoltage, ), _ctx))

        def begin_setVoltage(self, theVoltage, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setVoltage.begin(self, ((theVoltage, ), _response, _ex, _sent, _ctx))

        def end_setVoltage(self, _r):
            return _M_omero.model.Detector._op_setVoltage.end(self, _r)

        def getGain(self, _ctx=None):
            return _M_omero.model.Detector._op_getGain.invoke(self, ((), _ctx))

        def begin_getGain(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getGain.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getGain(self, _r):
            return _M_omero.model.Detector._op_getGain.end(self, _r)

        def setGain(self, theGain, _ctx=None):
            return _M_omero.model.Detector._op_setGain.invoke(self, ((theGain, ), _ctx))

        def begin_setGain(self, theGain, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setGain.begin(self, ((theGain, ), _response, _ex, _sent, _ctx))

        def end_setGain(self, _r):
            return _M_omero.model.Detector._op_setGain.end(self, _r)

        def getOffsetValue(self, _ctx=None):
            return _M_omero.model.Detector._op_getOffsetValue.invoke(self, ((), _ctx))

        def begin_getOffsetValue(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getOffsetValue.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getOffsetValue(self, _r):
            return _M_omero.model.Detector._op_getOffsetValue.end(self, _r)

        def setOffsetValue(self, theOffsetValue, _ctx=None):
            return _M_omero.model.Detector._op_setOffsetValue.invoke(self, ((theOffsetValue, ), _ctx))

        def begin_setOffsetValue(self, theOffsetValue, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setOffsetValue.begin(self, ((theOffsetValue, ), _response, _ex, _sent, _ctx))

        def end_setOffsetValue(self, _r):
            return _M_omero.model.Detector._op_setOffsetValue.end(self, _r)

        def getZoom(self, _ctx=None):
            return _M_omero.model.Detector._op_getZoom.invoke(self, ((), _ctx))

        def begin_getZoom(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getZoom.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getZoom(self, _r):
            return _M_omero.model.Detector._op_getZoom.end(self, _r)

        def setZoom(self, theZoom, _ctx=None):
            return _M_omero.model.Detector._op_setZoom.invoke(self, ((theZoom, ), _ctx))

        def begin_setZoom(self, theZoom, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setZoom.begin(self, ((theZoom, ), _response, _ex, _sent, _ctx))

        def end_setZoom(self, _r):
            return _M_omero.model.Detector._op_setZoom.end(self, _r)

        def getAmplificationGain(self, _ctx=None):
            return _M_omero.model.Detector._op_getAmplificationGain.invoke(self, ((), _ctx))

        def begin_getAmplificationGain(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getAmplificationGain.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getAmplificationGain(self, _r):
            return _M_omero.model.Detector._op_getAmplificationGain.end(self, _r)

        def setAmplificationGain(self, theAmplificationGain, _ctx=None):
            return _M_omero.model.Detector._op_setAmplificationGain.invoke(self, ((theAmplificationGain, ), _ctx))

        def begin_setAmplificationGain(self, theAmplificationGain, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setAmplificationGain.begin(self, ((theAmplificationGain, ), _response, _ex, _sent, _ctx))

        def end_setAmplificationGain(self, _r):
            return _M_omero.model.Detector._op_setAmplificationGain.end(self, _r)

        def getType(self, _ctx=None):
            return _M_omero.model.Detector._op_getType.invoke(self, ((), _ctx))

        def begin_getType(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getType.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getType(self, _r):
            return _M_omero.model.Detector._op_getType.end(self, _r)

        def setType(self, theType, _ctx=None):
            return _M_omero.model.Detector._op_setType.invoke(self, ((theType, ), _ctx))

        def begin_setType(self, theType, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setType.begin(self, ((theType, ), _response, _ex, _sent, _ctx))

        def end_setType(self, _r):
            return _M_omero.model.Detector._op_setType.end(self, _r)

        def getInstrument(self, _ctx=None):
            return _M_omero.model.Detector._op_getInstrument.invoke(self, ((), _ctx))

        def begin_getInstrument(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getInstrument.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getInstrument(self, _r):
            return _M_omero.model.Detector._op_getInstrument.end(self, _r)

        def setInstrument(self, theInstrument, _ctx=None):
            return _M_omero.model.Detector._op_setInstrument.invoke(self, ((theInstrument, ), _ctx))

        def begin_setInstrument(self, theInstrument, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setInstrument.begin(self, ((theInstrument, ), _response, _ex, _sent, _ctx))

        def end_setInstrument(self, _r):
            return _M_omero.model.Detector._op_setInstrument.end(self, _r)

        def unloadAnnotationLinks(self, _ctx=None):
            return _M_omero.model.Detector._op_unloadAnnotationLinks.invoke(self, ((), _ctx))

        def begin_unloadAnnotationLinks(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_unloadAnnotationLinks.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_unloadAnnotationLinks(self, _r):
            return _M_omero.model.Detector._op_unloadAnnotationLinks.end(self, _r)

        def sizeOfAnnotationLinks(self, _ctx=None):
            return _M_omero.model.Detector._op_sizeOfAnnotationLinks.invoke(self, ((), _ctx))

        def begin_sizeOfAnnotationLinks(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_sizeOfAnnotationLinks.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_sizeOfAnnotationLinks(self, _r):
            return _M_omero.model.Detector._op_sizeOfAnnotationLinks.end(self, _r)

        def copyAnnotationLinks(self, _ctx=None):
            return _M_omero.model.Detector._op_copyAnnotationLinks.invoke(self, ((), _ctx))

        def begin_copyAnnotationLinks(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_copyAnnotationLinks.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_copyAnnotationLinks(self, _r):
            return _M_omero.model.Detector._op_copyAnnotationLinks.end(self, _r)

        def addDetectorAnnotationLink(self, target, _ctx=None):
            return _M_omero.model.Detector._op_addDetectorAnnotationLink.invoke(self, ((target, ), _ctx))

        def begin_addDetectorAnnotationLink(self, target, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_addDetectorAnnotationLink.begin(self, ((target, ), _response, _ex, _sent, _ctx))

        def end_addDetectorAnnotationLink(self, _r):
            return _M_omero.model.Detector._op_addDetectorAnnotationLink.end(self, _r)

        def addAllDetectorAnnotationLinkSet(self, targets, _ctx=None):
            return _M_omero.model.Detector._op_addAllDetectorAnnotationLinkSet.invoke(self, ((targets, ), _ctx))

        def begin_addAllDetectorAnnotationLinkSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_addAllDetectorAnnotationLinkSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_addAllDetectorAnnotationLinkSet(self, _r):
            return _M_omero.model.Detector._op_addAllDetectorAnnotationLinkSet.end(self, _r)

        def removeDetectorAnnotationLink(self, theTarget, _ctx=None):
            return _M_omero.model.Detector._op_removeDetectorAnnotationLink.invoke(self, ((theTarget, ), _ctx))

        def begin_removeDetectorAnnotationLink(self, theTarget, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_removeDetectorAnnotationLink.begin(self, ((theTarget, ), _response, _ex, _sent, _ctx))

        def end_removeDetectorAnnotationLink(self, _r):
            return _M_omero.model.Detector._op_removeDetectorAnnotationLink.end(self, _r)

        def removeAllDetectorAnnotationLinkSet(self, targets, _ctx=None):
            return _M_omero.model.Detector._op_removeAllDetectorAnnotationLinkSet.invoke(self, ((targets, ), _ctx))

        def begin_removeAllDetectorAnnotationLinkSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_removeAllDetectorAnnotationLinkSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_removeAllDetectorAnnotationLinkSet(self, _r):
            return _M_omero.model.Detector._op_removeAllDetectorAnnotationLinkSet.end(self, _r)

        def clearAnnotationLinks(self, _ctx=None):
            return _M_omero.model.Detector._op_clearAnnotationLinks.invoke(self, ((), _ctx))

        def begin_clearAnnotationLinks(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_clearAnnotationLinks.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_clearAnnotationLinks(self, _r):
            return _M_omero.model.Detector._op_clearAnnotationLinks.end(self, _r)

        def reloadAnnotationLinks(self, toCopy, _ctx=None):
            return _M_omero.model.Detector._op_reloadAnnotationLinks.invoke(self, ((toCopy, ), _ctx))

        def begin_reloadAnnotationLinks(self, toCopy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_reloadAnnotationLinks.begin(self, ((toCopy, ), _response, _ex, _sent, _ctx))

        def end_reloadAnnotationLinks(self, _r):
            return _M_omero.model.Detector._op_reloadAnnotationLinks.end(self, _r)

        def getAnnotationLinksCountPerOwner(self, _ctx=None):
            return _M_omero.model.Detector._op_getAnnotationLinksCountPerOwner.invoke(self, ((), _ctx))

        def begin_getAnnotationLinksCountPerOwner(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getAnnotationLinksCountPerOwner.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getAnnotationLinksCountPerOwner(self, _r):
            return _M_omero.model.Detector._op_getAnnotationLinksCountPerOwner.end(self, _r)

        def linkAnnotation(self, addition, _ctx=None):
            return _M_omero.model.Detector._op_linkAnnotation.invoke(self, ((addition, ), _ctx))

        def begin_linkAnnotation(self, addition, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_linkAnnotation.begin(self, ((addition, ), _response, _ex, _sent, _ctx))

        def end_linkAnnotation(self, _r):
            return _M_omero.model.Detector._op_linkAnnotation.end(self, _r)

        def addDetectorAnnotationLinkToBoth(self, link, bothSides, _ctx=None):
            return _M_omero.model.Detector._op_addDetectorAnnotationLinkToBoth.invoke(self, ((link, bothSides), _ctx))

        def begin_addDetectorAnnotationLinkToBoth(self, link, bothSides, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_addDetectorAnnotationLinkToBoth.begin(self, ((link, bothSides), _response, _ex, _sent, _ctx))

        def end_addDetectorAnnotationLinkToBoth(self, _r):
            return _M_omero.model.Detector._op_addDetectorAnnotationLinkToBoth.end(self, _r)

        def findDetectorAnnotationLink(self, removal, _ctx=None):
            return _M_omero.model.Detector._op_findDetectorAnnotationLink.invoke(self, ((removal, ), _ctx))

        def begin_findDetectorAnnotationLink(self, removal, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_findDetectorAnnotationLink.begin(self, ((removal, ), _response, _ex, _sent, _ctx))

        def end_findDetectorAnnotationLink(self, _r):
            return _M_omero.model.Detector._op_findDetectorAnnotationLink.end(self, _r)

        def unlinkAnnotation(self, removal, _ctx=None):
            return _M_omero.model.Detector._op_unlinkAnnotation.invoke(self, ((removal, ), _ctx))

        def begin_unlinkAnnotation(self, removal, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_unlinkAnnotation.begin(self, ((removal, ), _response, _ex, _sent, _ctx))

        def end_unlinkAnnotation(self, _r):
            return _M_omero.model.Detector._op_unlinkAnnotation.end(self, _r)

        def removeDetectorAnnotationLinkFromBoth(self, link, bothSides, _ctx=None):
            return _M_omero.model.Detector._op_removeDetectorAnnotationLinkFromBoth.invoke(self, ((link, bothSides), _ctx))

        def begin_removeDetectorAnnotationLinkFromBoth(self, link, bothSides, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_removeDetectorAnnotationLinkFromBoth.begin(self, ((link, bothSides), _response, _ex, _sent, _ctx))

        def end_removeDetectorAnnotationLinkFromBoth(self, _r):
            return _M_omero.model.Detector._op_removeDetectorAnnotationLinkFromBoth.end(self, _r)

        def linkedAnnotationList(self, _ctx=None):
            return _M_omero.model.Detector._op_linkedAnnotationList.invoke(self, ((), _ctx))

        def begin_linkedAnnotationList(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_linkedAnnotationList.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_linkedAnnotationList(self, _r):
            return _M_omero.model.Detector._op_linkedAnnotationList.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.DetectorPrx.ice_checkedCast(proxy, '::omero::model::Detector', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.DetectorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::Detector'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_DetectorPrx = IcePy.defineProxy('::omero::model::Detector', DetectorPrx)

    _M_omero.model._t_Detector = IcePy.declareClass('::omero::model::Detector')

    _M_omero.model._t_Detector = IcePy.defineClass('::omero::model::Detector', Detector, -1, (), True, False, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt, False, 0),
        ('_manufacturer', (), _M_omero._t_RString, False, 0),
        ('_model', (), _M_omero._t_RString, False, 0),
        ('_lotNumber', (), _M_omero._t_RString, False, 0),
        ('_serialNumber', (), _M_omero._t_RString, False, 0),
        ('_voltage', (), _M_omero.model._t_ElectricPotential, False, 0),
        ('_gain', (), _M_omero._t_RDouble, False, 0),
        ('_offsetValue', (), _M_omero._t_RDouble, False, 0),
        ('_zoom', (), _M_omero._t_RDouble, False, 0),
        ('_amplificationGain', (), _M_omero._t_RDouble, False, 0),
        ('_type', (), _M_omero.model._t_DetectorType, False, 0),
        ('_instrument', (), _M_omero.model._t_Instrument, False, 0),
        ('_annotationLinksSeq', (), _M_omero.model._t_DetectorAnnotationLinksSeq, False, 0),
        ('_annotationLinksLoaded', (), IcePy._t_bool, False, 0),
        ('_annotationLinksCountPerOwner', (), _M_omero.sys._t_CountMap, False, 0)
    ))
    Detector._ice_type = _M_omero.model._t_Detector

    Detector._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RInt, False, 0), ())
    Detector._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RInt, False, 0),), (), None, ())
    Detector._op_getManufacturer = IcePy.Operation('getManufacturer', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Detector._op_setManufacturer = IcePy.Operation('setManufacturer', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    Detector._op_getModel = IcePy.Operation('getModel', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Detector._op_setModel = IcePy.Operation('setModel', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    Detector._op_getLotNumber = IcePy.Operation('getLotNumber', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Detector._op_setLotNumber = IcePy.Operation('setLotNumber', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    Detector._op_getSerialNumber = IcePy.Operation('getSerialNumber', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Detector._op_setSerialNumber = IcePy.Operation('setSerialNumber', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    Detector._op_getVoltage = IcePy.Operation('getVoltage', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_ElectricPotential, False, 0), ())
    Detector._op_setVoltage = IcePy.Operation('setVoltage', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ElectricPotential, False, 0),), (), None, ())
    Detector._op_getGain = IcePy.Operation('getGain', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    Detector._op_setGain = IcePy.Operation('setGain', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    Detector._op_getOffsetValue = IcePy.Operation('getOffsetValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    Detector._op_setOffsetValue = IcePy.Operation('setOffsetValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    Detector._op_getZoom = IcePy.Operation('getZoom', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    Detector._op_setZoom = IcePy.Operation('setZoom', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    Detector._op_getAmplificationGain = IcePy.Operation('getAmplificationGain', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    Detector._op_setAmplificationGain = IcePy.Operation('setAmplificationGain', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    Detector._op_getType = IcePy.Operation('getType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_DetectorType, False, 0), ())
    Detector._op_setType = IcePy.Operation('setType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_DetectorType, False, 0),), (), None, ())
    Detector._op_getInstrument = IcePy.Operation('getInstrument', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Instrument, False, 0), ())
    Detector._op_setInstrument = IcePy.Operation('setInstrument', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Instrument, False, 0),), (), None, ())
    Detector._op_unloadAnnotationLinks = IcePy.Operation('unloadAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Detector._op_sizeOfAnnotationLinks = IcePy.Operation('sizeOfAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())
    Detector._op_copyAnnotationLinks = IcePy.Operation('copyAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_DetectorAnnotationLinksSeq, False, 0), ())
    Detector._op_addDetectorAnnotationLink = IcePy.Operation('addDetectorAnnotationLink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_DetectorAnnotationLink, False, 0),), (), None, ())
    Detector._op_addAllDetectorAnnotationLinkSet = IcePy.Operation('addAllDetectorAnnotationLinkSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_DetectorAnnotationLinksSeq, False, 0),), (), None, ())
    Detector._op_removeDetectorAnnotationLink = IcePy.Operation('removeDetectorAnnotationLink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_DetectorAnnotationLink, False, 0),), (), None, ())
    Detector._op_removeAllDetectorAnnotationLinkSet = IcePy.Operation('removeAllDetectorAnnotationLinkSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_DetectorAnnotationLinksSeq, False, 0),), (), None, ())
    Detector._op_clearAnnotationLinks = IcePy.Operation('clearAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Detector._op_reloadAnnotationLinks = IcePy.Operation('reloadAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Detector, False, 0),), (), None, ())
    Detector._op_getAnnotationLinksCountPerOwner = IcePy.Operation('getAnnotationLinksCountPerOwner', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.sys._t_CountMap, False, 0), ())
    Detector._op_linkAnnotation = IcePy.Operation('linkAnnotation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Annotation, False, 0),), (), ((), _M_omero.model._t_DetectorAnnotationLink, False, 0), ())
    Detector._op_addDetectorAnnotationLinkToBoth = IcePy.Operation('addDetectorAnnotationLinkToBoth', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_DetectorAnnotationLink, False, 0), ((), IcePy._t_bool, False, 0)), (), None, ())
    Detector._op_findDetectorAnnotationLink = IcePy.Operation('findDetectorAnnotationLink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Annotation, False, 0),), (), ((), _M_omero.model._t_DetectorAnnotationLinksSeq, False, 0), ())
    Detector._op_unlinkAnnotation = IcePy.Operation('unlinkAnnotation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Annotation, False, 0),), (), None, ())
    Detector._op_removeDetectorAnnotationLinkFromBoth = IcePy.Operation('removeDetectorAnnotationLinkFromBoth', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_DetectorAnnotationLink, False, 0), ((), IcePy._t_bool, False, 0)), (), None, ())
    Detector._op_linkedAnnotationList = IcePy.Operation('linkedAnnotationList', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_DetectorLinkedAnnotationSeq, False, 0), ())

    _M_omero.model.Detector = Detector
    del Detector

    _M_omero.model.DetectorPrx = DetectorPrx
    del DetectorPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
