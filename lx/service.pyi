from typeing import Tuple

from . import object


class AudioAnim(object):
    def Audio(self):
        """Audio object = Audio()"""
        ...

    def End(self):
        """float = End()"""
        ...

    def Item(self):
        """Item object = Item()"""
        ...

    def ItemAudio(self, obj):
        """Unknown object = ItemAudio(object obj)"""
        ...

    def ItemSample(self, obj, loop, time, type, value):
        """ItemSample(object obj,integer loop,float time,integer type,pointer value)"""
        ...

    def Loop(self):
        """integer = Loop()"""
        ...

    def Mute(self):
        """integer = Mute()"""
        ...

    def Playing(self):
        """integer = Playing()"""
        ...

    def Preview(self, startTime, endTime):
        """Audio object = Preview(float startTime,float endTime)"""
        ...

    def Sample(self, time, type, value):
        """Sample(float time,integer type,data[] value)"""
        ...

    def Scrub(self):
        """integer = Scrub()"""
        ...

    def Start(self):
        """float = Start()"""
        ...



class Cache(object):
    def GetData(self, name, key):
        """Unknown object = GetData(string name,integer key)"""
        ...

    def PurgeData(self, name):
        """PurgeData(string name)"""
        ...

    def Register(self, name):
        """Register(string name)"""
        ...

    def Release(self, name):
        """Release(string name)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def SetData(self, name, key, data):
        """SetData(string name,integer key,object data)"""
        ...



class ChannelUI(object):
    def ChannelDescription(self, item, channel):
        """string desc = ChannelDescription(object item,integer channel)"""
        ...

    def ChannelToolTip(self, item, channel):
        """string tip = ChannelToolTip(object item,integer channel)"""
        ...

    def ChannelUserName(self, item, channel):
        """string = ChannelUserName(object item,integer channel)"""
        ...

    def ItemTypeDesc(self, typeID, useSuper):
        """string name = ItemTypeDesc(integer typeID,integer useSuper)"""
        ...

    def ItemTypeIconText(self, typeID, useSuper):
        """string = ItemTypeIconText(integer typeID,integer useSuper)"""
        ...

    def ItemTypeName(self, typeID, useSuper):
        """string name = ItemTypeName(integer typeID,integer useSuper)"""
        ...

    def MeshMapUserName(self, name, addIcon):
        """string = MeshMapUserName(string name,integer addIcon)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...



class ColorMapping(object):
    def ConfigCount(self):
        """integer = ConfigCount()"""
        ...

    def ConfigFullPath(self, index):
        """string configPath = ConfigFullPath(integer index)"""
        ...

    def ConfigName(self, index):
        """string configName = ConfigName(integer index)"""
        ...

    def GetDisplayColorMapping(self):
        """ColorMapping object = GetDisplayColorMapping()"""
        ...

    def GetNumericColorMapping(self):
        """ColorMapping object = GetNumericColorMapping()"""
        ...

    def MakeColorMapping(self, colorspaceName, toLinear):
        """ColorMapping object = MakeColorMapping(string colorspaceName,integer toLinear)"""
        ...

    def RegisterColorspaceForConfig(self, configName, colorspaceName):
        """RegisterColorspaceForConfig(string configName,string colorspaceName)"""
        ...



