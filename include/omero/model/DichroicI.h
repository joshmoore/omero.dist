   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.h for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef DICHROICI_H
#define DICHROICI_H
#include <omero/IceNoWarnPush.h>
#include <omero/RTypes.h>
#include <omero/model/RTypes.h>
#include <omero/model/IObject.h>
#include <omero/model/Dichroic.h>
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
    class OMERO_CLIENT DichroicI;
  }
}
#if ICE_INT_VERSION / 100 >= 304
namespace IceInternal {
  OMERO_CLIENT ::Ice::Object* upCast(::omero::model::DichroicI*);
}
#endif
namespace omero {
  namespace model {
#if ICE_INT_VERSION / 100 >= 304
  typedef IceInternal::Handle<DichroicI> DichroicIPtr;
#else
  typedef IceUtil::Handle<DichroicI> DichroicIPtr;
#endif
    class OMERO_CLIENT DichroicI : virtual public Dichroic {
   public:
      static const std::string MANUFACTURER;
      static const std::string MODEL;
      static const std::string LOTNUMBER;
      static const std::string SERIALNUMBER;
      static const std::string INSTRUMENT;
      static const std::string ANNOTATIONLINKS;
      static const std::string DETAILS;
    protected:
      void errorIfUnloaded();
      void throwNullCollectionException(std::string propertyName);
      virtual void toggleCollectionsLoaded(bool load);
      virtual ~DichroicI();
    public:
      DichroicI();
      DichroicI(omero::RLongPtr idPtr, bool isLoaded = false);
      DichroicI(Ice::Long id, bool isLoaded = false);
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
      //  Dichroic.manufacturer
      //
      virtual void unloadManufacturer();
      virtual omero::RStringPtr getManufacturer(const Ice::Current& current = Ice::Current());
      virtual void setManufacturer(const omero::RStringPtr& _manufacturer, const Ice::Current& current = Ice::Current());

      //
      //  Dichroic.model
      //
      virtual void unloadModel();
      virtual omero::RStringPtr getModel(const Ice::Current& current = Ice::Current());
      virtual void setModel(const omero::RStringPtr& _model, const Ice::Current& current = Ice::Current());

      //
      //  Dichroic.lotNumber
      //
      virtual void unloadLotNumber();
      virtual omero::RStringPtr getLotNumber(const Ice::Current& current = Ice::Current());
      virtual void setLotNumber(const omero::RStringPtr& _lotNumber, const Ice::Current& current = Ice::Current());

      //
      //  Dichroic.serialNumber
      //
      virtual void unloadSerialNumber();
      virtual omero::RStringPtr getSerialNumber(const Ice::Current& current = Ice::Current());
      virtual void setSerialNumber(const omero::RStringPtr& _serialNumber, const Ice::Current& current = Ice::Current());

      //
      //  Dichroic.instrument
      //
      virtual void unloadInstrument();
      virtual omero::model::InstrumentPtr getInstrument(const Ice::Current& current = Ice::Current());
      virtual void setInstrument(const omero::model::InstrumentPtr& _instrument, const Ice::Current& current = Ice::Current());

      //
      //  Dichroic.annotationLinks
      //
      virtual void unloadAnnotationLinks(const Ice::Current& current = Ice::Current());
    protected:
      virtual DichroicAnnotationLinksSeq getAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual void setAnnotationLinks(const DichroicAnnotationLinksSeq& _annotationLinks, const Ice::Current& current = Ice::Current());
    public:
      virtual bool isAnnotationLinksLoaded();
      virtual Ice::Int sizeOfAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual DichroicAnnotationLinksSeq copyAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual DichroicAnnotationLinksSeq::iterator beginAnnotationLinks();
      virtual DichroicAnnotationLinksSeq::iterator endAnnotationLinks();
      virtual void addDichroicAnnotationLink(const DichroicAnnotationLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void addAllDichroicAnnotationLinkSet(const DichroicAnnotationLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void removeDichroicAnnotationLink(const DichroicAnnotationLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void removeAllDichroicAnnotationLinkSet(const DichroicAnnotationLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void clearAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual void reloadAnnotationLinks(const DichroicPtr& toCopy, const Ice::Current& current = Ice::Current());
      virtual omero::sys::CountMap getAnnotationLinksCountPerOwner(const Ice::Current& current = Ice::Current());
      virtual DichroicAnnotationLinkPtr linkAnnotation(const AnnotationPtr& addition, const Ice::Current& current = Ice::Current());
      virtual void addDichroicAnnotationLinkToBoth(const DichroicAnnotationLinkPtr& link, bool /*unused*/, const Ice::Current& current = Ice::Current());
      virtual DichroicAnnotationLinksSeq findDichroicAnnotationLink(const AnnotationPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void unlinkAnnotation(const AnnotationPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void removeDichroicAnnotationLinkFromBoth(const DichroicAnnotationLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
       virtual DichroicLinkedAnnotationSeq linkedAnnotationList(const Ice::Current& current = Ice::Current());
 };

}}
#endif // DICHROICI_H
