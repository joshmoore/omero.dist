// **********************************************************************
//
// Copyright (c) 2003-2011 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************
//
// Ice version 3.4.2
//
// <auto-generated>
//
// Generated from file `ScriptJob.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

#ifndef __omero_model__opt_hudson_workspace_OMERO_5_0_release_src_components_blitz_generated_omero_model_ScriptJob_h__
#define __omero_model__opt_hudson_workspace_OMERO_5_0_release_src_components_blitz_generated_omero_model_ScriptJob_h__

#include <Ice/LocalObjectF.h>
#include <Ice/ProxyF.h>
#include <Ice/ObjectF.h>
#include <Ice/Exception.h>
#include <Ice/LocalObject.h>
#include <Ice/Proxy.h>
#include <Ice/Object.h>
#include <Ice/Outgoing.h>
#include <Ice/OutgoingAsync.h>
#include <Ice/Incoming.h>
#include <Ice/Direct.h>
#include <Ice/FactoryTableInit.h>
#include <IceUtil/ScopedArray.h>
#include <Ice/StreamF.h>
#include <omero/model/IObject.h>
#include <omero/RTypes.h>
#include <omero/System.h>
#include <omero/Collections.h>
#include <omero/model/Job.h>
#include <Ice/UndefSysMacros.h>

#ifndef ICE_IGNORE_VERSION
#   if ICE_INT_VERSION / 100 != 304
#       error Ice version mismatch!
#   endif
#   if ICE_INT_VERSION % 100 > 50
#       error Beta header file detected
#   endif
#   if ICE_INT_VERSION % 100 < 2
#       error Ice patch level mismatch!
#   endif
#endif

namespace IceProxy
{

namespace omero
{

namespace model
{

class JobStatus;

class JobOriginalFileLink;

class OriginalFile;

class Details;

class ScriptJob;

}

}

}

namespace omero
{

namespace model
{

class JobStatus;
bool operator==(const JobStatus&, const JobStatus&);
bool operator<(const JobStatus&, const JobStatus&);

class JobOriginalFileLink;
bool operator==(const JobOriginalFileLink&, const JobOriginalFileLink&);
bool operator<(const JobOriginalFileLink&, const JobOriginalFileLink&);

class OriginalFile;
bool operator==(const OriginalFile&, const OriginalFile&);
bool operator<(const OriginalFile&, const OriginalFile&);

class Details;
bool operator==(const Details&, const Details&);
bool operator<(const Details&, const Details&);

class ScriptJob;
bool operator==(const ScriptJob&, const ScriptJob&);
bool operator<(const ScriptJob&, const ScriptJob&);

}

}

namespace IceInternal
{

::Ice::Object* upCast(::omero::model::JobStatus*);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::JobStatus*);

::Ice::Object* upCast(::omero::model::JobOriginalFileLink*);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::JobOriginalFileLink*);

::Ice::Object* upCast(::omero::model::OriginalFile*);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::OriginalFile*);

::Ice::Object* upCast(::omero::model::Details*);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::Details*);

::Ice::Object* upCast(::omero::model::ScriptJob*);
::IceProxy::Ice::Object* upCast(::IceProxy::omero::model::ScriptJob*);

}

namespace omero
{

namespace model
{

typedef ::IceInternal::Handle< ::omero::model::JobStatus> JobStatusPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::JobStatus> JobStatusPrx;

void __read(::IceInternal::BasicStream*, JobStatusPrx&);
void __patch__JobStatusPtr(void*, ::Ice::ObjectPtr&);

typedef ::IceInternal::Handle< ::omero::model::JobOriginalFileLink> JobOriginalFileLinkPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::JobOriginalFileLink> JobOriginalFileLinkPrx;

void __read(::IceInternal::BasicStream*, JobOriginalFileLinkPrx&);
void __patch__JobOriginalFileLinkPtr(void*, ::Ice::ObjectPtr&);

typedef ::IceInternal::Handle< ::omero::model::OriginalFile> OriginalFilePtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::OriginalFile> OriginalFilePrx;

void __read(::IceInternal::BasicStream*, OriginalFilePrx&);
void __patch__OriginalFilePtr(void*, ::Ice::ObjectPtr&);

typedef ::IceInternal::Handle< ::omero::model::Details> DetailsPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::Details> DetailsPrx;

void __read(::IceInternal::BasicStream*, DetailsPrx&);
void __patch__DetailsPtr(void*, ::Ice::ObjectPtr&);

typedef ::IceInternal::Handle< ::omero::model::ScriptJob> ScriptJobPtr;
typedef ::IceInternal::ProxyHandle< ::IceProxy::omero::model::ScriptJob> ScriptJobPrx;

void __read(::IceInternal::BasicStream*, ScriptJobPrx&);
void __patch__ScriptJobPtr(void*, ::Ice::ObjectPtr&);

}

}