class Command(object):
    def ScriptQuery(self) -> object.Unknown:
        """Unknown object = ScriptQuery()"""
        ...

    def MasterStatus(self) -> int:
        """integer status = MasterStatus()"""
        ...

    def GetNameSep(self) -> int:
        """integer sep = GetNameSep()"""
        ...

    def SetNameSep(self, sep: int):
        """SetNameSep(integer sep)"""
        ...

    def Proto(self, tag: int, name: str) -> object.Command:
        """ This returns the ILxCommand interface of the prototype command, thus allowing basic
        non-editable data to be read out, such as the command's name, tag and attributes.
        The object must be released when no longer needed.  Note that it is legal to pass
        in a full command argument string with name, and only the part up to the first space
        will be treated as a name (the arguments are ignored).

        Command object = Proto(integer tag,string name)

        """
        ...

    def ProtoFromCommand(self, cmd: object.Command):
        """ This returns the prototype of a command from an alreadly instanced one.

        Command object = ProtoFromCommand(object cmd)"""
        ...

    def Lookup(self, name: str) -> int:
        """ Should you want to, this returns a command's tag, which can be used to create an
        instance of a command instead of using its name.

        integer tag = Lookup(string name)"""
        ...

    def Spawn(self, tag: int, name: str) -> object.Unknown:
        """ This spawns a new command object given its name or tag, which means it creates
        a fully functional command object whose args can be set for firing and querying.
        The object needs to be released with XObjectRelease() when no longer needed.

        Command object = Spawn(integer tag,string name)"""
        ...

    def SpawnFromCommand(self, cmd: object.Unknown) -> object.Command:
        """ This spawns a new command object given another command object.  Note that the spawned
        command will include any aliasing that was applied, even if the original command was
        create with SpawnUnaliased().

        Command object = SpawnFromCommand(object cmd)"""
        ...

    def SpawnFromString(self, args: str) -> (int, int, object.Command):
        """ This super-wrapper spawns a command from an argument string and sets all the arguments
        found.  It will also return the index of the query argument, if one was set in the
        argument string; the query argument will be -1 if no query argument is set.

        Also, execution flags passed in will be modified based on the leading characters of the
        command string (!, +, ?, etc).  Note that the execFlags should be iniitalized to some
        useful execution flags, such as LXfCMD_EXEC_DEFAULT, as this will also be used to present
        parsing errors.

        Once the command has been spawned in this way, it is ready for execution or querying.

        (integer execFlags,integer queryArgIndex,Command object) = SpawnFromString(string args)"""
        ...

    def ExecuteArgString(self, execFlags: int, tag: int, args: str):
        """ This is a high-level function that parses arguments and fires the command all in
        one go.  If the tag is CTAG_NULL, it is assumed that the command name begins the
        argument string.

        If the tag is CTAG_NULL, then there are some special characters that can be used
        to modify the execution state.  These flags are insereted at the very beginning of
        the arugment string, before the command name.

        A single exclamation point "!" can be used to turn off the SHOWERR and GETARGS
        flags for this command only.  An opposite effect can be achieved by using a
        single leading plus "+".  This adds SHOWERR and GETARGS to the command.

        Note that the above only affect this specific command.  All sub-commands can be
        affected be using double exclamation points "!!" or double pluses "++" where
        appropriate.  These will add SHOWERR_FORCESUB_OFF and GETARGS_FORCESUB_OFF or
        SHOWERR_FORCESUB and GETARGS_FORCESUB to the execFlags.

        This function also handles special UI-level behaviors.  For example, if a
        required argument is missing, the command dialog will open.  Similarly, if
        a query operator is specified for an argument, it will be applied.  This
        includes using a question mark by itself on an argument that can be
        represented by a popup, thereby forcing it to open a menu at the current
        mouse position, or in the case of a boolean argument, causing it toggle it
        on or off.

        ExecuteArgString(integer execFlags,integer tag,string args)"""
        ...

    def ExecuteToggleArgString(self, execFlags: int, tag: int, args: str, newState: int):
        """ Similar, but also allows a toggle arg to be flipped.  -1 can be used to invert
        the current state.

        ExecuteToggleArgString(integer execFlags, integer tag, string args, integer newState)"""
        ...

    def IsToggleArgString(self, string: str) -> bool:
        """ This processes a command string (name and args) and returns LXe_TRUE if it is
        a toggle arg command, and LXe_FALSE if not.  If true, this means the command
        can be executed with ExecuteToggleArgString() to toggle argument.

        boolean = IsToggleArgString(string string)"""
        ...

    def IsBooleanArgString(self, string: str) -> bool:
        """ Commands with queried boolean arguments can also be somewhat tedious to test,
        toggle and execute, especially considering the multiple ways that a boolean
        argument can be specified.  This function takes a command string, and if
        the boolean argument contains any query operators (including a question mark
        alone), this returns true.

        boolean = IsBooleanArgString(string string)"""
        ...

    def ExecuteBooleanArgString(self, execFlags: int, tag: int, args: str):
        """ This allows the boolean argument's value to be easily changed to an alternate
        state.  As above, the boolean argument is expected to be marked with a query
        operator, and the argument's value will be toggled based on the argument's
        currently queried value before being executed..

        ExecuteBooleanArgString(integer execFlags,integer tag,string args)"""
        ...

    def ExecuteSpecial(self, execFlags: int, cmd: object.Command, specialArgIndex: int):
        """ This executes a command object, but also takes a special argument index.  If the
        index is not -1, then special behaviors specific to that argument may be taken
        (i.e., opening a popup), or the command may be executed normal or a command dialog
        may appear as normal. This same behavior is taken automatically when executing
        a command from a string using ExecuteArgString().

        ExecuteSpecial(integer execFlags,object cmd,integer specialArgIndex)"""
        ...

    def ExecuteAttribObject(self, execFlags: int, tag: int, cmdName: str, attribArgs: object.Attributes):
        """ Finally, we support using an ILxAttributes interface to provide the arguments to
        the command.  The Name(), Count(), Value(), GetString(), GetInt() and GetFloat()
        arguments are used, but the Type() argument is not used.

        It works like this: First the Count() and Name() methods are called to see which
        argument this is.  Then one of Value(), GetInt(), GetFloat() or GetString() is
        called depending on the datatype of the argument (note that the Type() method is
        not usd).  If the method fails, the GetString() method is used as an encoded
        string.  If that fails, then the execution fails.

        ExecuteAttribObject(integer execFlags,integer tag,string cmdName,object attribArgs)"""
        ...

    def ProcessStringFlags(self, flags: int, string: str) -> (int, str):
        """ This function can be used to parse the special prefix characters mentioned above
        out the string, and combine them with other execution flags.  This is useful when
        you are directly creating an ILxCommand object from a user-entered string.
        The function takes the original execution and/or alert flags and the source string.
        It returns new flags and a pointer to the first character after the flags characters
        in the source string.  Either newFlags or afterFlags may be NULL if desired.

        (integer newFlags,string afterFlags) = ProcessStringFlags(integer flags,string string)"""
        ...

    def ExecFlagsAsPrefixString(self, flags: int) -> str:
        """ This inverse function takes the exec flags and converts them back into a prefix
        string.

        string = ExecFlagsAsPrefixString(integer flags)"""
        ...

    def SetToggleArgState(self, cmd: object.Command, state: int):
        """ These functions makes it easy to flip the toggle of a Toggle Argument command,
        and to tell if the state is on or off.  1 is on, 0 is off, and -1 inverts the
        current state.

        SetToggleArgState(object cmd,integer state)"""
        ...

    def GetToggleArgState(self, cmd: object.Command) -> (int, object.Value):
        """ When getting the value, both a simple on/off state and the current value of the
        arg can be provided, or either can be NULL.

        (integer state,Value object) = GetToggleArgState(object cmd)"""
        ...

    def IsImplicitScript(self, definition: str) -> bool:
        """ Scripts can be more easily executed using this function.  Before looking up any
        commands, this should be called to see if it starts with the script marker (the @
        symbol).  Note that the definition string should include entire command like, not
        just the @ and script name; if If it does, the next function will create the
        implicit script command and and set the script name and arg string arguments
        automatically.  Scripts cannot be queried, so the command returned is only useful
        for execution.  The command can otherwise be treated a a normal command object
        after it is created.

        See if the command is an implicit script execution.

        boolean = IsImplicitScript(string definition)"""
        ...

    def SpawnImplicitScript(self, definition: str) -> object.Command:
        """ Spawn a command to launch the script.  This "definition" string should include any
        arguments to pass to the script.

        Command object = SpawnImplicitScript(string definition)"""
        ...

    def ExecuteImplicitScript(self, definition: str, execFlags: int):
        """ Execute an implicit script directly.

        ExecuteImplicitScript(string definition,integer execFlags)"""
        ...

    def RefireBegin(self):
        """ Some commands are fired many times over and over again as the user changes a
        value.  An example of this is the the Move Tool; each time the users drags
        the mouse, the Move Tool fires a new AddPosition (or whatever) command.  This
        clutters up the command histroy quite a bit.  Instead, the Move Tool should
        fire the AddPosition command effectively once with the final value, thus
        resulting in a single entry in the command history.
        This process has been dubbed "Refiring".  On mouse down, a tool calls
        CmdRefireBegin(), and on mouse up calls CmdRefireEnd().  In between it
        fires commands using CmdEntryFireArgs() or CmdEntryFireTag() to fire
        a command.  When a command is refired, the previous execution is undone
        just before the command is re-executed.

        Each successive time CmdEntryFire...() is called within a refire block,
        the previously fired command is undone.

            IT IS REQUIRED THAT THE COMMAND BEING FIRED IS UNDOABLE!

        Large annoying requesters will pop up if you try to use any non-undoable
        commands.

        Only a single command can be executed inside a refire block, although that
        command may execute others.  Attempting to execute more than one will cause
        those later commands to fail.  If you need to fire multiple commands, you
        can wrap them in a command block via BlockBegin()/BlockEnd(), in which case
        the name of the block is used to identify it.  RefireBegin() does not nest,
        and cannot be called while any commands are executing.  It will return false
        if a previous RefireBegin() hasn't been ended yet via RefireEnd() or if it
        is called while any command is being executed.

        Beginning refiring can take a tag, name or an ILxCommandID if you have one
        handy.

        RefireBegin()"""
        ...

    def RefireEnd(self):
        """RefireEnd()"""
        ...

    def RefireState(self) -> int:
        """integer state = RefireState()"""
        ...

    def RefireCmd(self) -> object.Command:
        """Command object = RefireCmd()"""
        ...

    def RefireBlock(self) -> str:
        """string name = RefireBlock()"""
        ...

    def PostModeBegin(self, cmd: object.Command, tag: int, name: str, args: str, postEndObj: object.Unknown):
        """ The being and end functions.  In begin, any of cmd, tag or args can be provided.
        If all are NULL, it is assumed that the command name prefixes the arguments.
        Otherwise, the argument list is optional.

        PostModeBegin(object cmd,integer tag,string name,string args,object postEndObj)"""
        ...

    def PostModeEnd(self):
        """PostModeEnd()"""
        ...

    def PostModeState(self):
        """ This fetches the current post-mode state (i.e., on or off).

        PostModeState()"""
        ...

    def PostModeRestart(self):
        """ This resets all undoable states since the PostModeBegin() call.  An example
        usage is ToolRefluxRestart() in tools.qq.

        PostModeRestart()"""
        ...

    def CurrentExecDepth(self) -> int:
        """ This returns the current command execution depth.  -1 means no commands are
        currently executing.  This information is useful in rare situations.  Note
        that this count includes both commands and command blocks.

        integer depth = CurrentExecDepth()"""
        ...

    def BlockBegin(self, name: str, flags: int):
        """ It is sometimes desirable to have multiple commands executed as a single
        undoable event.  This can be done by creating command blocks.  Blocks can
        be nested as needed.  Each block can be given a name that will be sent in
        the block create event and undo data and be displayed in the command history.
        Block names should be localized, and can take the form of "@table@message@"

        - PRESERVE_SELECTION
        The PRESERVE_SELECTION flag will keep a copy of the entire selection list.
        This copy will be restored after the block is closed.  This allows the command
        to change the selection in any way it wishes without damaging it later.
        - UI
        If present, the block can be triggered during refiring events without
        disrupting them.  This should only be used with commands supporting
        LXfCMD_UI or with side effect commands.

        - UNDO_UI
        If present, the block is expected to contain undoable UI blocks.

        - UNDO_AFTER_EXEC
        If applied to an UNDO (default) or UNDO_UI block, the undo actions are 
        undone on completion.

        - SANDBOXED
        Should be set if the block is in a sandbox.

        - POSTMODE
        Command block is being used as part of a post command execution.

        - STEPUNDO
        Taz, any idea what this is for?

        - TOP_OF_CYCLE_SAFE
        This is a special behavior used only in rare circumstances.  Normally,
        a command block is not allwoed to remain open at the top of the input
        cycle.  This flag allows that condition to be ignored.  This is used by
        tree panes to allow the user to click and drag down a column to change
        a series of checkmarks without releasing the mouse, while having all of
        the commands contained within a single command block.

        BlockBegin(string name,integer flags)"""
        ...

    def BlockEnd(self):
        """ Each block must be closed with this function.  Bad things will happen if you
        miss one so don't forget.

        BlockEnd()"""
        ...

    def SandboxFlags(self) -> int:
        """integer flags = SandboxFlags()"""
        ...

    def SandboxAddObject(self, object: object.Unknown):
        """ This method adds an object to a sandbox.  The object is AddRef()'ed when added, and
        released when the sandbox is destroyed.

        SandboxAddObject(object object)"""
        ...

    def SandboxObjectCount(self) -> int:
        """ A list of objects can be read with these functions.

        integer count = SandboxObjectCount()"""
        ...

    def SandboxObjectByIndex(self, index: int) -> object.Unknown:
        """Unknown object = SandboxObjectByIndex(integer index)"""
        ...

    def SandboxObjectLookup(self, guid: str) -> object.Unknown:
        """ An object can be looked up by the interfaces it supports.  The first object with the
        GUID will be returned, or the method fails.  Since this method caches interface queries,
        it is recommended instead of walking the object list directly.

        Unknown object = SandboxObjectLookup(string guid)"""
        ...

    def SandboxObjectByCommand(self, cmd: object.Command) -> object.Unknown:
        """ More commonly, this method would be used to get the object associated with the command's
        SandboxGUID() method.

        Unknown object = SandboxObjectByCommand(object cmd)"""
        ...

    def SandboxBegin(self, flags: int):
        """ Command sandboxes can be started through this method.  Flags are any combination of
        LXfCMDSANDBOX_ flags, and cannot be changed once the sandbox is created.

        SandboxBegin(integer flags)"""
        ...

    def SandboxState(self):
        """ This method returns LXe_CMD_SANDBOX_GLOBAL if there are no sandboxes on the stack, and
        LXe_CMD_SANDBOXED if there is at least one.  Any other return code is a failure.

        SandboxState()"""
        ...

    def SandboxEnd(self):
        """ When the sandbox is no longer needed, it must be popped off the stack with this method.

        SandboxEnd()"""
        ...

    def ParseArgString(self, cmd: object.Command, alertFlags: int, args: str):
        """ This is similar to CmdEntryFireTag(), and takes a string representing the
        arguments.

        ParseArgString(object cmd,integer alertFlags,string args)"""
        ...

    def ParseAttribObject(self, cmd: object.Command, alertFlags: int, attribArgs: object.Attributes):
        """ParseAttribObject(object cmd,integer alertFlags,object attribArgs)"""
        ...

    def Usage(self, cmd: object.Command) -> str:
        """ This function composes and returns a string describing the arguments of the
        command in a user-readable format.  This string is dynamically generated from
        the command's own argument list, and includes the command name.

        string buffer = Usage(object cmd)"""
        ...

    def ArgsAsString(self, cmd: object.Command, includeCmd: int) -> str:
        """ This function returns the argument list as a string which would result in
        the same arguments for the command if parsed.  This is mainly used for
        recording the command in an executable history.  If includeCmd is true, the
        internal command name will prefix the argument portion.

        string = ArgsAsString(object cmd,integer includeCmd)"""
        ...

    def Query(self, cmd: object.Command, index: int) -> object.ValueArray:
        """ This queries a command for its values, providing a new ILxValueArray that
        must be released by the client.

        ValueArray object = Query(object cmd,integer index)"""
        ...

    def QueryArgString(self, cmd: object.Command, alertFlags: int, args: str, includesCmdName: bool) -> (object.ValueArray, int):
        """ This is similar, but takes an argument string instead of an index.  One argument
        may be marked with a ?, and that one will be queried.  The index of that argument
        can be obtained through the queryIndex argument, or NULL can be passed NULL if you
        don't want it back.  Similarly, the ILxValueArrayID argument can be NULL if only the
        queryIndex itself is desired but not the actual queried values.
        If includesCmdName is true, the first part of the argument string is assumed to
        be the command name and will be skipped.  The alertFlags (LXfCMD_ALERT_ defines)
        are used to decide how to present errors to the user during parsing; passing 0 will
        suppress any error dialogs.

        If successful parsed, the command object provided will be populated with the arguments
        present in the args string.

        (ValueArray object,integer queryIndex) = QueryArgString(object cmd,integer alertFlags,string args,integer includesCmdName)"""
        ...

    def CreateQueryObject(self, typeName: str) -> object.ValueArray:
        """ This creates a new ILxValueArray interface given an ExoType name.

        ValueArray object = CreateQueryObject(string typeName)"""
        ...

    def AliasCreate(self, name: str, targetCmd: object.Command, targetTag: int, targetName: str, args: str):
        """ Commands can be aliased.  This allows one command to replace another, and to create
        shortcut commands that have arguments preset.  Aliases themselves cannot be aliased.
        When creating or deleting aliases, any one of cmd, tag or name may be set.  The
        argument string used during creation will be used to provide default values for the
        command.  The arguments set in the cmd (if provided) are ignored.

        Note that using aliased arguments is only completely supported for commands that
        do not use dynamic datatypes.  The issue is that if the user changes the the
        REQFORVARIABLE argument, the other arguments will need to be reset, thus overriding
        the aliased defaults.  This shouldn't pose any issues in most situations.

        AliasCreate(string name,object targetCmd,integer targetTag,string targetName,string args)"""
        ...

    def AliasDelete(self, alias: object.Unknown, tag: int, name: str):
        """AliasDelete(object alias,integer tag,string name)"""
        ...

    def IsContainer(self, cmd: object.Command) -> bool:
        """ There are currently three types of commands:  normal commands, containers and aliases.
        This functions can be used to tell if the command is a container.

        boolean = IsContainer(object cmd)"""
        ...

    def IsAliased(self, cmd: object.Command) -> bool:
        """ This succeeds if the command is aliased.  Note that a command can be both a container
        and aliased.

        boolean = IsAliased(object cmd)"""
        ...

    def CommandCount(self):
        """ The command list can be walked with these functions, returning the prototype.
        Commands are sorted by internal name.  Note that commands will be loaded from
        plug-ins if necessary as the list is walked.

        integer count = CommandCount()"""
        ...

    def CommandByIndex(self, index: int) -> object.Command:
        """Command object = CommandByIndex(integer index)"""
        ...

    def ExecEntryType(self, index: int) -> int:
        """integer type = ExecEntryType(integer index)"""
        ...

    def ExecEntryUserName(self, index: int) -> str:
        """ The username can be obtained for both commands and blocks.

        string userName = ExecEntryUserName(integer index)"""
        ...

    def ExecEntryName(self, index: int) -> str:
        """string name = ExecEntryName(integer index)"""
        ...

    def ExecEntryAsArgString(self, index: int) -> str:
        """ For commands, an argument string suitable for executing it can be read with
        this function.

        string = ExecEntryAsArgString(integer index)"""
        ...

    def IsGlobalInteractionOK(self) -> bool:
        """ This returns LXe_TRUE if a command is executing and the interaction flags are
        set.  This means that if this returns LXe_FALSE, the client should not open any
        dialogs and instead should perform its default behavior.  The interaction flags
        are often unset when running from a script or when in headless mode, during which
        time modo's own dialogs (such as ILxMessage-based dialogs) will be automatically
        suppressed, acting as though the user had hit cancel/abort/no.  By testing
        IsGlobalInteractionOK(), clients can skip the message and perform a reasonable
        default action instead of failing.

        This method is only intended to be used by non-command clients.  Commands
        themselves should check their exec flags (as passed to the Execute() methods)
        via LXxCMD_IS_USER_INTERACTION_OK() instead.

        boolean = IsGlobalInteractionOK()"""
        ...

    def ArgsAsStringLen(self, cmd: object.Command, includeCmd: int) -> str:
        """ This is identical to ArgsAsString, but is a safer function that takes a buffer
        length to reduce the chance of a buffer overflow.

        ArgAsString() was updated a long time ago to include a len argument, making it
        identical to this function.  Before nexus 12, there was a bug in ArgAsString()
        that kept it from working properly, but as of 12 both are identical.

        Since the "len" argument was added to ArgAsString(), the two functions are now
        completley identical, and are only both maintained to avoid breaking old plug-ins.

        string = ArgsAsStringLen(object cmd,integer includeCmd)"""
        ...

    def SpawnUnaliased(self, tag: int, name: str) -> object.Command:
        """ Commands can be aliased such that they replace an existing command.  This is useful
        when you want an alias to be able to completely replace built-in functionality.
        This method can be used to spawn an instance of the original, unaliased command,
        thus allowing the alias to call the original command's methods.

        Command object = SpawnUnaliased(integer tag,string name)"""
        ...

    def SetIsGlobalInteractionOK(self, isOK: int):
        """ It is sometimes useful to be able to lock out interaction on a global level.
        A common case is Slave mode, where we don't want any dialogs opening as these
        machines are usually unattended.  This state can only be set from within a
        command, and is automatically cleared when the stack is emptied.  It cannot
        be manually cleared if it was not set by the client.

        SetIsGlobalInteractionOK(integer isOK)"""
        ...

    def ExecuteArgString2(self, execFlags: int, tag: int, args: str) -> object.Command:
        """ These functions are identical to their non-'2' counterparts, but will indirectly
        return a COM object representing the command object.  This allows you to read
        post-execution flags and messages from the executed command, without having to
        manually spawn the command, set the argumetns, and do everything else you have
        to do to set up and execute a command manually.

        It's important to note that this object may be NULL if the command could not be
        spawned.  If the object returned is non-NULL, it must be released by the caller
        when no longer needed.

        Command object = ExecuteArgString2(integer execFlags,integer tag,string args)"""
        ...

    def ExecuteToggleArgString2(self, execFlags: int, tag: int, args: str, newState: int) -> object.Command:
        """Command object = ExecuteToggleArgString2(integer execFlags,integer tag,string args,integer newState)"""
        ...

    def ExecuteBooleanArgString2(self, execFlags: int, tag: int, args: str) -> object.Command:
        """Command object = ExecuteBooleanArgString2(integer execFlags,integer tag,string args)"""
        ...

    def ExecuteAttribObject2(self, execFlags: int, tag: int, cmdName: str, attribArgs: object.Attributes) -> object.Command:
        """Command object = ExecuteAttribObject2(integer execFlags,integer tag,string cmdName,object attribArgs)"""
        ...

    def ExecuteImplicitScript2(self, definition: str, execFlags: int) -> object.Command:
        """Command object = ExecuteImplicitScript2(string definition,integer execFlags)"""
        ...

    def AllocateUIHintsFromCommand(self, cmd: object.Command, argIndex: int) -> object.UIHints:
        """ This allocates an ILxUIHints object, has the provided command populate it, and returns it.
        The obejct can be cast to an ILxUIHintsRead interface to read the values of the hints.
        Since a new object is allocated, the returned hints object can also be modified by the
        caller and returned by their own commands if so desired.

        The argument index can be a specific arguments for hints for that argument, or LXiATTRUI_ANY
        for command-level hints, as is common for the form filter priority.

        UIHints object = AllocateUIHintsFromCommand(object cmd,integer argIndex)"""
        ...

    def DoAtEndOfRootLevelUndoableCommand(self, visitor: object.Visitor):
        """ Sometimes a large undoable operation occurs that causes a lot of events to come in,
        and you want to do one undoable operation once everything else is done.  You could
        use ScriptService::DoWhenUserIsIdle(), which is general useful for deferred and lazy
        operations, but if you want to perform an undoable operation you'll have have to fire
        a command, and that means the user will have to do an extra undo to go back, which
        isn't ideal and makes the undos feel broken.

        This method can only be called while an undoable command is being fired, and will
        fail otherwise.  It registers a visitor that will be called after the root-level
        undoable command or block is about to return, but the undo block is still open.
        Calling this method twice with the same object pointer does nothing; the object
        is only registered once.

        DoAtEndOfRootLevelUndoableCommand(object visitor)"""
        ...

    def CancelDoAtEndOfRootLevelUndoableCommand(self, visitor: object.Visitor):
        """ The cancel method can be used to remove the registration, but the object passed
        in must be exactly the same as the one passed for registration, as this does a
        pointer compare.  When doing this from Python, this means that you must pass the
        exact same visitor COM object (not Python object).  This is also necessary when
        removing listeners and canceling timers, as discussed here: http://modo.sdk.thefoundry.co.uk/wiki/FAQ#Q:_How_do_I_remove_a_listener_object_in_Python.3F

        Note that unlike user idle, these functions are not thread-safe.  This is because
        they are usually called in response to listeners from an actively-firing command,
        both of which happen from the main thread.

        If the command is aborted or fails, these actions are not executed, since the
        effects of the operation were all undo and it's as though the operation never
        happened.  This also does nothing if the root command's eventual state wasn't
        either model or model-undoable (UI undos are not supported).

        CancelDoAtEndOfRootLevelUndoableCommand(object visitor)"""
        ...

    def ArgsAsStringWithOptions(self, cmd: object.Command, options: int) -> str:
        """string = ArgsAsStringWithOptions(object cmd,integer options)"""
        ...

    def CurrentExecIsRoot(self, ignoreBlocks: int):
        """CurrentExecIsRoot(integer ignoreBlocks)"""
        ...



