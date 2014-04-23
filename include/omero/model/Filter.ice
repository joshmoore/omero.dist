   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef FILTER_ICE
#define FILTER_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {
    class FilterType;
    class TransmittanceRange;
    class Instrument;
    class FilterSetExcitationFilterLink;
    class FilterSet;
    class FilterSetEmissionFilterLink;
    class FilterSet;
    class Details;
    ["java:type:java.util.ArrayList"] sequence<omero::model::FilterSetExcitationFilterLink> FilterExcitationFilterLinkSeq;
    ["java:type:java.util.ArrayList"] sequence<omero::model::FilterSet> FilterLinkedExcitationFilterSeq;
    ["java:type:java.util.ArrayList"] sequence<omero::model::FilterSetEmissionFilterLink> FilterEmissionFilterLinkSeq;
    ["java:type:java.util.ArrayList"] sequence<omero::model::FilterSet> FilterLinkedEmissionFilterSeq;
    ["protected"] class Filter
    extends omero::model::IObject
    {
      omero::RInt version;
      omero::RInt getVersion();
      void setVersion(omero::RInt theVersion);
      omero::RString manufacturer;
      omero::RString getManufacturer();
      void setManufacturer(omero::RString theManufacturer);
      omero::RString model;
      omero::RString getModel();
      void setModel(omero::RString theModel);
      omero::RString lotNumber;
      omero::RString getLotNumber();
      void setLotNumber(omero::RString theLotNumber);
      omero::RString serialNumber;
      omero::RString getSerialNumber();
      void setSerialNumber(omero::RString theSerialNumber);
      omero::RString filterWheel;
      omero::RString getFilterWheel();
      void setFilterWheel(omero::RString theFilterWheel);
      omero::model::FilterType type;
      omero::model::FilterType getType();
      void setType(omero::model::FilterType theType);
      omero::model::TransmittanceRange transmittanceRange;
      omero::model::TransmittanceRange getTransmittanceRange();
      void setTransmittanceRange(omero::model::TransmittanceRange theTransmittanceRange);
      omero::model::Instrument instrument;
      omero::model::Instrument getInstrument();
      void setInstrument(omero::model::Instrument theInstrument);
      FilterExcitationFilterLinkSeq excitationFilterLinkSeq;
      bool excitationFilterLinkLoaded;
      omero::sys::CountMap excitationFilterLinkCountPerOwner;
      /*
       * Unloads the excitationFilterLink collection. Any access to this
       * collection will throw an omero.UnloadedCollectionException.
       *
       * See sizeOfExcitationFilterLink() on how to test for unloaded collections.
       * See reloadExcitationFilterLink() on how to reset the value.
       *
       */
      void unloadExcitationFilterLink();
      int sizeOfExcitationFilterLink();
      FilterExcitationFilterLinkSeq copyExcitationFilterLink();
      // See language-specific iterator methods
      void addFilterSetExcitationFilterLink(FilterSetExcitationFilterLink target);
      /*
       * Adds all the members of the FilterExcitationFilterLinkSeq sequence to
       * the excitationFilterLinkSeq field.
       */
      void addAllFilterSetExcitationFilterLinkSet(FilterExcitationFilterLinkSeq targets);
      void removeFilterSetExcitationFilterLink(FilterSetExcitationFilterLink theTarget);
      /*
       * Removes all the members of the FilterExcitationFilterLinkSeq sequence from
       * the excitationFilterLinkSeq field.
       */
      void removeAllFilterSetExcitationFilterLinkSet(FilterExcitationFilterLinkSeq targets);
      void clearExcitationFilterLink();

      /*
       * Allows reloading the protected excitationFilterLink collection
       * from another instance of Filter. The argument's collection
       * will be unloaded and all member entities will have their
       * inverse property altered.
       *
       * The argument's id must match and it's update id must be present and
       * greater than or equal to that of the current object.
       */
      void reloadExcitationFilterLink(Filter toCopy);
      omero::sys::CountMap getExcitationFilterLinkCountPerOwner();
      FilterSetExcitationFilterLink linkExcitationFilter(FilterSet addition);

      /*
       * Add the link to the current instance and if bothSides is true AND
       * the other side of the link is loaded, add the current instance to
       * it as well.
       */
      void addFilterSetExcitationFilterLinkToBoth(omero::model::FilterSetExcitationFilterLink link, bool bothSides);
      FilterExcitationFilterLinkSeq findFilterSetExcitationFilterLink(FilterSet removal);
      void unlinkExcitationFilter(FilterSet removal);

      /*
       * Remove the link from the current instance and if bothSides is true AND
       * the other side of the link is loaded, remove the current instance from
       * it as well.
       */
      void removeFilterSetExcitationFilterLinkFromBoth(omero::model::FilterSetExcitationFilterLink link, bool bothSides);
      FilterLinkedExcitationFilterSeq linkedExcitationFilterList();
      FilterEmissionFilterLinkSeq emissionFilterLinkSeq;
      bool emissionFilterLinkLoaded;
      omero::sys::CountMap emissionFilterLinkCountPerOwner;
      /*
       * Unloads the emissionFilterLink collection. Any access to this
       * collection will throw an omero.UnloadedCollectionException.
       *
       * See sizeOfEmissionFilterLink() on how to test for unloaded collections.
       * See reloadEmissionFilterLink() on how to reset the value.
       *
       */
      void unloadEmissionFilterLink();
      int sizeOfEmissionFilterLink();
      FilterEmissionFilterLinkSeq copyEmissionFilterLink();
      // See language-specific iterator methods
      void addFilterSetEmissionFilterLink(FilterSetEmissionFilterLink target);
      /*
       * Adds all the members of the FilterEmissionFilterLinkSeq sequence to
       * the emissionFilterLinkSeq field.
       */
      void addAllFilterSetEmissionFilterLinkSet(FilterEmissionFilterLinkSeq targets);
      void removeFilterSetEmissionFilterLink(FilterSetEmissionFilterLink theTarget);
      /*
       * Removes all the members of the FilterEmissionFilterLinkSeq sequence from
       * the emissionFilterLinkSeq field.
       */
      void removeAllFilterSetEmissionFilterLinkSet(FilterEmissionFilterLinkSeq targets);
      void clearEmissionFilterLink();

      /*
       * Allows reloading the protected emissionFilterLink collection
       * from another instance of Filter. The argument's collection
       * will be unloaded and all member entities will have their
       * inverse property altered.
       *
       * The argument's id must match and it's update id must be present and
       * greater than or equal to that of the current object.
       */
      void reloadEmissionFilterLink(Filter toCopy);
      omero::sys::CountMap getEmissionFilterLinkCountPerOwner();
      FilterSetEmissionFilterLink linkEmissionFilter(FilterSet addition);

      /*
       * Add the link to the current instance and if bothSides is true AND
       * the other side of the link is loaded, add the current instance to
       * it as well.
       */
      void addFilterSetEmissionFilterLinkToBoth(omero::model::FilterSetEmissionFilterLink link, bool bothSides);
      FilterEmissionFilterLinkSeq findFilterSetEmissionFilterLink(FilterSet removal);
      void unlinkEmissionFilter(FilterSet removal);

      /*
       * Remove the link from the current instance and if bothSides is true AND
       * the other side of the link is loaded, remove the current instance from
       * it as well.
       */
      void removeFilterSetEmissionFilterLinkFromBoth(omero::model::FilterSetEmissionFilterLink link, bool bothSides);
      FilterLinkedEmissionFilterSeq linkedEmissionFilterList();
    };
  };
};
#endif // FILTER_ICE