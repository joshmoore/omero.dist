   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.h for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef CONTRASTSTRETCHINGCONTEXTI_H
#define CONTRASTSTRETCHINGCONTEXTI_H
#include <omero/IceNoWarnPush.h>
#include <omero/RTypes.h>
#include <omero/model/RTypes.h>
#include <omero/model/IObject.h>
#include <omero/model/ContrastStretchingContext.h>
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
    class OMERO_CLIENT ContrastStretchingContextI;
  }
}
namespace IceInternal {
  OMERO_CLIENT ::Ice::Object* upCast(::omero::model::ContrastStretchingContextI*);
}
namespace omero {
  namespace model {
  typedef IceInternal::Handle<ContrastStretchingContextI> ContrastStretchingContextIPtr;
    class OMERO_CLIENT ContrastStretchingContextI : virtual public ContrastStretchingContext {
   public:
      static const std::string XSTART;
      static const std::string YSTART;
      static const std::string XEND;
      static const std::string YEND;
      static const std::string CHANNELBINDING;
      static const std::string DETAILS;
    protected:
      void errorIfUnloaded();
      void throwNullCollectionException(std::string propertyName);
      virtual void toggleCollectionsLoaded(bool /*unused*/);
      virtual ~ContrastStretchingContextI();
    public:
      ContrastStretchingContextI();
      ContrastStretchingContextI(omero::RLongPtr idPtr, bool isLoaded = false);
      ContrastStretchingContextI(Ice::Long id, bool isLoaded = false);
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
      //  ContrastStretchingContext.xstart
      //
      virtual void unloadXstart();
      virtual omero::RIntPtr getXstart(const Ice::Current& current = Ice::Current());
      virtual void setXstart(const omero::RIntPtr& _xstart, const Ice::Current& current = Ice::Current());

      //
      //  ContrastStretchingContext.ystart
      //
      virtual void unloadYstart();
      virtual omero::RIntPtr getYstart(const Ice::Current& current = Ice::Current());
      virtual void setYstart(const omero::RIntPtr& _ystart, const Ice::Current& current = Ice::Current());

      //
      //  ContrastStretchingContext.xend
      //
      virtual void unloadXend();
      virtual omero::RIntPtr getXend(const Ice::Current& current = Ice::Current());
      virtual void setXend(const omero::RIntPtr& _xend, const Ice::Current& current = Ice::Current());

      //
      //  ContrastStretchingContext.yend
      //
      virtual void unloadYend();
      virtual omero::RIntPtr getYend(const Ice::Current& current = Ice::Current());
      virtual void setYend(const omero::RIntPtr& _yend, const Ice::Current& current = Ice::Current());

      //
      //  ContrastStretchingContext.channelBinding
      //
      virtual void unloadChannelBinding();
      virtual omero::model::ChannelBindingPtr getChannelBinding(const Ice::Current& current = Ice::Current());
      virtual void setChannelBinding(const omero::model::ChannelBindingPtr& _channelBinding, const Ice::Current& current = Ice::Current());
 };

}}
#endif // CONTRASTSTRETCHINGCONTEXTI_H