class Deformer(object):
    def DeformEltToItem(self, elt):
        """object = DeformEltToItem(id elt)"""
        ...

    def DeformerChannel(self, item):
        """integer index = DeformerChannel(object item)"""
        ...

    def DeformerDeformationItem(self, defItem):
        """item object = DeformerDeformationItem(object defItem)"""
        ...

    def DeformerFlags(self, item):
        """integer flags = DeformerFlags(object item)"""
        ...

    def GroupDeformer(self, dgroup, chanRead):
        """GroupDeformer object = GroupDeformer(object dgroup,object chanRead)"""
        ...

    def InvalidateTargets(self, scene):
        """InvalidateTargets(object scene)"""
        ...

    def ItemToDeformElt(self, item):
        """id = ItemToDeformElt(object item)"""
        ...

    def MergeChangeState(self, c1, c2):
        """MergeChangeState(integer c1,integer c2)"""
        ...

    def MeshByIndex(self, defItem, index):
        """Item object = MeshByIndex(object defItem,integer index)"""
        ...

    def MeshCount(self, defItem):
        """integer count = MeshCount(object defItem)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def StackTargetByIndex(self, defItem, index):
        """Item object = StackTargetByIndex(object defItem,integer index)"""
        ...

    def StackTargetCount(self, defItem):
        """integer count = StackTargetCount(object defItem)"""
        ...



class DirCache(object):
    def AddClient(self):
        """AddClient()"""
        ...

    def ArePathsEqual(self, path1, path2):
        """ArePathsEqual(string path1,string path2)"""
        ...

    def AttributesChanged(self, dirCacheEntry, which, attribute):
        """AttributesChanged(object dirCacheEntry,integer which,string attribute)"""
        ...

    def CachedThumbnailAsyncCancel(self, ident):
        """CachedThumbnailAsyncCancel(string ident)"""
        ...

    def CanBeRenamed(self, path):
        """CanBeRenamed(string path)"""
        ...

    def IsChildOfPath(self, possibleChild, parentToTestAgainsts, orIsSame):
        """IsChildOfPath(string possibleChild,string parentToTestAgainsts,integer orIsSame)"""
        ...

    def Lookup(self, path):
        """DirCacheEntry object = Lookup(string path)"""
        ...

    def MakeDirHierarchy(self, path, skipLastPart):
        """MakeDirHierarchy(string path,integer skipLastPart)"""
        ...

    def MakeUniqueIn(self, object, filename):
        """string = MakeUniqueIn(object object,string filename)"""
        ...

    def ParseName(self, filename, baseName, baseNameLen, path, pathLen):
        """ParseName(string filename,byte[] baseName,integer baseNameLen,byte[] path,integer pathLen)"""
        ...

    def PathCompose(self, filename, filenameLen, baseName, path):
        """PathCompose(byte[] filename,integer filenameLen,string baseName,string path)"""
        ...

    def RemoveClient(self):
        """RemoveClient()"""
        ...

    def RootByIndex(self, index):
        """DirCacheEntry object = RootByIndex(integer index)"""
        ...

    def RootCount(self):
        """integer count = RootCount()"""
        ...

    def RootLock(self):
        """RootLock()"""
        ...

    def RootUnlock(self):
        """RootUnlock()"""
        ...

    def ScanForChanges(self, path):
        """ScanForChanges(string path)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def SetPosOnDrop(self, path, dest):
        """SetPosOnDrop(string path,object dest)"""
        ...

    def ToLocalAlias(self, path):
        """string = ToLocalAlias(byte[] path)"""
        ...



class Drop(object):
    def Action(self):
        """(string serverName,integer actionCode) = Action()"""
        ...

    def Destination(self):
        """Unknown object = Destination()"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def Source(self):
        """(string sourceType,Unknown object) = Source()"""
        ...



class File(object):
    def AllocRedirect(self):
        """FileRedirect object = AllocRedirect()"""
        ...

    def AllocReference(self, path):
        """FileReference object = AllocReference(string path)"""
        ...

    def ArePathsEqual(self, path1, path2):
        """boolean = ArePathsEqual(string path1,string path2)"""
        ...

    def ComposePath(self, basename, path):
        """string = ComposePath(string basename,string path)"""
        ...

    def DirDelete(self, filename):
        """DirDelete(string filename)"""
        ...

    def Execute(self, show, force32):
        """string argv = Execute(integer show,integer force32)"""
        ...

    def FileCopy(self, srcFilePath, dstFilePath, overwrite):
        """FileCopy(string srcFilePath,string dstFilePath,integer overwrite)"""
        ...

    def FileDateString(self, filename):
        """string = FileDateString(string filename)"""
        ...

    def FileDelete(self, filename):
        """FileDelete(string filename)"""
        ...

    def FileFromURL(self, url):
        """string = FileFromURL(string url)"""
        ...

    def FileSystemPath(self, name):
        """string path = FileSystemPath(string name)"""
        ...

    def FileToURL(self, filename):
        """string = FileToURL(string filename)"""
        ...

    def FindSequenceBounds(self, pattern):
        """(integer first,integer last) = FindSequenceBounds(string pattern)"""
        ...

    def FindSequencePattern(self, filename):
        """string = FindSequencePattern(string filename)"""
        ...

    def FromLocal(self, local):
        """string = FromLocal(string local)"""
        ...

    def GenerateSequenceName(self, pattern, frame):
        """string = GenerateSequenceName(string pattern,integer frame)"""
        ...

    def IsAbsolutePath(self, path):
        """boolean = IsAbsolutePath(string path)"""
        ...

    def MakeDirectory(self, path):
        """MakeDirectory(string path)"""
        ...

    def MakeLegalFilename(self, filename, replaceDot):
        """MakeLegalFilename(byte[] filename,integer replaceDot)"""
        ...

    def MakeRelative(self, filename, path):
        """string = MakeRelative(string filename,string path)"""
        ...

    def MakeUnique(self, filename):
        """string = MakeUnique(string filename)"""
        ...

    def OpenFileWithDefaultApp(self, filename):
        """OpenFileWithDefaultApp(string filename)"""
        ...

    def ParsePath(self, filename, component):
        """string = ParsePath(string filename,integer component)"""
        ...

    def PkgCountFiles(self, package):
        """integer = PkgCountFiles(string package)"""
        ...

    def PkgExtract(self, package, file, dest):
        """PkgExtract(string package,string file,string dest)"""
        ...

    def PkgExtractAll(self, package, dest, subDir):
        """PkgExtractAll(string package,string dest,string subDir)"""
        ...

    def PkgFilename(self, package, id):
        """string = PkgFilename(string package,integer id)"""
        ...

    def PkgHasFile(self, package, file):
        """PkgHasFile(string package,string file)"""
        ...

    def RenameFile(self, from_str, to_str):
        """RenameFile(string from_str,string to_str)"""
        ...

    def RevealInFileViewer(self, filename):
        """RevealInFileViewer(string filename)"""
        ...

    def SetExtension(self, filename, extension):
        """string = SetExtension(string filename,string extension)"""
        ...

    def TestFileMode(self, filename):
        """integer mode = TestFileMode(string filename)"""
        ...

    def TestFileType(self, filename):
        """(boolean,integer type) = TestFileType(string filename)"""
        ...

    def ToLocal(self, neutral):
        """string = ToLocal(byte[] neutral)"""
        ...

    def ToLocalAlias(self, neutral):
        """string = ToLocalAlias(string neutral)"""
        ...

    def ValidateLicense(self, product, versionNum):
        """ValidateLicense(string product,integer versionNum)"""
        ...



class GUID(object):
    def Class(self, guid):
        """string = Class(string guid)"""
        ...

    def ClassName(self, guid):
        """string = ClassName(string guid)"""
        ...

    def Compare(self, guid1, guid2):
        """integer = Compare(string guid1,string guid2)"""
        ...

    def Fixed(self, guid):
        """string = Fixed(string guid)"""
        ...

    def GetName(self, guid):
        """string = GetName(string guid)"""
        ...

    def Translate(self, guidStr):
        """string = Translate(string guidStr)"""
        ...



class Host(object):
    def AddServer(self, factory):
        """AddServer(object factory)"""
        ...

    def DefaultPath(self):
        """string path = DefaultPath()"""
        ...

    def LookupServer(self, className, name, allowLoad):
        """Factory object = LookupServer(string className,string name,integer allowLoad)"""
        ...

    def NumServers(self, className):
        """integer = NumServers(string className)"""
        ...

    def SaverSave(self, filename, format, object, monitor):
        """SaverSave(string filename,string format,object object,object monitor)"""
        ...

    def SaverVerify(self, format, object, msg):
        """SaverVerify(string format,object object,object msg)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def ServerByIndex(self, className, index):
        """Factory object = ServerByIndex(string className,integer index)"""
        ...

    def ServerGetIndex(self, className, name):
        """integer index = ServerGetIndex(string className,string name)"""
        ...

    def SpawnForTagsOnly(self):
        """SpawnForTagsOnly()"""
        ...

    def TestServer(self, className, name):
        """boolean = TestServer(string className,string name)"""
        ...

    def UpdateModule(self, name):
        """UpdateModule(string name)"""
        ...



