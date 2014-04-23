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
// Generated from file `BooleanAnnotation.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

#ifndef __omero_model__opt_hudson_workspace_OMERO_5_0_release_src_components_blitz_generated_omero_model_BooleanAnnotation_h__
#define __omero_model__opt_hudson_workspace_OMERO_5_0_release_src_components_blitz_generated_omero_model_BooleanAnnotation_h__

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
#include <omero/model/IObject.h>
#include <omero/RTypes.h>
#include <omero/System.h>
#include <omero/Collections.h>
#include <omero/model/BasicAnnotation.h>
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

namespace model
{

class AnnotationAnnotationLink;
void __read(::IceInternal::BasicStream*, ::IceInternal::ProxyHandle< ::IceProxy::omero::model::AnnotationAnnotationLink>&);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::AnnotationAnnotationLink*);

class Annotation;
void __read(::IceInternal::BasicStream*, ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Annotation>&);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::Annotation*);

class Details;
void __read(::IceInternal::BasicStream*, ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Details>&);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::Details*);

class BooleanAnnotation;
void __read(::IceInternal::BasicStream*, ::IceInternal::ProxyHandle< ::IceProxy::omero::model::BooleanAnnotation>&);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::BooleanAnnotation*);

}

}

}

namespace omero
{

namespace model
{

class AnnotationAnnotationLink;
bool operator==(const AnnotationAnnotationLink&, const AnnotationAnnotationLink&);
bool operator<(const AnnotationAnnotationLink&, const AnnotationAnnotationLink&);
::Ice::Object* upCast(::omero::model::AnnotationAnnotationLink*);
typedef ::IceInternal::Handle< ::omero::model::AnnotationAnnotationLink> AnnotationAnnotationLinkPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::AnnotationAnnotationLink> AnnotationAnnotationLinkPrx;
void __patch(AnnotationAnnotationLinkPtr&, const ::Ice::ObjectPtr&);

class Annotation;
bool operator==(const Annotation&, const Annotation&);
bool operator<(const Annotation&, const Annotation&);
::Ice::Object* upCast(::omero::model::Annotation*);
typedef ::IceInternal::Handle< ::omero::model::Annotation> AnnotationPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Annotation> AnnotationPrx;
void __patch(AnnotationPtr&, const ::Ice::ObjectPtr&);

class Details;
bool operator==(const Details&, const Details&);
bool operator<(const Details&, const Details&);
::Ice::Object* upCast(::omero::model::Details*);
typedef ::IceInternal::Handle< ::omero::model::Details> DetailsPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Details> DetailsPrx;
void __patch(DetailsPtr&, const ::Ice::ObjectPtr&);

class BooleanAnnotation;
bool operator==(const BooleanAnnotation&, const BooleanAnnotation&);
bool operator<(const BooleanAnnotation&, const BooleanAnnotation&);
::Ice::Object* upCast(::omero::model::BooleanAnnotation*);
typedef ::IceInternal::Handle< ::omero::model::BooleanAnnotation> BooleanAnnotationPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::BooleanAnnotation> BooleanAnnotationPrx;
void __patch(BooleanAnnotationPtr&, const ::Ice::ObjectPtr&);

}

}

namespace omero
{

namespace model
{

class Callback_BooleanAnnotation_getBoolValue_Base : virtual public ::IceInternal::CallbackBase { };
typedef ::IceUtil::Handle< Callback_BooleanAnnotation_getBoolValue_Base> Callback_BooleanAnnotation_getBoolValuePtr;

class Callback_BooleanAnnotation_setBoolValue_Base : virtual public ::IceInternal::CallbackBase { };
typedef ::IceUtil::Handle< Callback_BooleanAnnotation_setBoolValue_Base> Callback_BooleanAnnotation_setBoolValuePtr;

}

}

namespace IceProxy
{

namespace omero
{

namespace model
{

class BooleanAnnotation : virtual public ::IceProxy::omero::model::BasicAnnotation
{
public:

