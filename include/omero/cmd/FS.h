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
// Generated from file `FS.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

#ifndef __omero_cmd__opt_hudson_workspace_OMERO_5_0_release_src_components_blitz_generated_omero_cmd_FS_h__
#define __omero_cmd__opt_hudson_workspace_OMERO_5_0_release_src_components_blitz_generated_omero_cmd_FS_h__

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
#include <Ice/IncomingAsync.h>
#include <Ice/Direct.h>
#include <Ice/FactoryTableInit.h>
#include <IceUtil/ScopedArray.h>
#include <IceUtil/Optional.h>
#include <Ice/StreamF.h>
#include <Ice/SlicedDataF.h>
#include <omero/Collections.h>
#include <omero/cmd/API.h>
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

namespace omero
{

namespace cmd
{

class OriginalMetadataRequest;
void __read(::IceInternal::BasicStream*, ::IceInternal::ProxyHandle< ::IceProxy::omero::cmd::OriginalMetadataRequest>&);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::cmd::OriginalMetadataRequest*);

class OriginalMetadataResponse;
void __read(::IceInternal::BasicStream*, ::IceInternal::ProxyHandle< ::IceProxy::omero::cmd::OriginalMetadataResponse>&);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::cmd::OriginalMetadataResponse*);

}

}

}

namespace omero
{

namespace cmd
{

class OriginalMetadataRequest;
bool operator==(const OriginalMetadataRequest&, const OriginalMetadataRequest&);
bool operator<(const OriginalMetadataRequest&, const OriginalMetadataRequest&);
::Ice::Object* upCast(::omero::cmd::OriginalMetadataRequest*);
typedef ::IceInternal::Handle< ::omero::cmd::OriginalMetadataRequest> OriginalMetadataRequestPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::cmd::OriginalMetadataRequest> OriginalMetadataRequestPrx;
void __patch(OriginalMetadataRequestPtr&, const ::Ice::ObjectPtr&);

class OriginalMetadataResponse;
bool operator==(const OriginalMetadataResponse&, const OriginalMetadataResponse&);
bool operator<(const OriginalMetadataResponse&, const OriginalMetadataResponse&);
::Ice::Object* upCast(::omero::cmd::OriginalMetadataResponse*);
typedef ::IceInternal::Handle< ::omero::cmd::OriginalMetadataResponse> OriginalMetadataResponsePtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::cmd::OriginalMetadataResponse> OriginalMetadataResponsePrx;
void __patch(OriginalMetadataResponsePtr&, const ::Ice::ObjectPtr&);

}

}

namespace IceAsync
{

}

namespace omero
{

namespace cmd
{

}

}

namespace IceProxy
{

namespace omero
{

namespace cmd
{

class OriginalMetadataRequest : virtual public ::IceProxy::omero::cmd::Request
{
public:
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_context(const ::Ice::Context& __context) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_context(__context).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_adapterId(const ::std::string& __id) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_adapterId(__id).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_endpoints(const ::Ice::EndpointSeq& __endpoints) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_endpoints(__endpoints).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_locatorCacheTimeout(int __timeout) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_locatorCacheTimeout(__timeout).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_connectionCached(bool __cached) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_connectionCached(__cached).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_endpointSelection(::Ice::EndpointSelectionType __est) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_endpointSelection(__est).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_secure(bool __secure) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_secure(__secure).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_preferSecure(bool __preferSecure) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_preferSecure(__preferSecure).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_router(const ::Ice::RouterPrx& __router) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_router(__router).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_locator(const ::Ice::LocatorPrx& __locator) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_locator(__locator).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_collocationOptimized(bool __co) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_collocationOptimized(__co).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_twoway() const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_twoway().get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_oneway() const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_oneway().get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_batchOneway() const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_batchOneway().get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_datagram() const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_datagram().get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_batchDatagram() const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_batchDatagram().get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_compress(bool __compress) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_compress(__compress).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_timeout(int __timeout) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_timeout(__timeout).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_connectionId(const ::std::string& __id) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_connectionId(__id).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataRequest> ice_encodingVersion(const ::Ice::EncodingVersion& __v) const
    {
        return dynamic_cast<OriginalMetadataRequest*>(::IceProxy::Ice::Object::ice_encodingVersion(__v).get());
    }
    
