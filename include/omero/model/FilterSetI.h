   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.h for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef FILTERSETI_H
#define FILTERSETI_H
#include <omero/RTypes.h>
#include <omero/ClientErrors.h>
#include <omero/model/IObject.h>
#include <omero/model/DetailsI.h>
#include <omero/model/FilterSet.h>
#include <omero/templates.h>
#include <IceUtil/Config.h>
#if ICE_INT_VERSION / 100 >= 304
#   include <Ice/Handle.h>
#else
#   include <IceUtil/Handle.h>
#endif
#ifndef OMERO_API
#   ifdef OMERO_API_EXPORTS
#       define OMERO_API ICE_DECLSPEC_EXPORT
#   else
#       define OMERO_API ICE_DECLSPEC_IMPORT
#   endif
#endif
namespace omero {
  namespace model {
    class OMERO_API FilterSetI;
  }
}
#if ICE_INT_VERSION / 100 >= 304
namespace IceInternal {
  OMERO_API ::Ice::Object* upCast(::omero::model::FilterSetI*);
}
#endif
namespace omero {
  namespace model {
#if ICE_INT_VERSION / 100 >= 304
  typedef IceInternal::Handle<FilterSetI> FilterSetIPtr;
#else
  typedef IceUtil::Handle<FilterSetI> FilterSetIPtr;
#endif
    class OMERO_API FilterSetI : virtual public FilterSet {
   public:
      static const std::string MANUFACTURER;
      static const std::string MODEL;
      static const std::string LOTNUMBER;
      static const std::string SERIALNUMBER;
      static const std::string INSTRUMENT;
      static const std::string EXCITATIONFILTERLINK;
      static const std::string DICHROIC;
      static const std::string EMISSIONFILTERLINK;
      static const std::string DETAILS;
    protected:
      void errorIfUnloaded();
      void throwNullCollectionException(std::string propertyName);
      virtual void toggleCollectionsLoaded(bool load);
      virtual ~FilterSetI();
    public:
      FilterSetI();
      FilterSetI(omero::RLongPtr idPtr, bool isLoaded = false);
      FilterSetI(Ice::Long id, bool isLoaded = false);
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
      //  FilterSet.manufacturer
      //
      virtual void unloadManufacturer();
      virtual omero::RStringPtr getManufacturer(const Ice::Current& current = Ice::Current());
      virtual void setManufacturer(const omero::RStringPtr& _manufacturer, const Ice::Current& current = Ice::Current());

      //
      //  FilterSet.model
      //
      virtual void unloadModel();
      virtual omero::RStringPtr getModel(const Ice::Current& current = Ice::Current());
      virtual void setModel(const omero::RStringPtr& _model, const Ice::Current& current = Ice::Current());

      //
      //  FilterSet.lotNumber
      //
      virtual void unloadLotNumber();
      virtual omero::RStringPtr getLotNumber(const Ice::Current& current = Ice::Current());
      virtual void setLotNumber(const omero::RStringPtr& _lotNumber, const Ice::Current& current = Ice::Current());

      //
      //  FilterSet.serialNumber
      //
      virtual void unloadSerialNumber();
      virtual omero::RStringPtr getSerialNumber(const Ice::Current& current = Ice::Current());
      virtual void setSerialNumber(const omero::RStringPtr& _serialNumber, const Ice::Current& current = Ice::Current());

      //
      //  FilterSet.instrument
      //
      virtual void unloadInstrument();
      virtual omero::model::InstrumentPtr getInstrument(const Ice::Current& current = Ice::Current());
      virtual void setInstrument(const omero::model::InstrumentPtr& _instrument, const Ice::Current& current = Ice::Current());

