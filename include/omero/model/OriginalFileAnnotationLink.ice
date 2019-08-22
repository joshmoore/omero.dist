   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef ORIGINALFILEANNOTATIONLINK_ICE
#define ORIGINALFILEANNOTATIONLINK_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {
    class OriginalFile;
    class Annotation;
    class Details;
    ["protected"] class OriginalFileAnnotationLink
    extends omero::model::IObject
    {
      omero::RInt version;
      omero::RInt getVersion();
      void setVersion(omero::RInt theVersion);
      omero::model::OriginalFile parent;
      omero::model::OriginalFile getParent();
      void setParent(omero::model::OriginalFile theParent);
      omero::model::Annotation child;
      omero::model::Annotation getChild();
      void setChild(omero::model::Annotation theChild);
      void link(OriginalFile theParent, Annotation theChild);
    };
  };
};
#endif // ORIGINALFILEANNOTATIONLINK_ICE
