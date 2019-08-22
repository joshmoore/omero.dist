   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef BOOLEANANNOTATION_ICE
#define BOOLEANANNOTATION_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
#include <omero/model/BasicAnnotation.ice>
module omero {
  module model {
    class AnnotationAnnotationLink;
    class Annotation;
    class Details;
    ["protected"] class BooleanAnnotation
    extends omero::model::BasicAnnotation
    {
      omero::RBool boolValue;
      omero::RBool getBoolValue();
      void setBoolValue(omero::RBool theBoolValue);
    };
  };
};
#endif // BOOLEANANNOTATION_ICE
