   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef PLANESLICINGCONTEXT_ICE
#define PLANESLICINGCONTEXT_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
#include <omero/model/CodomainMapContext.ice>
module omero {
  module model {
    class ChannelBinding;
    class Details;
    ["protected"] class PlaneSlicingContext
    extends omero::model::CodomainMapContext
    {
      omero::RInt upperLimit;
      omero::RInt getUpperLimit();
      void setUpperLimit(omero::RInt theUpperLimit);
      omero::RInt lowerLimit;
      omero::RInt getLowerLimit();
      void setLowerLimit(omero::RInt theLowerLimit);
      omero::RInt planeSelected;
      omero::RInt getPlaneSelected();
      void setPlaneSelected(omero::RInt thePlaneSelected);
      omero::RInt planePrevious;
      omero::RInt getPlanePrevious();
      void setPlanePrevious(omero::RInt thePlanePrevious);
      omero::RBool constant;
      omero::RBool getConstant();
      void setConstant(omero::RBool theConstant);
    };
  };
};
#endif // PLANESLICINGCONTEXT_ICE
