   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef PROJECTIONDEF_ICE
#define PROJECTIONDEF_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {
    class RenderingDef;
    class ProjectionAxis;
    class ProjectionType;
    class Details;
    ["protected"] class ProjectionDef
    extends omero::model::IObject
    {
      omero::RInt version;
      omero::RInt getVersion();
      void setVersion(omero::RInt theVersion);
      omero::model::RenderingDef renderingDef;
      omero::model::RenderingDef getRenderingDef();
      void setRenderingDef(omero::model::RenderingDef theRenderingDef);
      omero::model::ProjectionAxis axis;
      omero::model::ProjectionAxis getAxis();
      void setAxis(omero::model::ProjectionAxis theAxis);
      omero::model::ProjectionType type;
      omero::model::ProjectionType getType();
      void setType(omero::model::ProjectionType theType);
      omero::RBool active;
      omero::RBool getActive();
      void setActive(omero::RBool theActive);
      omero::RInt startPlane;
      omero::RInt getStartPlane();
      void setStartPlane(omero::RInt theStartPlane);
      omero::RInt endPlane;
      omero::RInt getEndPlane();
      void setEndPlane(omero::RInt theEndPlane);
      omero::RInt stepping;
      omero::RInt getStepping();
      void setStepping(omero::RInt theStepping);
    };
  };
};
#endif // PROJECTIONDEF_ICE
