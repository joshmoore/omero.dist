"""
   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
"""
import Ice
import IceImport
import omero
IceImport.load("omero_model_DetailsI")
IceImport.load("omero_model_Objective_ice")
from omero.rtypes import rlong
from collections import namedtuple
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class ObjectiveI(_omero_model.Objective):

      # Property Metadata
      _field_info_data = namedtuple("FieldData", ["wrapper", "nullable"])
      _field_info_type = namedtuple("FieldInfo", [
          "manufacturer",
          "model",
          "lotNumber",
          "serialNumber",
          "nominalMagnification",
          "calibratedMagnification",
          "lensNA",
          "immersion",
          "correction",
          "workingDistance",
          "iris",
          "instrument",
          "details",
      ])
      _field_info = _field_info_type(
          manufacturer=_field_info_data(wrapper=omero.rtypes.rstring, nullable=True),
          model=_field_info_data(wrapper=omero.rtypes.rstring, nullable=True),
          lotNumber=_field_info_data(wrapper=omero.rtypes.rstring, nullable=True),
          serialNumber=_field_info_data(wrapper=omero.rtypes.rstring, nullable=True),
          nominalMagnification=_field_info_data(wrapper=omero.rtypes.rdouble, nullable=True),
          calibratedMagnification=_field_info_data(wrapper=omero.rtypes.rdouble, nullable=True),
          lensNA=_field_info_data(wrapper=omero.rtypes.rdouble, nullable=True),
          immersion=_field_info_data(wrapper=omero.proxy_to_instance, nullable=False),
          correction=_field_info_data(wrapper=omero.proxy_to_instance, nullable=False),
          workingDistance=_field_info_data(wrapper=omero.rtypes.rdouble, nullable=True),
          iris=_field_info_data(wrapper=omero.rtypes.rbool, nullable=True),
          instrument=_field_info_data(wrapper=omero.proxy_to_instance, nullable=False),
          details=_field_info_data(wrapper=omero.proxy_to_instance, nullable=True),
      )  # end _field_info
      MANUFACTURER =  "ome.model.acquisition.Objective_manufacturer"
      MODEL =  "ome.model.acquisition.Objective_model"
      LOTNUMBER =  "ome.model.acquisition.Objective_lotNumber"
      SERIALNUMBER =  "ome.model.acquisition.Objective_serialNumber"
      NOMINALMAGNIFICATION =  "ome.model.acquisition.Objective_nominalMagnification"
      CALIBRATEDMAGNIFICATION =  "ome.model.acquisition.Objective_calibratedMagnification"
      LENSNA =  "ome.model.acquisition.Objective_lensNA"
      IMMERSION =  "ome.model.acquisition.Objective_immersion"
      CORRECTION =  "ome.model.acquisition.Objective_correction"
      WORKINGDISTANCE =  "ome.model.acquisition.Objective_workingDistance"
      IRIS =  "ome.model.acquisition.Objective_iris"
      INSTRUMENT =  "ome.model.acquisition.Objective_instrument"
      DETAILS =  "ome.model.acquisition.Objective_details"
      def errorIfUnloaded(self):
          if not self._loaded:
              raise _omero.UnloadedEntityException("Object unloaded:"+str(self))

      def throwNullCollectionException(self,propertyName):
          raise _omero.UnloadedEntityException(""+
          "Error updating collection:" + propertyName +"\n"+
          "Collection is currently null. This can be seen\n" +
          "by testing \""+ propertyName +"Loaded\". This implies\n"+
          "that this collection was unloaded. Please refresh this object\n"+
          "in order to update this collection.\n")

      def _toggleCollectionsLoaded(self,load):
          pass

      def __init__(self, id=None, loaded=None):
          super(ObjectiveI, self).__init__()
          if id is not None and isinstance(id, (str, unicode)) and ":" in id:
              parts = id.split(":")
              if len(parts) != 2:
                  raise Exception("Invalid proxy string: %s", id)
              if parts[0] != self.__class__.__name__ and \
                 parts[0]+"I" != self.__class__.__name__:
                  raise Exception("Proxy class mismatch: %s<>%s" %
                  (self.__class__.__name__, parts[0]))
              self._id = rlong(parts[1])
              if loaded is None:
                  # If no loadedness was requested with
                  # a proxy string, then assume False.
                  loaded = False
          else:
              # Relying on omero.rtypes.rlong's error-handling
              self._id = rlong(id)
              if loaded is None:
                  loaded = True  # Assume true as previously
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadManufacturer( )
          self.unloadModel( )
          self.unloadLotNumber( )
          self.unloadSerialNumber( )
          self.unloadNominalMagnification( )
          self.unloadCalibratedMagnification( )
          self.unloadLensNA( )
          self.unloadImmersion( )
          self.unloadCorrection( )
          self.unloadWorkingDistance( )
          self.unloadIris( )
          self.unloadInstrument( )
          self.unloadDetails( )

      def isLoaded(self, current = None):
          return self._loaded
      def unloadCollections(self, current = None):
          self._toggleCollectionsLoaded( False )
      def isGlobal(self, current = None):
          return  False ;
      def isMutable(self, current = None):
          return  True ;
      def isAnnotated(self, current = None):
          return  False ;
      def isLink(self, current = None):
          return  False ;
      def shallowCopy(self, current = None):
            if not self._loaded: return self.proxy()
            copy = ObjectiveI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return ObjectiveI( self._id.getValue(), False )

      def getDetails(self, current = None):
          self.errorIfUnloaded()
          return self._details

      def unloadDetails(self, current = None):
          self._details = None

      def getId(self, current = None):
          return self._id

      def setId(self, _id, current = None):
          self._id = _id

      def checkUnloadedProperty(self, value, loadedField):
          if value == None:
              self.__dict__[loadedField] = False
          else:
              self.__dict__[loadedField] = True

      def getVersion(self, current = None):
          self.errorIfUnloaded()
          return self._version

      def setVersion(self, version, current = None):
          self.errorIfUnloaded()
          self._version = version

      def unloadManufacturer(self, ):
          self._manufacturerLoaded = False
          self._manufacturer = None;

      def getManufacturer(self, current = None):
          self.errorIfUnloaded()
          return self._manufacturer

      def setManufacturer(self, _manufacturer, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.manufacturer.wrapper is not None:
              if _manufacturer is not None:
                  _manufacturer = self._field_info.manufacturer.wrapper(_manufacturer)
          self._manufacturer = _manufacturer
          pass

      def unloadModel(self, ):
          self._modelLoaded = False
          self._model = None;

      def getModel(self, current = None):
          self.errorIfUnloaded()
          return self._model

      def setModel(self, _model, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.model.wrapper is not None:
              if _model is not None:
                  _model = self._field_info.model.wrapper(_model)
          self._model = _model
          pass

      def unloadLotNumber(self, ):
          self._lotNumberLoaded = False
          self._lotNumber = None;

      def getLotNumber(self, current = None):
          self.errorIfUnloaded()
          return self._lotNumber

      def setLotNumber(self, _lotNumber, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.lotNumber.wrapper is not None:
              if _lotNumber is not None:
                  _lotNumber = self._field_info.lotNumber.wrapper(_lotNumber)
          self._lotNumber = _lotNumber
          pass

      def unloadSerialNumber(self, ):
          self._serialNumberLoaded = False
          self._serialNumber = None;

      def getSerialNumber(self, current = None):
          self.errorIfUnloaded()
          return self._serialNumber

      def setSerialNumber(self, _serialNumber, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.serialNumber.wrapper is not None:
              if _serialNumber is not None:
                  _serialNumber = self._field_info.serialNumber.wrapper(_serialNumber)
          self._serialNumber = _serialNumber
          pass

      def unloadNominalMagnification(self, ):
          self._nominalMagnificationLoaded = False
          self._nominalMagnification = None;

      def getNominalMagnification(self, current = None):
          self.errorIfUnloaded()
          return self._nominalMagnification

      def setNominalMagnification(self, _nominalMagnification, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.nominalMagnification.wrapper is not None:
              if _nominalMagnification is not None:
                  _nominalMagnification = self._field_info.nominalMagnification.wrapper(_nominalMagnification)
          self._nominalMagnification = _nominalMagnification
          pass

      def unloadCalibratedMagnification(self, ):
          self._calibratedMagnificationLoaded = False
          self._calibratedMagnification = None;

      def getCalibratedMagnification(self, current = None):
          self.errorIfUnloaded()
          return self._calibratedMagnification

      def setCalibratedMagnification(self, _calibratedMagnification, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.calibratedMagnification.wrapper is not None:
              if _calibratedMagnification is not None:
                  _calibratedMagnification = self._field_info.calibratedMagnification.wrapper(_calibratedMagnification)
          self._calibratedMagnification = _calibratedMagnification
          pass

      def unloadLensNA(self, ):
          self._lensNALoaded = False
          self._lensNA = None;

      def getLensNA(self, current = None):
          self.errorIfUnloaded()
          return self._lensNA

      def setLensNA(self, _lensNA, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.lensNA.wrapper is not None:
              if _lensNA is not None:
                  _lensNA = self._field_info.lensNA.wrapper(_lensNA)
          self._lensNA = _lensNA
          pass

      def unloadImmersion(self, ):
          self._immersionLoaded = False
          self._immersion = None;

      def getImmersion(self, current = None):
          self.errorIfUnloaded()
          return self._immersion

      def setImmersion(self, _immersion, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.immersion.wrapper is not None:
              if _immersion is not None:
                  _immersion = self._field_info.immersion.wrapper(_immersion)
          self._immersion = _immersion
          pass

      def unloadCorrection(self, ):
          self._correctionLoaded = False
          self._correction = None;

      def getCorrection(self, current = None):
          self.errorIfUnloaded()
          return self._correction

      def setCorrection(self, _correction, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.correction.wrapper is not None:
              if _correction is not None:
                  _correction = self._field_info.correction.wrapper(_correction)
          self._correction = _correction
          pass

      def unloadWorkingDistance(self, ):
          self._workingDistanceLoaded = False
          self._workingDistance = None;

      def getWorkingDistance(self, current = None):
          self.errorIfUnloaded()
          return self._workingDistance

      def setWorkingDistance(self, _workingDistance, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.workingDistance.wrapper is not None:
              if _workingDistance is not None:
                  _workingDistance = self._field_info.workingDistance.wrapper(_workingDistance)
          self._workingDistance = _workingDistance
          pass

      def unloadIris(self, ):
          self._irisLoaded = False
          self._iris = None;

      def getIris(self, current = None):
          self.errorIfUnloaded()
          return self._iris

      def setIris(self, _iris, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.iris.wrapper is not None:
              if _iris is not None:
                  _iris = self._field_info.iris.wrapper(_iris)
          self._iris = _iris
          pass

      def unloadInstrument(self, ):
          self._instrumentLoaded = False
          self._instrument = None;

      def getInstrument(self, current = None):
          self.errorIfUnloaded()
          return self._instrument

      def setInstrument(self, _instrument, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.instrument.wrapper is not None:
              if _instrument is not None:
                  _instrument = self._field_info.instrument.wrapper(_instrument)
          self._instrument = _instrument
          pass


      def ice_postUnmarshal(self):
          """
          Provides additional initialization once all data loaded
          """
          pass # Currently unused


      def ice_preMarshal(self):
          """
          Provides additional validation before data is sent
          """
          pass # Currently unused

      def __getattr__(self, name):
          import __builtin__
          """
          Reroutes all access to object.field through object.getField() or object.isField()
          """
          if "_" in name:  # Ice disallows underscores, so these should be treated normally.
              return object.__getattribute__(self, name)
          field  = "_" + name
          capitalized = name[0].capitalize() + name[1:]
          getter = "get" + capitalized
          questn = "is" + capitalized
          try:
              self.__dict__[field]
              if hasattr(self, getter):
                  method = getattr(self, getter)
                  return method()
              elif hasattr(self, questn):
                  method = getattr(self, questn)
                  return method()
          except:
              pass
          raise AttributeError("'%s' object has no attribute '%s' or '%s'" % (self.__class__.__name__, getter, questn))

      def __setattr__(self, name, value):
          """
          Reroutes all access to object.field through object.getField(), with the caveat
          that all sets on variables starting with "_" are permitted directly.
          """
          if name.startswith("_"):
              self.__dict__[name] = value
              return
          else:
              field  = "_" + name
              setter = "set" + name[0].capitalize() + name[1:]
              if hasattr(self, field) and hasattr(self, setter):
                  method = getattr(self, setter)
                  return method(value)
          raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, setter))

_omero_model.ObjectiveI = ObjectiveI