    ::omero::RBoolPtr getBoolValue()
    {
        return getBoolValue(0);
    }
    ::omero::RBoolPtr getBoolValue(const ::Ice::Context& __ctx)
    {
        return getBoolValue(&__ctx);
    }
#ifdef ICE_CPP11
    ::Ice::AsyncResultPtr
    begin_getBoolValue(const ::IceInternal::Function<void (const ::omero::RBoolPtr&)>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception = ::IceInternal::Function<void (const ::Ice::Exception&)>(), const ::IceInternal::Function<void (bool)>& __sent = ::IceInternal::Function<void (bool)>())
    {
        return __begin_getBoolValue(0, __response, __exception, __sent);
    }
    ::Ice::AsyncResultPtr
    begin_getBoolValue(const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __completed, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __sent = ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>())
    {
        return begin_getBoolValue(0, ::Ice::newCallback(__completed, __sent), 0);
    }
    ::Ice::AsyncResultPtr
    begin_getBoolValue(const ::Ice::Context& __ctx, const ::IceInternal::Function<void (const ::omero::RBoolPtr&)>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception = ::IceInternal::Function<void (const ::Ice::Exception&)>(), const ::IceInternal::Function<void (bool)>& __sent = ::IceInternal::Function<void (bool)>())
    {
        return __begin_getBoolValue(&__ctx, __response, __exception, __sent);
    }
    ::Ice::AsyncResultPtr
    begin_getBoolValue(const ::Ice::Context& __ctx, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __completed, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __sent = ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>())
    {
        return begin_getBoolValue(&__ctx, ::Ice::newCallback(__completed, __sent));
    }
    
private:

    ::Ice::AsyncResultPtr __begin_getBoolValue(const ::Ice::Context* __ctx, const ::IceInternal::Function<void (const ::omero::RBoolPtr&)>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception, const ::IceInternal::Function<void (bool)>& __sent)
    {
        class Cpp11CB : public ::IceInternal::Cpp11FnCallbackNC
        {
        public:

            Cpp11CB(const ::std::function<void (const ::omero::RBoolPtr&)>& responseFunc, const ::std::function<void (const ::Ice::Exception&)>& exceptionFunc, const ::std::function<void (bool)>& sentFunc) :
                ::IceInternal::Cpp11FnCallbackNC(exceptionFunc, sentFunc),
                _response(responseFunc)
            {
                CallbackBase::checkCallback(true, responseFunc || exceptionFunc != nullptr);
            }

            virtual void __completed(const ::Ice::AsyncResultPtr& __result) const
            {
                ::omero::model::BooleanAnnotationPrx __proxy = ::omero::model::BooleanAnnotationPrx::uncheckedCast(__result->getProxy());
                ::omero::RBoolPtr __ret;
                try
                {
                    __ret = __proxy->end_getBoolValue(__result);
                }
                catch(::Ice::Exception& ex)
                {
                    Cpp11FnCallbackNC::__exception(__result, ex);
                    return;
                }
                if(_response != nullptr)
                {
                    _response(__ret);
                }
            }
        
        private:
            
            ::std::function<void (const ::omero::RBoolPtr&)> _response;
        };
        return begin_getBoolValue(__ctx, new Cpp11CB(__response, __exception, __sent));
    }
    
public:
#endif