class IO(object):
    def OpenBlockStore(self, filename, format, flags):
        """(boolean,BlockStore object) = OpenBlockStore(string filename,string format,integer flags)"""
        ...

    def PeekOptions(self):
        """object = PeekOptions()"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def SetOptions(self, options):
        """SetOptions(object options)"""
        ...



class Image(object):
    """ Image facilities can be accessed through the SDK using a global service interface. """
    def ScriptQuery(self) -> object.Unknown:
        """Unknown object = ScriptQuery()"""
        ...

    def Create(self, width: int, height: int, type: int, maxIndex: int) -> object.Image:
        """Image object = Create(integer width,integer height,integer type,integer maxIndex)"""
        ...

    def Duplicate(self, source: object.Image, type: int) -> object.Image:
        """ Creates and returns a copy of source image with type defining the pixel format. 

        Image object = Duplicate(object source,integer type)"""
        ...

    def Load(self, filePath: str) -> object.Image:
        """Image object = Load(string filePath)"""
        ...

    def Save(self, image: object.Image, filePath: str, format: str, monitor: object.Monitor):
        """

        >>> image_service = lx.service.Image()
        >>> image = image_service.Create(256, 256, lx.symbol.iIMV_RGB, 0)
        >>> image_write = lx.object.ImageWrite(image)
        >>> color = lx.object.storage("b", image.Format())
        >>> for y in range(256):
        ...     for x in range(256):
		...         color.set((x, y, 0))
        ...         image_write.SetPixel(x, y, image.Format(), color)
        >>> image_service.Save(image, "C:/Users/username/Desktop/gradient.tga", "$Targa", 0)

        Save(object image,string filePath,string format,object monitor)"""
        ...

    def Resample(self, dest: object.Image, source: object.Image, hint: int):
        """ Resamples the image from source to dest with hints being either of following symbols.
        
        lx.symbol.iPROCESS_FAST
        lx.symbol.iPROCESS_MEDIUM
        lx.symbol.iPROCESS_ACCURATE

        Resample(object dest,object source,integer hint)"""
        ...

    def Composite(self, dest: object.Image, source: object.Image, pos: object.storage):
        """Composite(object dest,object source,vector pos)"""
        ...

    def DrawLine(self, image: object.Image, p0: Tuple[int, int], p1: Tuple[int, int], color: object.storage):
        """ DrawLine(object image,vector p0,vector p1,vector color)"""
        ...

    def Kelvin2RGB(self, kelvin: float) -> Tuple[float, float, float]:
        """ Color temperature in kelvin converted to RGB colors as three floats.

        >>> image_service = lx.service.Image()
        >>> image_service.Kelvin2RGB(4500.0)
        (1.0, 0.8742517828941345, 0.5419720411300659)

        vector rgbColor = Kelvin2RGB(float kelvin)"""
        ...

    def RGB2Kelvin(self, rgbColor: Tuple[float, float, float]) -> float:
        """ Color RGB to color temperature in kelvins

        >>> image_service = lx.service.Image()
        >>> image_service.RGB2Kelvin((1.0, 0.9, 0.5))
        4394.7978515625

        float kelvin = RGB2Kelvin(vector rgbColor)"""
        ...

    def CreateCrop(self, sourceImage: object.Image, x: float, y: float, w: float, h: float) -> object.Image:
        """Image object = CreateCrop(object sourceImage,float x,float y,float w,float h)"""
        ...

    def ImageGetBuffer(self, sourceImage: object.Image, type: int, buf: object.storage):
        """ This reads the entire image into a single buffer given the pixel format. This is just
        like Image::GetLine() except that it does all the lines at once.

        ImageGetBuffer(object sourceImage,integer type,data[] buf)"""
        ...

    def LoadNoCache(self, filePath: str) -> object.Image:
        """ Same a Load() but the image is not added to the internal cache. This is useful when
        the image is only needed once (say, because it is being loaded and resized)

        Image object = LoadNoCache(string filePath)"""
        ...

    def CreateLayered(self, width: int, height: int, layerNum: int) -> object.Unknown:
        """Unknown object = CreateLayered(integer width,integer height,integer layerNum)"""
        ...

    def SaveLayered(self, layeredImage: object.LayeredImage, filePath: str, format: str, monitor: object.Monitor):
        """SaveLayered(object layeredImage,string filePath,string format,object monitor)"""
        ...



class ImageMonitor(object):
    def RefreshViews(self, imageSource, immediate):
        """RefreshViews(string imageSource,integer immediate)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def ServerByIndex(self, index):
        """ImageMonitor object = ServerByIndex(integer index)"""
        ...

    def ServerCount(self):
        """integer count = ServerCount()"""
        ...

    def ServerLookup(self, name):
        """ImageMonitor object = ServerLookup(string name)"""
        ...

    def ServerNameByIndex(self, index):
        """string name = ServerNameByIndex(integer index)"""
        ...

    def ServerUserNameByIndex(self, index):
        """string name = ServerUserNameByIndex(integer index)"""
        ...

    def SetImage(self, imageSource, image, frameBuffer, bufferIndex, x1, y1, x2, y2, imageProc, processedThumbnail):
        """SetImage(string imageSource,object image,object frameBuffer,integer bufferIndex,float x1,float y1,float x2,float y2,object imageProc,object processedThumbnail)"""
        ...

    def SourceCount(self):
        """integer count = SourceCount()"""
        ...

    def SourceNameByIndex(self, index):
        """string name = SourceNameByIndex(integer index)"""
        ...

    def SourceUserNameByIndex(self, index):
        """string username = SourceUserNameByIndex(integer index)"""
        ...



class ImageProcessing(object):
    def Create(self):
        """ImageProcessing object = Create()"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...



class InputMap(object):
    def CanEventsCoexist(self, im, event1, event2):
        """CanEventsCoexist(id im,integer event1,integer event2)"""
        ...

    def ContextCount(self):
        """integer count = ContextCount()"""
        ...

    def DefineClientTests(self, tester):
        """DefineClientTests(object tester)"""
        ...

    def DefineCustomEvent(self, event, name, flags):
        """DefineCustomEvent(integer event,string name,integer flags)"""
        ...

    def DefineGroup(self, group):
        """DefineGroup(string group)"""
        ...

    def DefineRegion(self, event, name):
        """DefineRegion(integer event,string name)"""
        ...

    def DefineStandardEvent(self, event, flags):
        """DefineStandardEvent(integer event,integer flags)"""
        ...

    def Desc(self, im):
        """string desc = Desc(id im)"""
        ...

    def EventCount(self, im):
        """integer count = EventCount(id im)"""
        ...

    def EventDesc(self, im, stateName, name, index):
        """string desc = EventDesc(id im,string stateName,string name,integer index)"""
        ...

    def EventFlags(self, im, index):
        """integer flags = EventFlags(id im,integer index)"""
        ...

    def EventHelpURL(self, im, stateName, name, index):
        """string helpURL = EventHelpURL(id im,string stateName,string name,integer index)"""
        ...

    def EventName(self, im, index):
        """string name = EventName(id im,integer index)"""
        ...

    def EventType(self, im, index):
        """integer type = EventType(id im,integer index)"""
        ...

    def EventUserName(self, im, stateName, name, index):
        """string username = EventUserName(id im,string stateName,string name,integer index)"""
        ...

    def FindEvent(self, im, name, type):
        """integer index = FindEvent(id im,string name,integer type)"""
        ...

    def FindRegion(self, im, name, type):
        """integer index = FindRegion(id im,string name,integer type)"""
        ...

    def GetMouseMap(self, im):
        """Unknown object = GetMouseMap(id im)"""
        ...

    def GroupUserName(self, path, depth):
        """string username = GroupUserName(string path,integer depth)"""
        ...

    def HelpURL(self, im):
        """string helpURL = HelpURL(id im)"""
        ...

    def Name(self, im):
        """string name = Name(id im)"""
        ...

    def RefreshContexts(self):
        """RefreshContexts()"""
        ...

    def RefreshStates(self, flags):
        """RefreshStates(integer flags)"""
        ...

    def RegionCount(self, im):
        """integer count = RegionCount(id im)"""
        ...

    def RegionDesc(self, im, stateName, name, index):
        """string desc = RegionDesc(id im,string stateName,string name,integer index)"""
        ...

    def RegionHelpURL(self, im, stateName, name, index):
        """string helpURL = RegionHelpURL(id im,string stateName,string name,integer index)"""
        ...

    def RegionName(self, im, i):
        """string name = RegionName(id im,integer i)"""
        ...

    def RegionType(self, im, i):
        """integer type = RegionType(id im,integer i)"""
        ...

    def RegionUserName(self, im, stateName, name, index):
        """string username = RegionUserName(id im,string stateName,string name,integer index)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def StandardEventFlags(self, event):
        """integer flags = StandardEventFlags(integer event)"""
        ...

    def StandardEventName(self, event):
        """string name = StandardEventName(integer event)"""
        ...

    def StateCatUserName(self, cat):
        """string name = StateCatUserName(string cat)"""
        ...

    def StateCount(self, im):
        """integer count = StateCount(id im)"""
        ...

    def StateUIFallbacksCount(self, stateName):
        """integer count = StateUIFallbacksCount(string stateName)"""
        ...

    def StateUIFallbacksName(self, stateName, index):
        """string name = StateUIFallbacksName(string stateName,integer index)"""
        ...

    def StateUIListCatCount(self):
        """integer count = StateUIListCatCount()"""
        ...

    def StateUIListCatName(self, index):
        """string name = StateUIListCatName(integer index)"""
        ...

    def StateUIListCount(self, cat):
        """integer count = StateUIListCount(string cat)"""
        ...

    def StateUIListName(self, cat, index):
        """string name = StateUIListName(string cat,integer index)"""
        ...

    def StateUITestEvent(self, im, stateName, eventID):
        """StateUITestEvent(id im,string stateName,integer eventID)"""
        ...

    def StateUITestRegion(self, im, stateName, regionID):
        """StateUITestRegion(id im,string stateName,integer regionID)"""
        ...

    def StateUserName(self, state):
        """string name = StateUserName(string state)"""
        ...

    def TestState(self, im, state):
        """integer priority = TestState(id im,string state)"""
        ...

    def UpdateDeviceInstance(self, name):
        """UpdateDeviceInstance(string name)"""
        ...

    def UpdateDeviceList(self):
        """UpdateDeviceList()"""
        ...

    def UserName(self, im):
        """string username = UserName(id im)"""
        ...



