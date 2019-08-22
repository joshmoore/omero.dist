   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef EXTERNALINFO_ICE
#define EXTERNALINFO_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {
    class Details;
    ["protected"] class ExternalInfo
    extends omero::model::IObject
    {
      omero::RLong entityId;
      omero::RLong getEntityId();
      void setEntityId(omero::RLong theEntityId);
      omero::RString entityType;
      omero::RString getEntityType();
      void setEntityType(omero::RString theEntityType);
      omero::RString lsid;
      omero::RString getLsid();
      void setLsid(omero::RString theLsid);
      omero::RString uuid;
      omero::RString getUuid();
      void setUuid(omero::RString theUuid);
    };
  };
};
#endif // EXTERNALINFO_ICE
