   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef STAGELABEL_ICE
#define STAGELABEL_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {
    class Details;
    ["protected"] class StageLabel
    extends omero::model::IObject
    {
      omero::RInt version;
      omero::RInt getVersion();
      void setVersion(omero::RInt theVersion);
      omero::RDouble positionX;
      omero::RDouble getPositionX();
      void setPositionX(omero::RDouble thePositionX);
      omero::RDouble positionY;
      omero::RDouble getPositionY();
      void setPositionY(omero::RDouble thePositionY);
      omero::RDouble positionZ;
      omero::RDouble getPositionZ();
      void setPositionZ(omero::RDouble thePositionZ);
      omero::RString name;
      omero::RString getName();
      void setName(omero::RString theName);
    };
  };
};
#endif // STAGELABEL_ICE