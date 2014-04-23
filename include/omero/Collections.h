// **********************************************************************
//
// Copyright (c) 2003-2013 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************
//
// Ice version 3.5.1
//
// <auto-generated>
//
// Generated from file `Collections.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

#ifndef __omero__opt_hudson_workspace_OMERO_5_0_release_src_components_blitz_generated_omero_Collections_h__
#define __omero__opt_hudson_workspace_OMERO_5_0_release_src_components_blitz_generated_omero_Collections_h__

#include <Ice/ProxyF.h>
#include <Ice/ObjectF.h>
#include <Ice/Exception.h>
#include <Ice/LocalObject.h>
#include <Ice/StreamHelpers.h>
#include <Ice/Proxy.h>
#include <Ice/Object.h>
#include <Ice/Outgoing.h>
#include <Ice/OutgoingAsync.h>
#include <Ice/Incoming.h>
#include <Ice/Direct.h>
#include <Ice/FactoryTableInit.h>
#include <IceUtil/ScopedArray.h>
#include <IceUtil/Optional.h>
#include <Ice/StreamF.h>
#include <omero/ModelF.h>
#include <omero/RTypes.h>
#include <omero/System.h>
#include <Ice/UndefSysMacros.h>

#ifndef ICE_IGNORE_VERSION
#   if ICE_INT_VERSION / 100 != 305
#       error Ice version mismatch!
#   endif
#   if ICE_INT_VERSION % 100 > 50
#       error Beta header file detected
#   endif
#   if ICE_INT_VERSION % 100 < 1
#       error Ice patch level mismatch!
#   endif
#endif

namespace IceProxy
{

}

namespace omero
{

namespace api
{

typedef ::std::map< ::std::string, ::omero::model::AnnotationPtr> SearchMetadata;

typedef ::std::vector< ::std::string> StringSet;

typedef ::std::vector< ::Ice::Long> LongList;

typedef ::std::vector< ::Ice::Int> IntegerList;

typedef ::std::vector< ::omero::api::SearchMetadata> SearchMetadataList;

typedef ::std::vector< ::omero::model::ExperimenterPtr> ExperimenterList;

typedef ::std::vector< ::omero::model::ExperimenterGroupPtr> ExperimenterGroupList;

typedef ::std::vector< ::omero::model::EventPtr> EventList;

typedef ::std::vector< ::omero::model::EventLogPtr> EventLogList;

typedef ::std::vector< ::omero::model::AnnotationPtr> AnnotationList;

typedef ::std::vector< ::omero::model::SessionPtr> SessionList;

typedef ::std::vector< ::omero::model::IObjectPtr> IObjectList;

typedef ::std::vector< ::omero::model::ProjectPtr> ProjectList;

typedef ::std::vector< ::omero::model::DatasetPtr> DatasetList;

typedef ::std::vector< ::omero::model::ImagePtr> ImageList;

typedef ::std::vector< ::omero::model::LogicalChannelPtr> LogicalChannelList;

typedef ::std::vector< ::omero::model::OriginalFilePtr> OriginalFileList;

typedef ::std::vector< ::omero::model::PixelsPtr> PixelsList;

typedef ::std::vector< ::omero::model::PixelsTypePtr> PixelsTypeList;

typedef ::std::vector< ::omero::model::RoiPtr> RoiList;

typedef ::std::vector< ::omero::model::ScriptJobPtr> ScriptJobList;

typedef ::std::vector< ::omero::model::ShapePtr> ShapeList;

typedef ::std::vector< ::omero::model::ChecksumAlgorithmPtr> ChecksumAlgorithmList;

typedef ::std::vector<bool> BoolArray;

typedef ::std::vector< ::Ice::Byte> ByteArray;

typedef ::std::vector< ::Ice::Short> ShortArray;

typedef ::std::vector< ::Ice::Int> IntegerArray;

typedef ::std::vector< ::Ice::Long> LongArray;

typedef ::std::vector< ::Ice::Float> FloatArray;

typedef ::std::vector< ::Ice::Double> DoubleArray;

typedef ::std::vector< ::std::string> StringArray;

typedef ::std::vector< ::omero::api::ByteArray> ByteArrayArray;

typedef ::std::vector< ::omero::api::ShortArray> ShortArrayArray;

typedef ::std::vector< ::omero::api::IntegerArray> IntegerArrayArray;

typedef ::std::vector< ::omero::api::IntegerArrayArray> IntegerArrayArrayArray;

typedef ::std::vector< ::omero::api::LongArray> LongArrayArray;

typedef ::std::vector< ::omero::api::FloatArray> FloatArrayArray;

typedef ::std::vector< ::omero::api::FloatArrayArray> FloatArrayArrayArray;

typedef ::std::vector< ::omero::api::DoubleArray> DoubleArrayArray;

typedef ::std::vector< ::omero::api::DoubleArrayArray> DoubleArrayArrayArray;

typedef ::std::vector< ::omero::api::StringArray> StringArrayArray;

typedef ::std::vector< ::omero::RTypeDict> RTypeDictArray;

typedef ::std::map< ::Ice::Long, ::std::string> LongStringMap;

typedef ::std::map< ::Ice::Long, ::Ice::Int> LongIntMap;

typedef ::std::map< ::Ice::Long, ::omero::api::ByteArray> LongByteArrayMap;

typedef ::std::map< ::Ice::Long, ::omero::model::PixelsPtr> LongPixelsMap;

typedef ::std::map< ::Ice::Int, ::std::string> IntStringMap;

typedef ::std::map< ::std::string, ::omero::RTypePtr> StringRTypeMap;

typedef ::std::map< ::std::string, ::omero::model::ExperimenterPtr> UserMap;

typedef ::std::map< ::std::string, ::omero::model::OriginalFilePtr> OriginalFileMap;

typedef ::std::map< ::std::string, ::std::string> StringStringMap;

typedef ::std::map< ::std::string, ::omero::api::StringArray> StringStringArrayMap;

typedef ::std::map< ::std::string, ::Ice::Long> StringLongMap;

typedef ::std::map< ::std::string, ::Ice::Int> StringIntMap;

typedef ::std::map< ::std::string, ::Ice::LongSeq> IdListMap;

typedef ::std::map< ::std::string, ::omero::api::LongList> StringLongListMap;

typedef ::std::map<bool, ::omero::api::LongList> BooleanLongListMap;

typedef ::std::map<bool, ::omero::sys::LongList> BooleanIdListMap;

typedef ::std::map< ::std::string, ::omero::api::IObjectList> IObjectListMap;

typedef ::std::map< ::Ice::Long, ::omero::api::IObjectList> LongIObjectListMap;

typedef ::std::map< ::std::string, ::omero::api::ShapeList> StringShapeListMap;

typedef ::std::map< ::Ice::Long, ::omero::api::ShapeList> LongShapeListMap;

typedef ::std::map< ::Ice::Int, ::omero::api::ShapeList> IntShapeListMap;

typedef ::std::map< ::Ice::Long, ::omero::api::AnnotationList> LongAnnotationListMap;

typedef ::std::map< ::Ice::Long, ::omero::api::BooleanLongListMap> IdBooleanLongListMapMap;

}

}

namespace IceProxy
{

}

namespace IceDelegate
{

}

namespace IceDelegateM
{

}

namespace IceDelegateD
{

}

#endif
