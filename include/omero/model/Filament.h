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
// Generated from file `Filament.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

#ifndef __omero_model__opt_hudson_workspace_OMERO_5_0_release_src_components_blitz_generated_omero_model_Filament_h__
#define __omero_model__opt_hudson_workspace_OMERO_5_0_release_src_components_blitz_generated_omero_model_Filament_h__

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
#include <omero/model/LightSource.h>
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

class FilamentType;
void __read(::IceInternal::BasicStream*, ::IceInternal::ProxyHandle< ::IceProxy::omero::model::FilamentType>&);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::FilamentType*);

class Instrument;
void __read(::IceInternal::BasicStream*, ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Instrument>&);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::Instrument*);

class Details;
void __read(::IceInternal::BasicStream*, ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Details>&);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::Details*);

class Filament;
void __read(::IceInternal::BasicStream*, ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Filament>&);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::Filament*);

}

}

}

namespace omero
{

namespace model
{

class FilamentType;
bool operator==(const FilamentType&, const FilamentType&);
bool operator<(const FilamentType&, const FilamentType&);
::Ice::Object* upCast(::omero::model::FilamentType*);
typedef ::IceInternal::Handle< ::omero::model::FilamentType> FilamentTypePtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::FilamentType> FilamentTypePrx;
void __patch(FilamentTypePtr&, const ::Ice::ObjectPtr&);

class Instrument;
bool operator==(const Instrument&, const Instrument&);
bool operator<(const Instrument&, const Instrument&);
::Ice::Object* upCast(::omero::model::Instrument*);
typedef ::IceInternal::Handle< ::omero::model::Instrument> InstrumentPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Instrument> InstrumentPrx;
void __patch(InstrumentPtr&, const ::Ice::ObjectPtr&);

class Details;
bool operator==(const Details&, const Details&);
bool operator<(const Details&, const Details&);
::Ice::Object* upCast(::omero::model::Details*);
typedef ::IceInternal::Handle< ::omero::model::Details> DetailsPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Details> DetailsPrx;
void __patch(DetailsPtr&, const ::Ice::ObjectPtr&);

class Filament;
bool operator==(const Filament&, const Filament&);
bool operator<(const Filament&, const Filament&);
::Ice::Object* upCast(::omero::model::Filament*);
typedef ::IceInternal::Handle< ::omero::model::Filament> FilamentPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Filament> FilamentPrx;
void __patch(FilamentPtr&, const ::Ice::ObjectPtr&);

}

}

namespace omero
{

namespace model
{

class Callback_Filament_getType_Base : virtual public ::IceInternal::CallbackBase { };
typedef ::IceUtil::Handle< Callback_Filament_getType_Base> Callback_Filament_getTypePtr;

class Callback_Filament_setType_Base : virtual public ::IceInternal::CallbackBase { };
typedef ::IceUtil::Handle< Callback_Filament_setType_Base> Callback_Filament_setTypePtr;

}

}

namespace IceProxy
{

namespace omero
{

namespace model
{

class Filament : virtual public ::IceProxy::omero::model::LightSource
{
public:

    ::omero::model::FilamentTypePtr getType()
    {
        return getType(0);
    }
    ::omero::model::FilamentTypePtr getType(const ::Ice::Context& __ctx)
    {
        return getType(&__ctx);
    }
#ifdef ICE_CPP11
    ::Ice::AsyncResultPtr
    begin_getType(const ::IceInternal::Function<void (const ::omero::model::FilamentTypePtr&)>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception = ::IceInternal::Function<void (const ::Ice::Exception&)>(), const ::IceInternal::Function<void (bool)>& __sent = ::IceInternal::Function<void (bool)>())
    {
        return __begin_getType(0, __response, __exception, __sent);
    }
    ::Ice::AsyncResultPtr
    begin_getType(const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __completed, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __sent = ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>())
    {
        return begin_getType(0, ::Ice::newCallback(__completed, __sent), 0);
    }
    ::Ice::AsyncResultPtr
    begin_getType(const ::Ice::Context& __ctx, const ::IceInternal::Function<void (const ::omero::model::FilamentTypePtr&)>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception = ::IceInternal::Function<void (const ::Ice::Exception&)>(), const ::IceInternal::Function<void (bool)>& __sent = ::IceInternal::Function<void (bool)>())
    {
        return __begin_getType(&__ctx, __response, __exception, __sent);
    }
    ::Ice::AsyncResultPtr
    begin_getType(const ::Ice::Context& __ctx, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __completed, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __sent = ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>())
    {
        return begin_getType(&__ctx, ::Ice::newCallback(__completed, __sent));
    }
    
private:

