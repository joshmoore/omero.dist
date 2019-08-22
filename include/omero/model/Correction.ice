   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef CORRECTION_ICE
#define CORRECTION_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {

    module enums {
        const string CorrectionUV = "UV";
        const string CorrectionPlanApo = "PlanApo";
        const string CorrectionPlanFluor = "PlanFluor";
        const string CorrectionSuperFluor = "SuperFluor";
        const string CorrectionVioletCorrected = "VioletCorrected";
        const string CorrectionAchro = "Achro";
        const string CorrectionAchromat = "Achromat";
        const string CorrectionFluor = "Fluor";
        const string CorrectionFl = "Fl";
        const string CorrectionFluar = "Fluar";
        const string CorrectionNeofluar = "Neofluar";
        const string CorrectionFluotar = "Fluotar";
        const string CorrectionApo = "Apo";
        const string CorrectionOther = "Other";
        const string CorrectionUnknown = "Unknown";
    };

    class Details;
    ["protected"] class Correction
    extends omero::model::IObject
    {
      omero::RString value;
      omero::RString getValue();
      void setValue(omero::RString theValue);
    };
  };
};
#endif // CORRECTION_ICE
