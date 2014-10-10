# **********************************************************************
#
# Copyright (c) 2003-2011 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.4.2
#
# <auto-generated>
#
# Generated from file `ServerErrors.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy, __builtin__
import Glacier2_Session_ice
import omero_Collections_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Start of module omero
__name__ = 'omero'
_M_omero.__doc__ = '''Exceptions thrown by OMERO server components. Exceptions thrown client side
are available defined in each language binding separately, but will usually
subclass from "ClientError" For more information, see:

http://trac.openmicroscopy.org.uk/ome/wiki/ExceptionHandling

including examples of what a appropriate try/catch block would look like.

All exceptions that are thrown by a remote call (any call on a *Prx instance)
will be either a subclass of [Ice::UserException] or [Ice::LocalException].
Inheritance Hierarchy for Exceptions
from the Ice manual shows the entire exception hierarchy. The exceptions described in
this file will subclass from [Ice::UserException]. Other Ice-runtime exceptions subclass
from [Ice::LocalException].

OMERO Specific:
===============
ServerError (root server exception)
|
|_ InternalException (server bug)
|
|_ ResourceError (non-recoverable)
|  \_ NoProcessorAvailable
|
|_ ConcurrencyException (recoverable)
|  |_ ConcurrentModification (data was changed)
|  |_ OptimisticLockException (changed data conflicts)
|  |_ LockTimeout (took too long to aquire lock)
|  |_ TryAgain (some processing required before server is ready)
|  \_ TooManyUsersException
|     \_ DatabaseBusyException
|
|_ ApiUsageException (misuse of services)
|   |_ OverUsageException (too much)
|   |_ QueryException (bad query string)
|   |_ ValidationException (bad data)
|      |_ ChecksumValidationException (checksum mismatch)
|      \_ FilePathNamingException (repository path badly named)
|
|_ SecurityViolation (some no-no)
|   \_ GroupSecurityViolation
|      |_ PermissionMismatchGroupSecurityViolation
|      \_ ReadOnlyGroupSecurityViolation
|
\_SessionException
|_ RemovedSessionException (accessing a non-extant session)
|_ SessionTimeoutException (session timed out; not yet removed)
\_ ShutdownInProgress      (session on this server will most likely be destroyed)

However, in addition to [Ice::LocalException] subclasses, the Ice runtime also
defines subclasses of [Ice::UserException]. In some cases, OMERO subclasses
from these exceptions. The subclasses shown below are not exhaustive, but show those
which an application's exception handler may want to deal with.

Ice::Exception (root of all Ice exceptions)
|
|_ Ice::UserException (super class of all application exceptions)
|  |
|  |_ Glacier2::CannotCreateSessionException (1 of 2 exceptions throwable by createSession)
|  |   |_ omero::AuthenticationException (bad login)
|  |   |_ omero::ExpiredCredentialException (old password)
|  |   |_ omero::WrappedCreateSessionException (any other server error during createSession)
|  |   \_ omero::licenses::NoAvailableLicensesException (see tools/licenses/resources/omero/LicensesAPI.ice)
|  |
|  \_ Glacier2::PermissionDeniedException (other of 2 exceptions throwable by createSession)
|
\_ Ice::LocalException (should generally be considered fatal. See exceptions below)
|
|_ Ice::ProtocolException (something went wrong on the wire. Wrong version?)
|
|_ Ice::RequestFailedException
|   |_ ObjectNotExistException (Service timeout or similar?)
|   \_ OperationNotExistException (Improper use of uncheckedCast?)
|
|_ Ice::UnknownException (server threw an unexpected exception. Bug!)
|
\_ Ice::TimeoutException
\_ Ice::ConnectTimeoutException (Couldn't establish a connection. Retry?)'''

if not _M_omero.__dict__.has_key('ServerError'):
    _M_omero.ServerError = Ice.createTempClass()
    class ServerError(Ice.UserException):
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            self.serverStackTrace = serverStackTrace
            self.serverExceptionClass = serverExceptionClass
            self.message = message

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::ServerError'

    _M_omero._t_ServerError = IcePy.defineException('::omero::ServerError', ServerError, (), None, (
        ('serverStackTrace', (), IcePy._t_string),
        ('serverExceptionClass', (), IcePy._t_string),
        ('message', (), IcePy._t_string)
    ))
    ServerError._ice_type = _M_omero._t_ServerError

    _M_omero.ServerError = ServerError
    del ServerError

