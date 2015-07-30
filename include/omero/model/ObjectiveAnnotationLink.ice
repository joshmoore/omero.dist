   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef OBJECTIVEANNOTATIONLINK_ICE
#define OBJECTIVEANNOTATIONLINK_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {
    class Objective;
    class Annotation;
    class Details;
    ["protected"] class ObjectiveAnnotationLink
    extends omero::model::IObject
    {
      omero::RInt version;
      omero::RInt getVersion();
      void setVersion(omero::RInt theVersion);
      omero::model::Objective parent;
      omero::model::Objective getParent();
      void setParent(omero::model::Objective theParent);
      omero::model::Annotation child;
      omero::model::Annotation getChild();
      void setChild(omero::model::Annotation theChild);
      void link(Objective theParent, Annotation theChild);
    };
  };
};
#endif // OBJECTIVEANNOTATIONLINK_ICE