class Interviewer(object):
    def Arm(self, serverName, target):
        """Arm(string serverName,integer target)"""
        ...

    def ClearDismissTimer(self, serverName):
        """ClearDismissTimer(string serverName)"""
        ...

    def Disarm(self, serverName, allowRearm):
        """Disarm(string serverName,integer allowRearm)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def WasFired(self, serverName):
        """boolean = WasFired(string serverName)"""
        ...



class Layer(object):
    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def SetScene(self, scene):
        """ The layer service functions operate with to a certain scene.  This scene should
        be specified by the client BEFORE any other methods are used, as an initialization
        step.  The scene can also be reset at any time, either to a new scene, or to force a refresh
        of the layer data.

        SetScene(object scene)

        """
        ...

    def Scene(self) -> object.Unknown:
        """Scene object = Scene()"""
        ...

    def Count(self) -> int:
        """integer count = Count()"""
        ...

    def Name(self, index: int) -> str:
        """string name = Name(integer index)"""
        ...

    def Slot(self, index):
        """integer slot = Slot(integer index)"""
        ...

    def Item(self, index: int) -> object.Item:
        """Item object = Item(integer index)"""
        ...

    def Mesh(self, index):
        """Mesh object = Mesh(integer index)"""
        ...

    def Flags(self, index):
        """integer flags = Flags(integer index)"""
        ...

    def Pivot(self, index):
        """float pivot = Pivot(integer index)"""
        ...

    def PatchSubdivision(self, index):
        """integer level = PatchSubdivision(integer index)"""
        ...

    def Bounds(self, index: int) -> tuple[object.vector, object.vector]:
        """(vector min,vector max) = Bounds(integer index)"""
        ...

    def CurveSmoothAngle(self, index):
        """float angle = CurveSmoothAngle(integer index)"""
        ...

    def SplinePatchSubdivision(self, index):
        """integer level = SplinePatchSubdivision(integer index)"""
        ...

    def ItemLookup(self, mode, item):
        """integer index = ItemLookup(integer mode,object item)"""
        raise NotImplementedError

    def NameLookup(self, mode: int, name: str):
        """ integer index = NameLookup(integer mode,string name)"""
        raise NotImplementedError

    def LayerParent(self, index):
        """integer parentIndex = LayerParent(integer index)"""
        ...

    def LayerChildCount(self, index):
        """integer num = LayerChildCount(integer index)"""
        ...

    def LayerChild(self, index, childNumber):
        """integer childIndex = LayerChild(integer index,integer childNumber)"""
        ...

    def LayerVMapCount(self):
        """integer num = LayerVMapCount()"""
        ...

    def LayerVMap(self, index):
        """Unknown object = LayerVMap(integer index)"""
        ...

    def LayerClipCount(self):
        """integer num = LayerClipCount()"""
        ...

    def LayerClip(self, index):
        """Item object = LayerClip(integer index)"""
        ...

    def LayerMaterialCount(self):
        """integer num = LayerMaterialCount()"""
        ...

    def LayerMaterial(self, index):
        """Item object = LayerMaterial(integer index)"""
        ...

    def LayerPartCount(self):
        """integer num = LayerPartCount()"""
        ...

    def LayerPart(self, index):
        """string part = LayerPart(integer index)"""
        ...

    def LayerSelSetCount(self, type):
        """integer num = LayerSelSetCount(integer type)"""
        ...

    def LayerSelSet(self, type: int, index: int) -> str:
        """string selSet = LayerSelSet(integer type,integer index)"""
        ...

    def LayerTextureCount(self, layer):
        """integer num = LayerTextureCount(integer layer)"""
        ...

    def LayerTexture(self, layer, index):
        """Item object = LayerTexture(integer layer,integer index)"""
        ...

    def LayerTagTextureCount(self, layer, type, tag):
        """integer num = LayerTagTextureCount(integer layer,integer type,string tag)"""
        ...

    def LayerTagTexture(self, layer, type, tag, index):
        """Item object = LayerTagTexture(integer layer,integer type,string tag,integer index)"""
        ...

    def LayerVertexCount(self, mode):
        """integer num = LayerVertexCount(integer mode)"""
        ...

    def LayerVertex(self, mode, index):
        """Unknown object = LayerVertex(integer mode,integer index)"""
        ...

    def LayerPolyCount(self, mode: int) -> int:
        """integer num = LayerPolyCount(integer mode)"""
        raise NotImplementedError

    def LayerPoly(self, mode, index):
        """Unknown object = LayerPoly(integer mode,integer index)"""
        ...

    def LayerEdgeCount(self, mode: int) -> int:
        """integer num = LayerEdgeCount(integer mode)"""
        ...

    def LayerEdge(self, mode, index):
        """Unknown object = LayerEdge(integer mode,integer index)"""
        ...

    def ScanAllocate(self, flags: int) -> object.LayerScan:
        """LayerScan object = ScanAllocate(integer flags)"""
        ...

    def CurrentMap(self, type):
        """string name = CurrentMap(integer type)"""
        ...

    def XfrmAllocate(self, toolVec):
        """TransformScan object = XfrmAllocate(object toolVec)"""
        ...

    def ScanAllocateItem(self, item, flags) -> object.LayerScan:
        """LayerScan object = ScanAllocateItem(object item,integer flags)"""
        ...

    def IsProcedural(self, index):
        """IsProcedural(integer index)"""
        ...

    def SetMark(self, item):
        """SetMark(object item)"""
        ...

    def ClearMark(self, item: object.Unknown) -> None:
        """ClearMark(object item)"""
        ...

    def TestMark(self, item):
        """integer = TestMark(object item)"""
        ...

    def CurrentDeformer(self, meshItem):
        """string name = CurrentDeformer(object meshItem)"""
        ...



class Listener(object):
    def AddListener(self, object):
        """AddListener(object object)"""
        ...

    def RemoveListener(self, object):
        """RemoveListener(object object)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...



class Log(object):
    def AcquireMonitor(self):
        """object = AcquireMonitor()"""
        ...

    def CreateEntryInfoBlock(self, type, blockName):
        """LogEntry object = CreateEntryInfoBlock(integer type,string blockName)"""
        ...

    def CreateEntryMessage(self, type, message):
        """LogEntry object = CreateEntryMessage(integer type,string message)"""
        ...

    def CreateEntryMessageFromMsgObj(self, msgObj):
        """LogEntry object = CreateEntryMessageFromMsgObj(object msgObj)"""
        ...

    def CreateEntryPaired(self, type):
        """LogEntry object = CreateEntryPaired(integer type)"""
        ...

    def DebugLogOutput(self, level, line):
        """DebugLogOutput(integer level,string line)"""
        ...

    def DebugLogOutputSys(self, level, logSystem, line):
        """DebugLogOutputSys(integer level,string logSystem,string line)"""
        ...

    def EnableLogging(self, systemName, state):
        """EnableLogging(string systemName,integer state)"""
        ...

    def ExceptionBlockCollect(self):
        """Message object = ExceptionBlockCollect()"""
        ...

    def ExceptionBlockStart(self):
        """ExceptionBlockStart()"""
        ...

    def ExceptionMessage(self, error, flags):
        """object = ExceptionMessage(integer error,integer flags)"""
        ...

    def InfoBlockByIndex(self, index):
        """LogInfoBlock object = InfoBlockByIndex(integer index)"""
        ...

    def InfoBlockCount(self):
        """integer count = InfoBlockCount()"""
        ...

    def InfoBlockFieldGetParts(self, name):
        """(string group,string sub) = InfoBlockFieldGetParts(string name)"""
        ...

    def InfoBlockFieldsAreSameGroup(self, name1, name2):
        """boolean = InfoBlockFieldsAreSameGroup(string name1,string name2)"""
        ...

    def InfoBlockLookup(self, name):
        """LogInfoBlock object = InfoBlockLookup(string name)"""
        ...

    def IsLoggingEnabled(self, systemName):
        """boolean = IsLoggingEnabled(string systemName)"""
        ...

    def MasterSubSystem(self):
        """Log object = MasterSubSystem()"""
        ...

    def ReplaceEntryMessage(self, logEntry, type, msg):
        """ReplaceEntryMessage(object logEntry,integer type,string msg)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def SetMonitor(self, monitor):
        """SetMonitor(object monitor)"""
        ...

    def SubSystemByIndex(self, index):
        """Log object = SubSystemByIndex(integer index)"""
        ...

    def SubSystemCount(self):
        """integer count = SubSystemCount()"""
        ...

    def SubSystemLookup(self, name):
        """Log object = SubSystemLookup(string name)"""
        ...



class Mesh(object):
    def ConvertMesh(self, triGroupObj, meshObj):
        """ConvertMesh(object triGroupObj,object meshObj)"""
        ...

    def CreateMesh(self):
        """Mesh object = CreateMesh()"""
        ...

    def CreateSlice(self):
        """PolygonSlice object = CreateSlice()"""
        ...

    def CreateSolidDrill(self):
        """SolidDrill object = CreateSolidDrill()"""
        ...

    def CurveGroupFromMesh(self, mesh, xfrm):
        """Unknown object = CurveGroupFromMesh(object mesh,matrix xfrm)"""
        ...

    def IsMeshProcedural(self, item):
        """boolean = IsMeshProcedural(object item)"""
        ...

    def ItemFromMesh(self, mesh):
        """Item object = ItemFromMesh(object mesh)"""
        ...

    def MeshFromSurface(self, meshObj, surfItem, surfObj):
        """MeshFromSurface(object meshObj,object surfItem,object surfObj)"""
        ...

    def MeshFromTriGroup(self, meshObj, triGroupObj):
        """MeshFromTriGroup(object meshObj,object triGroupObj)"""
        ...

    def ModeCompose(self, set, clear):
        """integer mode = ModeCompose(string set,string clear)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def SurfaceFromMesh(self, mesh, meshItem):
        """Surface object = SurfaceFromMesh(object mesh,object meshItem)"""
        ...

    def SurfaceToTriGroup(self, triGroupObj, surfObj):
        """SurfaceToTriGroup(object triGroupObj,object surfObj)"""
        ...

    def Tessellate(self, meshTess, meshSource, xfrm, flags):
        """Tessellate(object meshTess,object meshSource,matrix xfrm,integer flags)"""
        ...

    def TriGroupTransform(self, triGroupObj):
        """matrix xfrm = TriGroupTransform(object triGroupObj)"""
        ...

    def VMapDimension(self, type):
        """integer dimension = VMapDimension(integer type)"""
        ...

    def VMapIsContinuous(self, type):
        """boolean = VMapIsContinuous(integer type)"""
        ...

    def VMapIsEdgeMap(self, type):
        """boolean = VMapIsEdgeMap(integer type)"""
        ...

    def VMapLookupName(self, type):
        """string name = VMapLookupName(integer type)"""
        ...

    def VMapLookupType(self, name):
        """integer type = VMapLookupType(string name)"""
        ...

    def VMapZeroDefault(self, type):
        """boolean = VMapZeroDefault(integer type)"""
        ...

    def ValidateMetaData(self, mesh, name):
        """Unknown object = ValidateMetaData(object mesh,string name)"""
        ...



class Message(object):
    def Allocate(self):
        """Message object = Allocate()"""
        ...

    def ArgTypeDesc(self, argType):
        """string = ArgTypeDesc(string argType)"""
        ...

    def ArgTypeOptionDesc(self, argType, option):
        """string = ArgTypeOptionDesc(string argType,string option)"""
        ...

    def ArgTypeOptionUserName(self, argType, option):
        """string = ArgTypeOptionUserName(string argType,string option)"""
        ...

    def ArgTypeUserName(self, argType):
        """string = ArgTypeUserName(string argType)"""
        ...

    def Duplicate(self, msg):
        """Message object = Duplicate(object msg)"""
        ...

    def MessageText(self, msg):
        """string = MessageText(object msg)"""
        ...

    def MessageTextRich(self, msg):
        """string = MessageTextRich(object msg)"""
        ...

    def RawText(self, table, msg):
        """string text = RawText(string table,string msg)"""
        ...

    def RawTextRich(self, table, msg):
        """string text = RawTextRich(string table,string msg)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def StringLookup(self, table, ident):
        """string text = StringLookup(string table,string ident)"""
        ...

    def StripRichText(self, string):
        """string stripped = StripRichText(string string)"""
        ...



class Network(object):
    def OneOffHostListAdd(self, hostname, ip, port):
        """OneOffHostListAdd(string hostname,integer ip,integer port)"""
        ...

    def OneOffHostListRemove(self, hostname, ip, port):
        """OneOffHostListRemove(string hostname,integer ip,integer port)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...



class Nodal(object):
    def AddSampleChan(self, eval, item, chanIndex, type):
        """(integer,integer idxArray) = AddSampleChan(object eval,object item,integer chanIndex,integer type)"""
        ...

    def AddSampleChanName(self, eval, item, chanName, type):
        """(integer,integer idxArray) = AddSampleChanName(object eval,object item,string chanName,integer type)"""
        ...

    def AnyDrivenChans(self, count):
        """(integer,integer chans) = AnyDrivenChans(integer count)"""
        ...

    def GetFloat(self, etor, index, orig):
        """(float,integer idxArray) = GetFloat(object etor,integer index,float orig)"""
        ...

    def GetInt(self, etor, index, orig):
        """(integer,integer idxArray) = GetInt(object etor,integer index,integer orig)"""
        ...

    def GetValue(self, etor, index, orig):
        """(pointer,integer idxArray) = GetValue(object etor,integer index,pointer orig)"""
        ...

    def IsDriven(self, item, chanIndex):
        """integer = IsDriven(object item,integer chanIndex)"""
        ...

    def IsDrivenName(self, item, chanName):
        """integer = IsDrivenName(object item,string chanName)"""
        ...