if not _M_omero.__dict__.has_key('SessionException'):
    _M_omero.SessionException = Ice.createTempClass()
    class SessionException(_M_omero.ServerError):
        '''Base session exception, though in the OMERO.blitz
implementation, all exceptions thrown by the Glacier2
must subclass CannotCreateSessionException. See below.'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.ServerError.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::SessionException'

    _M_omero._t_SessionException = IcePy.defineException('::omero::SessionException', SessionException, (), _M_omero._t_ServerError, ())
    SessionException._ice_type = _M_omero._t_SessionException

    _M_omero.SessionException = SessionException
    del SessionException

if not _M_omero.__dict__.has_key('RemovedSessionException'):
    _M_omero.RemovedSessionException = Ice.createTempClass()
    class RemovedSessionException(_M_omero.SessionException):
        '''Session has been removed. Either it was closed, or it
timed out and one "SessionTimeoutException" has already
been thrown.'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.SessionException.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::RemovedSessionException'

    _M_omero._t_RemovedSessionException = IcePy.defineException('::omero::RemovedSessionException', RemovedSessionException, (), _M_omero._t_SessionException, ())
    RemovedSessionException._ice_type = _M_omero._t_RemovedSessionException

    _M_omero.RemovedSessionException = RemovedSessionException
    del RemovedSessionException

if not _M_omero.__dict__.has_key('SessionTimeoutException'):
    _M_omero.SessionTimeoutException = Ice.createTempClass()
    class SessionTimeoutException(_M_omero.SessionException):
        '''Session has timed out and will be removed.'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.SessionException.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::SessionTimeoutException'

    _M_omero._t_SessionTimeoutException = IcePy.defineException('::omero::SessionTimeoutException', SessionTimeoutException, (), _M_omero._t_SessionException, ())
    SessionTimeoutException._ice_type = _M_omero._t_SessionTimeoutException

    _M_omero.SessionTimeoutException = SessionTimeoutException
    del SessionTimeoutException

if not _M_omero.__dict__.has_key('ShutdownInProgress'):
    _M_omero.ShutdownInProgress = Ice.createTempClass()
    class ShutdownInProgress(_M_omero.SessionException):
        '''Server is in the progress of shutting down which will
typically lead to the current session being closed.'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.SessionException.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::ShutdownInProgress'

    _M_omero._t_ShutdownInProgress = IcePy.defineException('::omero::ShutdownInProgress', ShutdownInProgress, (), _M_omero._t_SessionException, ())
    ShutdownInProgress._ice_type = _M_omero._t_ShutdownInProgress

    _M_omero.ShutdownInProgress = ShutdownInProgress
    del ShutdownInProgress

if not _M_omero.__dict__.has_key('AuthenticationException'):
    _M_omero.AuthenticationException = Ice.createTempClass()
    class AuthenticationException(_M_Glacier2.CannotCreateSessionException):
        '''Thrown when the information provided omero.createSession() or more
specifically Glacier2.RouterPrx.createSession() is incorrect. This
does -not- subclass from the omero.ServerError class because the
Ice Glacier2::SessionManager interface can only throw CCSEs.'''
        def __init__(self, reason=''):
            _M_Glacier2.CannotCreateSessionException.__init__(self, reason)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::AuthenticationException'

    _M_omero._t_AuthenticationException = IcePy.defineException('::omero::AuthenticationException', AuthenticationException, (), _M_Glacier2._t_CannotCreateSessionException, ())
    AuthenticationException._ice_type = _M_omero._t_AuthenticationException

    _M_omero.AuthenticationException = AuthenticationException
    del AuthenticationException

if not _M_omero.__dict__.has_key('ExpiredCredentialException'):
    _M_omero.ExpiredCredentialException = Ice.createTempClass()
    class ExpiredCredentialException(_M_Glacier2.CannotCreateSessionException):
        '''Thrown when the password for a user has expried. Use: ISession.changeExpiredCredentials()
and login as guest. This does -not- subclass from the omero.ServerError class because the
Ice Glacier2::SessionManager interface can only throw CCSEs.'''
        def __init__(self, reason=''):
            _M_Glacier2.CannotCreateSessionException.__init__(self, reason)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::ExpiredCredentialException'

    _M_omero._t_ExpiredCredentialException = IcePy.defineException('::omero::ExpiredCredentialException', ExpiredCredentialException, (), _M_Glacier2._t_CannotCreateSessionException, ())
    ExpiredCredentialException._ice_type = _M_omero._t_ExpiredCredentialException

    _M_omero.ExpiredCredentialException = ExpiredCredentialException
    del ExpiredCredentialException

