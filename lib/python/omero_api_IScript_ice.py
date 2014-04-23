# **********************************************************************
#
# Copyright (c) 2003-2013 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.5.1
#
# <auto-generated>
#
# Generated from file `IScript.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy
import omero_ServicesF_ice
import omero_Scripts_ice

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

# Included module omero.grid
_M_omero.grid = Ice.openModule('omero.grid')

# Start of module omero
__name__ = 'omero'

# Start of module omero.api
__name__ = 'omero.api'

if 'IScript' not in _M_omero.api.__dict__:
    _M_omero.api.IScript = Ice.createTempClass()
    class IScript(_M_omero.api.ServiceInterface):
        '''Utility service for managing and launching scripts for execution by the Processor API.

Typical usage might include (PYTHON):

sf = client.createSession()
svc = sf.getScriptService()
scripts = svc.getScripts()

if len(scripts) >= 1:
script_id = svc.keys()[0]
else:
script_id = svc.uploadScript('/test/my_script.py', SCRIPT_TEXT)

params = svc.getParams(script_id)

# You will need to parse the params to create the proper input
inputs = {}

# The last parameter is how long to wait as an RInt
proc = svc.runScript(script_id, inputs, None)
try:
cb = omero.scripts.ProcessCallbackI(client, proc)
while not cb.block(1000): # ms.
pass
cb.close()
rv = proc.getResults(0)
finally:
proc.close(False)

See OMERO.scripts for more information.'''
        def __init__(self):
            if Ice.getType(self) == _M_omero.api.IScript:
                raise RuntimeError('omero.api.IScript is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::api::IScript', '::omero::api::ServiceInterface')

        def ice_id(self, current=None):
            return '::omero::api::IScript'

        def ice_staticId():
            return '::omero::api::IScript'
        ice_staticId = staticmethod(ice_staticId)

        def getScripts_async(self, _cb, current=None):
            '''This method returns official server scripts as a list of [omero::model::OriginalFile] objects.
These scripts will be executed by the server if submitted via [runScript]. The input parameters
necessary for proper functioning can be retrieved via [getParams].

The [omero::model::OriginalFil::path] value can be used in other official scripts via the
language specific import command, since the script directory will be placed on the appropriate
environment path variable.

scripts = scriptService.getScripts()
for script in scripts:
text = scriptService.getScriptText(script.id.val)
path = script.path.val[1:] # First symbol is a "/"
path = path.replace("/",".")
print "Possible import: %s" % path

Returns:
    see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
            pass

        def getUserScripts_async(self, _cb, acceptsList, current=None):
            '''Returns non-official scripts which have been uploaded by individual users.
These scripts will not be run by the server, though a user can
start a personal "usermode processor" which will allow the scripts to be
executed. This is particularly useful for testing new scripts.'''
            pass

        def getScriptID_async(self, _cb, path, current=None):
            '''Get the id of an official script by the script path.
The script service ensures that all script paths are unique.

Note: there is no similar method for user scripts (e.g. getUserScriptID)
since the path is not guaranteed to be unique.

Arguments:
    scriptName The name of the script.
Returns:
    see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
            pass

        def getScriptText_async(self, _cb, scriptID, current=None):
            '''Get the text from the server for the script with given id.

Arguments:
    scriptID see above.
Returns:
    see above.
Exceptions:
    ApiUsageException'''
            pass

        def uploadScript_async(self, _cb, path, scriptText, current=None):
            '''Upload a user script to the server and return the id. This method checks that
a script with that names does not exist and that the script has parameters
if possible, i.e. a usermode processor is running which for the
current user.

Arguments:
    script see above.
Returns:
    The new id of the script.
Exceptions:
    ApiUsageException
    SecurityViolation'''
            pass

        def uploadOfficialScript_async(self, _cb, path, scriptText, current=None):
            '''Like [uploadScript] but is only callable by administrators. The parameters
for the script are also checked.'''
            pass

        def editScript_async(self, _cb, fileObject, scriptText, current=None):
            '''Modify the text for the given script object.

Arguments:
    script see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
            pass

        def getScriptWithDetails_async(self, _cb, scriptID, current=None):
            '''Get the script from the server with details from OriginalFile