class NotifySys(object):
    def ByIndex(self, index):
        """Notifier object = ByIndex(integer index)"""
        ...

    def Count(self):
        """integer count = Count()"""
        ...

    def Lookup(self, name, args):
        """Notifier object = Lookup(string name,string args)"""
        ...

    def NameByIndex(self, index):
        """string name = NameByIndex(integer index)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def Spawn(self, name, args):
        """Notifier object = Spawn(string name,string args)"""
        ...



class Packet(object):
    def AddPacket(self, vtype: object.VectorType, name: str, flags: int):
        """AddPacket(object vtype,string name,integer flags)"""
        ...

    def CreateVectorType(self, category: str) -> object.VectorType:
        """VectorType object = CreateVectorType(string category)"""
        ...

    def FastPacket(self, vector: object.VectorType, offset: int):
        """pointer = FastPacket(object vector,integer offset)"""
        ...

    def Lookup(self, category: str, name: str) -> int:
        """integer offset = Lookup(string category,string name)"""
        ...

    def Name(self, category: str, offset: int) -> str:
        """string name = Name(string category,integer offset)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...



class Particle(object):
    def EnumParticleFeatures(self, item, visitor):
        """EnumParticleFeatures(object item,object visitor)"""
        ...

    def EnumeratorEvaluate(self, attr, index):
        """ReplicatorEnumerator object = EnumeratorEvaluate(object attr,integer index)"""
        ...

    def EnumeratorPrepare(self, eval, replItem):
        """integer index = EnumeratorPrepare(object eval,object replItem)"""
        ...

    def FeatureIdent(self):
        """string ident = FeatureIdent()"""
        ...

    def FeatureOffset(self):
        """integer offset = FeatureOffset()"""
        ...

    def GetReplicatorEnumerator(self, replicatorItem):
        """ReplicatorEnumerator object = GetReplicatorEnumerator(object replicatorItem)"""
        ...

    def ItemToParticle(self, item, chanRead):
        """Unknown object = ItemToParticle(object item,object chanRead)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def TriGroupBlend(self, triGroup0, triGroup1, blend):
        """TriGroupBlend(object triGroup0,object triGroup1,float blend)"""
        ...

    def TriGroupToParticle(self, triGroup):
        """Unknown object = TriGroupToParticle(object triGroup)"""
        ...



class Persistence(object):
    def AddValue(self, typeName):
        """AddValue(string typeName)"""
        ...

    def Configure(self, name, obj):
        """Configure(string name,object obj)"""
        ...

    def End(self):
        """PersistentEntry object = End()"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def Start(self, name, type):
        """Start(string name,integer type)"""
        ...



class Platform(object):
    def AppBuild(self) -> int:
        """ Get the build number of the application.

        integer build = AppBuild()"""
        ...

    def AppName(self) -> str:
        """ Get the application name.

        string name = AppName()"""
        ...

    def AppUsername(self) -> str:
        """string name = AppUsername()"""
        ...

    def AppVersion(self) -> int:
        """ Get the version number of the application.

        integer version = AppVersion()"""
        ...

    def AppVersionMajor(self) -> int:
        """integer version = AppVersionMajor()"""
        ...

    def AppVersionMinor(self) -> int:
        """integer version = AppVersionMinor()"""
        ...

    def AppVersionSP(self) -> int:
        """integer version = AppVersionSP()"""
        ...

    def CancelDoWhenUserIsIdle(self, visitor: object.Unknown, flags: int):
        """ This can be used to remove a pending user idle action.  It will do nothing if the
        idle action isn't armed.  Note that flags and the visitor pointer must be exactly
        the same as the one passed to DoWhenUserIsIdle(), or else it will not be found and
        the action will remain armed.

        .. Note::

            that when doing this from Python, you must pass the exact same visitor COM object
            (not Python object).  This is also necessary when removing listeners and canceling
            timers, as discussed here: https://learn.foundry.com/modo/developers/latest/sdk/pages/faqs/PythonFAQs.html#how-do-i-remove-a-listener-object-in-python

        CancelDoWhenUserIsIdle(object visitor,integer flags)"""
        ...

    def DoWhenUserIsIdle(self, visitor: object.Unknown, flags: int):
        """ This arms a user idle action, preferably only once until it has been fired, after
        which you can arm it again if necessary.

        DoWhenUserIsIdle(object visitor,integer flags)"""
        ...

    def ExpiresIn(self) -> int:
        """ Get the number of days left until the key expires, or -1 if the key is
        permanent.

        integer daysLeft = ExpiresIn()"""
        ...

    def ImportPathByIndex(self, index) -> str:
        """

        string path = ImportPathByIndex(integer index)"""
        ...

    def ImportPathCount(self) -> int:
        """ Walk the list of imported resource paths.

        integer index = ImportPathCount()"""
        ...

    def IsApp64Bit(self) -> bool:
        """ This returns true if the application (but not necessarily the platform) is 64 bit,
        and false if it's 32 bit.

        boolean = IsApp64Bit()"""
        ...

    def IsAppActive(self) -> bool:
        """boolean = IsAppActive()"""
        ...

    def IsHeadless(self) -> bool:
        """ This returns LXe_TRUE if the app is running in headless mode, and
        LXe_FALSE if not.

        boolean = IsHeadless()"""
        ...

    def IsSafeMode(self) -> bool:
        """boolean = IsSafeMode()"""
        ...

    def IsUserIdle(self) -> bool:
        """boolean = IsUserIdle()"""
        ...

    def LicensedTo(self) -> str:
        """ Get the user the app is licensed to.  If not licensed, this fails.

        string licensee = LicensedTo()"""
        ...

    def NumLicenses(self) -> int:
        """ Get the number of licenses this key works with.

        integer licenses = NumLicenses()"""
        ...

    def OSName(self) -> str:
        """string name = OSName()"""
        ...

    def OSType(self) -> int:
        """integer type = OSType()"""
        ...

    def OSVersion(self) -> str:
        """string version = OSVersion()"""
        ...

    def PathByIndex(self, index: int) -> str:
        """string path = PathByIndex(integer index)"""
        ...

    def PathCount(self) -> int:
        """ Walk the list of paths.

        integer count = PathCount()"""
        ...

    def PathNameByIndex(self, index) -> str:
        """ This returns the internal name of the path, or NULL if the path
        doesn't have one.

        string name = PathNameByIndex(integer index)"""
        ...

    def ScriptQuery(self) -> object.Unknown:
        """Unknown object = ScriptQuery()"""
        ...

    def SerialNumber(self) -> str:
        """ Get the serial number of this key.

        string serial = SerialNumber()"""
        ...

    def SessionStage(self) -> int:
        """ The current session stage can be read with this method, indicating the status of the
        application.

        The stage can be one of the following:

        #define LXfSESSIONSTAGE_STARTUP			    0x10000000
        #define LXfSESSIONSTAGE_READY			    0x20000000
        #define LXfSESSIONSTAGE_SHUTDOWN		    0x30000000

        #define LXiSESSIONSTAGE_NOT_READY		    0
        #define LXiSESSIONSTAGE_STARTUP_COMMANDS	(LXfSESSIONSTAGE_STARTUP  | 0)
        #define LXiSESSIONSTAGE_SYSTEM_READY		(LXfSESSIONSTAGE_READY    | 0)
        #define LXiSESSIONSTAGE_SHUTTING_DOWN		(LXfSESSIONSTAGE_SHUTDOWN | 0)

        integer stage = SessionStage()"""
        ...

    def TimerCancel(self, visitor: object.Unknown, idleFlags: int):
        """ A currently-running timer can be canceled with this function.  The visitor and flags
        must match what the timer was armed with.

        .. Note::

            that when doing this from Python, you must pass the exact same visitor COM object
            (not Python object).  This is also necessary when removing listeners and canceling
            user idle actions, as discussed here: https://learn.foundry.com/modo/developers/latest/sdk/pages/faqs/PythonFAQs.html#how-do-i-remove-a-listener-object-in-python

        TimerCancel(object visitor,integer idleFlags)"""
        ...

    def TimerStart(self, visitor: object.Unknown, milliseconds: int, idleFlags: int):
        """ Timers execute after a pre-determined number of milliseconds.  A timer executes only
        once, but you can re-arm it when it expires if you want.  The most common use of timers
        is to check files for changes or trigger periodic refreshes of part of the UI.

        .. Note::

            that timers can trigger at arbitrary and unsafe times, such as in the middle of
            rendering or while saving a file.  You should never execute a command from a timer,
            for example, but rather arm a user idle action (and even then executing commands is
            a bit iffy, since now you're adding something to the command history or undo list
            that the user didn't do directly, but sometimes it is necessary).

        If idleFlags are LXiUSERIDLE_ALWAYS, then the timer's visitor is called as soon as
        the timer expires.  Otherwise, the action is deferred until user idle state matches
        the flags.

        TimerStart(object visitor,integer milliseconds,integer idleFlags)"""
        ...