    ::Ice::AsyncResultPtr __begin_getType(const ::Ice::Context* __ctx, const ::IceInternal::Function<void (const ::omero::model::FilamentTypePtr&)>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception, const ::IceInternal::Function<void (bool)>& __sent)
    {
        class Cpp11CB : public ::IceInternal::Cpp11FnCallbackNC
        {
        public:

            Cpp11CB(const ::std::function<void (const ::omero::model::FilamentTypePtr&)>& responseFunc, const ::std::function<void (const ::Ice::Exception&)>& exceptionFunc, const ::std::function<void (bool)>& sentFunc) :
                ::IceInternal::Cpp11FnCallbackNC(exceptionFunc, sentFunc),
                _response(responseFunc)
            {
                CallbackBase::checkCallback(true, responseFunc || exceptionFunc != nullptr);
            }

            virtual void __completed(const ::Ice::AsyncResultPtr& __result) const
            {
                ::omero::model::FilamentPrx __proxy = ::omero::model::FilamentPrx::uncheckedCast(__result->getProxy());
                ::omero::model::FilamentTypePtr __ret;
                try
                {
                    __ret = __proxy->end_getType(__result);
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
            
            ::std::function<void (const ::omero::model::FilamentTypePtr&)> _response;
        };
        return begin_getType(__ctx, new Cpp11CB(__response, __exception, __sent));
    }
    
public:
#endif

    ::Ice::AsyncResultPtr begin_getType()
    {
        return begin_getType(0, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_getType(const ::Ice::Context& __ctx)
    {
        return begin_getType(&__ctx, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_getType(const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getType(0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_getType(const ::Ice::Context& __ctx, const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getType(&__ctx, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_getType(const ::omero::model::Callback_Filament_getTypePtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getType(0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_getType(const ::Ice::Context& __ctx, const ::omero::model::Callback_Filament_getTypePtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getType(&__ctx, __del, __cookie);
    }

    ::omero::model::FilamentTypePtr end_getType(const ::Ice::AsyncResultPtr&);
    
private:

    ::omero::model::FilamentTypePtr getType(const ::Ice::Context*);
    ::Ice::AsyncResultPtr begin_getType(const ::Ice::Context*, const ::IceInternal::CallbackBasePtr&, const ::Ice::LocalObjectPtr& __cookie = 0);
    
public:

    void setType(const ::omero::model::FilamentTypePtr& theType)
    {
        setType(theType, 0);
    }
    void setType(const ::omero::model::FilamentTypePtr& theType, const ::Ice::Context& __ctx)
    {
        setType(theType, &__ctx);
    }
#ifdef ICE_CPP11
    ::Ice::AsyncResultPtr
    begin_setType(const ::omero::model::FilamentTypePtr& theType, const ::IceInternal::Function<void ()>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception = ::IceInternal::Function<void (const ::Ice::Exception&)>(), const ::IceInternal::Function<void (bool)>& __sent = ::IceInternal::Function<void (bool)>())
    {
        return begin_setType(theType, 0, new ::IceInternal::Cpp11FnOnewayCallbackNC(__response, __exception, __sent));
    }
    ::Ice::AsyncResultPtr
    begin_setType(const ::omero::model::FilamentTypePtr& theType, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __completed, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __sent = ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>())
    {
        return begin_setType(theType, 0, ::Ice::newCallback(__completed, __sent), 0);
    }
    ::Ice::AsyncResultPtr
    begin_setType(const ::omero::model::FilamentTypePtr& theType, const ::Ice::Context& __ctx, const ::IceInternal::Function<void ()>& __response, const ::IceInternal::Function<void (const ::Ice::Exception&)>& __exception = ::IceInternal::Function<void (const ::Ice::Exception&)>(), const ::IceInternal::Function<void (bool)>& __sent = ::IceInternal::Function<void (bool)>())
    {
        return begin_setType(theType, &__ctx, new ::IceInternal::Cpp11FnOnewayCallbackNC(__response, __exception, __sent), 0);
    }
    ::Ice::AsyncResultPtr
    begin_setType(const ::omero::model::FilamentTypePtr& theType, const ::Ice::Context& __ctx, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __completed, const ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>& __sent = ::IceInternal::Function<void (const ::Ice::AsyncResultPtr&)>())
    {
        return begin_setType(theType, &__ctx, ::Ice::newCallback(__completed, __sent));
    }
#endif

    ::Ice::AsyncResultPtr begin_setType(const ::omero::model::FilamentTypePtr& theType)
    {
        return begin_setType(theType, 0, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_setType(const ::omero::model::FilamentTypePtr& theType, const ::Ice::Context& __ctx)
    {
        return begin_setType(theType, &__ctx, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_setType(const ::omero::model::FilamentTypePtr& theType, const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setType(theType, 0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_setType(const ::omero::model::FilamentTypePtr& theType, const ::Ice::Context& __ctx, const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setType(theType, &__ctx, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_setType(const ::omero::model::FilamentTypePtr& theType, const ::omero::model::Callback_Filament_setTypePtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setType(theType, 0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_setType(const ::omero::model::FilamentTypePtr& theType, const ::Ice::Context& __ctx, const ::omero::model::Callback_Filament_setTypePtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setType(theType, &__ctx, __del, __cookie);
    }

    void end_setType(const ::Ice::AsyncResultPtr&);
    
private:

    void setType(const ::omero::model::FilamentTypePtr&, const ::Ice::Context*);
    ::Ice::AsyncResultPtr begin_setType(const ::omero::model::FilamentTypePtr&, const ::Ice::Context*, const ::IceInternal::CallbackBasePtr&, const ::Ice::LocalObjectPtr& __cookie = 0);
    
public:
    
    ::IceInternal::ProxyHandle<Filament> ice_context(const ::Ice::Context& __context) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_context(__context).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_adapterId(const ::std::string& __id) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_adapterId(__id).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_endpoints(const ::Ice::EndpointSeq& __endpoints) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_endpoints(__endpoints).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_locatorCacheTimeout(int __timeout) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_locatorCacheTimeout(__timeout).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_connectionCached(bool __cached) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_connectionCached(__cached).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_endpointSelection(::Ice::EndpointSelectionType __est) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_endpointSelection(__est).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_secure(bool __secure) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_secure(__secure).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_preferSecure(bool __preferSecure) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_preferSecure(__preferSecure).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_router(const ::Ice::RouterPrx& __router) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_router(__router).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_locator(const ::Ice::LocatorPrx& __locator) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_locator(__locator).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_collocationOptimized(bool __co) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_collocationOptimized(__co).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_twoway() const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_twoway().get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_oneway() const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_oneway().get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_batchOneway() const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_batchOneway().get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_datagram() const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_datagram().get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_batchDatagram() const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_batchDatagram().get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_compress(bool __compress) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_compress(__compress).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_timeout(int __timeout) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_timeout(__timeout).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_connectionId(const ::std::string& __id) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_connectionId(__id).get());
    }
    
    ::IceInternal::ProxyHandle<Filament> ice_encodingVersion(const ::Ice::EncodingVersion& __v) const
    {
        return dynamic_cast<Filament*>(::IceProxy::Ice::Object::ice_encodingVersion(__v).get());
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

class Filament : virtual public ::IceDelegate::omero::model::LightSource
{
public:

    virtual ::omero::model::FilamentTypePtr getType(const ::Ice::Context*, ::IceInternal::InvocationObserver&) = 0;

    virtual void setType(const ::omero::model::FilamentTypePtr&, const ::Ice::Context*, ::IceInternal::InvocationObserver&) = 0;
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

class Filament : virtual public ::IceDelegate::omero::model::Filament,
                 virtual public ::IceDelegateM::omero::model::LightSource
{
public:

    virtual ::omero::model::FilamentTypePtr getType(const ::Ice::Context*, ::IceInternal::InvocationObserver&);

    virtual void setType(const ::omero::model::FilamentTypePtr&, const ::Ice::Context*, ::IceInternal::InvocationObserver&);
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

class Filament : virtual public ::IceDelegate::omero::model::Filament,
                 virtual public ::IceDelegateD::omero::model::LightSource
{
public:

    virtual ::omero::model::FilamentTypePtr getType(const ::Ice::Context*, ::IceInternal::InvocationObserver&);

    virtual void setType(const ::omero::model::FilamentTypePtr&, const ::Ice::Context*, ::IceInternal::InvocationObserver&);
};

}

}

}

namespace omero
{

namespace model
{

class Filament : public ::omero::model::LightSource
{
public:

    typedef FilamentPrx ProxyType;
    typedef FilamentPtr PointerType;

    Filament()
    {
    }

    Filament(const ::omero::RLongPtr& __ice_id, const ::omero::model::DetailsPtr& __ice_details, bool __ice_loaded, const ::omero::RIntPtr& __ice_version, const ::omero::RStringPtr& __ice_manufacturer, const ::omero::RStringPtr& __ice_model, const ::omero::RDoublePtr& __ice_power, const ::omero::RStringPtr& __ice_lotNumber, const ::omero::RStringPtr& __ice_serialNumber, const ::omero::model::InstrumentPtr& __ice_instrument, const ::omero::model::FilamentTypePtr& __ice_type) :
        ::omero::model::LightSource(__ice_id, __ice_details, __ice_loaded, __ice_version, __ice_manufacturer, __ice_model, __ice_power, __ice_lotNumber, __ice_serialNumber, __ice_instrument)
        ,
        type(__ice_type)
    {
    }

    virtual ::Ice::ObjectPtr ice_clone() const;

    virtual bool ice_isA(const ::std::string&, const ::Ice::Current& = ::Ice::Current()) const;
    virtual ::std::vector< ::std::string> ice_ids(const ::Ice::Current& = ::Ice::Current()) const;
    virtual const ::std::string& ice_id(const ::Ice::Current& = ::Ice::Current()) const;
    static const ::std::string& ice_staticId();

    virtual void __gcReachable(::IceInternal::GCCountMap&) const;
    virtual void __gcClear();

    virtual ::omero::model::FilamentTypePtr getType(const ::Ice::Current& = ::Ice::Current()) = 0;
    ::Ice::DispatchStatus ___getType(::IceInternal::Incoming&, const ::Ice::Current&);

    virtual void setType(const ::omero::model::FilamentTypePtr&, const ::Ice::Current& = ::Ice::Current()) = 0;
    ::Ice::DispatchStatus ___setType(::IceInternal::Incoming&, const ::Ice::Current&);

    virtual ::Ice::DispatchStatus __dispatch(::IceInternal::Incoming&, const ::Ice::Current&);

protected:
    virtual void __writeImpl(::IceInternal::BasicStream*) const;
    virtual void __readImpl(::IceInternal::BasicStream*);
    #ifdef __SUNPRO_CC
    using ::omero::model::LightSource::__writeImpl;
    using ::omero::model::LightSource::__readImpl;
    #endif

    ::omero::model::FilamentTypePtr type;
};

inline bool operator==(const Filament& l, const Filament& r)
{
    return static_cast<const ::Ice::Object&>(l) == static_cast<const ::Ice::Object&>(r);
}

inline bool operator<(const Filament& l, const Filament& r)
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
class CallbackNC_Filament_getType : public Callback_Filament_getType_Base, public ::IceInternal::TwowayCallbackNC<T>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception&);
    typedef void (T::*Sent)(bool);
    typedef void (T::*Response)(const ::omero::model::FilamentTypePtr&);

    CallbackNC_Filament_getType(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::TwowayCallbackNC<T>(obj, cb != 0, excb, sentcb), response(cb)
    {
    }

    virtual void __completed(const ::Ice::AsyncResultPtr& __result) const
    {
        ::omero::model::FilamentPrx __proxy = ::omero::model::FilamentPrx::uncheckedCast(__result->getProxy());
        ::omero::model::FilamentTypePtr __ret;
        try
        {
            __ret = __proxy->end_getType(__result);
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

template<class T> Callback_Filament_getTypePtr
newCallback_Filament_getType(const IceUtil::Handle<T>& instance, void (T::*cb)(const ::omero::model::FilamentTypePtr&), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_Filament_getType<T>(instance, cb, excb, sentcb);
}

template<class T> Callback_Filament_getTypePtr
newCallback_Filament_getType(T* instance, void (T::*cb)(const ::omero::model::FilamentTypePtr&), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_Filament_getType<T>(instance, cb, excb, sentcb);
}

template<class T, typename CT>
class Callback_Filament_getType : public Callback_Filament_getType_Base, public ::IceInternal::TwowayCallback<T, CT>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception& , const CT&);
    typedef void (T::*Sent)(bool , const CT&);
    typedef void (T::*Response)(const ::omero::model::FilamentTypePtr&, const CT&);

    Callback_Filament_getType(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::TwowayCallback<T, CT>(obj, cb != 0, excb, sentcb), response(cb)
    {
    }

    virtual void __completed(const ::Ice::AsyncResultPtr& __result) const
    {
        ::omero::model::FilamentPrx __proxy = ::omero::model::FilamentPrx::uncheckedCast(__result->getProxy());
        ::omero::model::FilamentTypePtr __ret;
        try
        {
            __ret = __proxy->end_getType(__result);
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

template<class T, typename CT> Callback_Filament_getTypePtr
newCallback_Filament_getType(const IceUtil::Handle<T>& instance, void (T::*cb)(const ::omero::model::FilamentTypePtr&, const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_Filament_getType<T, CT>(instance, cb, excb, sentcb);
}

template<class T, typename CT> Callback_Filament_getTypePtr
newCallback_Filament_getType(T* instance, void (T::*cb)(const ::omero::model::FilamentTypePtr&, const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_Filament_getType<T, CT>(instance, cb, excb, sentcb);
}

template<class T>
class CallbackNC_Filament_setType : public Callback_Filament_setType_Base, public ::IceInternal::OnewayCallbackNC<T>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception&);
    typedef void (T::*Sent)(bool);
    typedef void (T::*Response)();

    CallbackNC_Filament_setType(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::OnewayCallbackNC<T>(obj, cb, excb, sentcb)
    {
    }
};

template<class T> Callback_Filament_setTypePtr
newCallback_Filament_setType(const IceUtil::Handle<T>& instance, void (T::*cb)(), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_Filament_setType<T>(instance, cb, excb, sentcb);
}

template<class T> Callback_Filament_setTypePtr
newCallback_Filament_setType(const IceUtil::Handle<T>& instance, void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_Filament_setType<T>(instance, 0, excb, sentcb);
}

template<class T> Callback_Filament_setTypePtr
newCallback_Filament_setType(T* instance, void (T::*cb)(), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_Filament_setType<T>(instance, cb, excb, sentcb);
}

template<class T> Callback_Filament_setTypePtr
newCallback_Filament_setType(T* instance, void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_Filament_setType<T>(instance, 0, excb, sentcb);
}

template<class T, typename CT>
class Callback_Filament_setType : public Callback_Filament_setType_Base, public ::IceInternal::OnewayCallback<T, CT>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception& , const CT&);
    typedef void (T::*Sent)(bool , const CT&);
    typedef void (T::*Response)(const CT&);

    Callback_Filament_setType(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::OnewayCallback<T, CT>(obj, cb, excb, sentcb)
    {
    }
};

template<class T, typename CT> Callback_Filament_setTypePtr
newCallback_Filament_setType(const IceUtil::Handle<T>& instance, void (T::*cb)(const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_Filament_setType<T, CT>(instance, cb, excb, sentcb);
}

template<class T, typename CT> Callback_Filament_setTypePtr
newCallback_Filament_setType(const IceUtil::Handle<T>& instance, void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_Filament_setType<T, CT>(instance, 0, excb, sentcb);
}

template<class T, typename CT> Callback_Filament_setTypePtr
newCallback_Filament_setType(T* instance, void (T::*cb)(const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_Filament_setType<T, CT>(instance, cb, excb, sentcb);
}

template<class T, typename CT> Callback_Filament_setTypePtr
newCallback_Filament_setType(T* instance, void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_Filament_setType<T, CT>(instance, 0, excb, sentcb);
}

}

}

#endif