Arguments:
    scriptID see above
Returns:
    see above
Exceptions:
    ApiUsageException'''
            pass

        def getParams_async(self, _cb, scriptID, current=None):
            '''Get the parameters that the script takes and returns, along with
other metadata available from the script.

Arguments:
    scriptID see above.
Returns:
    see above.
Exceptions:
    ApiUsageException'''
            pass

        def deleteScript_async(self, _cb, scriptID, current=None):
            '''Delete the script on the server with id. The file will also be removed from disk.

Arguments:
    scriptID Id of the script to delete.
Exceptions:
    ApiUsageException
    SecurityViolation'''
            pass

        def runScript_async(self, _cb, scriptID, inputs, waitSecs, current=None):
            '''If [ResourceError] is thrown, then no [Processor] is available. Use [scheduleJob]
to create a [omero::model::ScriptJob] in the "Waiting" state. A [Processor] may
become available.

try:
proc = scriptService.runScript(1, {}, None)
except ResourceError:
job = scriptService.scheduleScript(1, {}, None)

The [ScriptProcess] proxy MUST be closed before exiting.
If you would like the script execution to continue in the
background, pass "True" as the argument.

try:
proc.poll()         # See if process is finished
finally:
proc.close(True)    # Detach and execution can continue
# proc.close(False) # OR script is immediately stopped.'''
            pass

        def canRunScript_async(self, _cb, scriptID, current=None):
            '''Returns true if there is a processor which will run the given script.

Either the script is an official script and this method will return true
(though an individual invocation may fail with an [omero::ResourceError]
for some reason) or this is a user script, and a usermode processor
must be active which takes the scripts user or group.'''
            pass

        def validateScript_async(self, _cb, j, acceptsList, current=None):
            '''Used internally by processor.py to check if the script attached to the [omero::model::Job]
has a valid script attached, based on the [acceptsList] and the current security context.

An example of an acceptsList might be Experimenter(myUserId, False), meaning that
only scripts belonging to me should be trusted. An empty list implies that the server should
return what it would by default trust.

A valid script will be returned if it exists; otherwise null.'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.api._t_IScript)

        __repr__ = __str__

    _M_omero.api.IScriptPrx = Ice.createTempClass()
    class IScriptPrx(_M_omero.api.ServiceInterfacePrx):

        '''This method returns official server scripts as a list of [omero::model::OriginalFile] objects.
These scripts will be executed by the server if submitted via [runScript]. The input parameters
necessary for proper functioning can be retrieved via [getParams].

The [omero::model::OriginalFil::path] value can be used in other official scripts via the
language specific import command, since the script directory will be placed on the appropriate
environment path variable.

scripts = scriptService.getScripts()
for script in scripts:
text = scriptService.getScriptText(script.id.val)
path = script.path.val[1:] # First symbol is a "/"
path = path.replace("/",".")
print "Possible import: %s" % path

Returns:
    see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def getScripts(self, _ctx=None):
            return _M_omero.api.IScript._op_getScripts.invoke(self, ((), _ctx))

        '''This method returns official server scripts as a list of [omero::model::OriginalFile] objects.
These scripts will be executed by the server if submitted via [runScript]. The input parameters
necessary for proper functioning can be retrieved via [getParams].

The [omero::model::OriginalFil::path] value can be used in other official scripts via the
language specific import command, since the script directory will be placed on the appropriate
environment path variable.

scripts = scriptService.getScripts()
for script in scripts:
text = scriptService.getScriptText(script.id.val)
path = script.path.val[1:] # First symbol is a "/"
path = path.replace("/",".")
print "Possible import: %s" % path

Returns:
    see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def begin_getScripts(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_getScripts.begin(self, ((), _response, _ex, _sent, _ctx))

        '''This method returns official server scripts as a list of [omero::model::OriginalFile] objects.
