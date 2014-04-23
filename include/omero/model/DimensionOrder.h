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
// Generated from file `DimensionOrder.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

#ifndef __omero_model__opt_hudson_workspace_OMERO_5_0_release_src_components_blitz_generated_omero_model_DimensionOrder_h__
#define __omero_model__opt_hudson_workspace_OMERO_5_0_release_src_components_blitz_generated_omero_model_DimensionOrder_h__

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

class Details;
void __read(::IceInternal::BasicStream*, ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Details>&);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::Details*);

class DimensionOrder;
void __read(::IceInternal::BasicStream*, ::IceInternal::ProxyHandle< ::IceProxy::omero::model::DimensionOrder>&);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::DimensionOrder*);

}

}

}

namespace omero
{

namespace model
{

class Details;
bool operator==(const Details&, const Details&);
bool operator<(const Details&, const Details&);
::Ice::Object* upCast(::omero::model::Details*);
typedef ::IceInternal::Handle< ::omero::model::Details> DetailsPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Details> DetailsPrx;
void __patch(DetailsPtr&, const ::Ice::ObjectPtr&);

class DimensionOrder;
bool operator==(const DimensionOrder&, const DimensionOrder&);
bool operator<(const DimensionOrder&, const DimensionOrder&);
::Ice::Object* upCast(::omero::model::DimensionOrder*);
typedef ::IceInternal::Handle< ::omero::model::DimensionOrder> DimensionOrderPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::DimensionOrder> DimensionOrderPrx;
void __patch(DimensionOrderPtr&, const ::Ice::ObjectPtr&);

}

}

namespace omero
{

namespace model
{

namespace enums
{

const ::std::string DimensionOrderXYZCT = "XYZCT";

const ::std::string DimensionOrderXYZTC = "XYZTC";

const ::std::string DimensionOrderXYCTZ = "XYCTZ";

const ::std::string DimensionOrderXYCZT = "XYCZT";

const ::std::string DimensionOrderXYTCZ = "XYTCZ";

const ::std::string DimensionOrderXYTZC = "XYTZC";

}

}

}

namespace omero
{

namespace model
{

class Callback_DimensionOrder_getValue_Base : virtual public ::IceInternal::CallbackBase { };
typedef ::IceUtil::Handle< Callback_DimensionOrder_getValue_Base> Callback_DimensionOrder_getValuePtr;

class Callback_DimensionOrder_setValue_Base : virtual public ::IceInternal::CallbackBase { };
typedef ::IceUtil::Handle< Callback_DimensionOrder_setValue_Base> Callback_DimensionOrder_setValuePtr;

}

}

namespace IceProxy
{

namespace omero
{

namespace model
{

class DimensionOrder : virtual public ::IceProxy::omero::model::IObject
{
public:

    ::omero::RStringPtr getValue()
    {
        return getValue(0);
    }
    ::omero::RStringPtr getValue(const ::Ice::Context& __ctx)
    {
        return getValue(&__ctx);
    }
#ifdef ICE_CPP11
    ::Ice::AsyncResultPtr
    begin_getValue(const ::IceInternal::Function<void (const ::omero::RStringPtr&)>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception = ::IceInternal::Function<void (const ::Ice::Exception&)>(), const ::IceInternal::Function<void (bool)>& __sent = ::IceInternal::Function<void (bool)>())
    {
        return __begin_getValue(0, __response, __exception, __sent);
    }
    ::Ice::AsyncResultPtr
    begin_getValue(const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __completed, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __sent = ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>())
    {
        return begin_getValue(0, ::Ice::newCallback(__completed, __sent), 0);
    }
    ::Ice::AsyncResultPtr
    begin_getValue(const ::Ice::Context& __ctx, const ::IceInternal::Function<void (const ::omero::RStringPtr&)>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception = ::IceInternal::Function<void (const ::Ice::Exception&)>(), const ::IceInternal::Function<void (bool)>& __sent = ::IceInternal::Function<void (bool)>())
    {
        return __begin_getValue(&__ctx, __response, __exception, __sent);
    }
    ::Ice::AsyncResultPtr
    begin_getValue(const ::Ice::Context& __ctx, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __completed, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __sent = ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>())
    {
        return begin_getValue(&__ctx, ::Ice::newCallback(__completed, __sent));
    }
    
private:

