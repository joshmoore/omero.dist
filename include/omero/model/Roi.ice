   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.ice for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef ROI_ICE
#define ROI_ICE
#include <omero/model/IObject.ice>
#include <omero/RTypes.ice>
#include <omero/model/RTypes.ice>
#include <omero/System.ice>
#include <omero/Collections.ice>
module omero {
  module model {
    class Shape;
    class Image;
    class OriginalFile;
    class RoiAnnotationLink;
    class Annotation;
    class Details;
    ["java:type:java.util.ArrayList"] sequence<omero::model::Shape> RoiShapesSeq;
    ["java:type:java.util.ArrayList"] sequence<omero::model::RoiAnnotationLink> RoiAnnotationLinksSeq;
    ["java:type:java.util.ArrayList"] sequence<omero::model::Annotation> RoiLinkedAnnotationSeq;
    ["protected"] class Roi
    extends omero::model::IObject
    {
      omero::RInt version;
      omero::RInt getVersion();
      void setVersion(omero::RInt theVersion);
      omero::RString name;
      omero::RString getName();
      void setName(omero::RString theName);
      RoiShapesSeq shapesSeq;
      bool shapesLoaded;
      /*
       * Unloads the shapes collection. Any access to this
       * collection will throw an omero.UnloadedCollectionException.
       *
       * See sizeOfShapes() on how to test for unloaded collections.
       * See reloadShapes() on how to reset the value.
       *
       */
      void unloadShapes();
      int sizeOfShapes();
      RoiShapesSeq copyShapes();
      // See language-specific iterator methods
      void addShape(Shape target);
      /*
       * Adds all the members of the RoiShapesSeq sequence to
       * the shapesSeq field.
       */
      void addAllShapeSet(RoiShapesSeq targets);
      void removeShape(Shape theTarget);
      /*
       * Removes all the members of the RoiShapesSeq sequence from
       * the shapesSeq field.
       */
      void removeAllShapeSet(RoiShapesSeq targets);
      void clearShapes();

      /*
       * Allows reloading the protected shapes collection
       * from another instance of Roi. The argument's collection
       * will be unloaded and all member entities will have their
       * inverse property altered.
       *
       * The argument's id must match and it's update id must be present and
       * greater than or equal to that of the current object.
       */
      void reloadShapes(Roi toCopy);
      Shape getShape(int index);
      Shape setShape(int index, Shape theElement);
      Shape getPrimaryShape();
      Shape setPrimaryShape(Shape theElement);
      omero::model::Image image;
      omero::model::Image getImage();
      void setImage(omero::model::Image theImage);
      omero::model::OriginalFile source;
      omero::model::OriginalFile getSource();
      void setSource(omero::model::OriginalFile theSource);
      omero::api::StringArray namespaces;
      omero::api::StringArray getNamespaces();
      void setNamespaces(omero::api::StringArray theNamespaces);
      omero::api::StringArrayArray keywords;
      omero::api::StringArrayArray getKeywords();
      void setKeywords(omero::api::StringArrayArray theKeywords);
      RoiAnnotationLinksSeq annotationLinksSeq;
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
      RoiAnnotationLinksSeq copyAnnotationLinks();
      // See language-specific iterator methods
      void addRoiAnnotationLink(RoiAnnotationLink target);
      /*
       * Adds all the members of the RoiAnnotationLinksSeq sequence to
       * the annotationLinksSeq field.
       */
      void addAllRoiAnnotationLinkSet(RoiAnnotationLinksSeq targets);
      void removeRoiAnnotationLink(RoiAnnotationLink theTarget);
      /*
       * Removes all the members of the RoiAnnotationLinksSeq sequence from
       * the annotationLinksSeq field.
       */
      void removeAllRoiAnnotationLinkSet(RoiAnnotationLinksSeq targets);
      void clearAnnotationLinks();

      /*
       * Allows reloading the protected annotationLinks collection
       * from another instance of Roi. The argument's collection
       * will be unloaded and all member entities will have their
       * inverse property altered.
       *
       * The argument's id must match and it's update id must be present and
       * greater than or equal to that of the current object.
       */
      void reloadAnnotationLinks(Roi toCopy);
      omero::sys::CountMap getAnnotationLinksCountPerOwner();
      RoiAnnotationLink linkAnnotation(Annotation addition);

      /*
       * Add the link to the current instance and if bothSides is true AND
       * the other side of the link is loaded, add the current instance to
       * it as well.
       */
      void addRoiAnnotationLinkToBoth(omero::model::RoiAnnotationLink link, bool bothSides);
      RoiAnnotationLinksSeq findRoiAnnotationLink(Annotation removal);
      void unlinkAnnotation(Annotation removal);

      /*
       * Remove the link from the current instance and if bothSides is true AND
       * the other side of the link is loaded, remove the current instance from
       * it as well.
       */
      void removeRoiAnnotationLinkFromBoth(omero::model::RoiAnnotationLink link, bool bothSides);
      RoiLinkedAnnotationSeq linkedAnnotationList();
      omero::RString description;
      omero::RString getDescription();
      void setDescription(omero::RString theDescription);
    };
  };
};
#endif // ROI_ICE