class PresetBrowser(object):
    def GetSpecialSelModePath(self, identifier):
        """string = GetSpecialSelModePath(string identifier)"""
        ...

    def IsViewportVisible(self, identifier, hash):
        """boolean = IsViewportVisible(string identifier,string hash)"""
        ...

    def RecognizeFile(self, path, flags):
        """(string serverName,string category) = RecognizeFile(string path,integer flags)"""
        ...

    def RecognizeFileForce(self, path, flags):
        """(string serverName,string category) = RecognizeFileForce(string path,integer flags)"""
        ...

    def Rescan(self, path):
        """Rescan(string path)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def ServerByIndex(self, index):
        """PresetType object = ServerByIndex(integer index)"""
        ...

    def ServerCount(self):
        """integer count = ServerCount()"""
        ...

    def ServerLookup(self, name):
        """PresetType object = ServerLookup(string name)"""
        ...

    def ServerNameByIndex(self, index):
        """string name = ServerNameByIndex(integer index)"""
        ...

    def ServerUserNameByIndex(self, index):
        """string name = ServerUserNameByIndex(integer index)"""
        ...

    def SetSpecialSelModePath(self, identifier, path, asInteractive):
        """SetSpecialSelModePath(string identifier,string path,integer asInteractive)"""
        ...

    def SubtypeFromIdentifier(self, identifier):
        """integer subtype = SubtypeFromIdentifier(string identifier)"""
        ...

    def UpdateIdentifierState(self, identifier, path):
        """UpdateIdentifierState(string identifier,string path)"""
        ...



class PresetDestination(object):
    def ApplyMeshPresetToMeshPD(self, predest, filepath):
        """ApplyMeshPresetToMeshPD(object predest,string filepath)"""
        ...

    def ApplyProfilePDToMesh(self, predest, tolerance, freeze, axis, mesh):
        """ApplyProfilePDToMesh(object predest,float tolerance,integer freeze,integer axis,object mesh)"""
        ...

    def CreateMeshLayerPD(self, mesh, shadeItem):
        """Unknown object = CreateMeshLayerPD(object mesh,object shadeItem)"""
        ...

    def Profile1DPDFromPath(self, filepath):
        """Unknown object = Profile1DPDFromPath(string filepath)"""
        ...

    def Profile2DPDFromPath(self, filepath):
        """Unknown object = Profile2DPDFromPath(string filepath)"""
        ...

    def ShaderPDFromItem(self, item):
        """Unknown object = ShaderPDFromItem(object item)"""
        ...



class Preview(object):
    def CreatePreview(self):
        """Preview object = CreatePreview()"""
        ...

    def GetMeshPreview(self, item, width, height):
        """Unknown object = GetMeshPreview(object item,integer width,integer height)"""
        ...



class Render(object):
    def FrameDelete(self, slotIndex):
        """FrameDelete(integer slotIndex)"""
        ...

    def FrameRecall(self, slotIndex, passIndex, monitor):
        """FrameBuffer object = FrameRecall(integer slotIndex,integer passIndex,object monitor)"""
        ...

    def FrameRecallStats(self, slotIndex):
        """RenderStats object = FrameRecallStats(integer slotIndex)"""
        ...

    def FrameRecallThumbnail(self, slotIndex):
        """Image object = FrameRecallThumbnail(integer slotIndex)"""
        ...

    def FrameRenderPassCount(self, slotIndex):
        """integer numPasses = FrameRenderPassCount(integer slotIndex)"""
        ...

    def FrameRenderPassInfo(self, slotIndex, passIndex, name):
        """(integer width,integer height,integer outputCount,integer isStereo,integer eyeDisplay,integer stereoComposite) = FrameRenderPassInfo(integer slotIndex,integer passIndex,byte[] name)"""
        ...

    def FrameSaveImage(self, framebuffer, bufferIndex, filename, format, message, monitor):
        """FrameSaveImage(object framebuffer,integer bufferIndex,string filename,string format,object message,object monitor)"""
        ...

    def FrameSaveLayered(self, framebuffer, filename, format, message, monitor):
        """FrameSaveLayered(object framebuffer,string filename,string format,object message,object monitor)"""
        ...

    def FrameSavePassLayered(self, framebuffer, filename, format, message, monitor):
        """FrameSavePassLayered(object framebuffer,string filename,string format,object message,object monitor)"""
        ...

    def FrameSavePassesAsImages(self, slotIndex, filename, format, message, monitor):
        """FrameSavePassesAsImages(integer slotIndex,string filename,string format,object message,object monitor)"""
        ...

    def FrameSavePassesAsLayeredImages(self, slotIndex, filename, format, message, monitor):
        """FrameSavePassesAsLayeredImages(integer slotIndex,string filename,string format,object message,object monitor)"""
        ...

    def FrameStore(self, frameBuffer, writePixels):
        """FrameStore(object frameBuffer,integer writePixels)"""
        ...

    def FrameStoreStats(self, slotIndex, stats):
        """FrameStoreStats(integer slotIndex,object stats)"""
        ...

    def FrameStoreThumbnail(self, slotIndex, image):
        """FrameStoreThumbnail(integer slotIndex,object image)"""
        ...

    def FrameTestRecall(self, slotIndex, passIndex):
        """boolean = FrameTestRecall(integer slotIndex,integer passIndex)"""
        ...

    def JobAbort(self):
        """ This aborts a currently running render job.  It will fail if no jobs are
        currently rendering.  Note that although this function returns immediately,
        it may take some time before the render has finished aborting.

        JobAbort()

        """
        ...

    def JobCleanup(self, clearJob):
        """JobCleanup(integer clearJob)"""
        ...

    def JobCurrent(self):
        """ This returns the current render job, failing if there is no current job.  The
        returned object must be released by the caller if the method returns success.

        RenderJob object = JobCurrent()"""
        ...

    def JobIsSlave(self):
        """integer = JobIsSlave()"""
        ...

    def JobRenderOutputCount(self):
        """integer count = JobRenderOutputCount()"""
        ...

    def JobRenderOutputName(self, index):
        """string name = JobRenderOutputName(integer index)"""
        ...

    def JobRenderOutputType(self, index):
        """integer type = JobRenderOutputType(integer index)"""
        ...

    def JobSetCurrent(self, job: object.Unknown):
        """ The client provides information about how to render a scene with a render job.
        This is a COM object with an ILxRenderJob interface, as described below.
        Frames, animations, turntables and baking can be rendered by providing a job
        to the render service.

        A specific render job can be set as the current job with this method, or the
        current job can be set to nothing by passing NULL.  Attempting to set the
        render job will fail if another job is currently being rendered.  The job
        provided will be AddRef()'ed by the service.

        JobSetCurrent(object job)"""
        ...

    def JobStart(self):
        """ This method can be used to start rendering the current job, using the
        properties of the job to render the scene.  This function does not block,
        and will return immediately.  Status updates are sent to various methods
        on the job object itself.

        JobStart()"""
        ...

    def JobStats(self):
        """ This returns an ILxRenderStats container object containing information about the current
        render  See the ILxRenderStats description below for more information.  The container and
        the individual stats objects are dynamically updated while rendering, so you can hold on
        to the container object for the life of the render.  The object must be released when no
        longer needed.

        object = JobStats()"""
        ...

    def JobStatus(self):
        """ This returns the current status of a render job as an LxResult code.

        - LXe_RENDER_IDLE
        A job is loaded (JobCurrent() would succeed), but is not currently rendering
        a frame.  The system is effectively idle and waiting for JobStart() to be
        called, or for a new job to be loaded.
        
        - LXe_RENDER_RENDERING
        Returns true if the currently loaded job is rendering a frame.
        
        - LXe_RENDER_NO_JOB
        There is no current current job (and thus JobCurrent() would fail).  A new
        job must be set with JobSetCurrent() before calling JobStart().
        
        - LXe_RENDER_ABORTING
        JobAbort() was called and the job is in the process of aborting, but has not
        yet finished.

        JobStatus()"""
        ...

    def RefreshProgressImageMetrics(self):
        """RefreshProgressImageMetrics()"""
        ...

    def RenderEffectFromRenderType(self, type):
        """string effectName = RenderEffectFromRenderType(integer type)"""
        ...

    def RenderEffectToType(self, effect):
        """(integer type,integer size) = RenderEffectToType(string effect)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def UpdateProgressImage(self):
        """UpdateProgressImage()"""
        ...



class RenderCache(object):
    def CreateRenderCache(self, createFlags):
        """RenderCache object = CreateRenderCache(integer createFlags)"""
        ...



class Scene(object):
    def AllocEmptyCollection(self):
        """ItemCollection object = AllocEmptyCollection()"""
        ...

    def ChannelVectorSize(self, mode):
        """integer size = ChannelVectorSize(integer mode)"""
        ...

    def ChannelVectorTextHints(self):
        """hints hints = ChannelVectorTextHints()"""
        ...

    def CloseCollection(self, collection, mode):
        """CloseCollection(object collection,integer mode)"""
        ...

    def CreateScene(self):
        """Scene object = CreateScene()"""
        ...

    def DestroyScene(self, scene):
        """DestroyScene(object scene)"""
        ...

    def GetMeshInstSourceItem(self, inst):
        """Item object = GetMeshInstSourceItem(object inst)"""
        ...

    def GetReplicatorEnumerator(self, replicatorItem):
        """ReplicatorEnumerator object = GetReplicatorEnumerator(object replicatorItem)"""
        ...

    def ItemGraphCollection(self, collection, type, graph, fwd):
        """ItemGraphCollection(object collection,integer type,string graph,integer fwd)"""
        ...

    def ItemSubTypeByIndex(self, type, index):
        """string subtype = ItemSubTypeByIndex(integer type,integer index)"""
        ...

    def ItemSubTypeCount(self, type):
        """integer count = ItemSubTypeCount(integer type)"""
        ...

    def ItemTypeByIndex(self, index):
        """integer type = ItemTypeByIndex(integer index)"""
        ...

    def ItemTypeCommonChannels(self, item1, item2):
        """integer count = ItemTypeCommonChannels(object item1,object item2)"""
        ...

    def ItemTypeCount(self):
        """integer = ItemTypeCount()"""
        ...

    def ItemTypeGetTag(self, type, tag, super):
        """string value = ItemTypeGetTag(integer type,string tag,integer super)"""
        ...

    def ItemTypeLookup(self, name: str) -> int:
        """ Given a type name, this returns the type ID.

        integer type = ItemTypeLookup(string name)"""
        ...

    def ItemTypeName(self, type):
        """string name = ItemTypeName(integer type)"""
        ...

    def ItemTypeSuper(self, type):
        """integer super = ItemTypeSuper(integer type)"""
        ...

    def ItemTypeSupportsInterface(self, type, guid):
        """boolean = ItemTypeSupportsInterface(integer type,string guid)"""
        ...

    def ItemTypeTest(self, what, isA):
        """boolean = ItemTypeTest(integer what,integer isA)"""
        ...

    def LoadImage(self, scene, path, monitor):
        """Item object = LoadImage(object scene,string path,object monitor)"""
        ...

    def MeshInstanceByIndex(self, mesh, index):
        """Item object = MeshInstanceByIndex(object mesh,integer index)"""
        ...

    def MeshInstanceCount(self, mesh):
        """integer = MeshInstanceCount(object mesh)"""
        ...

    def Root(self):
        """Scene object = Root()"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def SubSceneAdd(self, scene, other, refItems):
        """SubSceneAdd(object scene,object other,integer refItems)"""
        ...

    def SubSceneLoad(self, scene, path, monitor):
        """Scene object = SubSceneLoad(object scene,string path,object monitor)"""
        ...



class ScriptSys(object):
    def ByIndex(self, index):
        """ScriptManager object = ByIndex(integer index)"""
        ...

    def Count(self):
        """integer count = Count()"""
        ...

    def Desc(self, manager):
        """string name = Desc(object manager)"""
        ...

    def KitByIndex(self, index, visible):
        """Kit object = KitByIndex(integer index,integer visible)"""
        ...

    def KitCount(self, visible):
        """integer count = KitCount(integer visible)"""
        ...

    def KitLookup(self, name):
        """Kit object = KitLookup(string name)"""
        ...

    def Lookup(self, name):
        """ScriptManager object = Lookup(string name)"""
        ...

    def NameByIndex(self, index):
        """string name = NameByIndex(integer index)"""
        ...

    def ResolveAlias(self, alias):
        """string path = ResolveAlias(string alias)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def UserName(self, manager):
        """string name = UserName(object manager)"""
        ...

    def UserValueByIndex(self, index):
        """UserValue object = UserValueByIndex(integer index)"""
        ...

    def UserValueCount(self):
        """integer count = UserValueCount()"""
        ...

    def UserValueLookup(self, name):
        """UserValue object = UserValueLookup(string name)"""
        ...



class Selection(object):
    def AbortBatch(self):
        """AbortBatch()"""
        ...

    def Allocate(self, name: str) -> object:
        """SelectionType object = Allocate(string name)"""
        ...

    def ByIndex(self, type, idx) -> int:
        """pointer = ByIndex(integer type,integer idx)"""
        ...

    def Clear(self, type: int):
        """ This is like Drop() but doesn't change the current selection mode.

        Clear(integer type)

        """
        ...

    def Count(self, type: int) -> int:
        """integer = Count(integer type)"""
        ...

    def CurrentSubTypes(self, type: int, sub: lx.object.storage, len: int):
        """integer num = CurrentSubTypes(integer type,unsigned[] sub,integer len)"""
        ...

    def CurrentType(self, types: lx.object.storage):
        """ This returns the most recent selection type -- the one the user acted on last.
        If 'types' is non-null, it will be an array of types terminated with zero,
        and the type returned will be one of the ones in the list.

        >>> selection_service = lx.service.Selection()
        >>> current_type = selection_service.CurrentType(lx.object.storage('i'))

        integer = CurrentType(unsigned[] types)

        """
        ...

    def Deselect(self, type, packet):
        """Deselect(integer type,pointer packet)"""
        ...

    def Drop(self, type):
        """Drop(integer type)"""
        ...

    def EndBatch(self):
        """EndBatch()"""
        ...

    def GetTime(self):
        """float = GetTime()"""
        ...

    def LookupName(self, type):
        """string = LookupName(integer type)"""
        ...

    def LookupType(self, name):
        """integer = LookupType(string name)"""
        ...

    def Recent(self, type):
        """pointer = Recent(integer type)"""
        ...

    def Remove(self, type, packet):
        """Remove(integer type,pointer packet)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def Select(self, type, packet):
        """Select(integer type,pointer packet)"""
        ...

    def SetTime(self, time):
        """SetTime(float time)"""
        ...

    def StartBatch(self):
        """StartBatch()"""
        ...

    def State(self, type, packet):
        """ This is similar to Test(), but returns the actual selection state for
        the element. State can have one or more of the LXf_SELECTION_* bits
        set, or be LXf_SELECTION_NONE.

        integer = State(integer type,pointer packet)"""
        ...

    def Test(self, type, packet):
        """boolean = Test(integer type,pointer packet)"""
        ...

    def Toggle(self, type, packet):
        """Toggle(integer type,pointer packet)"""
        ...



class Shader(object):
    def CollectMaterials(self, collection):
        """CollectMaterials(object collection)"""
        ...

    def ColorBlendValue(self, c1, c2, opa, mode):
        """vector c = ColorBlendValue(vector c1,vector c2,float opa,integer mode)"""
        ...

    def ComputeFresnel(self, inRay, normalRay, normReflAmt):
        """float = ComputeFresnel(vector inRay,vector normalRay,float normReflAmt)"""
        ...

    def MeshShaderAccessor(self, meshItem):
        """Shader object = MeshShaderAccessor(object meshItem)"""
        ...

    def NextRandom(self, vector):
        """float = NextRandom(object vector)"""
        ...

    def PoissonOffset(self, vector):
        """(float u,float v) = PoissonOffset(object vector)"""
        ...

    def PolyShaderAccessor(self, meshItem, polyID):
        """Shader object = PolyShaderAccessor(object meshItem,id polyID)"""
        ...

    def RussianRoulette(self, vector, importance):
        """float = RussianRoulette(object vector,float importance)"""
        ...

    def SampleCloud(self, sample):
        """SampleCloud object = SampleCloud(object sample)"""
        ...

    def ScalarBlendValue(self, v1, v2, opa, mode):
        """float = ScalarBlendValue(float v1,float v2,float opa,integer mode)"""
        ...

    def SquareToCircle(self, x, y):
        """SquareToCircle(float[] x,float[] y)"""
        ...



class StdDialog(object):
    def AsyncMonitorAllocate(self, system, title):
        """AsyncMonitor object = AsyncMonitorAllocate(string system,string title)"""
        ...

    def AsyncMonitorAllocateWithoutAbort(self, system, title):
        """Unknown object = AsyncMonitorAllocateWithoutAbort(string system,string title)"""
        ...

    def AsyncMonitorLookup(self, ident):
        """Monitor object = AsyncMonitorLookup(string ident)"""
        ...

    def AsyncMonitorRelease(self, monitor):
        """AsyncMonitorRelease(object monitor)"""
        ...

    def AsyncMonitorSubAllocate(self, parent, title):
        """AsyncMonitor object = AsyncMonitorSubAllocate(object parent,string title)"""
        ...

    def AsyncMonitorSystemByIndex(self, index):
        """AsyncMonitorSystem object = AsyncMonitorSystemByIndex(integer index)"""
        ...

    def AsyncMonitorSystemCount(self):
        """integer count = AsyncMonitorSystemCount()"""
        ...

    def AsyncMonitorSystemLookup(self, name):
        """AsyncMonitorSystem object = AsyncMonitorSystemLookup(string name)"""
        ...

    def FileDialog(self, dlgObj):
        """FileDialog(object dlgObj)"""
        ...

    def MessageAllocate(self):
        """Message object = MessageAllocate()"""
        ...

    def MessageOpen(self, message, title, helpURL, cookie):
        """MessageOpen(object message,string title,string helpURL,string cookie)"""
        ...

    def MonitorAllocate(self, title: str) -> object.Monitor:
        """Monitor object = MonitorAllocate(string title)"""
        ...

    def MonitorRelease(self):
        """MonitorRelease()"""
        ...

    def MonitorReleaseObj(self, monitor: object.Unknown) -> None:
        """MonitorReleaseObj(object monitor)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...