These scripts will be executed by the server if submitted via [runScript]. The input parameters
necessary for proper functioning can be retrieved via [getParams].

The [omero::model::OriginalFil::path] value can be used in other official scripts via the
language specific import command, since the script directory will be placed on the appropriate
environment path variable.

scripts = scriptService.getScripts()
for script in scripts:
text = scriptService.getScriptText(script.id.val)
path = script.path.val[1:] # First symbol is a "/"
path = path.replace("/",".")
print "Possible import: %s" % path

Returns:
    see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def end_getScripts(self, _r):
            return _M_omero.api.IScript._op_getScripts.end(self, _r)

        '''This method returns official server scripts as a list of [omero::model::OriginalFile] objects.
These scripts will be executed by the server if submitted via [runScript]. The input parameters
necessary for proper functioning can be retrieved via [getParams].

The [omero::model::OriginalFil::path] value can be used in other official scripts via the
language specific import command, since the script directory will be placed on the appropriate
environment path variable.

scripts = scriptService.getScripts()
for script in scripts:
text = scriptService.getScriptText(script.id.val)
path = script.path.val[1:] # First symbol is a "/"
path = path.replace("/",".")
print "Possible import: %s" % path

Returns:
    see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def getScripts_async(self, _cb, _ctx=None):
            return _M_omero.api.IScript._op_getScripts.invokeAsync(self, (_cb, (), _ctx))

        '''Returns non-official scripts which have been uploaded by individual users.
These scripts will not be run by the server, though a user can
start a personal "usermode processor" which will allow the scripts to be
executed. This is particularly useful for testing new scripts.'''
        def getUserScripts(self, acceptsList, _ctx=None):
            return _M_omero.api.IScript._op_getUserScripts.invoke(self, ((acceptsList, ), _ctx))

        '''Returns non-official scripts which have been uploaded by individual users.
These scripts will not be run by the server, though a user can
start a personal "usermode processor" which will allow the scripts to be
executed. This is particularly useful for testing new scripts.'''
        def begin_getUserScripts(self, acceptsList, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_getUserScripts.begin(self, ((acceptsList, ), _response, _ex, _sent, _ctx))

        '''Returns non-official scripts which have been uploaded by individual users.
These scripts will not be run by the server, though a user can
start a personal "usermode processor" which will allow the scripts to be
executed. This is particularly useful for testing new scripts.'''
        def end_getUserScripts(self, _r):
            return _M_omero.api.IScript._op_getUserScripts.end(self, _r)

        '''Returns non-official scripts which have been uploaded by individual users.
These scripts will not be run by the server, though a user can
start a personal "usermode processor" which will allow the scripts to be
executed. This is particularly useful for testing new scripts.'''
        def getUserScripts_async(self, _cb, acceptsList, _ctx=None):
            return _M_omero.api.IScript._op_getUserScripts.invokeAsync(self, (_cb, (acceptsList, ), _ctx))

        '''Get the id of an official script by the script path.
The script service ensures that all script paths are unique.

Note: there is no similar method for user scripts (e.g. getUserScriptID)
since the path is not guaranteed to be unique.

Arguments:
    scriptName The name of the script.
Returns:
    see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def getScriptID(self, path, _ctx=None):
            return _M_omero.api.IScript._op_getScriptID.invoke(self, ((path, ), _ctx))

        '''Get the id of an official script by the script path.
The script service ensures that all script paths are unique.

Note: there is no similar method for user scripts (e.g. getUserScriptID)
since the path is not guaranteed to be unique.

Arguments:
    scriptName The name of the script.
Returns:
    see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def begin_getScriptID(self, path, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_getScriptID.begin(self, ((path, ), _response, _ex, _sent, _ctx))

        '''Get the id of an official script by the script path.
