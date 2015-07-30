   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef SHARE_ICE
#define SHARE_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
#include <omero/model/Session.ice>
module omero {
  module model {
    class ExperimenterGroup;
    class Node;
    class Experimenter;
    class Event;
    class SessionAnnotationLink;
    class Annotation;
    class Details;
    ["protected"] class Share
    extends omero::model::Session
    {
      omero::model::ExperimenterGroup group;
      omero::model::ExperimenterGroup getGroup();
      void setGroup(omero::model::ExperimenterGroup theGroup);
      omero::RLong itemCount;
      omero::RLong getItemCount();
      void setItemCount(omero::RLong theItemCount);
      omero::RBool active;
      omero::RBool getActive();
      void setActive(omero::RBool theActive);
      Ice::ByteSeq data;
      Ice::ByteSeq getData();
      void setData(Ice::ByteSeq theData);
    };
  };
};
#endif // SHARE_ICE