      //
      //  FilterSet.excitationFilterLink
      //
      virtual void unloadExcitationFilterLink(const Ice::Current& current = Ice::Current());
    protected:
      virtual FilterSetExcitationFilterLinkSeq getExcitationFilterLink(const Ice::Current& current = Ice::Current());
      virtual void setExcitationFilterLink(const FilterSetExcitationFilterLinkSeq& _excitationFilterLink, const Ice::Current& current = Ice::Current());
    public:
      virtual bool isExcitationFilterLinkLoaded();
      virtual Ice::Int sizeOfExcitationFilterLink(const Ice::Current& current = Ice::Current());
      virtual FilterSetExcitationFilterLinkSeq copyExcitationFilterLink(const Ice::Current& current = Ice::Current());
      virtual FilterSetExcitationFilterLinkSeq::iterator beginExcitationFilterLink();
      virtual FilterSetExcitationFilterLinkSeq::iterator endExcitationFilterLink();
      virtual void addFilterSetExcitationFilterLink(const FilterSetExcitationFilterLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void addAllFilterSetExcitationFilterLinkSet(const FilterSetExcitationFilterLinkSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void removeFilterSetExcitationFilterLink(const FilterSetExcitationFilterLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void removeAllFilterSetExcitationFilterLinkSet(const FilterSetExcitationFilterLinkSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void clearExcitationFilterLink(const Ice::Current& current = Ice::Current());
      virtual void reloadExcitationFilterLink(const FilterSetPtr& toCopy, const Ice::Current& current = Ice::Current());
      virtual omero::sys::CountMap getExcitationFilterLinkCountPerOwner(const Ice::Current& current = Ice::Current());
      virtual FilterSetExcitationFilterLinkPtr linkExcitationFilter(const FilterPtr& addition, const Ice::Current& current = Ice::Current());
      virtual void addFilterSetExcitationFilterLinkToBoth(const FilterSetExcitationFilterLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
      virtual FilterSetExcitationFilterLinkSeq findFilterSetExcitationFilterLink(const FilterPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void unlinkExcitationFilter(const FilterPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void removeFilterSetExcitationFilterLinkFromBoth(const FilterSetExcitationFilterLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
       virtual FilterSetLinkedExcitationFilterSeq linkedExcitationFilterList(const Ice::Current& current = Ice::Current());

      //
      //  FilterSet.dichroic
      //
      virtual void unloadDichroic();
      virtual omero::model::DichroicPtr getDichroic(const Ice::Current& current = Ice::Current());
      virtual void setDichroic(const omero::model::DichroicPtr& _dichroic, const Ice::Current& current = Ice::Current());

      //
      //  FilterSet.emissionFilterLink
      //
      virtual void unloadEmissionFilterLink(const Ice::Current& current = Ice::Current());
    protected:
      virtual FilterSetEmissionFilterLinkSeq getEmissionFilterLink(const Ice::Current& current = Ice::Current());
      virtual void setEmissionFilterLink(const FilterSetEmissionFilterLinkSeq& _emissionFilterLink, const Ice::Current& current = Ice::Current());
    public:
      virtual bool isEmissionFilterLinkLoaded();
      virtual Ice::Int sizeOfEmissionFilterLink(const Ice::Current& current = Ice::Current());
      virtual FilterSetEmissionFilterLinkSeq copyEmissionFilterLink(const Ice::Current& current = Ice::Current());
      virtual FilterSetEmissionFilterLinkSeq::iterator beginEmissionFilterLink();
      virtual FilterSetEmissionFilterLinkSeq::iterator endEmissionFilterLink();
      virtual void addFilterSetEmissionFilterLink(const FilterSetEmissionFilterLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void addAllFilterSetEmissionFilterLinkSet(const FilterSetEmissionFilterLinkSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void removeFilterSetEmissionFilterLink(const FilterSetEmissionFilterLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void removeAllFilterSetEmissionFilterLinkSet(const FilterSetEmissionFilterLinkSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void clearEmissionFilterLink(const Ice::Current& current = Ice::Current());
      virtual void reloadEmissionFilterLink(const FilterSetPtr& toCopy, const Ice::Current& current = Ice::Current());
      virtual omero::sys::CountMap getEmissionFilterLinkCountPerOwner(const Ice::Current& current = Ice::Current());
      virtual FilterSetEmissionFilterLinkPtr linkEmissionFilter(const FilterPtr& addition, const Ice::Current& current = Ice::Current());
      virtual void addFilterSetEmissionFilterLinkToBoth(const FilterSetEmissionFilterLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
      virtual FilterSetEmissionFilterLinkSeq findFilterSetEmissionFilterLink(const FilterPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void unlinkEmissionFilter(const FilterPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void removeFilterSetEmissionFilterLinkFromBoth(const FilterSetEmissionFilterLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
       virtual FilterSetLinkedEmissionFilterSeq linkedEmissionFilterList(const Ice::Current& current = Ice::Current());
 };

}}
#endif // FILTERSETI_H