if not _M_omero.__dict__.has_key('WrappedCreateSessionException'):
    _M_omero.WrappedCreateSessionException = Ice.createTempClass()
    class WrappedCreateSessionException(_M_Glacier2.CannotCreateSessionException):
        '''Thrown when any other server exception causes the session creation to fail.
Since working with the static information of Ice exceptions is not as easy
as with classes, here we use booleans to represent what has gone wrong.'''
        def __init__(self, reason='', concurrency=False, backOff=0, type=''):
            _M_Glacier2.CannotCreateSessionException.__init__(self, reason)
            self.concurrency = concurrency
            self.backOff = backOff
            self.type = type

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::WrappedCreateSessionException'

    _M_omero._t_WrappedCreateSessionException = IcePy.defineException('::omero::WrappedCreateSessionException', WrappedCreateSessionException, (), _M_Glacier2._t_CannotCreateSessionException, (
        ('concurrency', (), IcePy._t_bool),
        ('backOff', (), IcePy._t_long),
        ('type', (), IcePy._t_string)
    ))
    WrappedCreateSessionException._ice_type = _M_omero._t_WrappedCreateSessionException

    _M_omero.WrappedCreateSessionException = WrappedCreateSessionException
    del WrappedCreateSessionException

if not _M_omero.__dict__.has_key('InternalException'):
    _M_omero.InternalException = Ice.createTempClass()
    class InternalException(_M_omero.ServerError):
        '''Programmer error. Ideally should not be thrown.'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.ServerError.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::InternalException'

    _M_omero._t_InternalException = IcePy.defineException('::omero::InternalException', InternalException, (), _M_omero._t_ServerError, ())
    InternalException._ice_type = _M_omero._t_InternalException

    _M_omero.InternalException = InternalException
    del InternalException

if not _M_omero.__dict__.has_key('ResourceError'):
    _M_omero.ResourceError = Ice.createTempClass()
    class ResourceError(_M_omero.ServerError):
        '''Unrecoverable error. The resource being accessed is not available.'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.ServerError.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::ResourceError'

    _M_omero._t_ResourceError = IcePy.defineException('::omero::ResourceError', ResourceError, (), _M_omero._t_ServerError, ())
    ResourceError._ice_type = _M_omero._t_ResourceError

    _M_omero.ResourceError = ResourceError
    del ResourceError

if not _M_omero.__dict__.has_key('NoProcessorAvailable'):
    _M_omero.NoProcessorAvailable = Ice.createTempClass()
    class NoProcessorAvailable(_M_omero.ResourceError):
        '''A script cannot be executed because no matching processor
was found.'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message='', processorCount=0):
            _M_omero.ResourceError.__init__(self, serverStackTrace, serverExceptionClass, message)
            self.processorCount = processorCount

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::NoProcessorAvailable'

    _M_omero._t_NoProcessorAvailable = IcePy.defineException('::omero::NoProcessorAvailable', NoProcessorAvailable, (), _M_omero._t_ResourceError, (('processorCount', (), IcePy._t_int),))
    NoProcessorAvailable._ice_type = _M_omero._t_NoProcessorAvailable

    _M_omero.NoProcessorAvailable = NoProcessorAvailable
    del NoProcessorAvailable

if not _M_omero.__dict__.has_key('ConcurrencyException'):
    _M_omero.ConcurrencyException = Ice.createTempClass()
    class ConcurrencyException(_M_omero.ServerError):
        '''Recoverable error caused by simultaneous access of some form.'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message='', backOff=0):
            _M_omero.ServerError.__init__(self, serverStackTrace, serverExceptionClass, message)
            self.backOff = backOff

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::ConcurrencyException'

    _M_omero._t_ConcurrencyException = IcePy.defineException('::omero::ConcurrencyException', ConcurrencyException, (), _M_omero._t_ServerError, (('backOff', (), IcePy._t_long),))
    ConcurrencyException._ice_type = _M_omero._t_ConcurrencyException

    _M_omero.ConcurrencyException = ConcurrencyException
    del ConcurrencyException

