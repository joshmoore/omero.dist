   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef PATH_ICE
#define PATH_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
#include <omero/model/Shape.ice>
module omero {
  module model {
    class Roi;
    class Length;
    class Length;
    class ShapeAnnotationLink;
    class Annotation;
    class Details;
    ["protected"] class Path
    extends omero::model::Shape
    {
      omero::RString d;
      omero::RString getD();
      void setD(omero::RString theD);
      omero::RString textValue;
      omero::RString getTextValue();
      void setTextValue(omero::RString theTextValue);
    };
  };
};
#endif // PATH_ICE
