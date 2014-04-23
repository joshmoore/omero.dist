   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef ANNOTATION_ICE
#define ANNOTATION_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {
    class AnnotationAnnotationLink;
    class Annotation;
    class Details;
    ["java:type:java.util.ArrayList"] sequence<omero::model::AnnotationAnnotationLink> AnnotationAnnotationLinksSeq;
    ["java:type:java.util.ArrayList"] sequence<omero::model::Annotation> AnnotationLinkedAnnotationSeq;
    ["protected"] class Annotation
    extends omero::model::IObject
    {
      omero::RInt version;
      omero::RInt getVersion();
      void setVersion(omero::RInt theVersion);
      omero::RString ns;
      omero::RString getNs();
      void setNs(omero::RString theNs);
      omero::RString description;
      omero::RString getDescription();
      void setDescription(omero::RString theDescription);
      AnnotationAnnotationLinksSeq annotationLinksSeq;
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
      AnnotationAnnotationLinksSeq copyAnnotationLinks();
      // See language-specific iterator methods
      void addAnnotationAnnotationLink(AnnotationAnnotationLink target);
      /*
       * Adds all the members of the AnnotationAnnotationLinksSeq sequence to
       * the annotationLinksSeq field.
       */
      void addAllAnnotationAnnotationLinkSet(AnnotationAnnotationLinksSeq targets);
      void removeAnnotationAnnotationLink(AnnotationAnnotationLink theTarget);
      /*
       * Removes all the members of the AnnotationAnnotationLinksSeq sequence from
       * the annotationLinksSeq field.
       */
      void removeAllAnnotationAnnotationLinkSet(AnnotationAnnotationLinksSeq targets);
      void clearAnnotationLinks();

      /*
       * Allows reloading the protected annotationLinks collection
       * from another instance of Annotation. The argument's collection
       * will be unloaded and all member entities will have their
       * inverse property altered.
       *
       * The argument's id must match and it's update id must be present and
       * greater than or equal to that of the current object.
       */
      void reloadAnnotationLinks(Annotation toCopy);
      omero::sys::CountMap getAnnotationLinksCountPerOwner();
      AnnotationAnnotationLink linkAnnotation(Annotation addition);

      /*
       * Add the link to the current instance and if bothSides is true AND
       * the other side of the link is loaded, add the current instance to
       * it as well.
       */
      void addAnnotationAnnotationLinkToBoth(omero::model::AnnotationAnnotationLink link, bool bothSides);
      AnnotationAnnotationLinksSeq findAnnotationAnnotationLink(Annotation removal);
      void unlinkAnnotation(Annotation removal);

      /*
       * Remove the link from the current instance and if bothSides is true AND
       * the other side of the link is loaded, remove the current instance from
       * it as well.
       */
      void removeAnnotationAnnotationLinkFromBoth(omero::model::AnnotationAnnotationLink link, bool bothSides);
      AnnotationLinkedAnnotationSeq linkedAnnotationList();
    };
  };
};
#endif // ANNOTATION_ICE