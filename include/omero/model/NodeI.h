   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.h for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef NODEI_H
#define NODEI_H
#include <omero/IceNoWarnPush.h>
#include <omero/RTypes.h>
#include <omero/model/RTypes.h>
#include <omero/model/IObject.h>
#include <omero/model/Node.h>
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
    class OMERO_CLIENT NodeI;
  }
}
namespace IceInternal {
  OMERO_CLIENT ::Ice::Object* upCast(::omero::model::NodeI*);
}
namespace omero {
  namespace model {
  typedef IceInternal::Handle<NodeI> NodeIPtr;
    class OMERO_CLIENT NodeI : virtual public Node {
   public:
      static const std::string SESSIONS;
      static const std::string UUID;
      static const std::string CONN;
      static const std::string UP;
      static const std::string DOWN;
      static const std::string SCALE;
      static const std::string ANNOTATIONLINKS;
      static const std::string DETAILS;
    protected:
      void errorIfUnloaded();
      void throwNullCollectionException(std::string propertyName);
      virtual void toggleCollectionsLoaded(bool load);
      virtual ~NodeI();
    public:
      NodeI();
      NodeI(omero::RLongPtr idPtr, bool isLoaded = false);
      NodeI(Ice::Long id, bool isLoaded = false);
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
      //  Node.sessions
      //
      virtual void unloadSessions(const Ice::Current& current = Ice::Current());
    protected:
      virtual NodeSessionsSeq getSessions(const Ice::Current& current = Ice::Current());
      virtual void setSessions(const NodeSessionsSeq& _sessions, const Ice::Current& current = Ice::Current());
    public:
      virtual bool isSessionsLoaded();
      virtual Ice::Int sizeOfSessions(const Ice::Current& current = Ice::Current());
      virtual NodeSessionsSeq copySessions(const Ice::Current& current = Ice::Current());
      virtual NodeSessionsSeq::iterator beginSessions();
      virtual NodeSessionsSeq::iterator endSessions();
      virtual void addSession(const SessionPtr& target, const Ice::Current& current = Ice::Current());
      virtual void addAllSessionSet(const NodeSessionsSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void removeSession(const SessionPtr& target, const Ice::Current& current = Ice::Current());
      virtual void removeAllSessionSet(const NodeSessionsSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void clearSessions(const Ice::Current& current = Ice::Current());
      virtual void reloadSessions(const NodePtr& toCopy, const Ice::Current& current = Ice::Current());

      //
      //  Node.uuid
      //
      virtual void unloadUuid();
      virtual omero::RStringPtr getUuid(const Ice::Current& current = Ice::Current());
      virtual void setUuid(const omero::RStringPtr& _uuid, const Ice::Current& current = Ice::Current());

      //
      //  Node.conn
      //
      virtual void unloadConn();
      virtual omero::RStringPtr getConn(const Ice::Current& current = Ice::Current());
      virtual void setConn(const omero::RStringPtr& _conn, const Ice::Current& current = Ice::Current());

      //
      //  Node.up
      //
      virtual void unloadUp();
      virtual omero::RTimePtr getUp(const Ice::Current& current = Ice::Current());
      virtual void setUp(const omero::RTimePtr& _up, const Ice::Current& current = Ice::Current());

      //
      //  Node.down
      //
      virtual void unloadDown();
      virtual omero::RTimePtr getDown(const Ice::Current& current = Ice::Current());
      virtual void setDown(const omero::RTimePtr& _down, const Ice::Current& current = Ice::Current());

      //
      //  Node.scale
      //
      virtual void unloadScale();
      virtual omero::RIntPtr getScale(const Ice::Current& current = Ice::Current());
      virtual void setScale(const omero::RIntPtr& _scale, const Ice::Current& current = Ice::Current());

      //
      //  Node.annotationLinks
      //
      virtual void unloadAnnotationLinks(const Ice::Current& current = Ice::Current());
    protected:
      virtual NodeAnnotationLinksSeq getAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual void setAnnotationLinks(const NodeAnnotationLinksSeq& _annotationLinks, const Ice::Current& current = Ice::Current());
    public:
      virtual bool isAnnotationLinksLoaded();
      virtual Ice::Int sizeOfAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual NodeAnnotationLinksSeq copyAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual NodeAnnotationLinksSeq::iterator beginAnnotationLinks();
      virtual NodeAnnotationLinksSeq::iterator endAnnotationLinks();
      virtual void addNodeAnnotationLink(const NodeAnnotationLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void addAllNodeAnnotationLinkSet(const NodeAnnotationLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void removeNodeAnnotationLink(const NodeAnnotationLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void removeAllNodeAnnotationLinkSet(const NodeAnnotationLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void clearAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual void reloadAnnotationLinks(const NodePtr& toCopy, const Ice::Current& current = Ice::Current());
      virtual omero::sys::CountMap getAnnotationLinksCountPerOwner(const Ice::Current& current = Ice::Current());
      virtual NodeAnnotationLinkPtr linkAnnotation(const AnnotationPtr& addition, const Ice::Current& current = Ice::Current());
      virtual void addNodeAnnotationLinkToBoth(const NodeAnnotationLinkPtr& link, bool /*unused*/, const Ice::Current& current = Ice::Current());
      virtual NodeAnnotationLinksSeq findNodeAnnotationLink(const AnnotationPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void unlinkAnnotation(const AnnotationPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void removeNodeAnnotationLinkFromBoth(const NodeAnnotationLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
       virtual NodeLinkedAnnotationSeq linkedAnnotationList(const Ice::Current& current = Ice::Current());
 };

}}
#endif // NODEI_H
