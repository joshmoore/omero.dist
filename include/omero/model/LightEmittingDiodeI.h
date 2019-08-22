   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.h for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef LIGHTEMITTINGDIODEI_H
#define LIGHTEMITTINGDIODEI_H
#include <omero/IceNoWarnPush.h>
#include <omero/RTypes.h>
#include <omero/model/RTypes.h>
#include <omero/model/IObject.h>
#include <omero/model/LightEmittingDiode.h>
#include <omero/IceNoWarnPop.h>
#include <omero/ClientErrors.h>
#include <omero/model/DetailsI.h>
#include <omero/model/NamedValue.h>
#include <omero/templates.h>
#include <IceUtil/Config.h>
#include <Ice/Handle.h>
#ifndef OMERO_CLIENT
#   ifdef OMERO_CLIENT_EXPORTS
#       define OMERO_CLIENT ICE_DECLSPEC_EXPORT
#   else
#       define OMERO_CLIENT ICE_DECLSPEC_IMPORT
#   endif
#endif
namespace omero {
  namespace model {
    class OMERO_CLIENT LightEmittingDiodeI;
  }
}
namespace IceInternal {
  OMERO_CLIENT ::Ice::Object* upCast(::omero::model::LightEmittingDiodeI*);
}
namespace omero {
  namespace model {
  typedef IceInternal::Handle<LightEmittingDiodeI> LightEmittingDiodeIPtr;
    class OMERO_CLIENT LightEmittingDiodeI : virtual public LightEmittingDiode {
   public:
      static const std::string MANUFACTURER;
      static const std::string MODEL;
      static const std::string POWER;
      static const std::string LOTNUMBER;
      static const std::string SERIALNUMBER;
      static const std::string INSTRUMENT;
      static const std::string ANNOTATIONLINKS;
      static const std::string DETAILS;
    protected:
      void errorIfUnloaded();
      void throwNullCollectionException(std::string propertyName);
      virtual void toggleCollectionsLoaded(bool load);
      virtual ~LightEmittingDiodeI();
    public:
      LightEmittingDiodeI();
      LightEmittingDiodeI(omero::RLongPtr idPtr, bool isLoaded = false);
      LightEmittingDiodeI(Ice::Long id, bool isLoaded = false);
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
      //  LightEmittingDiode.manufacturer
      //
      virtual void unloadManufacturer();
      virtual omero::RStringPtr getManufacturer(const Ice::Current& current = Ice::Current());
      virtual void setManufacturer(const omero::RStringPtr& _manufacturer, const Ice::Current& current = Ice::Current());

      //
      //  LightEmittingDiode.model
      //
      virtual void unloadModel();
      virtual omero::RStringPtr getModel(const Ice::Current& current = Ice::Current());
      virtual void setModel(const omero::RStringPtr& _model, const Ice::Current& current = Ice::Current());

      //
      //  LightEmittingDiode.power
      //
      virtual void unloadPower();
      virtual omero::model::PowerPtr getPower(const Ice::Current& current = Ice::Current());
      virtual void setPower(const omero::model::PowerPtr& _power, const Ice::Current& current = Ice::Current());

      //
      //  LightEmittingDiode.lotNumber
      //
      virtual void unloadLotNumber();
      virtual omero::RStringPtr getLotNumber(const Ice::Current& current = Ice::Current());
      virtual void setLotNumber(const omero::RStringPtr& _lotNumber, const Ice::Current& current = Ice::Current());

      //
      //  LightEmittingDiode.serialNumber
      //
      virtual void unloadSerialNumber();
      virtual omero::RStringPtr getSerialNumber(const Ice::Current& current = Ice::Current());
      virtual void setSerialNumber(const omero::RStringPtr& _serialNumber, const Ice::Current& current = Ice::Current());

      //
      //  LightEmittingDiode.instrument
      //
      virtual void unloadInstrument();
      virtual omero::model::InstrumentPtr getInstrument(const Ice::Current& current = Ice::Current());
      virtual void setInstrument(const omero::model::InstrumentPtr& _instrument, const Ice::Current& current = Ice::Current());

      //
      //  LightEmittingDiode.annotationLinks
      //
      virtual void unloadAnnotationLinks(const Ice::Current& current = Ice::Current());
    protected:
      virtual LightSourceAnnotationLinksSeq getAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual void setAnnotationLinks(const LightSourceAnnotationLinksSeq& _annotationLinks, const Ice::Current& current = Ice::Current());
    public:
      virtual bool isAnnotationLinksLoaded();
      virtual Ice::Int sizeOfAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual LightSourceAnnotationLinksSeq copyAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual LightSourceAnnotationLinksSeq::iterator beginAnnotationLinks();
      virtual LightSourceAnnotationLinksSeq::iterator endAnnotationLinks();
      virtual void addLightSourceAnnotationLink(const LightSourceAnnotationLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void addAllLightSourceAnnotationLinkSet(const LightSourceAnnotationLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void removeLightSourceAnnotationLink(const LightSourceAnnotationLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void removeAllLightSourceAnnotationLinkSet(const LightSourceAnnotationLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void clearAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual void reloadAnnotationLinks(const LightSourcePtr& toCopy, const Ice::Current& current = Ice::Current());
      virtual omero::sys::CountMap getAnnotationLinksCountPerOwner(const Ice::Current& current = Ice::Current());
      virtual LightSourceAnnotationLinkPtr linkAnnotation(const AnnotationPtr& addition, const Ice::Current& current = Ice::Current());
      virtual void addLightSourceAnnotationLinkToBoth(const LightSourceAnnotationLinkPtr& link, bool /*unused*/, const Ice::Current& current = Ice::Current());
      virtual LightSourceAnnotationLinksSeq findLightSourceAnnotationLink(const AnnotationPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void unlinkAnnotation(const AnnotationPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void removeLightSourceAnnotationLinkFromBoth(const LightSourceAnnotationLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
       virtual LightSourceLinkedAnnotationSeq linkedAnnotationList(const Ice::Current& current = Ice::Current());
 };

}}
#endif // LIGHTEMITTINGDIODEI_H
