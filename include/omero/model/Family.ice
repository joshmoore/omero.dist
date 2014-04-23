   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef FAMILY_ICE
#define FAMILY_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {

    module enums {
        const string Familylinear = "linear";
        const string Familypolynomial = "polynomial";
        const string Familyexponential = "exponential";
        const string Familylogarithmic = "logarithmic";
    };

    class Details;
    ["protected"] class Family
    extends omero::model::IObject
    {
      omero::RString value;
      omero::RString getValue();
      void setValue(omero::RString theValue);
    };
  };
};
#endif // FAMILY_ICE