The script service ensures that all script paths are unique.

Note: there is no similar method for user scripts (e.g. getUserScriptID)
since the path is not guaranteed to be unique.

Arguments:
    scriptName The name of the script.
Returns:
    see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def end_getScriptID(self, _r):
            return _M_omero.api.IScript._op_getScriptID.end(self, _r)

        '''Get the id of an official script by the script path.
The script service ensures that all script paths are unique.

Note: there is no similar method for user scripts (e.g. getUserScriptID)
since the path is not guaranteed to be unique.

Arguments:
    scriptName The name of the script.
Returns:
    see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def getScriptID_async(self, _cb, path, _ctx=None):
            return _M_omero.api.IScript._op_getScriptID.invokeAsync(self, (_cb, (path, ), _ctx))

        '''Get the text from the server for the script with given id.

Arguments:
    scriptID see above.
Returns:
    see above.
Exceptions:
    ApiUsageException'''
        def getScriptText(self, scriptID, _ctx=None):
            return _M_omero.api.IScript._op_getScriptText.invoke(self, ((scriptID, ), _ctx))

        '''Get the text from the server for the script with given id.

Arguments:
    scriptID see above.
Returns:
    see above.
Exceptions:
    ApiUsageException'''
        def begin_getScriptText(self, scriptID, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_getScriptText.begin(self, ((scriptID, ), _response, _ex, _sent, _ctx))

        '''Get the text from the server for the script with given id.

Arguments:
    scriptID see above.
Returns:
    see above.
Exceptions:
    ApiUsageException'''
        def end_getScriptText(self, _r):
            return _M_omero.api.IScript._op_getScriptText.end(self, _r)

        '''Get the text from the server for the script with given id.

Arguments:
    scriptID see above.
Returns:
    see above.
Exceptions:
    ApiUsageException'''
        def getScriptText_async(self, _cb, scriptID, _ctx=None):
            return _M_omero.api.IScript._op_getScriptText.invokeAsync(self, (_cb, (scriptID, ), _ctx))

        '''Upload a user script to the server and return the id. This method checks that
a script with that names does not exist and that the script has parameters
if possible, i.e. a usermode processor is running which for the
current user.

Arguments:
    script see above.
Returns:
    The new id of the script.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def uploadScript(self, path, scriptText, _ctx=None):
            return _M_omero.api.IScript._op_uploadScript.invoke(self, ((path, scriptText), _ctx))

        '''Upload a user script to the server and return the id. This method checks that
a script with that names does not exist and that the script has parameters
if possible, i.e. a usermode processor is running which for the
current user.

Arguments:
    script see above.
Returns:
    The new id of the script.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def begin_uploadScript(self, path, scriptText, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_uploadScript.begin(self, ((path, scriptText), _response, _ex, _sent, _ctx))

        '''Upload a user script to the server and return the id. This method checks that
a script with that names does not exist and that the script has parameters
if possible, i.e. a usermode processor is running which for the
current user.

Arguments:
    script see above.
Returns:
    The new id of the script.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def end_uploadScript(self, _r):
            return _M_omero.api.IScript._op_uploadScript.end(self, _r)

        '''Upload a user script to the server and return the id. This method checks that
a script with that names does not exist and that the script has parameters
if possible, i.e. a usermode processor is running which for the
current user.

Arguments:
    script see above.
Returns:
    The new id of the script.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def uploadScript_async(self, _cb, path, scriptText, _ctx=None):
            return _M_omero.api.IScript._op_uploadScript.invokeAsync(self, (_cb, (path, scriptText), _ctx))

        '''Like [uploadScript] but is only callable by administrators. The parameters
for the script are also checked.'''
        def uploadOfficialScript(self, path, scriptText, _ctx=None):
            return _M_omero.api.IScript._op_uploadOfficialScript.invoke(self, ((path, scriptText), _ctx))

        '''Like [uploadScript] but is only callable by administrators. The parameters
