   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef ANNOTATIONANNOTATIONLINK_ICE
#define ANNOTATIONANNOTATIONLINK_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {
    class Annotation;
    class Annotation;
    class Details;
    ["protected"] class AnnotationAnnotationLink
    extends omero::model::IObject
    {
      omero::RInt version;
      omero::RInt getVersion();
      void setVersion(omero::RInt theVersion);
      omero::model::Annotation parent;
      omero::model::Annotation getParent();
      void setParent(omero::model::Annotation theParent);
      omero::model::Annotation child;
      omero::model::Annotation getChild();
      void setChild(omero::model::Annotation theChild);
      void link(Annotation theParent, Annotation theChild);
    };
  };
};
#endif // ANNOTATIONANNOTATIONLINK_ICE
