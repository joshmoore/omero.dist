   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef LOGICALCHANNEL_ICE
#define LOGICALCHANNEL_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {
    class Length;
    class Illumination;
    class ContrastMethod;
    class Length;
    class Length;
    class OTF;
    class DetectorSettings;
    class LightSettings;
    class FilterSet;
    class PhotometricInterpretation;
    class AcquisitionMode;
    class Channel;
    class LightPath;
    class Details;
    ["java:type:java.util.ArrayList"] sequence<omero::model::Channel> LogicalChannelChannelsSeq;
    ["protected"] class LogicalChannel
    extends omero::model::IObject
    {
      omero::RInt version;
      omero::RInt getVersion();
      void setVersion(omero::RInt theVersion);
      omero::RString name;
      omero::RString getName();
      void setName(omero::RString theName);
      omero::model::Length pinHoleSize;
      omero::model::Length getPinHoleSize();
      void setPinHoleSize(omero::model::Length thePinHoleSize);
      omero::model::Illumination illumination;
      omero::model::Illumination getIllumination();
      void setIllumination(omero::model::Illumination theIllumination);
      omero::model::ContrastMethod contrastMethod;
      omero::model::ContrastMethod getContrastMethod();
      void setContrastMethod(omero::model::ContrastMethod theContrastMethod);
      omero::model::Length excitationWave;
      omero::model::Length getExcitationWave();
      void setExcitationWave(omero::model::Length theExcitationWave);
      omero::model::Length emissionWave;
      omero::model::Length getEmissionWave();
      void setEmissionWave(omero::model::Length theEmissionWave);
      omero::RString fluor;
      omero::RString getFluor();
      void setFluor(omero::RString theFluor);
      omero::RDouble ndFilter;
      omero::RDouble getNdFilter();
      void setNdFilter(omero::RDouble theNdFilter);
      omero::model::OTF otf;
      omero::model::OTF getOtf();
      void setOtf(omero::model::OTF theOtf);
      omero::model::DetectorSettings detectorSettings;
      omero::model::DetectorSettings getDetectorSettings();
      void setDetectorSettings(omero::model::DetectorSettings theDetectorSettings);
      omero::model::LightSettings lightSourceSettings;
      omero::model::LightSettings getLightSourceSettings();
      void setLightSourceSettings(omero::model::LightSettings theLightSourceSettings);
      omero::model::FilterSet filterSet;
      omero::model::FilterSet getFilterSet();
      void setFilterSet(omero::model::FilterSet theFilterSet);
      omero::RInt samplesPerPixel;
      omero::RInt getSamplesPerPixel();
      void setSamplesPerPixel(omero::RInt theSamplesPerPixel);
      omero::model::PhotometricInterpretation photometricInterpretation;
      omero::model::PhotometricInterpretation getPhotometricInterpretation();
      void setPhotometricInterpretation(omero::model::PhotometricInterpretation thePhotometricInterpretation);
      omero::model::AcquisitionMode mode;
      omero::model::AcquisitionMode getMode();
      void setMode(omero::model::AcquisitionMode theMode);
      omero::RInt pockelCellSetting;
      omero::RInt getPockelCellSetting();
      void setPockelCellSetting(omero::RInt thePockelCellSetting);
      LogicalChannelChannelsSeq channelsSeq;
      bool channelsLoaded;
      /*
       * Unloads the channels collection. Any access to this
       * collection will throw an omero.UnloadedCollectionException.
       *
       * See sizeOfChannels() on how to test for unloaded collections.
       * See reloadChannels() on how to reset the value.
       *
       */
      void unloadChannels();
      int sizeOfChannels();
      LogicalChannelChannelsSeq copyChannels();
      // See language-specific iterator methods
      void addChannel(Channel target);
      /*
       * Adds all the members of the LogicalChannelChannelsSeq sequence to
       * the channelsSeq field.
       */
      void addAllChannelSet(LogicalChannelChannelsSeq targets);
      void removeChannel(Channel theTarget);
      /*
       * Removes all the members of the LogicalChannelChannelsSeq sequence from
       * the channelsSeq field.
       */
      void removeAllChannelSet(LogicalChannelChannelsSeq targets);
      void clearChannels();

      /*
       * Allows reloading the protected channels collection
       * from another instance of LogicalChannel. The argument's collection
       * will be unloaded and all member entities will have their
       * inverse property altered.
       *
       * The argument's id must match and it's update id must be present and
       * greater than or equal to that of the current object.
       */
      void reloadChannels(LogicalChannel toCopy);
      omero::model::LightPath lightPath;
      omero::model::LightPath getLightPath();
      void setLightPath(omero::model::LightPath theLightPath);
    };
  };
};
#endif // LOGICALCHANNEL_ICE