for the script are also checked.'''
        def begin_uploadOfficialScript(self, path, scriptText, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_uploadOfficialScript.begin(self, ((path, scriptText), _response, _ex, _sent, _ctx))

        '''Like [uploadScript] but is only callable by administrators. The parameters
for the script are also checked.'''
        def end_uploadOfficialScript(self, _r):
            return _M_omero.api.IScript._op_uploadOfficialScript.end(self, _r)

        '''Like [uploadScript] but is only callable by administrators. The parameters
for the script are also checked.'''
        def uploadOfficialScript_async(self, _cb, path, scriptText, _ctx=None):
            return _M_omero.api.IScript._op_uploadOfficialScript.invokeAsync(self, (_cb, (path, scriptText), _ctx))

        '''Modify the text for the given script object.

Arguments:
    script see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def editScript(self, fileObject, scriptText, _ctx=None):
            return _M_omero.api.IScript._op_editScript.invoke(self, ((fileObject, scriptText), _ctx))

        '''Modify the text for the given script object.

Arguments:
    script see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def begin_editScript(self, fileObject, scriptText, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_editScript.begin(self, ((fileObject, scriptText), _response, _ex, _sent, _ctx))

        '''Modify the text for the given script object.

Arguments:
    script see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def end_editScript(self, _r):
            return _M_omero.api.IScript._op_editScript.end(self, _r)

        '''Modify the text for the given script object.

Arguments:
    script see above.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def editScript_async(self, _cb, fileObject, scriptText, _ctx=None):
            return _M_omero.api.IScript._op_editScript.invokeAsync(self, (_cb, (fileObject, scriptText), _ctx))

        '''Get the script from the server with details from OriginalFile
Arguments:
    scriptID see above
Returns:
    see above
Exceptions:
    ApiUsageException'''
        def getScriptWithDetails(self, scriptID, _ctx=None):
            return _M_omero.api.IScript._op_getScriptWithDetails.invoke(self, ((scriptID, ), _ctx))

        '''Get the script from the server with details from OriginalFile
Arguments:
    scriptID see above
Returns:
    see above
Exceptions:
    ApiUsageException'''
        def begin_getScriptWithDetails(self, scriptID, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_getScriptWithDetails.begin(self, ((scriptID, ), _response, _ex, _sent, _ctx))

        '''Get the script from the server with details from OriginalFile
Arguments:
    scriptID see above
Returns:
    see above
Exceptions:
    ApiUsageException'''
        def end_getScriptWithDetails(self, _r):
            return _M_omero.api.IScript._op_getScriptWithDetails.end(self, _r)

        '''Get the script from the server with details from OriginalFile
Arguments:
    scriptID see above
Returns:
    see above
Exceptions:
    ApiUsageException'''
        def getScriptWithDetails_async(self, _cb, scriptID, _ctx=None):
            return _M_omero.api.IScript._op_getScriptWithDetails.invokeAsync(self, (_cb, (scriptID, ), _ctx))

        '''Get the parameters that the script takes and returns, along with
other metadata available from the script.

Arguments:
    scriptID see above.
Returns:
    see above.
Exceptions:
    ApiUsageException'''
        def getParams(self, scriptID, _ctx=None):
            return _M_omero.api.IScript._op_getParams.invoke(self, ((scriptID, ), _ctx))

        '''Get the parameters that the script takes and returns, along with
other metadata available from the script.

Arguments:
    scriptID see above.
Returns:
    see above.
Exceptions:
    ApiUsageException'''
        def begin_getParams(self, scriptID, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_getParams.begin(self, ((scriptID, ), _response, _ex, _sent, _ctx))

        '''Get the parameters that the script takes and returns, along with
other metadata available from the script.

Arguments:
    scriptID see above.
Returns:
    see above.
Exceptions:
    ApiUsageException'''
        def end_getParams(self, _r):
            return _M_omero.api.IScript._op_getParams.end(self, _r)

        '''Get the parameters that the script takes and returns, along with
