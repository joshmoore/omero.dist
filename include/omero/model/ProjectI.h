   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.h for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef PROJECTI_H
#define PROJECTI_H
#include <omero/RTypes.h>
#include <omero/ClientErrors.h>
#include <omero/model/IObject.h>
#include <omero/model/DetailsI.h>
#include <omero/model/Project.h>
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
    class OMERO_API ProjectI;
  }
}
#if ICE_INT_VERSION / 100 >= 304
namespace IceInternal {
  OMERO_API ::Ice::Object* upCast(::omero::model::ProjectI*);
}
#endif
namespace omero {
  namespace model {
#if ICE_INT_VERSION / 100 >= 304
  typedef IceInternal::Handle<ProjectI> ProjectIPtr;
#else
  typedef IceUtil::Handle<ProjectI> ProjectIPtr;
#endif
    class OMERO_API ProjectI : virtual public Project {
   public:
      static const std::string DATASETLINKS;
      static const std::string ANNOTATIONLINKS;
      static const std::string NAME;
      static const std::string DESCRIPTION;
      static const std::string DETAILS;
    protected:
      void errorIfUnloaded();
      void throwNullCollectionException(std::string propertyName);
      virtual void toggleCollectionsLoaded(bool load);
      virtual ~ProjectI();
    public:
      ProjectI();
      ProjectI(omero::RLongPtr idPtr, bool isLoaded = false);
      ProjectI(Ice::Long id, bool isLoaded = false);
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
      //  Project.datasetLinks
      //
      virtual void unloadDatasetLinks(const Ice::Current& current = Ice::Current());
    protected:
      virtual ProjectDatasetLinksSeq getDatasetLinks(const Ice::Current& current = Ice::Current());
      virtual void setDatasetLinks(const ProjectDatasetLinksSeq& _datasetLinks, const Ice::Current& current = Ice::Current());
    public:
      virtual bool isDatasetLinksLoaded();
      virtual Ice::Int sizeOfDatasetLinks(const Ice::Current& current = Ice::Current());
      virtual ProjectDatasetLinksSeq copyDatasetLinks(const Ice::Current& current = Ice::Current());
      virtual ProjectDatasetLinksSeq::iterator beginDatasetLinks();
      virtual ProjectDatasetLinksSeq::iterator endDatasetLinks();
      virtual void addProjectDatasetLink(const ProjectDatasetLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void addAllProjectDatasetLinkSet(const ProjectDatasetLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void removeProjectDatasetLink(const ProjectDatasetLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void removeAllProjectDatasetLinkSet(const ProjectDatasetLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void clearDatasetLinks(const Ice::Current& current = Ice::Current());
      virtual void reloadDatasetLinks(const ProjectPtr& toCopy, const Ice::Current& current = Ice::Current());
      virtual omero::sys::CountMap getDatasetLinksCountPerOwner(const Ice::Current& current = Ice::Current());
      virtual ProjectDatasetLinkPtr linkDataset(const DatasetPtr& addition, const Ice::Current& current = Ice::Current());
      virtual void addProjectDatasetLinkToBoth(const ProjectDatasetLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
      virtual ProjectDatasetLinksSeq findProjectDatasetLink(const DatasetPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void unlinkDataset(const DatasetPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void removeProjectDatasetLinkFromBoth(const ProjectDatasetLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
       virtual ProjectLinkedDatasetSeq linkedDatasetList(const Ice::Current& current = Ice::Current());

      //
      //  Project.annotationLinks
      //
      virtual void unloadAnnotationLinks(const Ice::Current& current = Ice::Current());
    protected:
      virtual ProjectAnnotationLinksSeq getAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual void setAnnotationLinks(const ProjectAnnotationLinksSeq& _annotationLinks, const Ice::Current& current = Ice::Current());
    public:
      virtual bool isAnnotationLinksLoaded();
      virtual Ice::Int sizeOfAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual ProjectAnnotationLinksSeq copyAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual ProjectAnnotationLinksSeq::iterator beginAnnotationLinks();
      virtual ProjectAnnotationLinksSeq::iterator endAnnotationLinks();
      virtual void addProjectAnnotationLink(const ProjectAnnotationLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void addAllProjectAnnotationLinkSet(const ProjectAnnotationLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void removeProjectAnnotationLink(const ProjectAnnotationLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void removeAllProjectAnnotationLinkSet(const ProjectAnnotationLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void clearAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual void reloadAnnotationLinks(const ProjectPtr& toCopy, const Ice::Current& current = Ice::Current());
      virtual omero::sys::CountMap getAnnotationLinksCountPerOwner(const Ice::Current& current = Ice::Current());
      virtual ProjectAnnotationLinkPtr linkAnnotation(const AnnotationPtr& addition, const Ice::Current& current = Ice::Current());
      virtual void addProjectAnnotationLinkToBoth(const ProjectAnnotationLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
      virtual ProjectAnnotationLinksSeq findProjectAnnotationLink(const AnnotationPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void unlinkAnnotation(const AnnotationPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void removeProjectAnnotationLinkFromBoth(const ProjectAnnotationLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
       virtual ProjectLinkedAnnotationSeq linkedAnnotationList(const Ice::Current& current = Ice::Current());

      //
      //  Project.name
      //
      virtual void unloadName();
      virtual omero::RStringPtr getName(const Ice::Current& current = Ice::Current());
      virtual void setName(const omero::RStringPtr& _name, const Ice::Current& current = Ice::Current());

      //
      //  Project.description
      //
      virtual void unloadDescription();
      virtual omero::RStringPtr getDescription(const Ice::Current& current = Ice::Current());
      virtual void setDescription(const omero::RStringPtr& _description, const Ice::Current& current = Ice::Current());
 };

}}
#endif // PROJECTI_H
