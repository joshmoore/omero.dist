   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef ACQUISITIONMODE_ICE
#define ACQUISITIONMODE_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {

    module enums {
        const string AcquisitionModeWideField = "WideField";
        const string AcquisitionModeLaserScanningConfocalMicroscopy = "LaserScanningConfocalMicroscopy";
        const string AcquisitionModeSpinningDiskConfocal = "SpinningDiskConfocal";
        const string AcquisitionModeSlitScanConfocal = "SlitScanConfocal";
        const string AcquisitionModeMultiPhotonMicroscopy = "MultiPhotonMicroscopy";
        const string AcquisitionModeStructuredIllumination = "StructuredIllumination";
        const string AcquisitionModeSingleMoleculeImaging = "SingleMoleculeImaging";
        const string AcquisitionModeTotalInternalReflection = "TotalInternalReflection";
        const string AcquisitionModeFluorescenceLifetime = "FluorescenceLifetime";
        const string AcquisitionModeSpectralImaging = "SpectralImaging";
        const string AcquisitionModeFluorescenceCorrelationSpectroscopy = "FluorescenceCorrelationSpectroscopy";
        const string AcquisitionModeNearFieldScanningOpticalMicroscopy = "NearFieldScanningOpticalMicroscopy";
        const string AcquisitionModeSecondHarmonicGenerationImaging = "SecondHarmonicGenerationImaging";
        const string AcquisitionModePALM = "PALM";
        const string AcquisitionModeSTORM = "STORM";
        const string AcquisitionModeSTED = "STED";
        const string AcquisitionModeTIRF = "TIRF";
        const string AcquisitionModeFSM = "FSM";
        const string AcquisitionModeLCM = "LCM";
        const string AcquisitionModeOther = "Other";
        const string AcquisitionModeUnknown = "Unknown";
        const string AcquisitionModeBrightField = "BrightField";
        const string AcquisitionModeSweptFieldConfocal = "SweptFieldConfocal";
        const string AcquisitionModeSPIM = "SPIM";
    };

    class Details;
    ["protected"] class AcquisitionMode
    extends omero::model::IObject
    {
      omero::RString value;
      omero::RString getValue();
      void setValue(omero::RString theValue);
    };
  };
};
#endif // ACQUISITIONMODE_ICE