namespace omero
{

namespace model
{

class Callback_ScriptJob_getDescription_Base : virtual public ::IceInternal::CallbackBase { };
typedef ::IceUtil::Handle< Callback_ScriptJob_getDescription_Base> Callback_ScriptJob_getDescriptionPtr;

class Callback_ScriptJob_setDescription_Base : virtual public ::IceInternal::CallbackBase { };
typedef ::IceUtil::Handle< Callback_ScriptJob_setDescription_Base> Callback_ScriptJob_setDescriptionPtr;

}

}

namespace IceProxy
{

namespace omero
{

namespace model
{

class ScriptJob : virtual public ::IceProxy::omero::model::Job
{
public:

    ::omero::RStringPtr getDescription()
    {
        return getDescription(0);
    }
    ::omero::RStringPtr getDescription(const ::Ice::Context& __ctx)
    {
        return getDescription(&__ctx);
    }

    ::Ice::AsyncResultPtr begin_getDescription()
    {
        return begin_getDescription(0, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_getDescription(const ::Ice::Context& __ctx)
    {
        return begin_getDescription(&__ctx, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_getDescription(const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getDescription(0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_getDescription(const ::Ice::Context& __ctx, const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getDescription(&__ctx, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_getDescription(const ::omero::model::Callback_ScriptJob_getDescriptionPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getDescription(0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_getDescription(const ::Ice::Context& __ctx, const ::omero::model::Callback_ScriptJob_getDescriptionPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_getDescription(&__ctx, __del, __cookie);
    }

    ::omero::RStringPtr end_getDescription(const ::Ice::AsyncResultPtr&);
    
private:

    ::omero::RStringPtr getDescription(const ::Ice::Context*);
    ::Ice::AsyncResultPtr begin_getDescription(const ::Ice::Context*, const ::IceInternal::CallbackBasePtr&, const ::Ice::LocalObjectPtr& __cookie = 0);
    
public:

    void setDescription(const ::omero::RStringPtr& theDescription)
    {
        setDescription(theDescription, 0);
    }
    void setDescription(const ::omero::RStringPtr& theDescription, const ::Ice::Context& __ctx)
    {
        setDescription(theDescription, &__ctx);
    }

    ::Ice::AsyncResultPtr begin_setDescription(const ::omero::RStringPtr& theDescription)
    {
        return begin_setDescription(theDescription, 0, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_setDescription(const ::omero::RStringPtr& theDescription, const ::Ice::Context& __ctx)
    {
        return begin_setDescription(theDescription, &__ctx, ::IceInternal::__dummyCallback, 0);
    }

    ::Ice::AsyncResultPtr begin_setDescription(const ::omero::RStringPtr& theDescription, const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setDescription(theDescription, 0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_setDescription(const ::omero::RStringPtr& theDescription, const ::Ice::Context& __ctx, const ::Ice::CallbackPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setDescription(theDescription, &__ctx, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_setDescription(const ::omero::RStringPtr& theDescription, const ::omero::model::Callback_ScriptJob_setDescriptionPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setDescription(theDescription, 0, __del, __cookie);
    }

    ::Ice::AsyncResultPtr begin_setDescription(const ::omero::RStringPtr& theDescription, const ::Ice::Context& __ctx, const ::omero::model::Callback_ScriptJob_setDescriptionPtr& __del, const ::Ice::LocalObjectPtr& __cookie = 0)
    {
        return begin_setDescription(theDescription, &__ctx, __del, __cookie);
    }

    void end_setDescription(const ::Ice::AsyncResultPtr&);
    
private:

    void setDescription(const ::omero::RStringPtr&, const ::Ice::Context*);
    ::Ice::AsyncResultPtr begin_setDescription(const ::omero::RStringPtr&, const ::Ice::Context*, const ::IceInternal::CallbackBasePtr&, const ::Ice::LocalObjectPtr& __cookie = 0);
    
public:
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_context(const ::Ice::Context& __context) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_context(__context).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_context(__context).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_adapterId(const std::string& __id) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_adapterId(__id).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_adapterId(__id).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_endpoints(const ::Ice::EndpointSeq& __endpoints) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_endpoints(__endpoints).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_endpoints(__endpoints).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_locatorCacheTimeout(int __timeout) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_locatorCacheTimeout(__timeout).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_locatorCacheTimeout(__timeout).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_connectionCached(bool __cached) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_connectionCached(__cached).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_connectionCached(__cached).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_endpointSelection(::Ice::EndpointSelectionType __est) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_endpointSelection(__est).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_endpointSelection(__est).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_secure(bool __secure) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_secure(__secure).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_secure(__secure).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_preferSecure(bool __preferSecure) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_preferSecure(__preferSecure).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_preferSecure(__preferSecure).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_router(const ::Ice::RouterPrx& __router) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_router(__router).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_router(__router).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_locator(const ::Ice::LocatorPrx& __locator) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_locator(__locator).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_locator(__locator).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_collocationOptimized(bool __co) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_collocationOptimized(__co).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_collocationOptimized(__co).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_twoway() const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_twoway().get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_twoway().get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_oneway() const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_oneway().get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_oneway().get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_batchOneway() const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_batchOneway().get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_batchOneway().get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_datagram() const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_datagram().get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_datagram().get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_batchDatagram() const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_batchDatagram().get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_batchDatagram().get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_compress(bool __compress) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_compress(__compress).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_compress(__compress).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_timeout(int __timeout) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_timeout(__timeout).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_timeout(__timeout).get());
    #endif
    }
    
    ::IceInternal::ProxyHandle<ScriptJob> ice_connectionId(const std::string& __id) const
    {
    #if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
        typedef ::IceProxy::Ice::Object _Base;
        return dynamic_cast<ScriptJob*>(_Base::ice_connectionId(__id).get());
    #else
        return dynamic_cast<ScriptJob*>(::IceProxy::Ice::Object::ice_connectionId(__id).get());
    #endif
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

class ScriptJob : virtual public ::IceDelegate::omero::model::Job
{
public:

    virtual ::omero::RStringPtr getDescription(const ::Ice::Context*) = 0;

    virtual void setDescription(const ::omero::RStringPtr&, const ::Ice::Context*) = 0;
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

class ScriptJob : virtual public ::IceDelegate::omero::model::ScriptJob,
                  virtual public ::IceDelegateM::omero::model::Job
{
public:

    virtual ::omero::RStringPtr getDescription(const ::Ice::Context*);

    virtual void setDescription(const ::omero::RStringPtr&, const ::Ice::Context*);
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

class ScriptJob : virtual public ::IceDelegate::omero::model::ScriptJob,
                  virtual public ::IceDelegateD::omero::model::Job
{
public:

    virtual ::omero::RStringPtr getDescription(const ::Ice::Context*);

    virtual void setDescription(const ::omero::RStringPtr&, const ::Ice::Context*);
};

}

}

}

namespace omero
{

namespace model
{

class ScriptJob : public ::omero::model::Job
{
public:

    typedef ScriptJobPrx ProxyType;
    typedef ScriptJobPtr PointerType;
    
    ScriptJob() {}
    ScriptJob(const ::omero::RLongPtr&, const ::omero::model::DetailsPtr&, bool, const ::omero::RIntPtr&, const ::omero::RStringPtr&, const ::omero::RStringPtr&, const ::omero::RStringPtr&, const ::omero::RStringPtr&, const ::omero::model::JobStatusPtr&, const ::omero::RTimePtr&, const ::omero::RTimePtr&, const ::omero::RTimePtr&, const ::omero::RTimePtr&, const ::omero::model::JobOriginalFileLinksSeq&, bool, const ::omero::sys::CountMap&, const ::omero::RStringPtr&);
    virtual ::Ice::ObjectPtr ice_clone() const;

    virtual bool ice_isA(const ::std::string&, const ::Ice::Current& = ::Ice::Current()) const;
    virtual ::std::vector< ::std::string> ice_ids(const ::Ice::Current& = ::Ice::Current()) const;
    virtual const ::std::string& ice_id(const ::Ice::Current& = ::Ice::Current()) const;
    static const ::std::string& ice_staticId();

    virtual void __gcReachable(::IceInternal::GCCountMap&) const;
    virtual void __gcClear();

    virtual ::omero::RStringPtr getDescription(const ::Ice::Current& = ::Ice::Current()) = 0;
    ::Ice::DispatchStatus ___getDescription(::IceInternal::Incoming&, const ::Ice::Current&);

    virtual void setDescription(const ::omero::RStringPtr&, const ::Ice::Current& = ::Ice::Current()) = 0;
    ::Ice::DispatchStatus ___setDescription(::IceInternal::Incoming&, const ::Ice::Current&);

    virtual ::Ice::DispatchStatus __dispatch(::IceInternal::Incoming&, const ::Ice::Current&);

    virtual void __write(::IceInternal::BasicStream*) const;
    virtual void __read(::IceInternal::BasicStream*, bool);
// COMPILERFIX: Stream API is not supported with VC++ 6
#if !defined(_MSC_VER) || (_MSC_VER >= 1300)
    virtual void __write(const ::Ice::OutputStreamPtr&) const;
    virtual void __read(const ::Ice::InputStreamPtr&, bool);
#endif

protected:

    ::omero::RStringPtr description;
};

inline bool operator==(const ScriptJob& l, const ScriptJob& r)
{
    return static_cast<const ::Ice::Object&>(l) == static_cast<const ::Ice::Object&>(r);
}

inline bool operator<(const ScriptJob& l, const ScriptJob& r)
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
class CallbackNC_ScriptJob_getDescription : public Callback_ScriptJob_getDescription_Base, public ::IceInternal::TwowayCallbackNC<T>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception&);
    typedef void (T::*Sent)(bool);
    typedef void (T::*Response)(const ::omero::RStringPtr&);

    CallbackNC_ScriptJob_getDescription(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::TwowayCallbackNC<T>(obj, cb != 0, excb, sentcb), response(cb)
    {
    }

    virtual void __completed(const ::Ice::AsyncResultPtr& __result) const
    {
        ::omero::model::ScriptJobPrx __proxy = ::omero::model::ScriptJobPrx::uncheckedCast(__result->getProxy());
        ::omero::RStringPtr __ret;
        try
        {
            __ret = __proxy->end_getDescription(__result);
        }
        catch(::Ice::Exception& ex)
        {
#if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
            __exception(__result, ex);
#else
            ::IceInternal::CallbackNC<T>::__exception(__result, ex);
#endif
            return;
        }
        if(response)
        {
#if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
            (callback.get()->*response)(__ret);
#else
            (::IceInternal::CallbackNC<T>::callback.get()->*response)(__ret);
#endif
        }
    }

    Response response;
};

template<class T> Callback_ScriptJob_getDescriptionPtr
newCallback_ScriptJob_getDescription(const IceUtil::Handle<T>& instance, void (T::*cb)(const ::omero::RStringPtr&), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_ScriptJob_getDescription<T>(instance, cb, excb, sentcb);
}

template<class T> Callback_ScriptJob_getDescriptionPtr
newCallback_ScriptJob_getDescription(T* instance, void (T::*cb)(const ::omero::RStringPtr&), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_ScriptJob_getDescription<T>(instance, cb, excb, sentcb);
}

template<class T, typename CT>
class Callback_ScriptJob_getDescription : public Callback_ScriptJob_getDescription_Base, public ::IceInternal::TwowayCallback<T, CT>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception& , const CT&);
    typedef void (T::*Sent)(bool , const CT&);
    typedef void (T::*Response)(const ::omero::RStringPtr&, const CT&);

    Callback_ScriptJob_getDescription(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::TwowayCallback<T, CT>(obj, cb != 0, excb, sentcb), response(cb)
    {
    }

    virtual void __completed(const ::Ice::AsyncResultPtr& __result) const
    {
        ::omero::model::ScriptJobPrx __proxy = ::omero::model::ScriptJobPrx::uncheckedCast(__result->getProxy());
        ::omero::RStringPtr __ret;
        try
        {
            __ret = __proxy->end_getDescription(__result);
        }
        catch(::Ice::Exception& ex)
        {
#if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
            __exception(__result, ex);
#else
            ::IceInternal::Callback<T, CT>::__exception(__result, ex);
#endif
            return;
        }
        if(response)
        {
#if defined(_MSC_VER) && (_MSC_VER < 1300) // VC++ 6 compiler bug
            (callback.get()->*response)(__ret, CT::dynamicCast(__result->getCookie()));
#else
            (::IceInternal::Callback<T, CT>::callback.get()->*response)(__ret, CT::dynamicCast(__result->getCookie()));
#endif
        }
    }

    Response response;
};

template<class T, typename CT> Callback_ScriptJob_getDescriptionPtr
newCallback_ScriptJob_getDescription(const IceUtil::Handle<T>& instance, void (T::*cb)(const ::omero::RStringPtr&, const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_ScriptJob_getDescription<T, CT>(instance, cb, excb, sentcb);
}

template<class T, typename CT> Callback_ScriptJob_getDescriptionPtr
newCallback_ScriptJob_getDescription(T* instance, void (T::*cb)(const ::omero::RStringPtr&, const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_ScriptJob_getDescription<T, CT>(instance, cb, excb, sentcb);
}

template<class T>
class CallbackNC_ScriptJob_setDescription : public Callback_ScriptJob_setDescription_Base, public ::IceInternal::OnewayCallbackNC<T>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception&);
    typedef void (T::*Sent)(bool);
    typedef void (T::*Response)();

    CallbackNC_ScriptJob_setDescription(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::OnewayCallbackNC<T>(obj, cb, excb, sentcb)
    {
    }
};

template<class T> Callback_ScriptJob_setDescriptionPtr
newCallback_ScriptJob_setDescription(const IceUtil::Handle<T>& instance, void (T::*cb)(), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_ScriptJob_setDescription<T>(instance, cb, excb, sentcb);
}

template<class T> Callback_ScriptJob_setDescriptionPtr
newCallback_ScriptJob_setDescription(const IceUtil::Handle<T>& instance, void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_ScriptJob_setDescription<T>(instance, 0, excb, sentcb);
}

template<class T> Callback_ScriptJob_setDescriptionPtr
newCallback_ScriptJob_setDescription(T* instance, void (T::*cb)(), void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_ScriptJob_setDescription<T>(instance, cb, excb, sentcb);
}

template<class T> Callback_ScriptJob_setDescriptionPtr
newCallback_ScriptJob_setDescription(T* instance, void (T::*excb)(const ::Ice::Exception&), void (T::*sentcb)(bool) = 0)
{
    return new CallbackNC_ScriptJob_setDescription<T>(instance, 0, excb, sentcb);
}

template<class T, typename CT>
class Callback_ScriptJob_setDescription : public Callback_ScriptJob_setDescription_Base, public ::IceInternal::OnewayCallback<T, CT>
{
public:

    typedef IceUtil::Handle<T> TPtr;

    typedef void (T::*Exception)(const ::Ice::Exception& , const CT&);
    typedef void (T::*Sent)(bool , const CT&);
    typedef void (T::*Response)(const CT&);

    Callback_ScriptJob_setDescription(const TPtr& obj, Response cb, Exception excb, Sent sentcb)
        : ::IceInternal::OnewayCallback<T, CT>(obj, cb, excb, sentcb)
    {
    }
};

template<class T, typename CT> Callback_ScriptJob_setDescriptionPtr
newCallback_ScriptJob_setDescription(const IceUtil::Handle<T>& instance, void (T::*cb)(const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_ScriptJob_setDescription<T, CT>(instance, cb, excb, sentcb);
}

template<class T, typename CT> Callback_ScriptJob_setDescriptionPtr
newCallback_ScriptJob_setDescription(const IceUtil::Handle<T>& instance, void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_ScriptJob_setDescription<T, CT>(instance, 0, excb, sentcb);
}

template<class T, typename CT> Callback_ScriptJob_setDescriptionPtr
newCallback_ScriptJob_setDescription(T* instance, void (T::*cb)(const CT&), void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_ScriptJob_setDescription<T, CT>(instance, cb, excb, sentcb);
}

template<class T, typename CT> Callback_ScriptJob_setDescriptionPtr
newCallback_ScriptJob_setDescription(T* instance, void (T::*excb)(const ::Ice::Exception&, const CT&), void (T::*sentcb)(bool, const CT&) = 0)
{
    return new Callback_ScriptJob_setDescription<T, CT>(instance, 0, excb, sentcb);
}

}

}

#endif