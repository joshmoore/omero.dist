   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.h for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef IMAGINGENVIRONMENTI_H
#define IMAGINGENVIRONMENTI_H
#include <omero/IceNoWarnPush.h>
#include <omero/RTypes.h>
#include <omero/model/RTypes.h>
#include <omero/model/IObject.h>
#include <omero/model/ImagingEnvironment.h>
#include <omero/IceNoWarnPop.h>
#include <omero/ClientErrors.h>
#include <omero/model/DetailsI.h>
#include <omero/model/NamedValue.h>
#include <omero/templates.h>
#include <IceUtil/Config.h>
#if ICE_INT_VERSION / 100 >= 304
#   include <Ice/Handle.h>
#else
#   include <IceUtil/Handle.h>
#endif
#ifndef OMERO_CLIENT
#   ifdef OMERO_CLIENT_EXPORTS
#       define OMERO_CLIENT ICE_DECLSPEC_EXPORT
#   else
#       define OMERO_CLIENT ICE_DECLSPEC_IMPORT
#   endif
#endif
namespace omero {
  namespace model {
    class OMERO_CLIENT ImagingEnvironmentI;
  }
}
#if ICE_INT_VERSION / 100 >= 304
namespace IceInternal {
  OMERO_CLIENT ::Ice::Object* upCast(::omero::model::ImagingEnvironmentI*);
}
#endif
namespace omero {
  namespace model {
#if ICE_INT_VERSION / 100 >= 304
  typedef IceInternal::Handle<ImagingEnvironmentI> ImagingEnvironmentIPtr;
#else
  typedef IceUtil::Handle<ImagingEnvironmentI> ImagingEnvironmentIPtr;
#endif
    class OMERO_CLIENT ImagingEnvironmentI : virtual public ImagingEnvironment {
   public:
      static const std::string TEMPERATURE;
      static const std::string AIRPRESSURE;
      static const std::string HUMIDITY;
      static const std::string CO2PERCENT;
      static const std::string MAP;
      static const std::string DETAILS;
    protected:
      void errorIfUnloaded();
      void throwNullCollectionException(std::string propertyName);
      virtual void toggleCollectionsLoaded(bool /*unused*/);
      virtual ~ImagingEnvironmentI();
    public:
      ImagingEnvironmentI();
      ImagingEnvironmentI(omero::RLongPtr idPtr, bool isLoaded = false);
      ImagingEnvironmentI(Ice::Long id, bool isLoaded = false);
      virtual void unload(const Ice::Current& current = Ice::Current());
      virtual bool isLoaded(const Ice::Current& current = Ice::Current());
      virtual void unloadCollections(const Ice::Current& current = Ice::Current());
      virtual bool isGlobal(const Ice::Current& current = Ice::Current());
      virtual bool isMutable(const Ice::Current& current = Ice::Current());
      virtual bool isAnnotated(const Ice::Current& current = Ice::Current());
      virtual bool isLink(const Ice::Current& current = Ice::Current());
      virtual omero::model::IObjectPtr shallowCopy(const Ice::Current& current = Ice::Current());
      virtual omero::model::IObjectPtr proxy(const Ice::Current& current = Ice::Current());
      virtual omero::model::DetailsPtr getDetails(const Ice::Current& current = Ice::Current());
      virtual void unloadDetails(const Ice::Current& current = Ice::Current());
      virtual omero::RLongPtr getId(const Ice::Current& current = Ice::Current());
      virtual void setId( const omero::RLongPtr& id, const Ice::Current& current = Ice::Current() );
      virtual omero::RIntPtr getVersion(const Ice::Current& current = Ice::Current());
      virtual void setVersion( const omero::RIntPtr& version, const Ice::Current& current = Ice::Current() );

      //
      //  ImagingEnvironment.temperature
      //
      virtual void unloadTemperature();
      virtual omero::model::TemperaturePtr getTemperature(const Ice::Current& current = Ice::Current());
      virtual void setTemperature(const omero::model::TemperaturePtr& _temperature, const Ice::Current& current = Ice::Current());

      //
      //  ImagingEnvironment.airPressure
      //
      virtual void unloadAirPressure();
      virtual omero::model::PressurePtr getAirPressure(const Ice::Current& current = Ice::Current());
      virtual void setAirPressure(const omero::model::PressurePtr& _airPressure, const Ice::Current& current = Ice::Current());

      //
      //  ImagingEnvironment.humidity
      //
      virtual void unloadHumidity();
      virtual omero::RDoublePtr getHumidity(const Ice::Current& current = Ice::Current());
      virtual void setHumidity(const omero::RDoublePtr& _humidity, const Ice::Current& current = Ice::Current());

      //
      //  ImagingEnvironment.co2percent
      //
      virtual void unloadCo2percent();
      virtual omero::RDoublePtr getCo2percent(const Ice::Current& current = Ice::Current());
      virtual void setCo2percent(const omero::RDoublePtr& _co2percent, const Ice::Current& current = Ice::Current());

      //
      //  ImagingEnvironment.map
      //
      virtual void unloadMap();
      virtual omero::api::NamedValueList getMap(const Ice::Current& current = Ice::Current());
      virtual void setMap(const omero::api::NamedValueList& _map, const Ice::Current& current = Ice::Current());
      virtual omero::api::StringStringMap getMapAsMap(const Ice::Current& current = Ice::Current());
 };

}}
#endif // IMAGINGENVIRONMENTI_H