class Tableau(object):
    def AllocVertex(self):
        """TableauVertex object = AllocVertex()"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def VertexFromFeatures(self, surfObj, vertex):
        """VertexFromFeatures(object surfObj,object vertex)"""
        ...



class TextEncoding(object):
    def Allocate(self):
        """TextEncoding object = Allocate()"""
        ...



class Thread(object):
    def CreateMutex(self) -> object.ThreadMutex:
        """ThreadMutex object = CreateMutex()"""
        ...

    def CreateCS(self) -> object.ThreadMutex:
        """ Create "Critical Section"

        ThreadMutex object = CreateCS()
        """
        ...

    def CreateGroup(self) -> object.ThreadGroup:
        """ Thread service interface allow new groups to be created.

        ThreadGroup object = CreateGroup()

        """
        ...

    def NumProcs(self) -> int:
        """ Determine how many processes are available

        integer = NumProcs()"""

        ...

    def IsMainThread(self) -> bool:
        """ Check if this is the main thread.

        bool = IsMainThread()

        """
        ...

    def CreateSlot(self, size: int, client: object.ThreadSlotClient) -> object.ThreadSlot:
        """ Allocating a new thread slot

        ThreadSlot object = CreateSlot(integer size,object client)

        """
        ...

    def ProcessShared(self, shared):
        """ You start with a single one of these objects that contains all the work. You then
        call the ProcesShared() method in the service. This will spawn enough of the shared
        work objects to populate the available computing resources. Each one will then process
        all the work it has, getting more from the main shared work object when they are
        empty. When all the work is done the sub-objects are destroyed.

        ProcessShared(object shared)"""
        ...

    def ProcessRange(self, data, startIndex: int, endIndex: int, rangeWorker: object.ThreadRangeWorker):
        """ Multi-processing over a range of indices (such as scanlines in an image).

        ProcessRange(pointer data,integer startIndex,integer endIndex,object rangeWorker)

        """
        ...

    def InitThread(self):
        """ If a plugin creates its own threads, using some external library (like pthreads or OpenMP),
        it needs to initialize itself before it can call Nexus functions. This function allows that.
        If the thread has already initialized itself, this function will do nothing.

        InitThread()

        """
        ...

    def CleanupThread(self):
        """ Once the thread has finished executing Nexus code, it needs to free the Nexus specific thread-data,
        so it must call CleanupThread, or there will be a memory leak.

        CleanupThread()

        """
        ...

    def ProcessWaterfall(self, waterfall: object.Waterfall, threads: int):
        """ This method takes a waterfall object and processes all the work it contains.
        New instances will be spawned to fill out the given number of threads, or
        one for each processor is the thread count is zero.

        ProcessWaterfall(object waterfall,integer threads)

        """
        ...


class Undo(object):
    def Apply(self, undo):
        """Apply(object undo)"""
        ...

    def Record(self, undo):
        """Record(object undo)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def State(self):
        """integer = State()"""
        ...


class Value(object):
    def ScriptQuery(self) -> lx.object.Unknown:
        """ Gets the ILxScriptQueryID interface for the system.

        Unknown object = ScriptQuery()

        """
        ...

    def TextHintEncode(self, value: int, hint: List[Tuple[int, str]]) -> str:
        """ This encodes a numeric value as a string.  If the 'buf' pointer is null, then
        a rolling buffer will be allocated and returned.  If the hint pointer is null
        then the value is written as a plain signed integer.

        This will return LXe_OK_INEXACT_MATCH when an integer is provided that does
        not exactly map to one of the choices.  This is only returned if there are
        choices.  LXe_OK_NO_CHOICES is returned if there are no choices at all.
        In both cases, the raw integer is encoded into the string buffer.  Both
        codes are "OK" codes, and do not signify an error, but rather provide hints
        about the content of the encoded string, and may help instruct an code path
        if you do need an exact match or were expecting choices.

        string = TextHintEncode(integer value, hints hint)

        >>> value_service = lx.service.Value()
        >>> hint = [(0, 'foo'), (1, 'bar'), (2, 'baz')]
        >>> print(value_service.TextHintEncode(1, hint))
        'bar'

        """
        ...

    def TextHintDecode(self, buf: str, hint: List[Tuple[int, str]]) -> int:
        """ This method decodes a string using the hint array.  If the string is a
        number it will be returned directly after being clamped to min or max limits.
        If nothing is recognized then the function end-of-list will be returned.
        This will return LXe_NOTFOUND when the string does not exactly match any
        text hints and cannot be converted into an integer (i.e., it doesn't start
        with a number).  LXe_OK_NO_CHOICES is returned when the string was
        sucessfully converted from a number into an integer and may have been
        constrained to any min/max hints present, but the hints contain no actual
        choices.  This may occur in the case of a hints array that is used only for
        min/max or similar properties, and is not meant to have a list of choices.

        integer value = TextHintDecode(string buf, hints hint)

        >>> value_service = lx.service.Value()
        >>> hint = [(0, 'foo'), (1, 'bar'), (2, 'baz')]
        >>> value_service.TextHintDecode('baz', hint)
        2

        """
        ...

    def CreateValue(self, type: str) -> lx.object.Value:
        """ This method creates a new value object of the given type.

        Value object = CreateValue(string type)

        """
        ...

    def ValueType(self, type: str) -> int:
        """ This gets the intrinsic type for a given value type, as one of the LXi_TYPE_* choices.

        integer valType = ValueType(string type)

        """
        ...

    def FloatType(self, val: float) -> int:
        """ Check a float for NaN or infinity. A zero return value is OK.

        integer = FloatType(float val)

        """
        ...

    def GetFPS(self) -> float:
        """ Returns the global Frames Per Second.

        float = GetFPS()

        """
        ...

    def TimeToFrame(self, time: float) -> float:
        """ Given a time and using the global Frames Per Second, returns an equivalent frame.

        float = TimeToFrame(float time)

        """
        ...

    def FrameToTime(self, frame: float) -> float:
        """ Given a frame and using the global Frames Per Second, returns an equivalent time.

        float = FrameToTime(float frame)

        """
        ...

    def TimeToFrameFPS(self, time: float, fps: float) -> float:
        """ Given a time and a Frames Per Second, returns an equivalent frame.

        float = TimeToFrameFPS(float time,float fps)

        """
        ...

    def FrameToTimeFPS(self, frame: float, fps: float):
        """ Given a frame and a Frames Per Second, returns an equivalent time.

        float = FrameToTimeFPS(float frame,float fps)

        """
        ...

    def ConvertValues(self, from_str: str, to_str: str) -> lx.object.Unknown:
        """ Given two different value type names, returns an ILxValueConversion 
        object that can be used to convert from one type to the other.

        ValueConversion object = ConvertValues(string from_str,string to_str)

        """
        ...


class ValueHUD(object):
    def ClearHUD(self, cookie):
        """ClearHUD(string cookie)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def SetHUDCommands(self, cookie, command1, command2, command3, alphaSort):
        """SetHUDCommands(string cookie,string command1,string command2,string command3,integer alphaSort)"""
        ...



class Variation(object):
    def InvalidateItem(self, item):
        """InvalidateItem(object item)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...



class VertexFeature(object):
    def AllocVertex(self):
        """TableauVertex object = AllocVertex()"""
        ...

    def DataType(self, ident):
        """string typeName = DataType(string ident)"""
        ...

    def Dimension(self, ident):
        """integer dimension = Dimension(string ident)"""
        ...

    def Lookup(self, type, name):
        """string ident = Lookup(integer type,string name)"""
        ...

    def Name(self, ident):
        """string name = Name(string ident)"""
        ...

    def ScriptQuery(self):
        """Unknown object = ScriptQuery()"""
        ...

    def TestCategory(self, ident, category):
        """boolean = TestCategory(string ident,string category)"""
        ...

    def Type(self, ident):
        """integer type = Type(string ident)"""
        ...

    def VectorType(self, ident):
        """string vecType = VectorType(string ident)"""
        ...



class View3Dport(object):
    def AddVirtualModel(self, vmodel: object.Unknown) -> None:
        """AddVirtualModel(object vmodel)"""
        ...

    def AllocGLViewport(self) -> object.Unknown:
        """Unknown object = AllocGLViewport()"""
        ...

    def Count(self) -> int:
        """integer = Count()"""
        ...

    def Current(self) -> int:
        """integer = Current()"""
        ...

    def GLMaterial(self, bin: object.Unknown, item: object.Unknown, view: object.Unknown) -> object.Unknown:
        """Unknown object = GLMaterial(object bin,object item,object view)"""
        ...

    def ImageToGLImage(self, image: object.Unknown) -> object.Unknown:
        """Unknown object = ImageToGLImage(object image)"""
        ...

    def InvalidateOverrider(self, scene: object.Unknown, pkgName: str):
        """integer = InvalidateOverrider(object scene,string pkgName)"""
        ...

    def Mouse(self) -> tuple[int, int, int]:
        """ Returns the index of the viewport currently under the mouse, or -1 if
        the mouse is not over a 3D view. The position relative to that view is
        filled into x and y, if they are not NULL.

        (integer view, integer x, integer y) = Mouse()"""
        ...

    def RemoveVirtualModel(self, vmodel: object.Unknown) -> None:
        """RemoveVirtualModel(object vmodel)"""
        ...

    def ScriptQuery(self) -> object.Unknown:
        """Unknown object = ScriptQuery()"""
        ...

    def SetHitUVMap(self, name: str):
        """SetHitUVMap(string name)"""
        ...

    def SurfaceToViewObject(self, type: int, item: object.Unknown) -> object.Unknown:
        """Unknown object = SurfaceToViewObject(integer type,object item)"""
        ...

    def TriGroupToViewObject(self, type: int, triGroup: object.Unknown) -> object.Unknown:
        """Unknown object = TriGroupToViewObject(integer type,object triGroup)"""
        ...

    def UpdateVirtualModel(self, vmodel: object.Unknown):
        """UpdateVirtualModel(object vmodel)"""
        ...

    def View(self, index: int) -> object.Unknown:
        """ Get the View3D object at index.

        >>> view_service = lx.service.View3Dport()
        >>> view_index = view_service.Current()
        >>> unknown = view_service.View(view_index)
        >>> view = lx.object.View3D(unknown)
        >>> view.test()
        True

        Unknown object = View(integer index)

        """
        ...

