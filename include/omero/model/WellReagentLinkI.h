   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.h for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef WELLREAGENTLINKI_H
#define WELLREAGENTLINKI_H
#include <omero/IceNoWarnPush.h>
#include <omero/RTypes.h>
#include <omero/model/RTypes.h>
#include <omero/model/IObject.h>
#include <omero/model/WellReagentLink.h>
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
    class OMERO_CLIENT WellReagentLinkI;
  }
}
namespace IceInternal {
  OMERO_CLIENT ::Ice::Object* upCast(::omero::model::WellReagentLinkI*);
}
namespace omero {
  namespace model {
  typedef IceInternal::Handle<WellReagentLinkI> WellReagentLinkIPtr;
    class OMERO_CLIENT WellReagentLinkI : virtual public WellReagentLink {
   public:
      static const std::string PARENT;
      static const std::string CHILD;
      static const std::string DETAILS;
    protected:
      void errorIfUnloaded();
      void throwNullCollectionException(std::string propertyName);
      virtual void toggleCollectionsLoaded(bool /*unused*/);
      virtual ~WellReagentLinkI();
    public:
      WellReagentLinkI();
      WellReagentLinkI(omero::RLongPtr idPtr, bool isLoaded = false);
      WellReagentLinkI(Ice::Long id, bool isLoaded = false);
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
      //  WellReagentLink.parent
      //
      virtual void unloadParent();
      virtual omero::model::WellPtr getParent(const Ice::Current& current = Ice::Current());
      virtual void setParent(const omero::model::WellPtr& _parent, const Ice::Current& current = Ice::Current());

      //
      //  WellReagentLink.child
      //
      virtual void unloadChild();
      virtual omero::model::ReagentPtr getChild(const Ice::Current& current = Ice::Current());
      virtual void setChild(const omero::model::ReagentPtr& _child, const Ice::Current& current = Ice::Current());
      virtual void link(const WellPtr& parent, const ReagentPtr& child, const Ice::Current& current = Ice::Current());
 };

}}
#endif // WELLREAGENTLINKI_H