if not _M_omero.__dict__.has_key('ConcurrentModification'):
    _M_omero.ConcurrentModification = Ice.createTempClass()
    class ConcurrentModification(_M_omero.ConcurrencyException):
        '''Currently unused.'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message='', backOff=0):
            _M_omero.ConcurrencyException.__init__(self, serverStackTrace, serverExceptionClass, message, backOff)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::ConcurrentModification'

    _M_omero._t_ConcurrentModification = IcePy.defineException('::omero::ConcurrentModification', ConcurrentModification, (), _M_omero._t_ConcurrencyException, ())
    ConcurrentModification._ice_type = _M_omero._t_ConcurrentModification

    _M_omero.ConcurrentModification = ConcurrentModification
    del ConcurrentModification

if not _M_omero.__dict__.has_key('DatabaseBusyException'):
    _M_omero.DatabaseBusyException = Ice.createTempClass()
    class DatabaseBusyException(_M_omero.ConcurrencyException):
        '''Too many simultaneous database users. This implies that a
connection to the database could not be acquired, no data
was saved or modifed. Clients may want to wait the given
backOff period, and retry.'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message='', backOff=0):
            _M_omero.ConcurrencyException.__init__(self, serverStackTrace, serverExceptionClass, message, backOff)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::DatabaseBusyException'

    _M_omero._t_DatabaseBusyException = IcePy.defineException('::omero::DatabaseBusyException', DatabaseBusyException, (), _M_omero._t_ConcurrencyException, ())
    DatabaseBusyException._ice_type = _M_omero._t_DatabaseBusyException

    _M_omero.DatabaseBusyException = DatabaseBusyException
    del DatabaseBusyException

if not _M_omero.__dict__.has_key('OptimisticLockException'):
    _M_omero.OptimisticLockException = Ice.createTempClass()
    class OptimisticLockException(_M_omero.ConcurrencyException):
        '''Conflicting changes to the same piece of data.'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message='', backOff=0):
            _M_omero.ConcurrencyException.__init__(self, serverStackTrace, serverExceptionClass, message, backOff)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::OptimisticLockException'

    _M_omero._t_OptimisticLockException = IcePy.defineException('::omero::OptimisticLockException', OptimisticLockException, (), _M_omero._t_ConcurrencyException, ())
    OptimisticLockException._ice_type = _M_omero._t_OptimisticLockException

    _M_omero.OptimisticLockException = OptimisticLockException
    del OptimisticLockException

if not _M_omero.__dict__.has_key('LockTimeout'):
    _M_omero.LockTimeout = Ice.createTempClass()
    class LockTimeout(_M_omero.ConcurrencyException):
        '''Lock cannot be acquired and has timed out.'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message='', backOff=0, seconds=0):
            _M_omero.ConcurrencyException.__init__(self, serverStackTrace, serverExceptionClass, message, backOff)
            self.seconds = seconds

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::LockTimeout'

    _M_omero._t_LockTimeout = IcePy.defineException('::omero::LockTimeout', LockTimeout, (), _M_omero._t_ConcurrencyException, (('seconds', (), IcePy._t_int),))
    LockTimeout._ice_type = _M_omero._t_LockTimeout

    _M_omero.LockTimeout = LockTimeout
    del LockTimeout

