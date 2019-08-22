   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef LASERMEDIUM_ICE
#define LASERMEDIUM_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {

    module enums {
        const string LaserMediumRhodamine6G = "Rhodamine6G";
        const string LaserMediumCoumarinC30 = "CoumarinC30";
        const string LaserMediumArFl = "ArFl";
        const string LaserMediumArCl = "ArCl";
        const string LaserMediumKrFl = "KrFl";
        const string LaserMediumKrCl = "KrCl";
        const string LaserMediumXeFl = "XeFl";
        const string LaserMediumXeCl = "XeCl";
        const string LaserMediumXeBr = "XeBr";
        const string LaserMediumGaAs = "GaAs";
        const string LaserMediumGaAlAs = "GaAlAs";
        const string LaserMediumEMinus = "EMinus";
        const string LaserMediumCu = "Cu";
        const string LaserMediumAg = "Ag";
        const string LaserMediumN = "N";
        const string LaserMediumAr = "Ar";
        const string LaserMediumKr = "Kr";
        const string LaserMediumXe = "Xe";
        const string LaserMediumHeNe = "HeNe";
        const string LaserMediumHeCd = "HeCd";
        const string LaserMediumCO = "CO";
        const string LaserMediumCO2 = "CO2";
        const string LaserMediumH2O = "H2O";
        const string LaserMediumHFl = "HFl";
        const string LaserMediumNdGlass = "NdGlass";
        const string LaserMediumNdYAG = "NdYAG";
        const string LaserMediumErGlass = "ErGlass";
        const string LaserMediumErYAG = "ErYAG";
        const string LaserMediumHoYLF = "HoYLF";
        const string LaserMediumHoYAG = "HoYAG";
        const string LaserMediumRuby = "Ruby";
        const string LaserMediumTiSapphire = "TiSapphire";
        const string LaserMediumAlexandrite = "Alexandrite";
        const string LaserMediumOther = "Other";
        const string LaserMediumUnknown = "Unknown";
    };

    class Details;
    ["protected"] class LaserMedium
    extends omero::model::IObject
    {
      omero::RString value;
      omero::RString getValue();
      void setValue(omero::RString theValue);
    };
  };
};
#endif // LASERMEDIUM_ICE
