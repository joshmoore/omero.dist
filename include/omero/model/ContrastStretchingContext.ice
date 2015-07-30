   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef CONTRASTSTRETCHINGCONTEXT_ICE
#define CONTRASTSTRETCHINGCONTEXT_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
#include <omero/model/CodomainMapContext.ice>
module omero {
  module model {
    class RenderingDef;
    class Details;
    ["protected"] class ContrastStretchingContext
    extends omero::model::CodomainMapContext
    {
      omero::RInt xstart;
      omero::RInt getXstart();
      void setXstart(omero::RInt theXstart);
      omero::RInt ystart;
      omero::RInt getYstart();
      void setYstart(omero::RInt theYstart);
      omero::RInt xend;
      omero::RInt getXend();
      void setXend(omero::RInt theXend);
      omero::RInt yend;
      omero::RInt getYend();
      void setYend(omero::RInt theYend);
    };
  };
};
#endif // CONTRASTSTRETCHINGCONTEXT_ICE