    ::Ice::AsyncResultPtr begin_getBoolValue()
    {
        return begin_getBoolValue(0, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_getBoolValue(const ::Ice::Context& __ctx)
    {
        return begin_getBoolValue(&__ctx, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_getBoolValue(const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getBoolValue(0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_getBoolValue(const ::Ice::Context& __ctx, const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getBoolValue(&__ctx, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_getBoolValue(const ::omero::model::Callback_BooleanAnnotation_getBoolValuePtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getBoolValue(0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_getBoolValue(const ::Ice::Context& __ctx, const ::omero::model::Callback_BooleanAnnotation_getBoolValuePtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getBoolValue(&__ctx, __del, __cookie);
    }

    ::omero::RBoolPtr end_getBoolValue(const ::Ice::AsyncResultPtr&);
    
private:

    ::omero::RBoolPtr getBoolValue(const ::Ice::Context*);
    ::Ice::AsyncResultPtr begin_getBoolValue(const ::Ice::Context*, const ::IceInternal::CallbackBasePtr&, const ::Ice::LocalObjectPtr& __cookie = 0);
    
public:

    void setBoolValue(const ::omero::RBoolPtr& theBoolValue)
    {
        setBoolValue(theBoolValue, 0);
    }
    void setBoolValue(const ::omero::RBoolPtr& theBoolValue, const ::Ice::Context& __ctx)
    {
        setBoolValue(theBoolValue, &__ctx);
    }
#ifdef ICE_CPP11
    ::Ice::AsyncResultPtr
    begin_setBoolValue(const ::omero::RBoolPtr& theBoolValue, const ::IceInternal::Function<void ()>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception = ::IceInternal::Function<void (const ::Ice::Exception&)>(), const ::IceInternal::Function<void (bool)>& __sent = ::IceInternal::Function<void (bool)>())
    {
        return begin_setBoolValue(theBoolValue, 0, new ::IceInternal::Cpp11FnOnewayCallbackNC(__response, __exception, __sent));
    }
    ::Ice::AsyncResultPtr
    begin_setBoolValue(const ::omero::RBoolPtr& theBoolValue, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __completed, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __sent = ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>())
    {
        return begin_setBoolValue(theBoolValue, 0, ::Ice::newCallback(__completed, __sent), 0);
    }
    ::Ice::AsyncResultPtr
    begin_setBoolValue(const ::omero::RBoolPtr& theBoolValue, const ::Ice::Context& __ctx, const ::IceInternal::Function<void ()>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception = ::IceInternal::Function<void (const ::Ice::Exception&)>(), const ::IceInternal::Function<void (bool)>& __sent = ::IceInternal::Function<void (bool)>())
    {
        return begin_setBoolValue(theBoolValue, &__ctx, new ::IceInternal::Cpp11FnOnewayCallbackNC(__response, __exception, __sent), 0);
    }
    ::Ice::AsyncResultPtr
    begin_setBoolValue(const ::omero::RBoolPtr& theBoolValue, const ::Ice::Context& __ctx, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __completed, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __sent = ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>())
    {
        return begin_setBoolValue(theBoolValue, &__ctx, ::Ice::newCallback(__completed, __sent));
    }
#endif

    ::Ice::AsyncResultPtr begin_setBoolValue(const ::omero::RBoolPtr& theBoolValue)
    {
        return begin_setBoolValue(theBoolValue, 0, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_setBoolValue(const ::omero::RBoolPtr& theBoolValue, const ::Ice::Context& __ctx)
    {
        return begin_setBoolValue(theBoolValue, &__ctx, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_setBoolValue(const ::omero::RBoolPtr& theBoolValue, const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setBoolValue(theBoolValue, 0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_setBoolValue(const ::omero::RBoolPtr& theBoolValue, const ::Ice::Context& __ctx, const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setBoolValue(theBoolValue, &__ctx, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_setBoolValue(const ::omero::RBoolPtr& theBoolValue, const ::omero::model::Callback_BooleanAnnotation_setBoolValuePtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setBoolValue(theBoolValue, 0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_setBoolValue(const ::omero::RBoolPtr& theBoolValue, const ::Ice::Context& __ctx, const ::omero::model::Callback_BooleanAnnotation_setBoolValuePtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setBoolValue(theBoolValue, &__ctx, __del, __cookie);
    }

    void end_setBoolValue(const ::Ice::AsyncResultPtr&);
    
private:

    void setBoolValue(const ::omero::RBoolPtr&, const ::Ice::Context*);
    ::Ice::AsyncResultPtr begin_setBoolValue(const ::omero::RBoolPtr&, const ::Ice::Context*, const ::IceInternal::CallbackBasePtr&, const ::Ice::LocalObjectPtr& __cookie = 0);
    
public:
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_context(const ::Ice::Context& __context) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_context(__context).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_adapterId(const ::std::string& __id) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_adapterId(__id).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_endpoints(const ::Ice::EndpointSeq& __endpoints) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_endpoints(__endpoints).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_locatorCacheTimeout(int __timeout) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_locatorCacheTimeout(__timeout).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_connectionCached(bool __cached) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_connectionCached(__cached).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_endpointSelection(::Ice::EndpointSelectionType __est) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_endpointSelection(__est).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_secure(bool __secure) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_secure(__secure).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_preferSecure(bool __preferSecure) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_preferSecure(__preferSecure).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_router(const ::Ice::RouterPrx& __router) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_router(__router).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_locator(const ::Ice::LocatorPrx& __locator) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_locator(__locator).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_collocationOptimized(bool __co) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_collocationOptimized(__co).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_twoway() const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_twoway().get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_oneway() const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_oneway().get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_batchOneway() const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_batchOneway().get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_datagram() const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_datagram().get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_batchDatagram() const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_batchDatagram().get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_compress(bool __compress) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_compress(__compress).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_timeout(int __timeout) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_timeout(__timeout).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_connectionId(const ::std::string& __id) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_connectionId(__id).get());
    }
    
    ::IceInternal::ProxyHandle<BooleanAnnotation> ice_encodingVersion(const ::Ice::EncodingVersion& __v) const
    {
        return dynamic_cast<BooleanAnnotation*>(::IceProxy::Ice::Object::ice_encodingVersion(__v).get());
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

namespace model
{

class BooleanAnnotation : virtual public ::IceDelegate::omero::model::BasicAnnotation
{
public:

    virtual ::omero::RBoolPtr getBoolValue(const ::Ice::Context*, ::IceInternal::InvocationObserver&) = 0;

    virtual void setBoolValue(const ::omero::RBoolPtr&, const ::Ice::Context*, ::IceInternal::InvocationObserver&) = 0;
};

}

}

}

namespace IceDelegateM
{

namespace omero
{

namespace model
{

class BooleanAnnotation : virtual public ::IceDelegate::omero::model::BooleanAnnotation,
                          virtual public ::IceDelegateM::omero::model::BasicAnnotation
{
public:

    virtual ::omero::RBoolPtr getBoolValue(const ::Ice::Context*, ::IceInternal::InvocationObserver&);

    virtual void setBoolValue(const ::omero::RBoolPtr&, const ::Ice::Context*, ::IceInternal::InvocationObserver&);
};

}

}

}

namespace IceDelegateD
{

namespace omero
{

namespace model
{

class BooleanAnnotation : virtual public ::IceDelegate::omero::model::BooleanAnnotation,
                          virtual public ::IceDelegateD::omero::model::BasicAnnotation
{
public:

    virtual ::omero::RBoolPtr getBoolValue(const ::Ice::Context*, ::IceInternal::InvocationObserver&);

    virtual void setBoolValue(const ::omero::RBoolPtr&, const ::Ice::Context*, ::IceInternal::InvocationObserver&);
};

}

}

}

namespace omero
{

namespace model
{

class BooleanAnnotation : public ::omero::model::BasicAnnotation
{
public:

    typedef BooleanAnnotationPrx ProxyType;
    typedef BooleanAnnotationPtr PointerType;

    BooleanAnnotation()
    {
    }

    BooleanAnnotation(const ::omero::RLongPtr& __ice_id, const ::omero::model::DetailsPtr& __ice_details, bool __ice_loaded, const ::omero::RIntPtr& __ice_version, const ::omero::RStringPtr& __ice_ns, const ::omero::RStringPtr& __ice_description, const ::omero::model::AnnotationAnnotationLinksSeq& __ice_annotationLinksSeq, bool __ice_annotationLinksLoaded, const ::omero::sys::CountMap& __ice_annotationLinksCountPerOwner, const ::omero::RBoolPtr& __ice_boolValue) :
        ::omero::model::BasicAnnotation(__ice_id, __ice_details, __ice_loaded, __ice_version, __ice_ns, __ice_description, __ice_annotationLinksSeq, __ice_annotationLinksLoaded, __ice_annotationLinksCountPerOwner)
        ,
        boolValue(__ice_boolValue)
    {
    }

    virtual ::Ice::ObjectPtr ice_clone() const;

    virtual bool ice_isA(const ::std::string&, const ::Ice::Current& = ::Ice::Current()) const;
    virtual ::std::vector< ::std::string> ice_ids(const ::Ice::Current& = ::Ice::Current()) const;
    virtual const ::std::string& ice_id(const ::Ice::Current& = ::Ice::Current()) const;
    static const ::std::string& ice_staticId();

    virtual void __gcReachable(::IceInternal::GCCountMap&) const;
    virtual void __gcClear();

    virtual ::omero::RBoolPtr getBoolValue(const ::Ice::Current& = ::Ice::Current()) = 0;
    ::Ice::DispatchStatus ___getBoolValue(::IceInternal::Incoming&, const ::Ice::Current&);

    virtual void setBoolValue(const ::omero::RBoolPtr&, const ::Ice::Current& = ::Ice::Current()) = 0;
    ::Ice::DispatchStatus ___setBoolValue(::IceInternal::Incoming&, const ::Ice::Current&);

    virtual ::Ice::DispatchStatus __dispatch(::IceInternal::Incoming&, const ::Ice::Current&);

protected:
    virtual void __writeImpl(::IceInternal::BasicStream*) const;
    virtual void __readImpl(::IceInternal::BasicStream*);
    #ifdef __SUNPRO_CC
    using ::omero::model::BasicAnnotation::__writeImpl;
    using ::omero::model::BasicAnnotation::__readImpl;
    #endif

    ::omero::RBoolPtr boolValue;
};

inline bool operator==(const BooleanAnnotation& l, const BooleanAnnotation& r)
{
    return static_cast<const ::Ice::Object&>(l) == static_cast<const ::Ice::Object&>(r);
}

inline bool operator<(const BooleanAnnotation& l, const BooleanAnnotation& r)
{
    return static_cast<const ::Ice::Object&>(l) < static_cast<const ::Ice::Object&>(r);
}

}

}

namespace omero
{

namespace model
{

template<class T>
class CallbackNC_BooleanAnnotation_getBoolValue : public Callback_BooleanAnnotation_getBoolValue_Base, public ::IceInternal::TwowayCallbackNC<T>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception&);
    typedef void (T::*Sent)(bool);
    typedef void (T::*Response)(const ::omero::RBoolPtr&);

    CallbackNC_BooleanAnnotation_getBoolValue(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::TwowayCallbackNC<T>(obj, cb != 0, excb, sentcb), response(cb)
    {
    }

    virtual void __completed(const ::Ice::AsyncResultPtr& __result) const
    {
        ::omero::model::BooleanAnnotationPrx __proxy = ::omero::model::BooleanAnnotationPrx::uncheckedCast(__result->getProxy());
        ::omero::RBoolPtr __ret;
        try
        {
            __ret = __proxy->end_getBoolValue(__result);
        }
        catch(::Ice::Exception& ex)
        {
            ::IceInternal::CallbackNC<T>::__exception(__result, ex);
            return;
        }
        if(response)
        {
            (::IceInternal::CallbackNC<T>::callback.get()->*response)(__ret);
        }
    }

    Response response;
};

template<class T> Callback_BooleanAnnotation_getBoolValuePtr
newCallback_BooleanAnnotation_getBoolValue(const IceUtil::Handle<T>& instance, void (T::*cb)(const ::omero::RBoolPtr&), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_BooleanAnnotation_getBoolValue<T>(instance, cb, excb, sentcb);
}

template<class T> Callback_BooleanAnnotation_getBoolValuePtr
newCallback_BooleanAnnotation_getBoolValue(T* instance, void (T::*cb)(const ::omero::RBoolPtr&), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_BooleanAnnotation_getBoolValue<T>(instance, cb, excb, sentcb);
}

template<class T, typename CT>
class Callback_BooleanAnnotation_getBoolValue : public Callback_BooleanAnnotation_getBoolValue_Base, public ::IceInternal::TwowayCallback<T, CT>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception& , const CT&);
    typedef void (T::*Sent)(bool , const CT&);
    typedef void (T::*Response)(const ::omero::RBoolPtr&, const CT&);

    Callback_BooleanAnnotation_getBoolValue(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::TwowayCallback<T, CT>(obj, cb != 0, excb, sentcb), response(cb)
    {
    }

    virtual void __completed(const ::Ice::AsyncResultPtr& __result) const
    {
        ::omero::model::BooleanAnnotationPrx __proxy = ::omero::model::BooleanAnnotationPrx::uncheckedCast(__result->getProxy());
        ::omero::RBoolPtr __ret;
        try
        {
            __ret = __proxy->end_getBoolValue(__result);
        }
        catch(::Ice::Exception& ex)
        {
            ::IceInternal::Callback<T, CT>::__exception(__result, ex);
            return;
        }
        if(response)
        {
            (::IceInternal::Callback<T, CT>::callback.get()->*response)(__ret, CT::dynamicCast(__result->getCookie()));
        }
    }

    Response response;
};

template<class T, typename CT> Callback_BooleanAnnotation_getBoolValuePtr
newCallback_BooleanAnnotation_getBoolValue(const IceUtil::Handle<T>& instance, void (T::*cb)(const ::omero::RBoolPtr&, const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_BooleanAnnotation_getBoolValue<T, CT>(instance, cb, excb, sentcb);
}

template<class T, typename CT> Callback_BooleanAnnotation_getBoolValuePtr
newCallback_BooleanAnnotation_getBoolValue(T* instance, void (T::*cb)(const ::omero::RBoolPtr&, const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_BooleanAnnotation_getBoolValue<T, CT>(instance, cb, excb, sentcb);
}

template<class T>
class CallbackNC_BooleanAnnotation_setBoolValue : public Callback_BooleanAnnotation_setBoolValue_Base, public ::IceInternal::OnewayCallbackNC<T>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception&);
    typedef void (T::*Sent)(bool);
    typedef void (T::*Response)();

    CallbackNC_BooleanAnnotation_setBoolValue(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::OnewayCallbackNC<T>(obj, cb, excb, sentcb)
    {
    }
};

template<class T> Callback_BooleanAnnotation_setBoolValuePtr
newCallback_BooleanAnnotation_setBoolValue(const IceUtil::Handle<T>& instance, void (T::*cb)(), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_BooleanAnnotation_setBoolValue<T>(instance, cb, excb, sentcb);
}

template<class T> Callback_BooleanAnnotation_setBoolValuePtr
newCallback_BooleanAnnotation_setBoolValue(const IceUtil::Handle<T>& instance, void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_BooleanAnnotation_setBoolValue<T>(instance, 0, excb, sentcb);
}

template<class T> Callback_BooleanAnnotation_setBoolValuePtr
newCallback_BooleanAnnotation_setBoolValue(T* instance, void (T::*cb)(), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_BooleanAnnotation_setBoolValue<T>(instance, cb, excb, sentcb);
}

template<class T> Callback_BooleanAnnotation_setBoolValuePtr
newCallback_BooleanAnnotation_setBoolValue(T* instance, void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_BooleanAnnotation_setBoolValue<T>(instance, 0, excb, sentcb);
}

template<class T, typename CT>
class Callback_BooleanAnnotation_setBoolValue : public Callback_BooleanAnnotation_setBoolValue_Base, public ::IceInternal::OnewayCallback<T, CT>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception& , const CT&);
    typedef void (T::*Sent)(bool , const CT&);
    typedef void (T::*Response)(const CT&);

    Callback_BooleanAnnotation_setBoolValue(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::OnewayCallback<T, CT>(obj, cb, excb, sentcb)
    {
    }
};

template<class T, typename CT> Callback_BooleanAnnotation_setBoolValuePtr
newCallback_BooleanAnnotation_setBoolValue(const IceUtil::Handle<T>& instance, void (T::*cb)(const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_BooleanAnnotation_setBoolValue<T, CT>(instance, cb, excb, sentcb);
}

template<class T, typename CT> Callback_BooleanAnnotation_setBoolValuePtr
newCallback_BooleanAnnotation_setBoolValue(const IceUtil::Handle<T>& instance, void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_BooleanAnnotation_setBoolValue<T, CT>(instance, 0, excb, sentcb);
}

template<class T, typename CT> Callback_BooleanAnnotation_setBoolValuePtr
newCallback_BooleanAnnotation_setBoolValue(T* instance, void (T::*cb)(const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_BooleanAnnotation_setBoolValue<T, CT>(instance, cb, excb, sentcb);
}

template<class T, typename CT> Callback_BooleanAnnotation_setBoolValuePtr
newCallback_BooleanAnnotation_setBoolValue(T* instance, void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_BooleanAnnotation_setBoolValue<T, CT>(instance, 0, excb, sentcb);
}

}

}

#endif