    static const ::std::string& ice_staticId();

private: 

    virtual ::IceInternal::Handle< ::IceDelegateM::Ice::Object> __createDelegateM();
    virtual ::IceInternal::Handle< ::IceDelegateD::Ice::Object> __createDelegateD();
    virtual ::IceProxy::Ice::Object* __newInstance() const;
};

class OriginalMetadataResponse : virtual public ::IceProxy::omero::cmd::Response
{
public:
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_context(const ::Ice::Context& __context) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_context(__context).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_adapterId(const ::std::string& __id) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_adapterId(__id).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_endpoints(const ::Ice::EndpointSeq& __endpoints) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_endpoints(__endpoints).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_locatorCacheTimeout(int __timeout) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_locatorCacheTimeout(__timeout).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_connectionCached(bool __cached) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_connectionCached(__cached).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_endpointSelection(::Ice::EndpointSelectionType __est) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_endpointSelection(__est).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_secure(bool __secure) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_secure(__secure).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_preferSecure(bool __preferSecure) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_preferSecure(__preferSecure).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_router(const ::Ice::RouterPrx& __router) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_router(__router).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_locator(const ::Ice::LocatorPrx& __locator) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_locator(__locator).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_collocationOptimized(bool __co) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_collocationOptimized(__co).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_twoway() const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_twoway().get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_oneway() const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_oneway().get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_batchOneway() const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_batchOneway().get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_datagram() const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_datagram().get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_batchDatagram() const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_batchDatagram().get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_compress(bool __compress) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_compress(__compress).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_timeout(int __timeout) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_timeout(__timeout).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_connectionId(const ::std::string& __id) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_connectionId(__id).get());
    }
    
    ::IceInternal::ProxyHandle<OriginalMetadataResponse> ice_encodingVersion(const ::Ice::EncodingVersion& __v) const
    {
        return dynamic_cast<OriginalMetadataResponse*>(::IceProxy::Ice::Object::ice_encodingVersion(__v).get());
    }
    
    static const ::std::string& ice_staticId();

private: 

    virtual ::IceInternal::Handle< ::IceDelegateM::Ice::Object> __createDelegateM();
    virtual ::IceInternal::Handle< ::IceDelegateD::Ice::Object> __createDelegateD();
    virtual ::IceProxy::Ice::Object* __newInstance() const;
};

}

}

}

namespace IceDelegate
{

namespace omero
{

namespace cmd
{

class OriginalMetadataRequest : virtual public ::IceDelegate::omero::cmd::Request
{
public:
};

class OriginalMetadataResponse : virtual public ::IceDelegate::omero::cmd::Response
{
public:
};

}

}

}

namespace IceDelegateM
{

namespace omero
{

namespace cmd
{

class OriginalMetadataRequest : virtual public ::IceDelegate::omero::cmd::OriginalMetadataRequest,
                                virtual public ::IceDelegateM::omero::cmd::Request
{
public:
};

class OriginalMetadataResponse : virtual public ::IceDelegate::omero::cmd::OriginalMetadataResponse,
                                 virtual public ::IceDelegateM::omero::cmd::Response
{
public:
};

}

}

}

namespace IceDelegateD
{

namespace omero
{

namespace cmd
{

class OriginalMetadataRequest : virtual public ::IceDelegate::omero::cmd::OriginalMetadataRequest,
                                virtual public ::IceDelegateD::omero::cmd::Request
{
public:
};

class OriginalMetadataResponse : virtual public ::IceDelegate::omero::cmd::OriginalMetadataResponse,
                                 virtual public ::IceDelegateD::omero::cmd::Response
{
public:
};

}

}

}

namespace omero
{

namespace cmd
{

class OriginalMetadataRequest : public ::omero::cmd::Request
{
public:

    typedef OriginalMetadataRequestPrx ProxyType;
    typedef OriginalMetadataRequestPtr PointerType;

    OriginalMetadataRequest()
    {
    }

    explicit OriginalMetadataRequest(::Ice::Long __ice_imageId) :
        imageId(__ice_imageId)
    {
    }

    virtual ::Ice::ObjectPtr ice_clone() const;

