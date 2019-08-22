   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.h for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef SCRIPTJOBI_H
#define SCRIPTJOBI_H
#include <omero/IceNoWarnPush.h>
#include <omero/RTypes.h>
#include <omero/model/RTypes.h>
#include <omero/model/IObject.h>
#include <omero/model/ScriptJob.h>
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
    class OMERO_CLIENT ScriptJobI;
  }
}
#if ICE_INT_VERSION / 100 >= 304
namespace IceInternal {
  OMERO_CLIENT ::Ice::Object* upCast(::omero::model::ScriptJobI*);
}
#endif
namespace omero {
  namespace model {
#if ICE_INT_VERSION / 100 >= 304
  typedef IceInternal::Handle<ScriptJobI> ScriptJobIPtr;
#else
  typedef IceUtil::Handle<ScriptJobI> ScriptJobIPtr;
#endif
    class OMERO_CLIENT ScriptJobI : virtual public ScriptJob {
   public:
      static const std::string DESCRIPTION;
      static const std::string USERNAME;
      static const std::string GROUPNAME;
      static const std::string TYPE;
      static const std::string MESSAGE;
      static const std::string STATUS;
      static const std::string SUBMITTED;
      static const std::string SCHEDULEDFOR;
      static const std::string STARTED;
      static const std::string FINISHED;
      static const std::string ORIGINALFILELINKS;
      static const std::string DETAILS;
    protected:
      void errorIfUnloaded();
      void throwNullCollectionException(std::string propertyName);
      virtual void toggleCollectionsLoaded(bool load);
      virtual ~ScriptJobI();
    public:
      ScriptJobI();
      ScriptJobI(omero::RLongPtr idPtr, bool isLoaded = false);
      ScriptJobI(Ice::Long id, bool isLoaded = false);
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
      //  ScriptJob.description
      //
      virtual void unloadDescription();
      virtual omero::RStringPtr getDescription(const Ice::Current& current = Ice::Current());
      virtual void setDescription(const omero::RStringPtr& _description, const Ice::Current& current = Ice::Current());

      //
      //  ScriptJob.username
      //
      virtual void unloadUsername();
      virtual omero::RStringPtr getUsername(const Ice::Current& current = Ice::Current());
      virtual void setUsername(const omero::RStringPtr& _username, const Ice::Current& current = Ice::Current());

      //
      //  ScriptJob.groupname
      //
      virtual void unloadGroupname();
      virtual omero::RStringPtr getGroupname(const Ice::Current& current = Ice::Current());
      virtual void setGroupname(const omero::RStringPtr& _groupname, const Ice::Current& current = Ice::Current());

      //
      //  ScriptJob.type
      //
      virtual void unloadType();
      virtual omero::RStringPtr getType(const Ice::Current& current = Ice::Current());
      virtual void setType(const omero::RStringPtr& _type, const Ice::Current& current = Ice::Current());

      //
      //  ScriptJob.message
      //
      virtual void unloadMessage();
      virtual omero::RStringPtr getMessage(const Ice::Current& current = Ice::Current());
      virtual void setMessage(const omero::RStringPtr& _message, const Ice::Current& current = Ice::Current());

      //
      //  ScriptJob.status
      //
      virtual void unloadStatus();
      virtual omero::model::JobStatusPtr getStatus(const Ice::Current& current = Ice::Current());
      virtual void setStatus(const omero::model::JobStatusPtr& _status, const Ice::Current& current = Ice::Current());

      //
      //  ScriptJob.submitted
      //
      virtual void unloadSubmitted();
      virtual omero::RTimePtr getSubmitted(const Ice::Current& current = Ice::Current());
      virtual void setSubmitted(const omero::RTimePtr& _submitted, const Ice::Current& current = Ice::Current());

      //
      //  ScriptJob.scheduledFor
      //
      virtual void unloadScheduledFor();
      virtual omero::RTimePtr getScheduledFor(const Ice::Current& current = Ice::Current());
      virtual void setScheduledFor(const omero::RTimePtr& _scheduledFor, const Ice::Current& current = Ice::Current());

      //
      //  ScriptJob.started
      //
      virtual void unloadStarted();
      virtual omero::RTimePtr getStarted(const Ice::Current& current = Ice::Current());
      virtual void setStarted(const omero::RTimePtr& _started, const Ice::Current& current = Ice::Current());

      //
      //  ScriptJob.finished
      //
      virtual void unloadFinished();
      virtual omero::RTimePtr getFinished(const Ice::Current& current = Ice::Current());
      virtual void setFinished(const omero::RTimePtr& _finished, const Ice::Current& current = Ice::Current());

      //
      //  ScriptJob.originalFileLinks
      //
      virtual void unloadOriginalFileLinks(const Ice::Current& current = Ice::Current());
    protected:
      virtual JobOriginalFileLinksSeq getOriginalFileLinks(const Ice::Current& current = Ice::Current());
      virtual void setOriginalFileLinks(const JobOriginalFileLinksSeq& _originalFileLinks, const Ice::Current& current = Ice::Current());
    public:
      virtual bool isOriginalFileLinksLoaded();
      virtual Ice::Int sizeOfOriginalFileLinks(const Ice::Current& current = Ice::Current());
      virtual JobOriginalFileLinksSeq copyOriginalFileLinks(const Ice::Current& current = Ice::Current());
      virtual JobOriginalFileLinksSeq::iterator beginOriginalFileLinks();
      virtual JobOriginalFileLinksSeq::iterator endOriginalFileLinks();
      virtual void addJobOriginalFileLink(const JobOriginalFileLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void addAllJobOriginalFileLinkSet(const JobOriginalFileLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void removeJobOriginalFileLink(const JobOriginalFileLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void removeAllJobOriginalFileLinkSet(const JobOriginalFileLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void clearOriginalFileLinks(const Ice::Current& current = Ice::Current());
      virtual void reloadOriginalFileLinks(const JobPtr& toCopy, const Ice::Current& current = Ice::Current());
      virtual omero::sys::CountMap getOriginalFileLinksCountPerOwner(const Ice::Current& current = Ice::Current());
      virtual JobOriginalFileLinkPtr linkOriginalFile(const OriginalFilePtr& addition, const Ice::Current& current = Ice::Current());
      virtual void addJobOriginalFileLinkToBoth(const JobOriginalFileLinkPtr& link, bool /*unused*/, const Ice::Current& current = Ice::Current());
      virtual JobOriginalFileLinksSeq findJobOriginalFileLink(const OriginalFilePtr& removal, const Ice::Current& current = Ice::Current());
      virtual void unlinkOriginalFile(const OriginalFilePtr& removal, const Ice::Current& current = Ice::Current());
      virtual void removeJobOriginalFileLinkFromBoth(const JobOriginalFileLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
       virtual JobLinkedOriginalFileSeq linkedOriginalFileList(const Ice::Current& current = Ice::Current());
 };

}}
#endif // SCRIPTJOBI_H
