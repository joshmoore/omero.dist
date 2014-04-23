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
IceImport.load("omero_model_PlaneSlicingContext_ice")
from omero.rtypes import rlong
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class PlaneSlicingContextI(_omero_model.PlaneSlicingContext):

      UPPERLIMIT =  "ome.model.display.PlaneSlicingContext_upperLimit"
      LOWERLIMIT =  "ome.model.display.PlaneSlicingContext_lowerLimit"
      PLANESELECTED =  "ome.model.display.PlaneSlicingContext_planeSelected"
      PLANEPREVIOUS =  "ome.model.display.PlaneSlicingContext_planePrevious"
      CONSTANT =  "ome.model.display.PlaneSlicingContext_constant"
      RENDERINGDEF =  "ome.model.display.PlaneSlicingContext_renderingDef"
      DETAILS =  "ome.model.display.PlaneSlicingContext_details"
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

      def __init__(self, id = None, loaded = True):
          super(PlaneSlicingContextI, self).__init__()
          # Relying on omero.rtypes.rlong's error-handling
          self._id = rlong(id)
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadUpperLimit( )
          self.unloadLowerLimit( )
          self.unloadPlaneSelected( )
          self.unloadPlanePrevious( )
          self.unloadConstant( )
          self.unloadRenderingDef( )
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
            copy = PlaneSlicingContextI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return PlaneSlicingContextI( self._id.getValue(), False )

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

      def unloadUpperLimit(self, ):
          self._upperLimitLoaded = False
          self._upperLimit = None;

      def getUpperLimit(self, current = None):
          self.errorIfUnloaded()
          return self._upperLimit

      def setUpperLimit(self, _upperLimit, current = None):
          self.errorIfUnloaded()
          self._upperLimit = _upperLimit
          pass

      def unloadLowerLimit(self, ):
          self._lowerLimitLoaded = False
          self._lowerLimit = None;

      def getLowerLimit(self, current = None):
          self.errorIfUnloaded()
          return self._lowerLimit

      def setLowerLimit(self, _lowerLimit, current = None):
          self.errorIfUnloaded()
          self._lowerLimit = _lowerLimit
          pass

      def unloadPlaneSelected(self, ):
          self._planeSelectedLoaded = False
          self._planeSelected = None;

      def getPlaneSelected(self, current = None):
          self.errorIfUnloaded()
          return self._planeSelected

      def setPlaneSelected(self, _planeSelected, current = None):
          self.errorIfUnloaded()
          self._planeSelected = _planeSelected
          pass

      def unloadPlanePrevious(self, ):
          self._planePreviousLoaded = False
          self._planePrevious = None;

      def getPlanePrevious(self, current = None):
          self.errorIfUnloaded()
          return self._planePrevious

      def setPlanePrevious(self, _planePrevious, current = None):
          self.errorIfUnloaded()
          self._planePrevious = _planePrevious
          pass

      def unloadConstant(self, ):
          self._constantLoaded = False
          self._constant = None;

      def getConstant(self, current = None):
          self.errorIfUnloaded()
          return self._constant

      def setConstant(self, _constant, current = None):
          self.errorIfUnloaded()
          self._constant = _constant
          pass

      def unloadRenderingDef(self, ):
          self._renderingDefLoaded = False
          self._renderingDef = None;

      def getRenderingDef(self, current = None):
          self.errorIfUnloaded()
          return self._renderingDef

      def setRenderingDef(self, _renderingDef, current = None):
          self.errorIfUnloaded()
          self._renderingDef = _renderingDef
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

_omero_model.PlaneSlicingContextI = PlaneSlicingContextI