    virtual bool ice_isA(const ::std::string&, const ::Ice::Current& = ::Ice::Current()) const;
    virtual ::std::vector< ::std::string> ice_ids(const ::Ice::Current& = ::Ice::Current()) const;
    virtual const ::std::string& ice_id(const ::Ice::Current& = ::Ice::Current()) const;
    static const ::std::string& ice_staticId();


    static const ::Ice::ObjectFactoryPtr& ice_factory();

protected:
    virtual void __writeImpl(::IceInternal::BasicStream*) const;
    virtual void __readImpl(::IceInternal::BasicStream*);
    #ifdef __SUNPRO_CC
    using ::omero::cmd::Request::__writeImpl;
    using ::omero::cmd::Request::__readImpl;
    #endif

public:

    ::Ice::Long imageId;

protected:

    virtual ~OriginalMetadataRequest() {}

    friend class OriginalMetadataRequest__staticInit;
};

class OriginalMetadataRequest__staticInit
{
public:

    ::omero::cmd::OriginalMetadataRequest _init;
};

static OriginalMetadataRequest__staticInit _OriginalMetadataRequest_init;

inline bool operator==(const OriginalMetadataRequest& l, const OriginalMetadataRequest& r)
{
    return static_cast<const ::Ice::Object&>(l) == static_cast<const ::Ice::Object&>(r);
}

inline bool operator<(const OriginalMetadataRequest& l, const OriginalMetadataRequest& r)
{
    return static_cast<const ::Ice::Object&>(l) < static_cast<const ::Ice::Object&>(r);
}

class OriginalMetadataResponse : public ::omero::cmd::Response, public IceInternal::GCShared
{
public:

    typedef OriginalMetadataResponsePrx ProxyType;
    typedef OriginalMetadataResponsePtr PointerType;

    OriginalMetadataResponse()
    {
    }

    OriginalMetadataResponse(const ::omero::RLongPtr& __ice_filesetId, const ::omero::RLongPtr& __ice_fileAnnotationId, const ::omero::RTypeDict& __ice_globalMetadata, const ::omero::RTypeDict& __ice_seriesMetadata) :
        filesetId(__ice_filesetId),
        fileAnnotationId(__ice_fileAnnotationId),
        globalMetadata(__ice_globalMetadata),
        seriesMetadata(__ice_seriesMetadata)
    {
    }

    virtual ::Ice::ObjectPtr ice_clone() const;

    virtual bool ice_isA(const ::std::string&, const ::Ice::Current& = ::Ice::Current()) const;
    virtual ::std::vector< ::std::string> ice_ids(const ::Ice::Current& = ::Ice::Current()) const;
    virtual const ::std::string& ice_id(const ::Ice::Current& = ::Ice::Current()) const;
    static const ::std::string& ice_staticId();

    virtual void __addObject(::IceInternal::GCCountMap&);
    virtual bool __usesGC();
    virtual void __gcReachable(::IceInternal::GCCountMap&) const;
    virtual void __gcClear();

    static const ::Ice::ObjectFactoryPtr& ice_factory();

protected:
    virtual void __writeImpl(::IceInternal::BasicStream*) const;
    virtual void __readImpl(::IceInternal::BasicStream*);
    #ifdef __SUNPRO_CC
    using ::omero::cmd::Response::__writeImpl;
    using ::omero::cmd::Response::__readImpl;
    #endif

public:

    ::omero::RLongPtr filesetId;

    ::omero::RLongPtr fileAnnotationId;

    ::omero::RTypeDict globalMetadata;

    ::omero::RTypeDict seriesMetadata;

protected:

    virtual ~OriginalMetadataResponse() {}
};

inline bool operator==(const OriginalMetadataResponse& l, const OriginalMetadataResponse& r)
{
    return static_cast<const ::Ice::Object&>(l) == static_cast<const ::Ice::Object&>(r);
}

inline bool operator<(const OriginalMetadataResponse& l, const OriginalMetadataResponse& r)
{
    return static_cast<const ::Ice::Object&>(l) < static_cast<const ::Ice::Object&>(r);
}

}

}

namespace omero
{

namespace cmd
{

}

}

#endif