    ::Ice::AsyncResultPtr __begin_getValue(const ::Ice::Context* __ctx, const ::IceInternal::Function<void (const ::omero::RStringPtr&)>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception, const ::IceInternal::Function<void (bool)>& __sent)
    {
        class Cpp11CB : public ::IceInternal::Cpp11FnCallbackNC
        {
        public:

            Cpp11CB(const ::std::function<void (const ::omero::RStringPtr&)>& responseFunc, const ::std::function<void (const ::Ice::Exception&)>& exceptionFunc, const ::std::function<void (bool)>& sentFunc) :
                ::IceInternal::Cpp11FnCallbackNC(exceptionFunc, sentFunc),
                _response(responseFunc)
            {
                CallbackBase::checkCallback(true, responseFunc || exceptionFunc != nullptr);
            }

            virtual void __completed(const ::Ice::AsyncResultPtr& __result) const
            {
                ::omero::model::DimensionOrderPrx __proxy = ::omero::model::DimensionOrderPrx::uncheckedCast(__result->getProxy());
                ::omero::RStringPtr __ret;
                try
                {
                    __ret = __proxy->end_getValue(__result);
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
            
            ::std::function<void (const ::omero::RStringPtr&)> _response;
        };
        return begin_getValue(__ctx, new Cpp11CB(__response, __exception, __sent));
    }
    
public:
#endif

    ::Ice::AsyncResultPtr begin_getValue()
    {
        return begin_getValue(0, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_getValue(const ::Ice::Context& __ctx)
    {
        return begin_getValue(&__ctx, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_getValue(const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getValue(0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_getValue(const ::Ice::Context& __ctx, const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getValue(&__ctx, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_getValue(const ::omero::model::Callback_DimensionOrder_getValuePtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getValue(0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_getValue(const ::Ice::Context& __ctx, const ::omero::model::Callback_DimensionOrder_getValuePtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getValue(&__ctx, __del, __cookie);
    }

    ::omero::RStringPtr end_getValue(const ::Ice::AsyncResultPtr&);
    
private:

    ::omero::RStringPtr getValue(const ::Ice::Context*);
    ::Ice::AsyncResultPtr begin_getValue(const ::Ice::Context*, const ::IceInternal::CallbackBasePtr&, const ::Ice::LocalObjectPtr& __cookie = 0);
    
public:

    void setValue(const ::omero::RStringPtr& theValue)
    {
        setValue(theValue, 0);
    }
    void setValue(const ::omero::RStringPtr& theValue, const ::Ice::Context& __ctx)
    {
        setValue(theValue, &__ctx);
    }
#ifdef ICE_CPP11
    ::Ice::AsyncResultPtr
    begin_setValue(const ::omero::RStringPtr& theValue, const ::IceInternal::Function<void ()>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception = ::IceInternal::Function<void (const ::Ice::Exception&)>(), const ::IceInternal::Function<void (bool)>& __sent = ::IceInternal::Function<void (bool)>())
    {
        return begin_setValue(theValue, 0, new ::IceInternal::Cpp11FnOnewayCallbackNC(__response, __exception, __sent));
    }
    ::Ice::AsyncResultPtr
    begin_setValue(const ::omero::RStringPtr& theValue, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __completed, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __sent = ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>())
    {
        return begin_setValue(theValue, 0, ::Ice::newCallback(__completed, __sent), 0);
    }
    ::Ice::AsyncResultPtr
    begin_setValue(const ::omero::RStringPtr& theValue, const ::Ice::Context& __ctx, const ::IceInternal::Function<void ()>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception = ::IceInternal::Function<void (const ::Ice::Exception&)>(), const ::IceInternal::Function<void (bool)>& __sent = ::IceInternal::Function<void (bool)>())
    {
        return begin_setValue(theValue, &__ctx, new ::IceInternal::Cpp11FnOnewayCallbackNC(__response, __exception, __sent), 0);
    }
    ::Ice::AsyncResultPtr
    begin_setValue(const ::omero::RStringPtr& theValue, const ::Ice::Context& __ctx, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __completed, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __sent = ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>())
    {
        return begin_setValue(theValue, &__ctx, ::Ice::newCallback(__completed, __sent));
    }
#endif

    ::Ice::AsyncResultPtr begin_setValue(const ::omero::RStringPtr& theValue)
    {
        return begin_setValue(theValue, 0, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_setValue(const ::omero::RStringPtr& theValue, const ::Ice::Context& __ctx)
    {
        return begin_setValue(theValue, &__ctx, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_setValue(const ::omero::RStringPtr& theValue, const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setValue(theValue, 0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_setValue(const ::omero::RStringPtr& theValue, const ::Ice::Context& __ctx, const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setValue(theValue, &__ctx, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_setValue(const ::omero::RStringPtr& theValue, const ::omero::model::Callback_DimensionOrder_setValuePtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setValue(theValue, 0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_setValue(const ::omero::RStringPtr& theValue, const ::Ice::Context& __ctx, const ::omero::model::Callback_DimensionOrder_setValuePtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setValue(theValue, &__ctx, __del, __cookie);
    }

    void end_setValue(const ::Ice::AsyncResultPtr&);
    
private:

    void setValue(const ::omero::RStringPtr&, const ::Ice::Context*);
    ::Ice::AsyncResultPtr begin_setValue(const ::omero::RStringPtr&, const ::Ice::Context*, const ::IceInternal::CallbackBasePtr&, const ::Ice::LocalObjectPtr& __cookie = 0);
    
public:
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_context(const ::Ice::Context& __context) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_context(__context).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_adapterId(const ::std::string& __id) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_adapterId(__id).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_endpoints(const ::Ice::EndpointSeq& __endpoints) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_endpoints(__endpoints).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_locatorCacheTimeout(int __timeout) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_locatorCacheTimeout(__timeout).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_connectionCached(bool __cached) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_connectionCached(__cached).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_endpointSelection(::Ice::EndpointSelectionType __est) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_endpointSelection(__est).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_secure(bool __secure) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_secure(__secure).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_preferSecure(bool __preferSecure) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_preferSecure(__preferSecure).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_router(const ::Ice::RouterPrx& __router) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_router(__router).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_locator(const ::Ice::LocatorPrx& __locator) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_locator(__locator).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_collocationOptimized(bool __co) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_collocationOptimized(__co).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_twoway() const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_twoway().get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_oneway() const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_oneway().get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_batchOneway() const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_batchOneway().get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_datagram() const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_datagram().get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_batchDatagram() const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_batchDatagram().get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_compress(bool __compress) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_compress(__compress).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_timeout(int __timeout) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_timeout(__timeout).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_connectionId(const ::std::string& __id) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_connectionId(__id).get());
    }
    
    ::IceInternal::ProxyHandle<DimensionOrder> ice_encodingVersion(const ::Ice::EncodingVersion& __v) const
    {
        return dynamic_cast<DimensionOrder*>(::IceProxy::Ice::Object::ice_encodingVersion(__v).get());
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

class DimensionOrder : virtual public ::IceDelegate::omero::model::IObject
{
public:

    virtual ::omero::RStringPtr getValue(const ::Ice::Context*, ::IceInternal::InvocationObserver&) = 0;

    virtual void setValue(const ::omero::RStringPtr&, const ::Ice::Context*, ::IceInternal::InvocationObserver&) = 0;
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

class DimensionOrder : virtual public ::IceDelegate::omero::model::DimensionOrder,
                       virtual public ::IceDelegateM::omero::model::IObject
{
public:

    virtual ::omero::RStringPtr getValue(const ::Ice::Context*, ::IceInternal::InvocationObserver&);

    virtual void setValue(const ::omero::RStringPtr&, const ::Ice::Context*, ::IceInternal::InvocationObserver&);
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

class DimensionOrder : virtual public ::IceDelegate::omero::model::DimensionOrder,
                       virtual public ::IceDelegateD::omero::model::IObject
{
public:

    virtual ::omero::RStringPtr getValue(const ::Ice::Context*, ::IceInternal::InvocationObserver&);

    virtual void setValue(const ::omero::RStringPtr&, const ::Ice::Context*, ::IceInternal::InvocationObserver&);
};

}

}

}

namespace omero
{

namespace model
{

class DimensionOrder : public ::omero::model::IObject
{
public:

    typedef DimensionOrderPrx ProxyType;
    typedef DimensionOrderPtr PointerType;

    DimensionOrder()
    {
    }

    DimensionOrder(const ::omero::RLongPtr& __ice_id, const ::omero::model::DetailsPtr& __ice_details, bool __ice_loaded, const ::omero::RStringPtr& __ice_value) :
        ::omero::model::IObject(__ice_id, __ice_details, __ice_loaded)
        ,
        value(__ice_value)
    {
    }

    virtual ::Ice::ObjectPtr ice_clone() const;

    virtual bool ice_isA(const ::std::string&, const ::Ice::Current& = ::Ice::Current()) const;
    virtual ::std::vector< ::std::string> ice_ids(const ::Ice::Current& = ::Ice::Current()) const;
    virtual const ::std::string& ice_id(const ::Ice::Current& = ::Ice::Current()) const;
    static const ::std::string& ice_staticId();

    virtual void __gcReachable(::IceInternal::GCCountMap&) const;
    virtual void __gcClear();

    virtual ::omero::RStringPtr getValue(const ::Ice::Current& = ::Ice::Current()) = 0;
    ::Ice::DispatchStatus ___getValue(::IceInternal::Incoming&, const ::Ice::Current&);

    virtual void setValue(const ::omero::RStringPtr&, const ::Ice::Current& = ::Ice::Current()) = 0;
    ::Ice::DispatchStatus ___setValue(::IceInternal::Incoming&, const ::Ice::Current&);

    virtual ::Ice::DispatchStatus __dispatch(::IceInternal::Incoming&, const ::Ice::Current&);

protected:
    virtual void __writeImpl(::IceInternal::BasicStream*) const;
    virtual void __readImpl(::IceInternal::BasicStream*);
    #ifdef __SUNPRO_CC
    using ::omero::model::IObject::__writeImpl;
    using ::omero::model::IObject::__readImpl;
    #endif

    ::omero::RStringPtr value;
};

inline bool operator==(const DimensionOrder& l, const DimensionOrder& r)
{
    return static_cast<const ::Ice::Object&>(l) == static_cast<const ::Ice::Object&>(r);
}

inline bool operator<(const DimensionOrder& l, const DimensionOrder& r)
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
class CallbackNC_DimensionOrder_getValue : public Callback_DimensionOrder_getValue_Base, public ::IceInternal::TwowayCallbackNC<T>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception&);
    typedef void (T::*Sent)(bool);
    typedef void (T::*Response)(const ::omero::RStringPtr&);

    CallbackNC_DimensionOrder_getValue(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::TwowayCallbackNC<T>(obj, cb != 0, excb, sentcb), response(cb)
    {
    }

    virtual void __completed(const ::Ice::AsyncResultPtr& __result) const
    {
        ::omero::model::DimensionOrderPrx __proxy = ::omero::model::DimensionOrderPrx::uncheckedCast(__result->getProxy());
        ::omero::RStringPtr __ret;
        try
        {
            __ret = __proxy->end_getValue(__result);
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

template<class T> Callback_DimensionOrder_getValuePtr
newCallback_DimensionOrder_getValue(const IceUtil::Handle<T>& instance, void (T::*cb)(const ::omero::RStringPtr&), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_DimensionOrder_getValue<T>(instance, cb, excb, sentcb);
}

template<class T> Callback_DimensionOrder_getValuePtr
newCallback_DimensionOrder_getValue(T* instance, void (T::*cb)(const ::omero::RStringPtr&), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_DimensionOrder_getValue<T>(instance, cb, excb, sentcb);
}

template<class T, typename CT>
class Callback_DimensionOrder_getValue : public Callback_DimensionOrder_getValue_Base, public ::IceInternal::TwowayCallback<T, CT>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception& , const CT&);
    typedef void (T::*Sent)(bool , const CT&);
    typedef void (T::*Response)(const ::omero::RStringPtr&, const CT&);

    Callback_DimensionOrder_getValue(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::TwowayCallback<T, CT>(obj, cb != 0, excb, sentcb), response(cb)
    {
    }

    virtual void __completed(const ::Ice::AsyncResultPtr& __result) const
    {
        ::omero::model::DimensionOrderPrx __proxy = ::omero::model::DimensionOrderPrx::uncheckedCast(__result->getProxy());
        ::omero::RStringPtr __ret;
        try
        {
            __ret = __proxy->end_getValue(__result);
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

template<class T, typename CT> Callback_DimensionOrder_getValuePtr
newCallback_DimensionOrder_getValue(const IceUtil::Handle<T>& instance, void (T::*cb)(const ::omero::RStringPtr&, const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_DimensionOrder_getValue<T, CT>(instance, cb, excb, sentcb);
}

template<class T, typename CT> Callback_DimensionOrder_getValuePtr
newCallback_DimensionOrder_getValue(T* instance, void (T::*cb)(const ::omero::RStringPtr&, const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_DimensionOrder_getValue<T, CT>(instance, cb, excb, sentcb);
}

template<class T>
class CallbackNC_DimensionOrder_setValue : public Callback_DimensionOrder_setValue_Base, public ::IceInternal::OnewayCallbackNC<T>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception&);
    typedef void (T::*Sent)(bool);
    typedef void (T::*Response)();

    CallbackNC_DimensionOrder_setValue(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::OnewayCallbackNC<T>(obj, cb, excb, sentcb)
    {
    }
};

template<class T> Callback_DimensionOrder_setValuePtr
newCallback_DimensionOrder_setValue(const IceUtil::Handle<T>& instance, void (T::*cb)(), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_DimensionOrder_setValue<T>(instance, cb, excb, sentcb);
}

template<class T> Callback_DimensionOrder_setValuePtr
newCallback_DimensionOrder_setValue(const IceUtil::Handle<T>& instance, void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_DimensionOrder_setValue<T>(instance, 0, excb, sentcb);
}

template<class T> Callback_DimensionOrder_setValuePtr
newCallback_DimensionOrder_setValue(T* instance, void (T::*cb)(), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_DimensionOrder_setValue<T>(instance, cb, excb, sentcb);
}

template<class T> Callback_DimensionOrder_setValuePtr
newCallback_DimensionOrder_setValue(T* instance, void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_DimensionOrder_setValue<T>(instance, 0, excb, sentcb);
}

template<class T, typename CT>
class Callback_DimensionOrder_setValue : public Callback_DimensionOrder_setValue_Base, public ::IceInternal::OnewayCallback<T, CT>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception& , const CT&);
    typedef void (T::*Sent)(bool , const CT&);
    typedef void (T::*Response)(const CT&);

    Callback_DimensionOrder_setValue(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::OnewayCallback<T, CT>(obj, cb, excb, sentcb)
    {
    }
};

template<class T, typename CT> Callback_DimensionOrder_setValuePtr
newCallback_DimensionOrder_setValue(const IceUtil::Handle<T>& instance, void (T::*cb)(const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_DimensionOrder_setValue<T, CT>(instance, cb, excb, sentcb);
}

template<class T, typename CT> Callback_DimensionOrder_setValuePtr
newCallback_DimensionOrder_setValue(const IceUtil::Handle<T>& instance, void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_DimensionOrder_setValue<T, CT>(instance, 0, excb, sentcb);
}

template<class T, typename CT> Callback_DimensionOrder_setValuePtr
newCallback_DimensionOrder_setValue(T* instance, void (T::*cb)(const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_DimensionOrder_setValue<T, CT>(instance, cb, excb, sentcb);
}

template<class T, typename CT> Callback_DimensionOrder_setValuePtr
newCallback_DimensionOrder_setValue(T* instance, void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_DimensionOrder_setValue<T, CT>(instance, 0, excb, sentcb);
}

}

}

#endif
