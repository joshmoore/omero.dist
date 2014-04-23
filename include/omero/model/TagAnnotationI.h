   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.h for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef TAGANNOTATIONI_H
#define TAGANNOTATIONI_H
#include <omero/RTypes.h>
#include <omero/ClientErrors.h>
#include <omero/model/IObject.h>
#include <omero/model/DetailsI.h>
#include <omero/model/TagAnnotation.h>
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
    class OMERO_API TagAnnotationI;
  }
}
#if ICE_INT_VERSION / 100 >= 304
namespace IceInternal {
  OMERO_API ::Ice::Object* upCast(::omero::model::TagAnnotationI*);
}
#endif
namespace omero {
  namespace model {
#if ICE_INT_VERSION / 100 >= 304
  typedef IceInternal::Handle<TagAnnotationI> TagAnnotationIPtr;
#else
  typedef IceUtil::Handle<TagAnnotationI> TagAnnotationIPtr;
#endif
    class OMERO_API TagAnnotationI : virtual public TagAnnotation {
   public:
      static const std::string TEXTVALUE;
      static const std::string NS;
      static const std::string DESCRIPTION;
      static const std::string ANNOTATIONLINKS;
      static const std::string DETAILS;
    protected:
      void errorIfUnloaded();
      void throwNullCollectionException(std::string propertyName);
      virtual void toggleCollectionsLoaded(bool load);
      virtual ~TagAnnotationI();
    public:
      TagAnnotationI();
      TagAnnotationI(omero::RLongPtr idPtr, bool isLoaded = false);
      TagAnnotationI(Ice::Long id, bool isLoaded = false);
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
      //  TagAnnotation.textValue
      //
      virtual void unloadTextValue();
      virtual omero::RStringPtr getTextValue(const Ice::Current& current = Ice::Current());
      virtual void setTextValue(const omero::RStringPtr& _textValue, const Ice::Current& current = Ice::Current());

      //
      //  TagAnnotation.ns
      //
      virtual void unloadNs();
      virtual omero::RStringPtr getNs(const Ice::Current& current = Ice::Current());
      virtual void setNs(const omero::RStringPtr& _ns, const Ice::Current& current = Ice::Current());

      //
      //  TagAnnotation.description
      //
      virtual void unloadDescription();
      virtual omero::RStringPtr getDescription(const Ice::Current& current = Ice::Current());
      virtual void setDescription(const omero::RStringPtr& _description, const Ice::Current& current = Ice::Current());

      //
      //  TagAnnotation.annotationLinks
      //
      virtual void unloadAnnotationLinks(const Ice::Current& current = Ice::Current());
    protected:
      virtual AnnotationAnnotationLinksSeq getAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual void setAnnotationLinks(const AnnotationAnnotationLinksSeq& _annotationLinks, const Ice::Current& current = Ice::Current());
    public:
      virtual bool isAnnotationLinksLoaded();
      virtual Ice::Int sizeOfAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual AnnotationAnnotationLinksSeq copyAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual AnnotationAnnotationLinksSeq::iterator beginAnnotationLinks();
      virtual AnnotationAnnotationLinksSeq::iterator endAnnotationLinks();
      virtual void addAnnotationAnnotationLink(const AnnotationAnnotationLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void addAllAnnotationAnnotationLinkSet(const AnnotationAnnotationLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void removeAnnotationAnnotationLink(const AnnotationAnnotationLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void removeAllAnnotationAnnotationLinkSet(const AnnotationAnnotationLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void clearAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual void reloadAnnotationLinks(const AnnotationPtr& toCopy, const Ice::Current& current = Ice::Current());
      virtual omero::sys::CountMap getAnnotationLinksCountPerOwner(const Ice::Current& current = Ice::Current());
      virtual AnnotationAnnotationLinkPtr linkAnnotation(const AnnotationPtr& addition, const Ice::Current& current = Ice::Current());
      virtual void addAnnotationAnnotationLinkToBoth(const AnnotationAnnotationLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
      virtual AnnotationAnnotationLinksSeq findAnnotationAnnotationLink(const AnnotationPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void unlinkAnnotation(const AnnotationPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void removeAnnotationAnnotationLinkFromBoth(const AnnotationAnnotationLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
       virtual AnnotationLinkedAnnotationSeq linkedAnnotationList(const Ice::Current& current = Ice::Current());
 };

}}
#endif // TAGANNOTATIONI_H
