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
# Generated from file `Format.ice'
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

# Start of module omero.model.enums
_M_omero.model.enums = Ice.openModule('omero.model.enums')
__name__ = 'omero.model.enums'

_M_omero.model.enums.FormatPNG = "PNG"

_M_omero.model.enums.FormatCompanionPNG = "Companion/PNG"

_M_omero.model.enums.FormatJPEG = "JPEG"

_M_omero.model.enums.FormatCompanionJPEG = "Companion/JPEG"

_M_omero.model.enums.FormatPGM = "PGM"

_M_omero.model.enums.FormatCompanionPGM = "Companion/PGM"

_M_omero.model.enums.FormatFits = "Fits"

_M_omero.model.enums.FormatCompanionFits = "Companion/Fits"

_M_omero.model.enums.FormatGIF = "GIF"

_M_omero.model.enums.FormatCompanionGIF = "Companion/GIF"

_M_omero.model.enums.FormatBMP = "BMP"

_M_omero.model.enums.FormatCompanionBMP = "Companion/BMP"

_M_omero.model.enums.FormatDicom = "Dicom"

_M_omero.model.enums.FormatCompanionDicom = "Companion/Dicom"

_M_omero.model.enums.FormatBioRad = "BioRad"

_M_omero.model.enums.FormatCompanionBioRad = "Companion/BioRad"

_M_omero.model.enums.FormatIPLab = "IPLab"

_M_omero.model.enums.FormatCompanionIPLab = "Companion/IPLab"

_M_omero.model.enums.FormatDeltavision = "Deltavision"

_M_omero.model.enums.FormatCompanionDeltavision = "Companion/Deltavision"

_M_omero.model.enums.FormatMRC = "MRC"

_M_omero.model.enums.FormatCompanionMRC = "Companion/MRC"

_M_omero.model.enums.FormatGatan = "Gatan"

_M_omero.model.enums.FormatCompanionGatan = "Companion/Gatan"

_M_omero.model.enums.FormatImaris = "Imaris"

_M_omero.model.enums.FormatCompanionImaris = "Companion/Imaris"

_M_omero.model.enums.FormatOpenlabRaw = "OpenlabRaw"

_M_omero.model.enums.FormatCompanionOpenlabRaw = "Companion/OpenlabRaw"

_M_omero.model.enums.FormatOMEXML = "OMEXML"

_M_omero.model.enums.FormatCompanionOMEXML = "Companion/OMEXML"

_M_omero.model.enums.FormatLIF = "LIF"

_M_omero.model.enums.FormatCompanionLIF = "Companion/LIF"

_M_omero.model.enums.FormatAVI = "AVI"

_M_omero.model.enums.FormatCompanionAVI = "Companion/AVI"

_M_omero.model.enums.FormatQT = "QT"

_M_omero.model.enums.FormatCompanionQT = "Companion/QT"

_M_omero.model.enums.FormatPict = "Pict"

_M_omero.model.enums.FormatCompanionPict = "Companion/Pict"

_M_omero.model.enums.FormatSDT = "SDT"

_M_omero.model.enums.FormatCompanionSDT = "Companion/SDT"

_M_omero.model.enums.FormatEPS = "EPS"

_M_omero.model.enums.FormatCompanionEPS = "Companion/EPS"

_M_omero.model.enums.FormatSlidebook = "Slidebook"

_M_omero.model.enums.FormatCompanionSlidebook = "Companion/Slidebook"

_M_omero.model.enums.FormatAlicona = "Alicona"

_M_omero.model.enums.FormatCompanionAlicona = "Companion/Alicona"

_M_omero.model.enums.FormatMNG = "MNG"

_M_omero.model.enums.FormatCompanionMNG = "Companion/MNG"

_M_omero.model.enums.FormatNRRD = "NRRD"

_M_omero.model.enums.FormatCompanionNRRD = "Companion/NRRD"

_M_omero.model.enums.FormatKhoros = "Khoros"

_M_omero.model.enums.FormatCompanionKhoros = "Companion/Khoros"

_M_omero.model.enums.FormatVisitech = "Visitech"

_M_omero.model.enums.FormatCompanionVisitech = "Companion/Visitech"

_M_omero.model.enums.FormatLIM = "LIM"

_M_omero.model.enums.FormatCompanionLIM = "Companion/LIM"

_M_omero.model.enums.FormatPSD = "PSD"

_M_omero.model.enums.FormatCompanionPSD = "Companion/PSD"

_M_omero.model.enums.FormatInCell = "InCell"

_M_omero.model.enums.FormatCompanionInCell = "Companion/InCell"

_M_omero.model.enums.FormatICS = "ICS"

_M_omero.model.enums.FormatCompanionICS = "Companion/ICS"

_M_omero.model.enums.FormatPerkinElmer = "PerkinElmer"

_M_omero.model.enums.FormatCompanionPerkinElmer = "Companion/PerkinElmer"

_M_omero.model.enums.FormatTCS = "TCS"

_M_omero.model.enums.FormatCompanionTCS = "Companion/TCS"

_M_omero.model.enums.FormatFV1000 = "FV1000"

_M_omero.model.enums.FormatCompanionFV1000 = "Companion/FV1000"

_M_omero.model.enums.FormatZeissZVI = "ZeissZVI"

_M_omero.model.enums.FormatCompanionZeissZVI = "Companion/ZeissZVI"

_M_omero.model.enums.FormatIPW = "IPW"

_M_omero.model.enums.FormatCompanionIPW = "Companion/IPW"