if not _M_omero.__dict__.has_key('TryAgain'):
    _M_omero.TryAgain = Ice.createTempClass()
    class TryAgain(_M_omero.ConcurrencyException):
        '''Background processing needed before server is ready'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message='', backOff=0):
            _M_omero.ConcurrencyException.__init__(self, serverStackTrace, serverExceptionClass, message, backOff)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::TryAgain'

    _M_omero._t_TryAgain = IcePy.defineException('::omero::TryAgain', TryAgain, (), _M_omero._t_ConcurrencyException, ())
    TryAgain._ice_type = _M_omero._t_TryAgain

    _M_omero.TryAgain = TryAgain
    del TryAgain

if not _M_omero.__dict__.has_key('MissingPyramidException'):
    _M_omero.MissingPyramidException = Ice.createTempClass()
    class MissingPyramidException(_M_omero.ConcurrencyException):
        def __init__(self, serverStackTrace='', serverExceptionClass='', message='', backOff=0, pixelsID=0):
            _M_omero.ConcurrencyException.__init__(self, serverStackTrace, serverExceptionClass, message, backOff)
            self.pixelsID = pixelsID

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::MissingPyramidException'

    _M_omero._t_MissingPyramidException = IcePy.defineException('::omero::MissingPyramidException', MissingPyramidException, (), _M_omero._t_ConcurrencyException, (('pixelsID', (), IcePy._t_long),))
    MissingPyramidException._ice_type = _M_omero._t_MissingPyramidException

    _M_omero.MissingPyramidException = MissingPyramidException
    del MissingPyramidException

if not _M_omero.__dict__.has_key('ApiUsageException'):
    _M_omero.ApiUsageException = Ice.createTempClass()
    class ApiUsageException(_M_omero.ServerError):
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.ServerError.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::ApiUsageException'

    _M_omero._t_ApiUsageException = IcePy.defineException('::omero::ApiUsageException', ApiUsageException, (), _M_omero._t_ServerError, ())
    ApiUsageException._ice_type = _M_omero._t_ApiUsageException

    _M_omero.ApiUsageException = ApiUsageException
    del ApiUsageException

if not _M_omero.__dict__.has_key('OverUsageException'):
    _M_omero.OverUsageException = Ice.createTempClass()
    class OverUsageException(_M_omero.ApiUsageException):
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.ApiUsageException.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::OverUsageException'

    _M_omero._t_OverUsageException = IcePy.defineException('::omero::OverUsageException', OverUsageException, (), _M_omero._t_ApiUsageException, ())
    OverUsageException._ice_type = _M_omero._t_OverUsageException

    _M_omero.OverUsageException = OverUsageException
    del OverUsageException

if not _M_omero.__dict__.has_key('QueryException'):
    _M_omero.QueryException = Ice.createTempClass()
    class QueryException(_M_omero.ApiUsageException):
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.ApiUsageException.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::QueryException'

    _M_omero._t_QueryException = IcePy.defineException('::omero::QueryException', QueryException, (), _M_omero._t_ApiUsageException, ())
    QueryException._ice_type = _M_omero._t_QueryException

    _M_omero.QueryException = QueryException
    del QueryException

if not _M_omero.__dict__.has_key('ValidationException'):
    _M_omero.ValidationException = Ice.createTempClass()
    class ValidationException(_M_omero.ApiUsageException):
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.ApiUsageException.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::ValidationException'

    _M_omero._t_ValidationException = IcePy.defineException('::omero::ValidationException', ValidationException, (), _M_omero._t_ApiUsageException, ())
    ValidationException._ice_type = _M_omero._t_ValidationException

    _M_omero.ValidationException = ValidationException
    del ValidationException

if not _M_omero.__dict__.has_key('ChecksumValidationException'):
    _M_omero.ChecksumValidationException = Ice.createTempClass()
    class ChecksumValidationException(_M_omero.ValidationException):
        def __init__(self, serverStackTrace='', serverExceptionClass='', message='', failingChecksums=None):
            _M_omero.ValidationException.__init__(self, serverStackTrace, serverExceptionClass, message)
            self.failingChecksums = failingChecksums

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::ChecksumValidationException'

    _M_omero._t_ChecksumValidationException = IcePy.defineException('::omero::ChecksumValidationException', ChecksumValidationException, (), _M_omero._t_ValidationException, (('failingChecksums', (), _M_omero.api._t_IntStringMap),))
    ChecksumValidationException._ice_type = _M_omero._t_ChecksumValidationException

    _M_omero.ChecksumValidationException = ChecksumValidationException
    del ChecksumValidationException

if not _M_omero.__dict__.has_key('FilePathNamingException'):
    _M_omero.FilePathNamingException = Ice.createTempClass()
    class FilePathNamingException(_M_omero.ValidationException):
        def __init__(self, serverStackTrace='', serverExceptionClass='', message='', illegalFilePath='', illegalCodePoints=None, illegalPrefixes=None, illegalSuffixes=None, illegalNames=None):
            _M_omero.ValidationException.__init__(self, serverStackTrace, serverExceptionClass, message)
            self.illegalFilePath = illegalFilePath
            self.illegalCodePoints = illegalCodePoints
            self.illegalPrefixes = illegalPrefixes
            self.illegalSuffixes = illegalSuffixes
            self.illegalNames = illegalNames

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::FilePathNamingException'

    _M_omero._t_FilePathNamingException = IcePy.defineException('::omero::FilePathNamingException', FilePathNamingException, (), _M_omero._t_ValidationException, (
        ('illegalFilePath', (), IcePy._t_string),
        ('illegalCodePoints', (), _M_omero.api._t_IntegerList),
        ('illegalPrefixes', (), _M_omero.api._t_StringSet),
        ('illegalSuffixes', (), _M_omero.api._t_StringSet),
        ('illegalNames', (), _M_omero.api._t_StringSet)
    ))
    FilePathNamingException._ice_type = _M_omero._t_FilePathNamingException

    _M_omero.FilePathNamingException = FilePathNamingException
    del FilePathNamingException

if not _M_omero.__dict__.has_key('SecurityViolation'):
    _M_omero.SecurityViolation = Ice.createTempClass()
    class SecurityViolation(_M_omero.ServerError):
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.ServerError.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::SecurityViolation'

    _M_omero._t_SecurityViolation = IcePy.defineException('::omero::SecurityViolation', SecurityViolation, (), _M_omero._t_ServerError, ())
    SecurityViolation._ice_type = _M_omero._t_SecurityViolation

    _M_omero.SecurityViolation = SecurityViolation
    del SecurityViolation

if not _M_omero.__dict__.has_key('GroupSecurityViolation'):
    _M_omero.GroupSecurityViolation = Ice.createTempClass()
    class GroupSecurityViolation(_M_omero.SecurityViolation):
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.SecurityViolation.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::GroupSecurityViolation'

    _M_omero._t_GroupSecurityViolation = IcePy.defineException('::omero::GroupSecurityViolation', GroupSecurityViolation, (), _M_omero._t_SecurityViolation, ())
    GroupSecurityViolation._ice_type = _M_omero._t_GroupSecurityViolation

    _M_omero.GroupSecurityViolation = GroupSecurityViolation
    del GroupSecurityViolation

if not _M_omero.__dict__.has_key('PermissionMismatchGroupSecurityViolation'):
    _M_omero.PermissionMismatchGroupSecurityViolation = Ice.createTempClass()
    class PermissionMismatchGroupSecurityViolation(_M_omero.SecurityViolation):
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.SecurityViolation.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::PermissionMismatchGroupSecurityViolation'

    _M_omero._t_PermissionMismatchGroupSecurityViolation = IcePy.defineException('::omero::PermissionMismatchGroupSecurityViolation', PermissionMismatchGroupSecurityViolation, (), _M_omero._t_SecurityViolation, ())
    PermissionMismatchGroupSecurityViolation._ice_type = _M_omero._t_PermissionMismatchGroupSecurityViolation

    _M_omero.PermissionMismatchGroupSecurityViolation = PermissionMismatchGroupSecurityViolation
    del PermissionMismatchGroupSecurityViolation

if not _M_omero.__dict__.has_key('ReadOnlyGroupSecurityViolation'):
    _M_omero.ReadOnlyGroupSecurityViolation = Ice.createTempClass()
    class ReadOnlyGroupSecurityViolation(_M_omero.SecurityViolation):
        def __init__(self, serverStackTrace='', serverExceptionClass='', message=''):
            _M_omero.SecurityViolation.__init__(self, serverStackTrace, serverExceptionClass, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::ReadOnlyGroupSecurityViolation'

    _M_omero._t_ReadOnlyGroupSecurityViolation = IcePy.defineException('::omero::ReadOnlyGroupSecurityViolation', ReadOnlyGroupSecurityViolation, (), _M_omero._t_SecurityViolation, ())
    ReadOnlyGroupSecurityViolation._ice_type = _M_omero._t_ReadOnlyGroupSecurityViolation

    _M_omero.ReadOnlyGroupSecurityViolation = ReadOnlyGroupSecurityViolation
    del ReadOnlyGroupSecurityViolation

if not _M_omero.__dict__.has_key('OmeroFSError'):
    _M_omero.OmeroFSError = Ice.createTempClass()
    class OmeroFSError(_M_omero.ServerError):
        '''OmeroFSError

Just one catch-all UserException for the present. It could be
subclassed to provide a finer grained level if necessary.

It should be fitted into or subsumed within the above hierarchy'''
        def __init__(self, serverStackTrace='', serverExceptionClass='', message='', reason=''):
            _M_omero.ServerError.__init__(self, serverStackTrace, serverExceptionClass, message)
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'omero::OmeroFSError'

    _M_omero._t_OmeroFSError = IcePy.defineException('::omero::OmeroFSError', OmeroFSError, (), _M_omero._t_ServerError, (('reason', (), IcePy._t_string),))
    OmeroFSError._ice_type = _M_omero._t_OmeroFSError

    _M_omero.OmeroFSError = OmeroFSError
    del OmeroFSError

# End of module omero