other metadata available from the script.

Arguments:
    scriptID see above.
Returns:
    see above.
Exceptions:
    ApiUsageException'''
        def getParams_async(self, _cb, scriptID, _ctx=None):
            return _M_omero.api.IScript._op_getParams.invokeAsync(self, (_cb, (scriptID, ), _ctx))

        '''Delete the script on the server with id. The file will also be removed from disk.

Arguments:
    scriptID Id of the script to delete.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def deleteScript(self, scriptID, _ctx=None):
            return _M_omero.api.IScript._op_deleteScript.invoke(self, ((scriptID, ), _ctx))

        '''Delete the script on the server with id. The file will also be removed from disk.

Arguments:
    scriptID Id of the script to delete.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def begin_deleteScript(self, scriptID, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_deleteScript.begin(self, ((scriptID, ), _response, _ex, _sent, _ctx))

        '''Delete the script on the server with id. The file will also be removed from disk.

Arguments:
    scriptID Id of the script to delete.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def end_deleteScript(self, _r):
            return _M_omero.api.IScript._op_deleteScript.end(self, _r)

        '''Delete the script on the server with id. The file will also be removed from disk.

Arguments:
    scriptID Id of the script to delete.
Exceptions:
    ApiUsageException
    SecurityViolation'''
        def deleteScript_async(self, _cb, scriptID, _ctx=None):
            return _M_omero.api.IScript._op_deleteScript.invokeAsync(self, (_cb, (scriptID, ), _ctx))

        '''If [ResourceError] is thrown, then no [Processor] is available. Use [scheduleJob]
to create a [omero::model::ScriptJob] in the "Waiting" state. A [Processor] may
become available.

try:
proc = scriptService.runScript(1, {}, None)
except ResourceError:
job = scriptService.scheduleScript(1, {}, None)

The [ScriptProcess] proxy MUST be closed before exiting.
If you would like the script execution to continue in the
background, pass "True" as the argument.

try:
proc.poll()         # See if process is finished
finally:
proc.close(True)    # Detach and execution can continue
# proc.close(False) # OR script is immediately stopped.'''
        def runScript(self, scriptID, inputs, waitSecs, _ctx=None):
            return _M_omero.api.IScript._op_runScript.invoke(self, ((scriptID, inputs, waitSecs), _ctx))

        '''If [ResourceError] is thrown, then no [Processor] is available. Use [scheduleJob]
to create a [omero::model::ScriptJob] in the "Waiting" state. A [Processor] may
become available.

try:
proc = scriptService.runScript(1, {}, None)
except ResourceError:
job = scriptService.scheduleScript(1, {}, None)

The [ScriptProcess] proxy MUST be closed before exiting.
If you would like the script execution to continue in the
background, pass "True" as the argument.

try:
proc.poll()         # See if process is finished
finally:
proc.close(True)    # Detach and execution can continue
# proc.close(False) # OR script is immediately stopped.'''
        def begin_runScript(self, scriptID, inputs, waitSecs, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_runScript.begin(self, ((scriptID, inputs, waitSecs), _response, _ex, _sent, _ctx))

        '''If [ResourceError] is thrown, then no [Processor] is available. Use [scheduleJob]
to create a [omero::model::ScriptJob] in the "Waiting" state. A [Processor] may
become available.

try:
proc = scriptService.runScript(1, {}, None)
except ResourceError:
job = scriptService.scheduleScript(1, {}, None)

The [ScriptProcess] proxy MUST be closed before exiting.
If you would like the script execution to continue in the
background, pass "True" as the argument.

try:
proc.poll()         # See if process is finished
finally:
proc.close(True)    # Detach and execution can continue
# proc.close(False) # OR script is immediately stopped.'''
        def end_runScript(self, _r):
            return _M_omero.api.IScript._op_runScript.end(self, _r)

        '''If [ResourceError] is thrown, then no [Processor] is available. Use [scheduleJob]
to create a [omero::model::ScriptJob] in the "Waiting" state. A [Processor] may
become available.

try:
proc = scriptService.runScript(1, {}, None)
except ResourceError:
job = scriptService.scheduleScript(1, {}, None)

The [ScriptProcess] proxy MUST be closed before exiting.
If you would like the script execution to continue in the
background, pass "True" as the argument.

try:
proc.poll()         # See if process is finished
finally:
proc.close(True)    # Detach and execution can continue
# proc.close(False) # OR script is immediately stopped.'''
        def runScript_async(self, _cb, scriptID, inputs, waitSecs, _ctx=None):
            return _M_omero.api.IScript._op_runScript.invokeAsync(self, (_cb, (scriptID, inputs, waitSecs), _ctx))

        '''Returns true if there is a processor which will run the given script.

Either the script is an official script and this method will return true
(though an individual invocation may fail with an [omero::ResourceError]
for some reason) or this is a user script, and a usermode processor
must be active which takes the scripts user or group.'''
        def canRunScript(self, scriptID, _ctx=None):
            return _M_omero.api.IScript._op_canRunScript.invoke(self, ((scriptID, ), _ctx))

        '''Returns true if there is a processor which will run the given script.

Either the script is an official script and this method will return true
(though an individual invocation may fail with an [omero::ResourceError]
for some reason) or this is a user script, and a usermode processor
must be active which takes the scripts user or group.'''
        def begin_canRunScript(self, scriptID, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_canRunScript.begin(self, ((scriptID, ), _response, _ex, _sent, _ctx))

        '''Returns true if there is a processor which will run the given script.

Either the script is an official script and this method will return true
(though an individual invocation may fail with an [omero::ResourceError]
for some reason) or this is a user script, and a usermode processor
must be active which takes the scripts user or group.'''
        def end_canRunScript(self, _r):
            return _M_omero.api.IScript._op_canRunScript.end(self, _r)

        '''Returns true if there is a processor which will run the given script.

Either the script is an official script and this method will return true
(though an individual invocation may fail with an [omero::ResourceError]
for some reason) or this is a user script, and a usermode processor
must be active which takes the scripts user or group.'''
        def canRunScript_async(self, _cb, scriptID, _ctx=None):
            return _M_omero.api.IScript._op_canRunScript.invokeAsync(self, (_cb, (scriptID, ), _ctx))

        '''Used internally by processor.py to check if the script attached to the [omero::model::Job]
has a valid script attached, based on the [acceptsList] and the current security context.

An example of an acceptsList might be Experimenter(myUserId, False), meaning that
only scripts belonging to me should be trusted. An empty list implies that the server should
return what it would by default trust.

A valid script will be returned if it exists; otherwise null.'''
        def validateScript(self, j, acceptsList, _ctx=None):
            return _M_omero.api.IScript._op_validateScript.invoke(self, ((j, acceptsList), _ctx))

        '''Used internally by processor.py to check if the script attached to the [omero::model::Job]
has a valid script attached, based on the [acceptsList] and the current security context.

An example of an acceptsList might be Experimenter(myUserId, False), meaning that
only scripts belonging to me should be trusted. An empty list implies that the server should
return what it would by default trust.

A valid script will be returned if it exists; otherwise null.'''
        def begin_validateScript(self, j, acceptsList, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IScript._op_validateScript.begin(self, ((j, acceptsList), _response, _ex, _sent, _ctx))

        '''Used internally by processor.py to check if the script attached to the [omero::model::Job]
has a valid script attached, based on the [acceptsList] and the current security context.

An example of an acceptsList might be Experimenter(myUserId, False), meaning that
only scripts belonging to me should be trusted. An empty list implies that the server should
return what it would by default trust.

A valid script will be returned if it exists; otherwise null.'''
        def end_validateScript(self, _r):
            return _M_omero.api.IScript._op_validateScript.end(self, _r)

        '''Used internally by processor.py to check if the script attached to the [omero::model::Job]
has a valid script attached, based on the [acceptsList] and the current security context.

An example of an acceptsList might be Experimenter(myUserId, False), meaning that
only scripts belonging to me should be trusted. An empty list implies that the server should
return what it would by default trust.

A valid script will be returned if it exists; otherwise null.'''
        def validateScript_async(self, _cb, j, acceptsList, _ctx=None):
            return _M_omero.api.IScript._op_validateScript.invokeAsync(self, (_cb, (j, acceptsList), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.api.IScriptPrx.ice_checkedCast(proxy, '::omero::api::IScript', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.api.IScriptPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.api._t_IScriptPrx = IcePy.defineProxy('::omero::api::IScript', IScriptPrx)

    _M_omero.api._t_IScript = IcePy.defineClass('::omero::api::IScript', IScript, -1, (), True, False, None, (_M_omero.api._t_ServiceInterface,), ())
    IScript._ice_type = _M_omero.api._t_IScript

    IScript._op_getScripts = IcePy.Operation('getScripts', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (), (), ((), _M_omero.api._t_OriginalFileList, False, 0), (_M_omero._t_ServerError,))
    IScript._op_getUserScripts = IcePy.Operation('getUserScripts', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (((), _M_omero.api._t_IObjectList, False, 0),), (), ((), _M_omero.api._t_OriginalFileList, False, 0), (_M_omero._t_ServerError,))
    IScript._op_getScriptID = IcePy.Operation('getScriptID', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_long, False, 0), (_M_omero._t_ServerError,))
    IScript._op_getScriptText = IcePy.Operation('getScriptText', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (((), IcePy._t_long, False, 0),), (), ((), IcePy._t_string, False, 0), (_M_omero._t_ServerError,))
    IScript._op_uploadScript = IcePy.Operation('uploadScript', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), IcePy._t_long, False, 0), (_M_omero._t_ServerError,))
    IScript._op_uploadOfficialScript = IcePy.Operation('uploadOfficialScript', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), IcePy._t_long, False, 0), (_M_omero._t_ServerError,))
    IScript._op_editScript = IcePy.Operation('editScript', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_omero.model._t_OriginalFile, False, 0), ((), IcePy._t_string, False, 0)), (), None, (_M_omero._t_ServerError,))
    IScript._op_getScriptWithDetails = IcePy.Operation('getScriptWithDetails', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (((), IcePy._t_long, False, 0),), (), ((), _M_omero._t_RTypeDict, False, 0), (_M_omero._t_ServerError,))
    IScript._op_getParams = IcePy.Operation('getParams', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (((), IcePy._t_long, False, 0),), (), ((), _M_omero.grid._t_JobParams, False, 0), (_M_omero._t_ServerError,))
    IScript._op_deleteScript = IcePy.Operation('deleteScript', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_long, False, 0),), (), None, (_M_omero._t_ServerError,))
    IScript._op_runScript = IcePy.Operation('runScript', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_long, False, 0), ((), _M_omero._t_RTypeDict, False, 0), ((), _M_omero._t_RInt, False, 0)), (), ((), _M_omero.grid._t_ScriptProcessPrx, False, 0), (_M_omero._t_ServerError,))
    IScript._op_canRunScript = IcePy.Operation('canRunScript', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_long, False, 0),), (), ((), IcePy._t_bool, False, 0), (_M_omero._t_ServerError,))
    IScript._op_validateScript = IcePy.Operation('validateScript', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_omero.model._t_Job, False, 0), ((), _M_omero.api._t_IObjectList, False, 0)), (), ((), _M_omero.model._t_OriginalFile, False, 0), (_M_omero._t_ServerError,))

    _M_omero.api.IScript = IScript
    del IScript

    _M_omero.api.IScriptPrx = IScriptPrx
    del IScriptPrx

# End of module omero.api

__name__ = 'omero'

# End of module omero
