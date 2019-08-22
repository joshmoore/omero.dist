   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef GROUPEXPERIMENTERMAP_ICE
#define GROUPEXPERIMENTERMAP_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {
    class ExperimenterGroup;
    class Experimenter;
    class Details;
    ["protected"] class GroupExperimenterMap
    extends omero::model::IObject
    {
      omero::RInt version;
      omero::RInt getVersion();
      void setVersion(omero::RInt theVersion);
      omero::model::ExperimenterGroup parent;
      omero::model::ExperimenterGroup getParent();
      void setParent(omero::model::ExperimenterGroup theParent);
      omero::model::Experimenter child;
      omero::model::Experimenter getChild();
      void setChild(omero::model::Experimenter theChild);
      omero::RBool owner;
      omero::RBool getOwner();
      void setOwner(omero::RBool theOwner);
      void link(ExperimenterGroup theParent, Experimenter theChild);
    };
  };
};
#endif // GROUPEXPERIMENTERMAP_ICE