_M_omero.model.enums.FormatLegacyND2 = "LegacyND2"

_M_omero.model.enums.FormatCompanionLegacyND2 = "Companion/LegacyND2"

_M_omero.model.enums.FormatND2 = "ND2"

_M_omero.model.enums.FormatCompanionND2 = "Companion/ND2"

_M_omero.model.enums.FormatPCI = "PCI"

_M_omero.model.enums.FormatCompanionPCI = "Companion/PCI"

_M_omero.model.enums.FormatImarisHDF = "ImarisHDF"

_M_omero.model.enums.FormatCompanionImarisHDF = "Companion/ImarisHDF"

_M_omero.model.enums.FormatMetamorph = "Metamorph"

_M_omero.model.enums.FormatCompanionMetamorph = "Companion/Metamorph"

_M_omero.model.enums.FormatZeissLSM = "ZeissLSM"

_M_omero.model.enums.FormatCompanionZeissLSM = "Companion/ZeissLSM"

_M_omero.model.enums.FormatSEQ = "SEQ"

_M_omero.model.enums.FormatCompanionSEQ = "Companion/SEQ"

_M_omero.model.enums.FormatGel = "Gel"

_M_omero.model.enums.FormatCompanionGel = "Companion/Gel"

_M_omero.model.enums.FormatImarisTiff = "ImarisTiff"

_M_omero.model.enums.FormatCompanionImarisTiff = "Companion/ImarisTiff"

_M_omero.model.enums.FormatFlex = "Flex"

_M_omero.model.enums.FormatCompanionFlex = "Companion/Flex"

_M_omero.model.enums.FormatSVS = "SVS"

_M_omero.model.enums.FormatCompanionSVS = "Companion/SVS"

_M_omero.model.enums.FormatLeica = "Leica"

_M_omero.model.enums.FormatCompanionLeica = "Companion/Leica"

_M_omero.model.enums.FormatNikon = "Nikon"

_M_omero.model.enums.FormatCompanionNikon = "Companion/Nikon"

_M_omero.model.enums.FormatFluoview = "Fluoview"

_M_omero.model.enums.FormatCompanionFluoview = "Companion/Fluoview"

_M_omero.model.enums.FormatPrairie = "Prairie"

_M_omero.model.enums.FormatCompanionPrairie = "Companion/Prairie"

_M_omero.model.enums.FormatMicromanager = "Micromanager"

_M_omero.model.enums.FormatCompanionMicromanager = "Companion/Micromanager"

_M_omero.model.enums.FormatImprovisionTiff = "ImprovisionTiff"

_M_omero.model.enums.FormatCompanionImprovisionTiff = "Companion/ImprovisionTiff"

_M_omero.model.enums.FormatOMETiff = "OMETiff"

_M_omero.model.enums.FormatCompanionOMETiff = "Companion/OMETiff"

_M_omero.model.enums.FormatMetamorphTiff = "MetamorphTiff"

_M_omero.model.enums.FormatCompanionMetamorphTiff = "Companion/MetamorphTiff"

_M_omero.model.enums.FormatTiff = "Tiff"

_M_omero.model.enums.FormatCompanionTiff = "Companion/Tiff"

_M_omero.model.enums.FormatOpenlab = "Openlab"

_M_omero.model.enums.FormatCompanionOpenlab = "Companion/Openlab"

_M_omero.model.enums.FormatMIAS = "MIAS"

_M_omero.model.enums.FormatCompanionMIAS = "Companion/MIAS"

# End of module omero.model.enums

__name__ = 'omero.model'

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('Format'):
    _M_omero.model.Format = Ice.createTempClass()
    class Format(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _value=None):
            if __builtin__.type(self) == _M_omero.model.Format:
                raise RuntimeError('omero.model.Format is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._value = _value

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Format', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::Format'

        def ice_staticId():
            return '::omero::model::Format'
        ice_staticId = staticmethod(ice_staticId)

        def getValue(self, current=None):
            pass

        def setValue(self, theValue, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Format)

        __repr__ = __str__

    _M_omero.model.FormatPrx = Ice.createTempClass()
    class FormatPrx(_M_omero.model.IObjectPrx):

        def getValue(self, _ctx=None):
            return _M_omero.model.Format._op_getValue.invoke(self, ((), _ctx))

        def begin_getValue(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Format._op_getValue.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getValue(self, _r):
            return _M_omero.model.Format._op_getValue.end(self, _r)

        def setValue(self, theValue, _ctx=None):
            return _M_omero.model.Format._op_setValue.invoke(self, ((theValue, ), _ctx))

        def begin_setValue(self, theValue, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Format._op_setValue.begin(self, ((theValue, ), _response, _ex, _sent, _ctx))

        def end_setValue(self, _r):
            return _M_omero.model.Format._op_setValue.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.FormatPrx.ice_checkedCast(proxy, '::omero::model::Format', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.FormatPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_FormatPrx = IcePy.defineProxy('::omero::model::Format', FormatPrx)

    _M_omero.model._t_Format = IcePy.declareClass('::omero::model::Format')

    _M_omero.model._t_Format = IcePy.defineClass('::omero::model::Format', Format, (), True, _M_omero.model._t_IObject, (), (('_value', (), _M_omero._t_RString),))
    Format._ice_type = _M_omero.model._t_Format

    Format._op_getValue = IcePy.Operation('getValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Format._op_setValue = IcePy.Operation('setValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())

    _M_omero.model.Format = Format
    del Format

    _M_omero.model.FormatPrx = FormatPrx
    del FormatPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
