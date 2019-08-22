   /*
   **   Generated by blitz/resources/templates/combined.vm
   **   See ../../README.h for information on these types.
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
#ifndef MASKI_H
#define MASKI_H
#include <omero/IceNoWarnPush.h>
#include <omero/RTypes.h>
#include <omero/model/RTypes.h>
#include <omero/model/IObject.h>
#include <omero/model/Mask.h>
#include <omero/IceNoWarnPop.h>
#include <omero/ClientErrors.h>
#include <omero/model/DetailsI.h>
#include <omero/model/NamedValue.h>
#include <omero/templates.h>
#include <IceUtil/Config.h>
#include <Ice/Handle.h>
#ifndef OMERO_CLIENT
#   ifdef OMERO_CLIENT_EXPORTS
#       define OMERO_CLIENT ICE_DECLSPEC_EXPORT
#   else
#       define OMERO_CLIENT ICE_DECLSPEC_IMPORT
#   endif
#endif
namespace omero {
  namespace model {
    class OMERO_CLIENT MaskI;
  }
}
namespace IceInternal {
  OMERO_CLIENT ::Ice::Object* upCast(::omero::model::MaskI*);
}
namespace omero {
  namespace model {
  typedef IceInternal::Handle<MaskI> MaskIPtr;
    class OMERO_CLIENT MaskI : virtual public Mask {
   public:
      static const std::string X;
      static const std::string Y;
      static const std::string WIDTH;
      static const std::string HEIGHT;
      static const std::string PIXELS;
      static const std::string TEXTVALUE;
      static const std::string BYTES;
      static const std::string THEZ;
      static const std::string THET;
      static const std::string THEC;
      static const std::string ROI;
      static const std::string LOCKED;
      static const std::string TRANSFORM;
      static const std::string FILLCOLOR;
      static const std::string FILLRULE;
      static const std::string STROKECOLOR;
      static const std::string STROKEDASHARRAY;
      static const std::string STROKEWIDTH;
      static const std::string FONTFAMILY;
      static const std::string FONTSIZE;
      static const std::string FONTSTYLE;
      static const std::string ANNOTATIONLINKS;
      static const std::string DETAILS;
    protected:
      void errorIfUnloaded();
      void throwNullCollectionException(std::string propertyName);
      virtual void toggleCollectionsLoaded(bool load);
      virtual ~MaskI();
    public:
      MaskI();
      MaskI(omero::RLongPtr idPtr, bool isLoaded = false);
      MaskI(Ice::Long id, bool isLoaded = false);
      virtual void unload(const Ice::Current& current = Ice::Current());
      virtual bool isLoaded(const Ice::Current& current = Ice::Current());
      virtual void unloadCollections(const Ice::Current& current = Ice::Current());
      virtual bool isGlobal(const Ice::Current& current = Ice::Current());
      virtual bool isMutable(const Ice::Current& current = Ice::Current());
      virtual bool isAnnotated(const Ice::Current& current = Ice::Current());
      virtual bool isLink(const Ice::Current& current = Ice::Current());
      virtual omero::model::IObjectPtr shallowCopy(const Ice::Current& current = Ice::Current());
      virtual omero::model::IObjectPtr proxy(const Ice::Current& current = Ice::Current());
      virtual omero::model::DetailsPtr getDetails(const Ice::Current& current = Ice::Current());
      virtual void unloadDetails(const Ice::Current& current = Ice::Current());
      virtual omero::RLongPtr getId(const Ice::Current& current = Ice::Current());
      virtual void setId( const omero::RLongPtr& id, const Ice::Current& current = Ice::Current() );
      virtual omero::RIntPtr getVersion(const Ice::Current& current = Ice::Current());
      virtual void setVersion( const omero::RIntPtr& version, const Ice::Current& current = Ice::Current() );

      //
      //  Mask.x
      //
      virtual void unloadX();
      virtual omero::RDoublePtr getX(const Ice::Current& current = Ice::Current());
      virtual void setX(const omero::RDoublePtr& _x, const Ice::Current& current = Ice::Current());

      //
      //  Mask.y
      //
      virtual void unloadY();
      virtual omero::RDoublePtr getY(const Ice::Current& current = Ice::Current());
      virtual void setY(const omero::RDoublePtr& _y, const Ice::Current& current = Ice::Current());

      //
      //  Mask.width
      //
      virtual void unloadWidth();
      virtual omero::RDoublePtr getWidth(const Ice::Current& current = Ice::Current());
      virtual void setWidth(const omero::RDoublePtr& _width, const Ice::Current& current = Ice::Current());

      //
      //  Mask.height
      //
      virtual void unloadHeight();
      virtual omero::RDoublePtr getHeight(const Ice::Current& current = Ice::Current());
      virtual void setHeight(const omero::RDoublePtr& _height, const Ice::Current& current = Ice::Current());

      //
      //  Mask.pixels
      //
      virtual void unloadPixels();
      virtual omero::model::PixelsPtr getPixels(const Ice::Current& current = Ice::Current());
      virtual void setPixels(const omero::model::PixelsPtr& _pixels, const Ice::Current& current = Ice::Current());

      //
      //  Mask.textValue
      //
      virtual void unloadTextValue();
      virtual omero::RStringPtr getTextValue(const Ice::Current& current = Ice::Current());
      virtual void setTextValue(const omero::RStringPtr& _textValue, const Ice::Current& current = Ice::Current());

      //
      //  Mask.bytes
      //
      virtual void unloadBytes();
      virtual Ice::ByteSeq getBytes(const Ice::Current& current = Ice::Current());
      virtual void setBytes(const Ice::ByteSeq& _bytes, const Ice::Current& current = Ice::Current());

      //
      //  Mask.theZ
      //
      virtual void unloadTheZ();
      virtual omero::RIntPtr getTheZ(const Ice::Current& current = Ice::Current());
      virtual void setTheZ(const omero::RIntPtr& _theZ, const Ice::Current& current = Ice::Current());

      //
      //  Mask.theT
      //
      virtual void unloadTheT();
      virtual omero::RIntPtr getTheT(const Ice::Current& current = Ice::Current());
      virtual void setTheT(const omero::RIntPtr& _theT, const Ice::Current& current = Ice::Current());

      //
      //  Mask.theC
      //
      virtual void unloadTheC();
      virtual omero::RIntPtr getTheC(const Ice::Current& current = Ice::Current());
      virtual void setTheC(const omero::RIntPtr& _theC, const Ice::Current& current = Ice::Current());

      //
      //  Mask.roi
      //
      virtual void unloadRoi();
      virtual omero::model::RoiPtr getRoi(const Ice::Current& current = Ice::Current());
      virtual void setRoi(const omero::model::RoiPtr& _roi, const Ice::Current& current = Ice::Current());

      //
      //  Mask.locked
      //
      virtual void unloadLocked();
      virtual omero::RBoolPtr getLocked(const Ice::Current& current = Ice::Current());
      virtual void setLocked(const omero::RBoolPtr& _locked, const Ice::Current& current = Ice::Current());

      //
      //  Mask.transform
      //
      virtual void unloadTransform();
      virtual omero::model::AffineTransformPtr getTransform(const Ice::Current& current = Ice::Current());
      virtual void setTransform(const omero::model::AffineTransformPtr& _transform, const Ice::Current& current = Ice::Current());

      //
      //  Mask.fillColor
      //
      virtual void unloadFillColor();
      virtual omero::RIntPtr getFillColor(const Ice::Current& current = Ice::Current());
      virtual void setFillColor(const omero::RIntPtr& _fillColor, const Ice::Current& current = Ice::Current());

      //
      //  Mask.fillRule
      //
      virtual void unloadFillRule();
      virtual omero::RStringPtr getFillRule(const Ice::Current& current = Ice::Current());
      virtual void setFillRule(const omero::RStringPtr& _fillRule, const Ice::Current& current = Ice::Current());

      //
      //  Mask.strokeColor
      //
      virtual void unloadStrokeColor();
      virtual omero::RIntPtr getStrokeColor(const Ice::Current& current = Ice::Current());
      virtual void setStrokeColor(const omero::RIntPtr& _strokeColor, const Ice::Current& current = Ice::Current());

      //
      //  Mask.strokeDashArray
      //
      virtual void unloadStrokeDashArray();
      virtual omero::RStringPtr getStrokeDashArray(const Ice::Current& current = Ice::Current());
      virtual void setStrokeDashArray(const omero::RStringPtr& _strokeDashArray, const Ice::Current& current = Ice::Current());

      //
      //  Mask.strokeWidth
      //
      virtual void unloadStrokeWidth();
      virtual omero::model::LengthPtr getStrokeWidth(const Ice::Current& current = Ice::Current());
      virtual void setStrokeWidth(const omero::model::LengthPtr& _strokeWidth, const Ice::Current& current = Ice::Current());

      //
      //  Mask.fontFamily
      //
      virtual void unloadFontFamily();
      virtual omero::RStringPtr getFontFamily(const Ice::Current& current = Ice::Current());
      virtual void setFontFamily(const omero::RStringPtr& _fontFamily, const Ice::Current& current = Ice::Current());

      //
      //  Mask.fontSize
      //
      virtual void unloadFontSize();
      virtual omero::model::LengthPtr getFontSize(const Ice::Current& current = Ice::Current());
      virtual void setFontSize(const omero::model::LengthPtr& _fontSize, const Ice::Current& current = Ice::Current());

      //
      //  Mask.fontStyle
      //
      virtual void unloadFontStyle();
      virtual omero::RStringPtr getFontStyle(const Ice::Current& current = Ice::Current());
      virtual void setFontStyle(const omero::RStringPtr& _fontStyle, const Ice::Current& current = Ice::Current());

      //
      //  Mask.annotationLinks
      //
      virtual void unloadAnnotationLinks(const Ice::Current& current = Ice::Current());
    protected:
      virtual ShapeAnnotationLinksSeq getAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual void setAnnotationLinks(const ShapeAnnotationLinksSeq& _annotationLinks, const Ice::Current& current = Ice::Current());
    public:
      virtual bool isAnnotationLinksLoaded();
      virtual Ice::Int sizeOfAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual ShapeAnnotationLinksSeq copyAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual ShapeAnnotationLinksSeq::iterator beginAnnotationLinks();
      virtual ShapeAnnotationLinksSeq::iterator endAnnotationLinks();
      virtual void addShapeAnnotationLink(const ShapeAnnotationLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void addAllShapeAnnotationLinkSet(const ShapeAnnotationLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void removeShapeAnnotationLink(const ShapeAnnotationLinkPtr& target, const Ice::Current& current = Ice::Current());
      virtual void removeAllShapeAnnotationLinkSet(const ShapeAnnotationLinksSeq& targets, const Ice::Current& current = Ice::Current());
      virtual void clearAnnotationLinks(const Ice::Current& current = Ice::Current());
      virtual void reloadAnnotationLinks(const ShapePtr& toCopy, const Ice::Current& current = Ice::Current());
      virtual omero::sys::CountMap getAnnotationLinksCountPerOwner(const Ice::Current& current = Ice::Current());
      virtual ShapeAnnotationLinkPtr linkAnnotation(const AnnotationPtr& addition, const Ice::Current& current = Ice::Current());
      virtual void addShapeAnnotationLinkToBoth(const ShapeAnnotationLinkPtr& link, bool /*unused*/, const Ice::Current& current = Ice::Current());
      virtual ShapeAnnotationLinksSeq findShapeAnnotationLink(const AnnotationPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void unlinkAnnotation(const AnnotationPtr& removal, const Ice::Current& current = Ice::Current());
      virtual void removeShapeAnnotationLinkFromBoth(const ShapeAnnotationLinkPtr& link, bool bothSides, const Ice::Current& current = Ice::Current());
       virtual ShapeLinkedAnnotationSeq linkedAnnotationList(const Ice::Current& current = Ice::Current());
 };

}}
#endif // MASKI_H
