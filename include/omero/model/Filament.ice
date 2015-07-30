   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef FILAMENT_ICE
#define FILAMENT_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
#include <omero/model/LightSource.ice>
module omero {
  module model {
    class FilamentType;
    class Power;
    class Instrument;
    class LightSourceAnnotationLink;
    class Annotation;
    class Details;
    ["protected"] class Filament
    extends omero::model::LightSource
    {
      omero::model::FilamentType type;
      omero::model::FilamentType getType();
      void setType(omero::model::FilamentType theType);
    };
  };
};
#endif // FILAMENT_ICE
