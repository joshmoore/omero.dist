   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.h for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef NODEANNOTATIONLINKI_H
#define NODEANNOTATIONLINKI_H
#include <omero/RTypes.h>
#include <omero/ClientErrors.h>
#include <omero/model/IObject.h>
#include <omero/model/DetailsI.h>
#include <omero/model/NodeAnnotationLink.h>
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
    class OMERO_API NodeAnnotationLinkI;
  }
}
#if ICE_INT_VERSION / 100 >= 304
namespace IceInternal {
  OMERO_API ::Ice::Object* upCast(::omero::model::NodeAnnotationLinkI*);
}
#endif
namespace omero {
  namespace model {
#if ICE_INT_VERSION / 100 >= 304
  typedef IceInternal::Handle<NodeAnnotationLinkI> NodeAnnotationLinkIPtr;
#else
  typedef IceUtil::Handle<NodeAnnotationLinkI> NodeAnnotationLinkIPtr;
#endif
    class OMERO_API NodeAnnotationLinkI : virtual public NodeAnnotationLink {
   public:
      static const std::string PARENT;
      static const std::string CHILD;
      static const std::string DETAILS;
    protected:
      void errorIfUnloaded();
      void throwNullCollectionException(std::string propertyName);
      virtual void toggleCollectionsLoaded(bool load);
      virtual ~NodeAnnotationLinkI();
    public:
      NodeAnnotationLinkI();
      NodeAnnotationLinkI(omero::RLongPtr idPtr, bool isLoaded = false);
      NodeAnnotationLinkI(Ice::Long id, bool isLoaded = false);
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
      //  NodeAnnotationLink.parent
      //
      virtual void unloadParent();
      virtual omero::model::NodePtr getParent(const Ice::Current& current = Ice::Current());
      virtual void setParent(const omero::model::NodePtr& _parent, const Ice::Current& current = Ice::Current());

      //
      //  NodeAnnotationLink.child
      //
      virtual void unloadChild();
      virtual omero::model::AnnotationPtr getChild(const Ice::Current& current = Ice::Current());
      virtual void setChild(const omero::model::AnnotationPtr& _child, const Ice::Current& current = Ice::Current());
      virtual void link(const NodePtr& parent, const AnnotationPtr& child, const Ice::Current& current = Ice::Current());
 };

}}
#endif // NODEANNOTATIONLINKI_H