   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef LIGHTPATH_ICE
#define LIGHTPATH_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {
    class LightPathExcitationFilterLink;
    class Filter;
    class Dichroic;
    class LightPathEmissionFilterLink;
    class Filter;
    class LightPathAnnotationLink;
    class Annotation;
    class Details;
    ["java:type:java.util.ArrayList"] sequence<omero::model::LightPathExcitationFilterLink> LightPathExcitationFilterLinkSeq;
    ["java:type:java.util.ArrayList"] sequence<omero::model::Filter> LightPathLinkedExcitationFilterSeq;
    ["java:type:java.util.ArrayList"] sequence<omero::model::LightPathEmissionFilterLink> LightPathEmissionFilterLinkSeq;
    ["java:type:java.util.ArrayList"] sequence<omero::model::Filter> LightPathLinkedEmissionFilterSeq;
    ["java:type:java.util.ArrayList"] sequence<omero::model::LightPathAnnotationLink> LightPathAnnotationLinksSeq;
    ["java:type:java.util.ArrayList"] sequence<omero::model::Annotation> LightPathLinkedAnnotationSeq;
    ["protected"] class LightPath
    extends omero::model::IObject
    {
      omero::RInt version;
      omero::RInt getVersion();
      void setVersion(omero::RInt theVersion);
      LightPathExcitationFilterLinkSeq excitationFilterLinkSeq;
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
      LightPathExcitationFilterLinkSeq copyExcitationFilterLink();
      // See language-specific iterator methods
      void addLightPathExcitationFilterLink(LightPathExcitationFilterLink target);
      /*
       * Adds all the members of the LightPathExcitationFilterLinkSeq sequence to
       * the excitationFilterLinkSeq field.
       */
      void addAllLightPathExcitationFilterLinkSet(LightPathExcitationFilterLinkSeq targets);
      void removeLightPathExcitationFilterLink(LightPathExcitationFilterLink theTarget);
      /*
       * Removes all the members of the LightPathExcitationFilterLinkSeq sequence from
       * the excitationFilterLinkSeq field.
       */
      void removeAllLightPathExcitationFilterLinkSet(LightPathExcitationFilterLinkSeq targets);
      void clearExcitationFilterLink();

      /*
       * Allows reloading the protected excitationFilterLink collection
       * from another instance of LightPath. The argument's collection
       * will be unloaded and all member entities will have their
       * inverse property altered.
       *
       * The argument's id must match and it's update id must be present and
       * greater than or equal to that of the current object.
       */
      void reloadExcitationFilterLink(LightPath toCopy);
      LightPathExcitationFilterLink getLightPathExcitationFilterLink(int index);
      LightPathExcitationFilterLink setLightPathExcitationFilterLink(int index, LightPathExcitationFilterLink theElement);
      LightPathExcitationFilterLink getPrimaryLightPathExcitationFilterLink();
      LightPathExcitationFilterLink setPrimaryLightPathExcitationFilterLink(LightPathExcitationFilterLink theElement);
      omero::sys::CountMap getExcitationFilterLinkCountPerOwner();
      LightPathExcitationFilterLink linkExcitationFilter(Filter addition);

      /*
       * Add the link to the current instance and if bothSides is true AND
       * the other side of the link is loaded, add the current instance to
       * it as well.
       */
      void addLightPathExcitationFilterLinkToBoth(omero::model::LightPathExcitationFilterLink link, bool bothSides);
      LightPathExcitationFilterLinkSeq findLightPathExcitationFilterLink(Filter removal);
      void unlinkExcitationFilter(Filter removal);

      /*
       * Remove the link from the current instance and if bothSides is true AND
       * the other side of the link is loaded, remove the current instance from
       * it as well.
       */
      void removeLightPathExcitationFilterLinkFromBoth(omero::model::LightPathExcitationFilterLink link, bool bothSides);
      LightPathLinkedExcitationFilterSeq linkedExcitationFilterList();
      omero::model::Dichroic dichroic;
      omero::model::Dichroic getDichroic();
      void setDichroic(omero::model::Dichroic theDichroic);
      LightPathEmissionFilterLinkSeq emissionFilterLinkSeq;
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
      LightPathEmissionFilterLinkSeq copyEmissionFilterLink();
      // See language-specific iterator methods
      void addLightPathEmissionFilterLink(LightPathEmissionFilterLink target);
      /*
       * Adds all the members of the LightPathEmissionFilterLinkSeq sequence to
       * the emissionFilterLinkSeq field.
       */
      void addAllLightPathEmissionFilterLinkSet(LightPathEmissionFilterLinkSeq targets);
      void removeLightPathEmissionFilterLink(LightPathEmissionFilterLink theTarget);
      /*
       * Removes all the members of the LightPathEmissionFilterLinkSeq sequence from
       * the emissionFilterLinkSeq field.
       */
      void removeAllLightPathEmissionFilterLinkSet(LightPathEmissionFilterLinkSeq targets);
      void clearEmissionFilterLink();

      /*
       * Allows reloading the protected emissionFilterLink collection
       * from another instance of LightPath. The argument's collection
       * will be unloaded and all member entities will have their
       * inverse property altered.
       *
       * The argument's id must match and it's update id must be present and
       * greater than or equal to that of the current object.
       */
      void reloadEmissionFilterLink(LightPath toCopy);
      omero::sys::CountMap getEmissionFilterLinkCountPerOwner();
      LightPathEmissionFilterLink linkEmissionFilter(Filter addition);

      /*
       * Add the link to the current instance and if bothSides is true AND
       * the other side of the link is loaded, add the current instance to
       * it as well.
       */
      void addLightPathEmissionFilterLinkToBoth(omero::model::LightPathEmissionFilterLink link, bool bothSides);
      LightPathEmissionFilterLinkSeq findLightPathEmissionFilterLink(Filter removal);
      void unlinkEmissionFilter(Filter removal);

      /*
       * Remove the link from the current instance and if bothSides is true AND
       * the other side of the link is loaded, remove the current instance from
       * it as well.
       */
      void removeLightPathEmissionFilterLinkFromBoth(omero::model::LightPathEmissionFilterLink link, bool bothSides);
      LightPathLinkedEmissionFilterSeq linkedEmissionFilterList();
      LightPathAnnotationLinksSeq annotationLinksSeq;
      bool annotationLinksLoaded;
      omero::sys::CountMap annotationLinksCountPerOwner;
      /*
       * Unloads the annotationLinks collection. Any access to this
       * collection will throw an omero.UnloadedCollectionException.
       *
       * See sizeOfAnnotationLinks() on how to test for unloaded collections.
       * See reloadAnnotationLinks() on how to reset the value.
       *
       */
      void unloadAnnotationLinks();
      int sizeOfAnnotationLinks();
      LightPathAnnotationLinksSeq copyAnnotationLinks();
      // See language-specific iterator methods
      void addLightPathAnnotationLink(LightPathAnnotationLink target);
      /*
       * Adds all the members of the LightPathAnnotationLinksSeq sequence to
       * the annotationLinksSeq field.
       */
      void addAllLightPathAnnotationLinkSet(LightPathAnnotationLinksSeq targets);
      void removeLightPathAnnotationLink(LightPathAnnotationLink theTarget);
      /*
       * Removes all the members of the LightPathAnnotationLinksSeq sequence from
       * the annotationLinksSeq field.
       */
      void removeAllLightPathAnnotationLinkSet(LightPathAnnotationLinksSeq targets);
      void clearAnnotationLinks();

      /*
       * Allows reloading the protected annotationLinks collection
       * from another instance of LightPath. The argument's collection
       * will be unloaded and all member entities will have their
       * inverse property altered.
       *
       * The argument's id must match and it's update id must be present and
       * greater than or equal to that of the current object.
       */
      void reloadAnnotationLinks(LightPath toCopy);
      omero::sys::CountMap getAnnotationLinksCountPerOwner();
      LightPathAnnotationLink linkAnnotation(Annotation addition);

      /*
       * Add the link to the current instance and if bothSides is true AND
       * the other side of the link is loaded, add the current instance to
       * it as well.
       */
      void addLightPathAnnotationLinkToBoth(omero::model::LightPathAnnotationLink link, bool bothSides);
      LightPathAnnotationLinksSeq findLightPathAnnotationLink(Annotation removal);
      void unlinkAnnotation(Annotation removal);

      /*
       * Remove the link from the current instance and if bothSides is true AND
       * the other side of the link is loaded, remove the current instance from
       * it as well.
       */
      void removeLightPathAnnotationLinkFromBoth(omero::model::LightPathAnnotationLink link, bool bothSides);
      LightPathLinkedAnnotationSeq linkedAnnotationList();
    };
  };
};
#endif // LIGHTPATH_ICE
