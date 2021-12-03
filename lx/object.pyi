""" lx.object stubs """


from typing import Tuple


# type hint for 4x4 matrices
Matrix4 = tuple[
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float], 
    tuple[float, float, float, float], 
]


class ActionClip(object):
    def __init__(self, *args, **kwargs):
        ...

    def Action(self, time: float):
        """ ChannelRead object = Action(float time)"""
        ...

    def Active(self) -> int:
        """ integer = Active()"""
        ...

    def Create(self):
        """ Create()"""
        ...

    def Enabled(self):
        """ integer = Enabled()"""
        ...

    def Extents(self, layers: int) -> Tuple[float, float]:
        """ (float timeS,float timeE) = Extents(integer layers)"""
        ...

    def SetActive(self, state: int):
        """ SetActive(integer state)"""
        ...

    def SetEnabled(self, state: int):
        """ SetEnabled(integer state)"""
        ...

    def SetParenting(self, group: object):
        """ SetParenting(object group)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...


class ActionLayerPacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Index(self, packet):
        """integer = Index(pointer packet)"""
        ...

    def Item(self, packet):
        """Item object = Item(pointer packet)"""
        ...

    def Packet(self, item, index):
        """pointer = Packet(object item,integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...


class ActionListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def ActionChannelConstantChange(self, item, channel):
        """ActionChannelConstantChange(object item,integer channel)"""
        ...

    def ActionChannelConstantPreChange(self, item, channel):
        """ActionChannelConstantPreChange(object item,integer channel)"""
        ...

    def ActionChannelSignal(self, item, channel):
        """ActionChannelSignal(object item,integer channel)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...


class AddChannel(object):
    def __init__(self, *args, **kwargs):
        ...

    def NewChannel(self, name, type):
        """NewChannel(string name,string type)"""
        ...

    def SetDefault(self, defFlt, defInt):
        """SetDefault(float defFlt,integer defInt)"""
        ...

    def SetDefaultObj(self):
        """Unknown object = SetDefaultObj()"""
        ...

    def SetDefaultVec(self, defVec):
        """SetDefaultVec(double[] defVec)"""
        ...

    def SetGradient(self, inType):
        """SetGradient(string inType)"""
        ...

    def SetHint(self, hint):
        """SetHint(hints hint)"""
        ...

    def SetInternal(self):
        """SetInternal()"""
        ...

    def SetStorage(self, stType):
        """SetStorage(string stType)"""
        ...

    def SetUserHint(self, hint):
        """SetUserHint(hints hint)"""
        ...

    def SetVector(self, vecType):
        """SetVector(string vecType)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...


class AddDropAction(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddAction(self, action, message):
        """AddAction(integer action,string message)"""
        ...

    def Peek(self):
        """Unknown object = Peek()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class AdjustTool(object):
    def __init__(self, *args, **kwargs):
        ...

    def Invalidate(self):
        """Invalidate()"""
        ...

    def Lock(self):
        """Lock()"""
        ...

    def SetFlt(self, index, val):
        """SetFlt(integer index,float val)"""
        ...

    def SetInt(self, index, val):
        """SetInt(integer index,integer val)"""
        ...

    def SetString(self, index, val):
        """SetString(integer index,string val)"""
        ...

    def Update(self):
        """Update()"""
        ...

    def Value(self, index, val):
        """Value(integer index,object val)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class AnimListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def EnterSetup(self):
        """EnterSetup()"""
        ...

    def LeaveSetup(self):
        """LeaveSetup()"""
        ...

    def PlayEnd(self):
        """PlayEnd()"""
        ...

    def PlayStart(self):
        """PlayStart()"""
        ...

    def ScrubEnd(self):
        """ScrubEnd()"""
        ...

    def ScrubTime(self):
        """ScrubTime()"""
        ...

    def TimeChange(self):
        """TimeChange()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class AppActiveListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def IsNowActive(self, isActive):
        """IsNowActive(integer isActive)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class AsyncMonitorInfo(object):
    def __init__(self, *args, **kwargs):
        ...

    def Abort(self):
        """Abort()"""
        ...

    def CanAbort(self):
        """CanAbort()"""
        ...

    def Child(self):
        """Unknown object = Child()"""
        ...

    def Identifier(self):
        """string ident = Identifier()"""
        ...

    def IsAborted(self):
        """IsAborted()"""
        ...

    def OverallProgress(self):
        """float progress = OverallProgress()"""
        ...

    def Parent(self):
        """Unknown object = Parent()"""
        ...

    def Progress(self):
        """float progress = Progress()"""
        ...

    def System(self):
        """string system = System()"""
        ...

    def Title(self):
        """string title = Title()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class AsyncMonitorSystem(object):
    def __init__(self, *args, **kwargs):
        ...

    def ByIndex(self, index):
        """Unknown object = ByIndex(integer index)"""
        ...

    def Count(self):
        """integer count = Count()"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class AttrSequence(object):
    def __init__(self, *args, **kwargs):
        ...

    def Float(self, name, value):
        """Float(string name,float value)"""
        ...

    def HaulingOverride(self, name, value):
        """HaulingOverride(string name,string value)"""
        ...

    def Integer(self, name, value):
        """Integer(string name,integer value)"""
        ...

    def String(self, name, value):
        """String(string name,string value)"""
        ...

    def Value(self, name, value):
        """Value(string name,object value)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Attributes(object):
    def __init__(self, *args, **kwargs):
        ...

    def Count(self):
        """integer = Count()"""
        ...

    def GetFlt(self, index):
        """float val = GetFlt(integer index)"""
        ...

    def GetInt(self, index):
        """integer val = GetInt(integer index)"""
        ...

    def GetString(self, index):
        """string = GetString(integer index)"""
        ...

    def Hints(self, index):
        """hints = Hints(integer index)"""
        ...

    def Lookup(self, name):
        """integer index = Lookup(string name)"""
        ...

    def Name(self, index):
        """string name = Name(integer index)"""
        ...

    def SetFlt(self, index, val):
        """SetFlt(integer index,float val)"""
        ...

    def SetInt(self, index, val):
        """SetInt(integer index,integer val)"""
        ...

    def SetString(self, index, val):
        """SetString(integer index,string val)"""
        ...

    def Type(self, index):
        """integer type = Type(integer index)"""
        ...

    def TypeName(self, index):
        """string tname = TypeName(integer index)"""
        ...

    def Value(self, index, writeOK):
        """Unknown object = Value(integer index,integer writeOK)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class AttributesUI(object):
    def __init__(self, *args, **kwargs):
        ...

    def DisableMsg(self, index, message):
        """DisableMsg(integer index,object message)"""
        ...

    def UIHints(self, index, hints):
        """UIHints(integer index,object hints)"""
        ...

    def UIValueHints(self, index):
        """UIValueHints object = UIValueHints(integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Audio(object):
    def __init__(self, *args, **kwargs):
        ...

    def Channels(self):
        """integer = Channels()"""
        ...

    def Data(self):
        """data[] = Data()"""
        ...

    def Duration(self):
        """float = Duration()"""
        ...

    def Filename(self):
        """string = Filename()"""
        ...

    def Frequency(self):
        """integer = Frequency()"""
        ...

    def Read(self, buff):
        """(integer frames,integer eof) = Read(data[] buff)"""
        ...

    def Sample(self, time, type, value):
        """Sample(float time,integer type,data[] value)"""
        ...

    def Seek(self, frame):
        """Seek(integer frame)"""
        ...

    def Size(self):
        """integer = Size()"""
        ...

    def Tell(self):
        """integer = Tell()"""
        ...

    def TrimStart(self):
        """float = TrimStart()"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class AudioDevice(object):
    def __init__(self, *args, **kwargs):
        ...

    def Handle(self, audio):
        """AudioHandle object = Handle(object audio)"""
        ...

    def PlayFile(self, filePath):
        """PlayFile(string filePath)"""
        ...

    def PlayRange(self, audio, start, end, volume, pitch):
        """PlayRange(object audio,float start,float end,float volume,float pitch)"""
        ...

    def Playing(self):
        """integer = Playing()"""
        ...

    def StopAll(self):
        """StopAll()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class AudioHandle(object):
    def __init__(self, *args, **kwargs):
        ...

    def Audio(self):
        """object = Audio()"""
        ...

    def Loop(self):
        """Loop()"""
        ...

    def Offset(self):
        """float = Offset()"""
        ...

    def Pause(self):
        """Pause()"""
        ...

    def Pitch(self):
        """float = Pitch()"""
        ...

    def Play(self, forward):
        """Play(integer forward)"""
        ...

    def Resume(self):
        """Resume()"""
        ...

    def SetLoop(self, loop):
        """SetLoop(integer loop)"""
        ...

    def SetOffset(self, offset):
        """SetOffset(float offset)"""
        ...

    def SetPitch(self, pitch):
        """SetPitch(float pitch)"""
        ...

    def SetVolume(self, volume):
        """SetVolume(float volume)"""
        ...

    def State(self):
        """integer state = State()"""
        ...

    def Stop(self):
        """Stop()"""
        ...

    def Volume(self):
        """float = Volume()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class AudioLoaderTarget(object):
    def __init__(self, *args, **kwargs):
        ...

    def SetChannels(self, channels):
        """SetChannels(integer channels)"""
        ...

    def SetFrequency(self, frequency):
        """SetFrequency(integer frequency)"""
        ...

    def SetSamples(self, samples):
        """SetSamples(integer samples)"""
        ...

    def SetType(self, type):
        """SetType(integer type)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class AudioWrite(object):
    def __init__(self, *args, **kwargs):
        ...

    def SetDuration(self, duration):
        """SetDuration(float duration)"""
        ...

    def SetSample(self, time, type, value):
        """SetSample(float time,integer type,data[] value)"""
        ...

    def SetStart(self, start):
        """SetStart(float start)"""
        ...

    def Write(self, data):
        """integer frames = Write(data[] data)"""
        ...

    def WriteEnd(self):
        """WriteEnd()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class AutoSaveListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def AutoSaveNow(self):
        """AutoSaveNow()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class BagGenerator(object):
    def __init__(self, *args, **kwargs):
        ...

    def Dispose(self, data):
        """Dispose(pointer data)"""
        ...

    def Generate(self, data, cloneMe):
        """pointer = Generate(pointer data,pointer cloneMe)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class BasePathAddDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddBasePath(self, setName, path):
        """AddBasePath(string setName,string path)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class BlockRead(object):
    def __init__(self, *args, **kwargs):
        ...

    def Depth(self):
        """integer = Depth()"""
        ...

    def End(self):
        """End()"""
        ...

    def FindBlock(self, head, flags):
        """integer blkId = FindBlock(blocks head,integer flags)"""
        ...

    def ReadFP(self, count):
        """(float data,integer ocount) = ReadFP(integer count)"""
        ...

    def ReadFP8(self, count):
        """(float data,integer ocount) = ReadFP8(integer count)"""
        ...

    def ReadI1(self, data, count):
        """integer ocount = ReadI1(byte[] data,integer count)"""
        ...

    def ReadI4(self, data, count):
        """integer ocount = ReadI4(int[] data,integer count)"""
        ...

    def ReadIDCode(self, list):
        """integer idCode = ReadIDCode(blocks list)"""
        ...

    def ReadString(self, buf, max, flags):
        """integer ocount = ReadString(byte[] buf,integer max,integer flags)"""
        ...

    def ReadU2(self, count):
        """(integer data,integer ocount) = ReadU2(integer count)"""
        ...

    def ReadU4(self, count):
        """(integer data,integer ocount) = ReadU4(integer count)"""
        ...

    def ReadVX(self, count):
        """(integer data,integer ocount) = ReadVX(integer count)"""
        ...

    def SetMiniBlockHeight(self, mini):
        """SetMiniBlockHeight(integer mini)"""
        ...

    def SetSourceEncoding(self, encoding):
        """SetSourceEncoding(integer encoding)"""
        ...

    def SetTargetEncoding(self, encoding):
        """SetTargetEncoding(integer encoding)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class BlockStore(object):
    def __init__(self, *args, **kwargs):
        ...

    def AllocBookmark(self):
        """id loc = AllocBookmark()"""
        ...

    def ByIndex(self, type, index, parent):
        """ByIndex(integer type,integer index,id parent)"""
        ...

    def Count(self, type, parent):
        """integer count = Count(integer type,id parent)"""
        ...

    def Delete(self):
        """Delete()"""
        ...

    def Ident(self):
        """string id = Ident()"""
        ...

    def Lookup(self, type, id, parent):
        """Lookup(integer type,string id,id parent)"""
        ...

    def ReadBlock(self, buf, offset, size):
        """ReadBlock(pointer buf,integer offset,integer size)"""
        ...

    def RestoreBookmark(self, loc):
        """RestoreBookmark(id loc)"""
        ...

    def SaveBookmark(self, loc):
        """SaveBookmark(id loc)"""
        ...

    def Stack(self, operation):
        """Stack(integer operation)"""
        ...

    def Type(self):
        """integer type = Type()"""
        ...

    def WriteBlock(self, buf, offset, size):
        """WriteBlock(data[] buf,integer offset,integer size)"""
        ...

    def WriteSize(self, size):
        """WriteSize(integer size)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class BlockWrite(object):
    def __init__(self, *args, **kwargs):
        ...

    def Depth(self):
        """integer = Depth()"""
        ...

    def End(self):
        """End()"""
        ...

    def SetSourceEncoding(self, encoding):
        """SetSourceEncoding(integer encoding)"""
        ...

    def SetTargetEncoding(self, encoding):
        """SetTargetEncoding(integer encoding)"""
        ...

    def WriteBlock(self, head, flags):
        """WriteBlock(blocks head,integer flags)"""
        ...

    def WriteFP(self, data, count):
        """WriteFP(float[] data,integer count)"""
        ...

    def WriteFP8(self, data, count):
        """WriteFP8(double[] data,integer count)"""
        ...

    def WriteI1(self, data, count):
        """WriteI1(string data,integer count)"""
        ...

    def WriteI4(self, data, count):
        """WriteI4(int[] data,integer count)"""
        ...

    def WriteIDCode(self, ident):
        """WriteIDCode(blocks ident)"""
        ...

    def WriteString(self, str):
        """WriteString(string str)"""
        ...

    def WriteU4(self, data, count):
        """WriteU4(unsigned[] data,integer count)"""
        ...

    def WriteVX(self, data, count):
        """WriteVX(unsigned[] data,integer count)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Buffer(object):
    def __init__(self, *args, **kwargs):
        ...

    def Clear(self, x, y):
        """Clear(integer x,integer y)"""
        ...

    def CreateImageTileTree(self):
        """CreateImageTileTree()"""
        ...

    def DataType(self):
        """integer = DataType()"""
        ...

    def DecrementTileTreeSize(self):
        """DecrementTileTreeSize()"""
        ...

    def DestroyImageTileTree(self):
        """DestroyImageTileTree()"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def GetImageTileTree(self):
        """id = GetImageTileTree()"""
        ...

    def GetSize(self):
        """(integer width,integer height) = GetSize()"""
        ...

    def IncrementTileTreeSize(self):
        """IncrementTileTreeSize()"""
        ...

    def Line(self, y):
        """pointer = Line(integer y)"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def Pixel(self, x, y):
        """pointer = Pixel(integer x,integer y)"""
        ...

    def ResetImageTileTree(self):
        """ResetImageTileTree()"""
        ...

    def SetEyeSide(self, eyeSide):
        """SetEyeSide(integer eyeSide)"""
        ...

    def SetFlags(self, flags):
        """SetFlags(integer flags)"""
        ...

    def SetSize(self, width, height, writeBucketsToDisk, isStereo):
        """SetSize(integer width,integer height,integer writeBucketsToDisk,integer isStereo)"""
        ...

    def SetUserName(self, name):
        """SetUserName(string name)"""
        ...

    def UserName(self):
        """string name = UserName()"""
        ...

    def VectorType(self):
        """object = VectorType()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class CacheData(object):
    def __init__(self, *args, **kwargs):
        ...

    def Size(self):
        """integer = Size()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class CenterPacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Item(self, packet):
        """Item object = Item(pointer packet)"""
        ...

    def Packet(self, item):
        """pointer = Packet(object item)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ChannelDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Channel(self):
        """Value object = Channel()"""
        ...

    def Location(self):
        """integer = Location()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ChannelDropPreview(object):
    def __init__(self, *args, **kwargs):
        ...

    def MarkChannel(self):
        """integer = MarkChannel()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ChannelGraph(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddLink(self, from_obj, fromChan, to_obj, toChan):
        """AddLink(object from_obj,integer fromChan,object to_obj,integer toChan)"""
        ...

    def DeleteLink(self, from_obj, fromChan, to_obj, toChan):
        """DeleteLink(object from_obj,integer fromChan,object to_obj,integer toChan)"""
        ...

    def FwdByIndex(self, item, channel, index):
        """(Item object,integer objChan) = FwdByIndex(object item,integer channel,integer index)"""
        ...

    def FwdCount(self, item, channel):
        """integer count = FwdCount(object item,integer channel)"""
        ...

    def RevByIndex(self, item, channel, index):
        """(Item object,integer objChan) = RevByIndex(object item,integer channel,integer index)"""
        ...

    def RevCount(self, item, channel):
        """integer count = RevCount(object item,integer channel)"""
        ...

    def SetLink(self, from_obj, fromChan, fromIndex, to_obj, toChan, toIndex):
        """SetLink(object from_obj,integer fromChan,integer fromIndex,object to_obj,integer toChan,integer toIndex)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ChannelModSetup(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddChannel(self, name, flags):
        """AddChannel(string name,integer flags)"""
        ...

    def AddTime(self):
        """AddTime()"""
        ...

    def GetEvaluation(self):
        """object = GetEvaluation()"""
        ...

    def ReadArray(self, name):
        """ValueArray object = ReadArray(string name)"""
        ...

    def ReadTimeValue(self):
        """Value object = ReadTimeValue()"""
        ...

    def ReadValue(self, name):
        """Value object = ReadValue(string name)"""
        ...

    def WriteValue(self, name):
        """Value object = WriteValue(string name)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ChannelModifier(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddInput(self, item, index):
        """AddInput(object item,integer index)"""
        ...

    def AddOutput(self, item, index):
        """AddOutput(object item,integer index)"""
        ...

    def AddTime(self):
        """AddTime()"""
        ...

    def InputCount(self, index):
        """integer nInputs = InputCount(integer index)"""
        ...

    def OutputCount(self, index):
        """integer nOutputs = OutputCount(integer index)"""
        ...

    def ReadInputAngle(self, attr, inputIndex):
        """float dVal = ReadInputAngle(object attr,integer inputIndex)"""
        ...

    def ReadInputFloat(self, attr, inputIndex):
        """float dVal = ReadInputFloat(object attr,integer inputIndex)"""
        ...

    def ReadInputFloatByIndex(self, attr, inputIndex, linkIndex):
        """float dVal = ReadInputFloatByIndex(object attr,integer inputIndex,integer linkIndex)"""
        ...

    def ReadInputInt(self, attr, inputIndex):
        """integer iVal = ReadInputInt(object attr,integer inputIndex)"""
        ...

    def ReadInputIntByIndex(self, attr, inputIndex, linkIndex):
        """integer iVal = ReadInputIntByIndex(object attr,integer inputIndex,integer linkIndex)"""
        ...

    def WriteOutputFloat(self, attr, outputIndex, dVal):
        """WriteOutputFloat(object attr,integer outputIndex,float dVal)"""
        ...

    def WriteOutputInt(self, attr, outputIndex, iVal):
        """WriteOutputInt(object attr,integer outputIndex,integer iVal)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ChannelPacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Index(self, packet):
        """integer = Index(pointer packet)"""
        ...

    def Item(self, packet):
        """Item object = Item(pointer packet)"""
        ...

    def Packet(self, item, index):
        """pointer = Packet(object item,integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ChannelRead(object)(object):
    def __init__(self, *args, **kwargs):
        ...

    def BakedSamples(self, item, channel):
        """(float firstSample,float spsRate,ValueArray object) = BakedSamples(object item,integer channel)"""
        ...

    def Double(self, item, channel):
        """float value = Double(object item,integer channel)"""
        ...

    def EncodedInt(self, item, channel):
        """string = EncodedInt(object item,integer channel)"""
        ...

    def Envelope(self, item, channel):
        """Envelope object = Envelope(object item,integer channel)"""
        ...

    def Integer(self, item, channel):
        """integer value = Integer(object item,integer channel)"""
        ...

    def IsAnimated(self, item, index):
        """integer = IsAnimated(object item,integer index)"""
        ...

    def IsBaked(self, item, channel):
        """boolean = IsBaked(object item,integer channel)"""
        ...

    def SetTime(self, time):
        """SetTime(float time)"""
        ...

    def String(self, item, channel):
        """string value = String(object item,integer channel)"""
        ...

    def Time(self):
        """float = Time()"""
        ...

    def Type(self, item, channel):
        """integer type = Type(object item,integer channel)"""
        ...

    def TypeName(self, item, channel):
        """string typeName = TypeName(object item,integer channel)"""
        ...

    def ValueObj(self, item, channel):
        """Unknown object = ValueObj(object item,integer channel)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ChannelUI(object):
    def __init__(self, *args, **kwargs):
        ...

    def Cookie(self, channelName, requestedFor):
        """string cookie = Cookie(string channelName,string requestedFor)"""
        ...

    def DependencyByIndex(self, channelName, index):
        """(integer depItemType,string depChannelName) = DependencyByIndex(string channelName,integer index)"""
        ...

    def DependencyByIndexName(self, channelName, index):
        """(string depItemTypeName,string depChannelName) = DependencyByIndexName(string channelName,integer index)"""
        ...

    def DependencyCount(self, channelName):
        """integer count = DependencyCount(string channelName)"""
        ...

    def Enabled(self, channelName, msg, item, chanRead):
        """Enabled(string channelName,object msg,object item,object chanRead)"""
        ...

    def ItemEnabled(self, msg, item):
        """ItemEnabled(object msg,object item)"""
        ...

    def ItemIcon(self, item):
        """string icon = ItemIcon(object item)"""
        ...

    def UIHints(self, channelName, hints):
        """UIHints(string channelName,object hints)"""
        ...

    def UIValueHints(self, channelName):
        """UIValueHints object = UIValueHints(string channelName)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ChannelWrite(object):
    def __init__(self, *args, **kwargs):
        ...

    def BakeSamples(self, item, channel, firstSample, spsRate):
        """ValueArray object = BakeSamples(object item,integer channel,float firstSample,float spsRate)"""
        ...

    def Double(self, item, channel, value):
        """Double(object item,integer channel,float value)"""
        ...

    def DoubleKey(self, item, channel, value, create):
        """DoubleKey(object item,integer channel,float value,integer create)"""
        ...

    def EncodedInt(self, item, channel, value):
        """EncodedInt(object item,integer channel,string value)"""
        ...

    def EncodedIntKey(self, item, channel, value):
        """EncodedIntKey(object item,integer channel,string value)"""
        ...

    def Envelope(self, item, channel):
        """Envelope object = Envelope(object item,integer channel)"""
        ...

    def Integer(self, item, channel, value):
        """Integer(object item,integer channel,integer value)"""
        ...

    def IntegerKey(self, item, channel, value, create):
        """IntegerKey(object item,integer channel,integer value,integer create)"""
        ...

    def SetState(self, item, channel, state):
        """SetState(object item,integer channel,integer state)"""
        ...

    def String(self, item, channel, value):
        """String(object item,integer channel,string value)"""
        ...

    def Type(self, item, channel):
        """integer type = Type(object item,integer channel)"""
        ...

    def TypeName(self, item, channel):
        """string typeName = TypeName(object item,integer channel)"""
        ...

    def ValueObj(self, item, channel):
        """Unknown object = ValueObj(object item,integer channel)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ClipDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Item(self):
        """Unknown object = Item()"""
        ...

    def Location(self):
        """integer = Location()"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class CmdSysListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def AliasAdded(self, name, isOverride):
        """AliasAdded(string name,integer isOverride)"""
        ...

    def AliasRemoved(self, name, isOverride):
        """AliasRemoved(string name,integer isOverride)"""
        ...

    def BlockBegin(self, block, isSandboxed):
        """BlockBegin(object block,integer isSandboxed)"""
        ...

    def BlockEnd(self, block, isSandboxed, wasDiscarded):
        """BlockEnd(object block,integer isSandboxed,integer wasDiscarded)"""
        ...

    def BlockEndedPostMode(self, name, isSandboxed):
        """BlockEndedPostMode(string name,integer isSandboxed)"""
        ...

    def CommandAdded(self, name):
        """CommandAdded(string name)"""
        ...

    def ExecutePost(self, cmd, isSandboxed, isPostCmd):
        """ExecutePost(object cmd,integer isSandboxed,integer isPostCmd)"""
        ...

    def ExecutePre(self, cmd, type, isSandboxed, isPostCmd):
        """ExecutePre(object cmd,integer type,integer isSandboxed,integer isPostCmd)"""
        ...

    def ExecuteResult(self, cmd, type, isSandboxed, isPostCmd, wasSuccessful):
        """ExecuteResult(object cmd,integer type,integer isSandboxed,integer isPostCmd,integer wasSuccessful)"""
        ...

    def PostModeBegin(self):
        """PostModeBegin()"""
        ...

    def PostModeEnd(self):
        """PostModeEnd()"""
        ...

    def PostModeRestart(self):
        """PostModeRestart()"""
        ...

    def PostModeUndoNext(self):
        """PostModeUndoNext()"""
        ...

    def RefireBegin(self):
        """RefireBegin()"""
        ...

    def RefireEnd(self):
        """RefireEnd()"""
        ...

    def RefiringNext(self):
        """RefiringNext()"""
        ...

    def SystemReady(self):
        """SystemReady()"""
        ...

    def UndoLockout(self, isLockedOut):
        """UndoLockout(integer isLockedOut)"""
        ...

    def UserRedo(self):
        """UserRedo()"""
        ...

    def UserUndo(self):
        """UserUndo()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Color(object):
    def __init__(self, *args, **kwargs):
        ...

    def Alpha(self):
        """float alpha = Alpha()"""
        ...

    def Color(self):
        """float color = Color()"""
        ...

    def ColorInModelSpace(self):
        """float vec = ColorInModelSpace()"""
        ...

    def ColorModel(self):
        """string model = ColorModel()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ColorDialog(object):
    def __init__(self, *args, **kwargs):
        ...

    def DoDialog(self, title, stops, gamma):
        """float rgb = DoDialog(string title,float stops,float gamma)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ColorMapping(object):
    def __init__(self, *args, **kwargs):
        ...

    def FromLinear(self, linearValues, length):
        """vector targetValues = FromLinear(vector linearValues,integer length)"""
        ...

    def FromLinearFast(self, length):
        """float buf = FromLinearFast(integer length)"""
        ...

    def GetCMServerName(self):
        """string = GetCMServerName()"""
        ...

    def GetName(self):
        """string = GetName()"""
        ...

    def Setup(self, toLinear):
        """Setup(integer toLinear)"""
        ...

    def ToLinear(self, sourceValues, length):
        """vector linearValues = ToLinear(vector sourceValues,integer length)"""
        ...

    def ToLinearFast(self, length):
        """float buf = ToLinearFast(integer length)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ColorMappingModule(object):
    def __init__(self, *args, **kwargs):
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ColorModel(object):
    def __init__(self, *args, **kwargs):
        ...

    def CanSliceBeReused(self, xAxis, yAxis, oldVec, newVec):
        """boolean = CanSliceBeReused(integer xAxis,integer yAxis,float[] oldVec,float[] newVec)"""
        ...

    def ComponentRange(self, component):
        """(float min,float max) = ComponentRange(integer component)"""
        ...

    def ComponentType(self, component):
        """string type = ComponentType(integer component)"""
        ...

    def DrawSlice(self, image, xAxis, yAxis, vec):
        """DrawSlice(object image,integer xAxis,integer yAxis,float[] vec)"""
        ...

    def DrawSliceMarker(self, image, xAxis, yAxis, downVec, vec):
        """DrawSliceMarker(object image,integer xAxis,integer yAxis,float[] downVec,float[] vec)"""
        ...

    def FromRGB(self, rgb, vector):
        """FromRGB(float[] rgb,float[] vector)"""
        ...

    def FromSlicePos(self, xAxis, yAxis, imgW, imgH, imgX, imgY, downVec, vec):
        """FromSlicePos(integer xAxis,integer yAxis,integer imgW,integer imgH,integer imgX,integer imgY,float[] downVec,float[] vec)"""
        ...

    def NumComponents(self):
        """integer = NumComponents()"""
        ...

    def StripBaseVector(self, axis, dynamic, vec):
        """StripBaseVector(integer axis,integer dynamic,float[] vec)"""
        ...

    def ToRGB(self, vector, rgb):
        """ToRGB(float[] vector,float[] rgb)"""
        ...

    def ToSlicePos(self, xAxis, yAxis, imgW, imgH, vec):
        """(integer imgX,integer imgY) = ToSlicePos(integer xAxis,integer yAxis,integer imgW,integer imgH,float[] vec)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ColorPreDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Apply(self):
        """Apply()"""
        ...

    def SetColor(self, rgb):
        """SetColor(vector rgb)"""
        ...

    def SetColorModel(self, name, vec):
        """SetColorModel(string name,double[] vec)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Command(object):
    def __init__(self, *args, **kwargs):
        ...

    def ArgClear(self, index):
        """ArgClear(integer index)"""
        ...

    def ArgDesc(self, index):
        """string desc = ArgDesc(integer index)"""
        ...

    def ArgEnable(self, arg):
        """ArgEnable(integer arg)"""
        ...

    def ArgExample(self, index):
        """string example = ArgExample(integer index)"""
        ...

    def ArgFlags(self, index):
        """integer flags = ArgFlags(integer index)"""
        ...

    def ArgOptionDesc(self, index, optIndex):
        """string desc = ArgOptionDesc(integer index,integer optIndex)"""
        ...

    def ArgOptionUserName(self, index, optIndex):
        """string userName = ArgOptionUserName(integer index,integer optIndex)"""
        ...

    def ArgParseString(self, argIndex, argString):
        """ArgParseString(integer argIndex,string argString)"""
        ...

    def ArgResetAll(self):
        """ArgResetAll()"""
        ...

    def ArgSetDatatypes(self):
        """ArgSetDatatypes()"""
        ...

    def ArgType(self, index):
        """string type = ArgType(integer index)"""
        ...

    def ArgTypeDesc(self, index):
        """string desc = ArgTypeDesc(integer index)"""
        ...

    def ArgTypeUserName(self, index):
        """string userName = ArgTypeUserName(integer index)"""
        ...

    def ArgUserName(self, index):
        """string userName = ArgUserName(integer index)"""
        ...

    def ButtonName(self):
        """string buttonName = ButtonName()"""
        ...

    def ContainedEnable(self):
        """integer types = ContainedEnable()"""
        ...

    def Copy(self, sourceCommand):
        """Copy(object sourceCommand)"""
        ...

    def Desc(self):
        """string desc = Desc()"""
        ...

    def DialogArgChange(self, arg):
        """DialogArgChange(integer arg)"""
        ...

    def DialogFormatting(self):
        """string formatting = DialogFormatting()"""
        ...

    def DialogInit(self):
        """DialogInit()"""
        ...

    def Enable(self, msg):
        """Enable(object msg)"""
        ...

    def Example(self):
        """string example = Example()"""
        ...

    def Execute(self, flags):
        """Execute(integer flags)"""
        ...

    def Flags(self):
        """integer flags = Flags()"""
        ...

    def Help(self):
        """string help = Help()"""
        ...

    def Icon(self):
        """string iconNames = Icon()"""
        ...

    def IconImage(self, w, h):
        """Image object = IconImage(integer w,integer h)"""
        ...

    def Interact(self):
        """Interact()"""
        ...

    def Message(self):
        """Message object = Message()"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def NotifyAddClient(self, argument, object):
        """NotifyAddClient(integer argument,object object)"""
        ...

    def NotifyRemoveClient(self, object):
        """NotifyRemoveClient(object object)"""
        ...

    def PostExecBehaviorFlags(self):
        """integer flags = PostExecBehaviorFlags()"""
        ...

    def PostExecFlags(self):
        """integer flags = PostExecFlags()"""
        ...

    def PostExecHints(self):
        """integer hints = PostExecHints()"""
        ...

    def PreExecute(self):
        """PreExecute()"""
        ...

    def Query(self, index, vaQuery):
        """Query(integer index,object vaQuery)"""
        ...

    def SandboxGUID(self):
        """string guid = SandboxGUID()"""
        ...

    def Tag(self):
        """integer tag = Tag()"""
        ...

    def ToggleArg(self):
        """(integer index,Value object,integer typeID,string typeName) = ToggleArg()"""
        ...

    def Tooltip(self):
        """string tooltip = Tooltip()"""
        ...

    def UserName(self):
        """string userName = UserName()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class CommandDBHelp(object):
    def __init__(self, *args, **kwargs):
        ...

    def DBHelp(self):
        """string dbhelp = DBHelp()"""
        ...

    def DBTooltip(self):
        """string dbtooltip = DBTooltip()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class CommandEvent(object):
    def __init__(self, *args, **kwargs):
        ...

    def Event(self, flags):
        """Event(integer flags)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class CompShader(object):
    def __init__(self, *args, **kwargs):
        ...

    def Cleanup(self, data):
        """Cleanup(pointer data)"""
        ...

    def CustomPacket(self):
        """string packet = CustomPacket()"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def LinkChannels(self, eval, item):
        """LinkChannels(object eval,object item)"""
        ...

    def SetOpaque(self):
        """integer opaque = SetOpaque()"""
        ...

    def SetupChannels(self, addChan):
        """SetupChannels(object addChan)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Curve(object):
    def __init__(self, *args, **kwargs):
        ...

    def BendCount(self):
        """integer = BendCount()"""
        ...

    def Closest(self, probe):
        """(float param,vector pos,vector norm) = Closest(vector probe)"""
        ...

    def Curvature(self):
        """float curv = Curvature()"""
        ...

    def GetBBox(self):
        """bounds bbox = GetBBox()"""
        ...

    def GuideCurveNormal(self, other):
        """vector normal = GuideCurveNormal(object other)"""
        ...

    def IsClosed(self):
        """boolean = IsClosed()"""
        ...

    def LenFraction(self):
        """float = LenFraction()"""
        ...

    def Length(self):
        """float = Length()"""
        ...

    def MeshNormal(self, meshObj):
        """(matrix xfrm,vector normal) = MeshNormal(object meshObj)"""
        ...

    def Normal(self):
        """vector normal = Normal()"""
        ...

    def Param(self):
        """float = Param()"""
        ...

    def Position(self):
        """vector pos = Position()"""
        ...

    def SetLenFraction(self, frac):
        """SetLenFraction(float frac)"""
        ...

    def SetParam(self, param):
        """SetParam(float param)"""
        ...

    def SplineByIndex(self, index):
        """(vector b0,vector b1,vector b2,vector b3) = SplineByIndex(integer index)"""
        ...

    def SplineCount(self):
        """integer count = SplineCount()"""
        ...

    def SplineLengthByIndex(self, index):
        """float length = SplineLengthByIndex(integer index)"""
        ...

    def Tangent(self):
        """vector tan = Tangent()"""
        ...

    def WalkByAngle(self, start, end, angle, visitor):
        """WalkByAngle(float start,float end,float angle,object visitor)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class CurveGroup(object):
    def __init__(self, *args, **kwargs):
        ...

    def ByIndex(self, index):
        """Curve object = ByIndex(integer index)"""
        ...

    def Count(self):
        """integer count = Count()"""
        ...

    def GetBBox(self):
        """bounds bbox = GetBBox()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class CustomMaterial(object):
    def __init__(self, *args, **kwargs):
        ...

    def Cleanup(self, data):
        """Cleanup(pointer data)"""
        ...

    def CustomPacket(self):
        """string packet = CustomPacket()"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def IsSampleDriven(self):
        """(integer,integer idx) = IsSampleDriven()"""
        ...

    def LinkChannels(self, eval, item):
        """LinkChannels(object eval,object item)"""
        ...

    def LinkSampleChannels(self, nodalEtor, item):
        """integer idx = LinkSampleChannels(object nodalEtor,object item)"""
        ...

    def MaterialEvaluate(self, etor, vector, data):
        """integer idx = MaterialEvaluate(object etor,object vector,pointer data)"""
        ...

    def SetBump(self):
        """(float bumpAmplitude,integer clearBump) = SetBump()"""
        ...

    def SetDisplacement(self):
        """float dispDist = SetDisplacement()"""
        ...

    def SetOpaque(self):
        """integer opaque = SetOpaque()"""
        ...

    def SetSmoothing(self):
        """(float smooth,float angle,integer weighting,integer normalMethod,integer creasing) = SetSmoothing()"""
        ...

    def SetupChannels(self, addChan):
        """SetupChannels(object addChan)"""
        ...

    def UpdatePreview(self, chanIdx):
        """integer flags = UpdatePreview(integer chanIdx)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class CustomPane(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetIdentifier(self):
        """string ident = GetIdentifier()"""
        ...

    def GetParent(self):
        """id handle = GetParent()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class CustomView(object):
    def __init__(self, *args, **kwargs):
        ...

    def Cleanup(self, pane):
        """Cleanup(object pane)"""
        ...

    def Init(self, pane):
        """Init(object pane)"""
        ...

    def RestoreState(self, pane):
        """RestoreState(object pane)"""
        ...

    def StoreState(self, pane):
        """StoreState(object pane)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DTBBadgeOverride(object):
    def __init__(self, *args, **kwargs):
        ...

    def BadgeAction(self, entry, badge):
        """BadgeAction(object entry,integer badge)"""
        ...

    def BadgeIsAlwaysVisible(self, entry, badge):
        """boolean = BadgeIsAlwaysVisible(object entry,integer badge)"""
        ...

    def BadgeOverride(self, entry, badge):
        """string = BadgeOverride(object entry,integer badge)"""
        ...

    def BadgeStarRatingAction(self, entry, rating):
        """BadgeStarRatingAction(object entry,integer rating)"""
        ...

    def BadgeStarRatingOverride(self, entry):
        """(integer rating,string) = BadgeStarRatingOverride(object entry)"""
        ...

    def BadgeTooltip(self, entry, badge):
        """string = BadgeTooltip(object entry,integer badge)"""
        ...

    def BadgesSupported(self, entry):
        """integer badges = BadgesSupported(object entry)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DTBDropPreview(object):
    def __init__(self, *args, **kwargs):
        ...

    def MarkAnywhere(self, path):
        """MarkAnywhere(string path)"""
        ...

    def MarkBetween(self, path, markBefore):
        """MarkBetween(string path,integer markBefore)"""
        ...

    def MarkEntry(self, path):
        """MarkEntry(string path)"""
        ...

    def MarkGridPos(self, path, x, y):
        """MarkGridPos(string path,integer x,integer y)"""
        ...

    def MarkNone(self):
        """MarkNone()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DTBGroupSortOverride(object):
    def __init__(self, *args, **kwargs):
        ...

    def SetArguments(self, args):
        """SetArguments(string args)"""
        ...

    def Sort(self, string1, string2):
        """integer = Sort(string string1,string string2)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Deformation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def OBSOLETE(self):
        """OBSOLETE()"""
        ...

    def OffsetF(self, position, idx, weight):
        """vector offset = OffsetF(vector position,integer idx,float weight)"""
        ...

    def Transform(self):
        """matrix xfrm = Transform()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Deformer(object):
    def __init__(self, *args, **kwargs):
        ...

    def Element(self):
        """(id,integer segment) = Element()"""
        ...

    def EnumeratePartition(self, visitor, part):
        """EnumeratePartition(object visitor,integer part)"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def Offset(self, elt, weight, pos, idx):
        """vector offset = Offset(id elt,float weight,vector pos,integer idx)"""
        ...

    def PartitionCount(self):
        """integer = PartitionCount()"""
        ...

    def SetPartition(self, part):
        """SetPartition(integer part)"""
        ...

    def Weight(self, elt, pos, idx):
        """float = Weight(id elt,vector pos,integer idx)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DirBrowserBasePathEntryDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def OrdinalAfter(self):
        """string ordinal = OrdinalAfter()"""
        ...

    def OrdinalBefore(self):
        """string ordinal = OrdinalBefore()"""
        ...

    def SetPath(self):
        """string path = SetPath()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DirCacheEntry(object):
    def __init__(self, *args, **kwargs):
        ...

    def CachedThumbnail(self, size):
        """(integer idealW,integer idealH,Image object) = CachedThumbnail(integer size)"""
        ...

    def CachedThumbnailAsync(self, size, asyncHandler):
        """(integer idealW,integer idealH,Image object) = CachedThumbnailAsync(integer size,object asyncHandler)"""
        ...

    def CachedThumbnailCustom(self, w, h):
        """(integer idealW,integer idealH,Image object) = CachedThumbnailCustom(integer w,integer h)"""
        ...

    def CachedThumbnailCustomAsync(self, w, h, asyncHandler):
        """(integer idealW,integer idealH,Image object) = CachedThumbnailCustomAsync(integer w,integer h,object asyncHandler)"""
        ...

    def ChildGridPositionLookup(self, childPath):
        """(integer x,integer y) = ChildGridPositionLookup(string childPath)"""
        ...

    def ChildGridPositionSet(self, childPath, x, y):
        """ChildGridPositionSet(string childPath,integer x,integer y)"""
        ...

    def ChildManualOrderLookup(self, childPath):
        """integer pos = ChildManualOrderLookup(string childPath)"""
        ...

    def ChildManualOrderSet(self, childPath, pos):
        """ChildManualOrderSet(string childPath,integer pos)"""
        ...

    def CommitSharedMarkup(self, sharedMarkup):
        """CommitSharedMarkup(object sharedMarkup)"""
        ...

    def CommitUserMarkup(self, userMarkup):
        """CommitUserMarkup(object userMarkup)"""
        ...

    def Desc(self):
        """string = Desc()"""
        ...

    def DirCount(self, listMode):
        """integer = DirCount(integer listMode)"""
        ...

    def DirList(self, listMode, asCopy):
        """Array object = DirList(integer listMode,integer asCopy)"""
        ...

    def Extension(self):
        """string = Extension()"""
        ...

    def GridExtents(self):
        """(integer bottom,integer right) = GridExtents()"""
        ...

    def GridInsert(self, doRows, x, y, count):
        """GridInsert(integer doRows,integer x,integer y,integer count)"""
        ...

    def GridIsEmpty(self, doRows, x, y):
        """boolean = GridIsEmpty(integer doRows,integer x,integer y)"""
        ...

    def GridIsEmptyCell(self, x, y):
        """(boolean,DirCacheEntry object) = GridIsEmptyCell(integer x,integer y)"""
        ...

    def GridRemove(self, doRows, x, y, count, force):
        """GridRemove(integer doRows,integer x,integer y,integer count,integer force)"""
        ...

    def GridSetExtents(self, bottom, right):
        """GridSetExtents(integer bottom,integer right)"""
        ...

    def Label(self):
        """string = Label()"""
        ...

    def Metadata(self):
        """Attributes object = Metadata()"""
        ...

    def ModTime(self):
        """string = ModTime()"""
        ...

    def Name(self):
        """string = Name()"""
        ...

    def OverrideParent(self):
        """string = OverrideParent()"""
        ...

    def Parent(self):
        """DirCacheEntry object = Parent()"""
        ...

    def Path(self):
        """string = Path()"""
        ...

    def ReferenceSource(self):
        """DirCacheEntry object = ReferenceSource()"""
        ...

    def ReferencedCount(self):
        """integer = ReferencedCount()"""
        ...

    def ReferencedList(self, asCopy):
        """Array object = ReferencedList(integer asCopy)"""
        ...

    def SharedMarkup(self, asWritable):
        """Unknown object = SharedMarkup(integer asWritable)"""
        ...

    def Size(self):
        """float size = Size()"""
        ...

    def Thumbnail(self, w, h):
        """(integer idealW,integer idealH,Image object) = Thumbnail(integer w,integer h)"""
        ...

    def ToolTip(self):
        """string = ToolTip()"""
        ...

    def Type(self):
        """integer type = Type()"""
        ...

    def UserMarkup(self, asWritable):
        """Unknown object = UserMarkup(integer asWritable)"""
        ...

    def Username(self):
        """string = Username()"""
        ...

    def WasRecognized(self):
        """WasRecognized()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DirCacheFileMetrics(object):
    def __init__(self, *args, **kwargs):
        ...

    def Flags(self):
        """integer flags = Flags()"""
        ...

    def Markup(self):
        """Attributes object = Markup()"""
        ...

    def Metadata(self):
        """Attributes object = Metadata()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DirCacheGridPosDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def GridPos(self):
        """(DirCacheEntry object,integer x,integer y) = GridPos()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DirCacheManualOrderDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def BetweenPaths(self, asPaths):
        """(DirCacheEntry object,string nameBefore,string nameAfter) = BetweenPaths(integer asPaths)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DirCacheSynthetic(object):
    def __init__(self, *args, **kwargs):
        ...

    def Lookup(self, path):
        """DirCacheSyntheticEntry object = Lookup(string path)"""
        ...

    def Root(self):
        """DirCacheSyntheticEntry object = Root()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DirCacheSyntheticEntry(object):
    def __init__(self, *args, **kwargs):
        ...

    def DirBuild(self):
        """DirBuild()"""
        ...

    def DirByIndex(self, listMode, index):
        """DirCacheSyntheticEntry object = DirByIndex(integer listMode,integer index)"""
        ...

    def DirCount(self, listMode):
        """integer = DirCount(integer listMode)"""
        ...

    def DirUsername(self):
        """string = DirUsername()"""
        ...

    def FileExtension(self):
        """string = FileExtension()"""
        ...

    def IsFile(self):
        """boolean = IsFile()"""
        ...

    def ModTime(self):
        """string = ModTime()"""
        ...

    def Name(self):
        """string = Name()"""
        ...

    def OverrideParent(self):
        """string = OverrideParent()"""
        ...

    def Path(self):
        """string = Path()"""
        ...

    def Size(self):
        """float = Size()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DirEntryThumbAsync(object):
    def __init__(self, *args, **kwargs):
        ...

    def Failed(self, dirCacheEntry):
        """Failed(object dirCacheEntry)"""
        ...

    def Ident(self):
        """string ident = Ident()"""
        ...

    def Ready(self, dirCacheEntry, idealW, idealH, image):
        """Ready(object dirCacheEntry,integer idealW,integer idealH,object image)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DrawingOverride(object):
    def __init__(self, *args, **kwargs):
        ...

    def AffectedItems(self, scene, collection):
        """AffectedItems(object scene,object collection)"""
        ...

    def CleanupContext(self):
        """CleanupContext()"""
        ...

    def DrawVisitor(self, scene, view):
        """Unknown object = DrawVisitor(object scene,object view)"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def InitContext(self):
        """InitContext()"""
        ...

    def SetItem(self, item):
        """integer styles = SetItem(object item)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Drop(object):
    def __init__(self, *args, **kwargs):
        ...

    def ActionList(self, source, dest, addDropAction):
        """ActionList(object source,object dest,object addDropAction)"""
        ...

    def Drop(self, source, dest, action):
        """Drop(object source,object dest,integer action)"""
        ...

    def Preview(self, source, dest, action, draw):
        """Preview(object source,object dest,integer action,object draw)"""
        ...

    def Recognize(self, source):
        """Recognize(object source)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class DropPreviewDefault(object):
    def __init__(self, *args, **kwargs):
        ...

    def Draw(self):
        """Draw()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Edge(object):
    def __init__(self, *args, **kwargs):
        ...

    def ClearMapValue(self, map):
        """ClearMapValue(id map)"""
        ...

    def Endpoints(self):
        """(id point0,id point1) = Endpoints()"""
        ...

    def Enumerate(self, mode, visitor, monitor):
        """Enumerate(integer mode,object visitor,object monitor)"""
        ...

    def ID(self):
        """id = ID()"""
        ...

    def Index(self):
        """integer index = Index()"""
        ...

    def IsBorder(self):
        """boolean = IsBorder()"""
        ...

    def MapEvaluate(self, map, value):
        """boolean = MapEvaluate(id map,float[] value)"""
        ...

    def MapValue(self, map, value):
        """boolean = MapValue(id map,float[] value)"""
        ...

    def Mesh(self):
        """Unknown object = Mesh()"""
        ...

    def OnSymmetryCenter(self):
        """OnSymmetryCenter()"""
        ...

    def PolygonByIndex(self, index):
        """id polygonID = PolygonByIndex(integer index)"""
        ...

    def PolygonCount(self):
        """integer count = PolygonCount()"""
        ...

    def RepresentativePolygon(self):
        """(id polygonID,integer index) = RepresentativePolygon()"""
        ...

    def Select(self, edge):
        """Select(id edge)"""
        ...

    def SelectByIndex(self, index):
        """SelectByIndex(integer index)"""
        ...

    def SelectEndpoints(self, v0, v1):
        """SelectEndpoints(id v0,id v1)"""
        ...

    def SetMapValue(self, map, value):
        """SetMapValue(id map,float[] value)"""
        ...

    def SetMarks(self, set):
        """SetMarks(integer set)"""
        ...

    def SharedPolygon(self, edgeID):
        """id polygonID = SharedPolygon(id edgeID)"""
        ...

    def Spawn(self):
        """Edge object = Spawn()"""
        ...

    def Symmetry(self):
        """id edgeID = Symmetry()"""
        ...

    def TestMarks(self, mode):
        """boolean = TestMarks(integer mode)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class EdgePacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Item(self, packet):
        """Item object = Item(pointer packet)"""
        ...

    def Mesh(self, packet):
        """Mesh object = Mesh(pointer packet)"""
        ...

    def Packet(self, vertexA, vertexB, polygon, mesh):
        """pointer = Packet(id vertexA,id vertexB,id polygon,object mesh)"""
        ...

    def Polygon(self, packet):
        """id polygon = Polygon(pointer packet)"""
        ...

    def Vertices(self, packet):
        """(id vertexA,id vertexB) = Vertices(pointer packet)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ElementAxisPacket(object):
    def __init__(self, *args, **kwargs):
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ElementCenterPacket(object):
    def __init__(self, *args, **kwargs):
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Envelope(object):
    def __init__(self, *args, **kwargs):
        ...

    def Clear(self):
        """Clear()"""
        ...

    def EndBehavior(self, side):
        """integer = EndBehavior(integer side)"""
        ...

    def Enumerator(self):
        """Keyframe object = Enumerator()"""
        ...

    def EvaluateF(self, time):
        """float value = EvaluateF(float time)"""
        ...

    def EvaluateI(self, time):
        """integer value = EvaluateI(float time)"""
        ...

    def Interpolation(self):
        """integer = Interpolation()"""
        ...

    def IsInt(self):
        """integer = IsInt()"""
        ...

    def SetEndBehavior(self, behavior, side):
        """SetEndBehavior(integer behavior,integer side)"""
        ...

    def SetInterpolation(self, type):
        """SetInterpolation(integer type)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class EvalModifier(object):
    def __init__(self, *args, **kwargs):
        ...

    def Alloc(self, item, index, eval):
        """Unknown object = Alloc(object item,integer index,object eval)"""
        ...

    def Next(self):
        """(object,integer index) = Next()"""
        ...

    def Reset(self, scene):
        """Reset(object scene)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Evaluation(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddChannel(self, item, index, type):
        """integer attr = AddChannel(object item,integer index,integer type)"""
        ...

    def AddChannelName(self, item, name, type):
        """integer attr = AddChannelName(object item,string name,integer type)"""
        ...

    def ClearAlternate(self):
        """ClearAlternate()"""
        ...

    def GetBakedSample(self, index, bracket):
        """(float fraction,Unknown object) = GetBakedSample(integer index,integer bracket)"""
        ...

    def GetCache(self):
        """pointer = GetCache()"""
        ...

    def GetDT(self):
        """float = GetDT()"""
        ...

    def ReadTime(self):
        """integer attr = ReadTime()"""
        ...

    def SetAlternate(self):
        """ChannelWrite object = SetAlternate()"""
        ...

    def SetAlternateSetup(self):
        """SetAlternateSetup()"""
        ...

    def SetAlternateTime(self, time):
        """SetAlternateTime(float time)"""
        ...

    def SetCache(self, cache):
        """SetCache(pointer cache)"""
        ...

    def SimulationRange(self):
        """(float start,float end) = SimulationRange()"""
        ...

    def SimulationState(self):
        """integer flags = SimulationState()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class EvaluationStack(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddFilter(self, filter):
        """AddFilter(object filter)"""
        ...

    def Branch(self):
        """EvaluationStack object = Branch()"""
        ...

    def Type(self):
        """string = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class EventGuide(object):
    def __init__(self, *args, **kwargs):
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def Limits(self, inner, outer):
        """integer = Limits(float inner,float outer)"""
        ...

    def Proximity(self, toolVector, element):
        """(integer,vector pos,float dist,integer priority) = Proximity(object toolVector,pointer element)"""
        ...

    def SetDrawState(self, flags):
        """integer = SetDrawState(integer flags)"""
        ...

    def SetFlags(self, flags):
        """SetFlags(integer flags)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class EventTranslatePacket(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddGuide(self, guide, client):
        """AddGuide(object guide,pointer client)"""
        ...

    def GetConstraint(self, toolVector):
        """(integer,vector center,vector vector) = GetConstraint(object toolVector)"""
        ...

    def GetNewPosition(self, toolVector):
        """vector pos = GetNewPosition(object toolVector)"""
        ...

    def HitHandle(self, toolVector, handle):
        """HitHandle(object toolVector,vector handle)"""
        ...

    def ModelDelta(self, toolVector, handle):
        """vector delta = ModelDelta(object toolVector,vector handle)"""
        ...

    def ModelLineDelta(self, toolVector, center, dir, handle):
        """vector delta = ModelLineDelta(object toolVector,vector center,vector dir,vector handle)"""
        ...

    def ModelPlaneDelta(self, toolVector, center, normal, handle):
        """vector delta = ModelPlaneDelta(object toolVector,vector center,vector normal,vector handle)"""
        ...

    def RemoveGuide(self, guide, client):
        """integer = RemoveGuide(object guide,pointer client)"""
        ...

    def ScreenToRay(self, toolVector, x, y):
        """(vector pos,vector dir) = ScreenToRay(object toolVector,float x,float y)"""
        ...

    def SetLinearConstraint(self, toolVector, center, dir):
        """SetLinearConstraint(object toolVector,vector center,vector dir)"""
        ...

    def SetLinearSnapConstraint(self, toolVector, center, dir):
        """SetLinearSnapConstraint(object toolVector,vector center,vector dir)"""
        ...

    def SetPlanarConstraint(self, toolVector, center, normal):
        """SetPlanarConstraint(object toolVector,vector center,vector normal)"""
        ...

    def SetPlanarSnapConstraint(self, toolVector, center, dir):
        """SetPlanarSnapConstraint(object toolVector,vector center,vector dir)"""
        ...

    def SetSnapRange(self, inner, outer):
        """SetSnapRange(float inner,float outer)"""
        ...

    def SnapPosition(self, toolVector, pos):
        """(integer,vector snapPos) = SnapPosition(object toolVector,vector pos)"""
        ...

    def ToModel(self, toolVector):
        """(integer,vector pos,vector axis) = ToModel(object toolVector)"""
        ...

    def ToModelLine(self, toolVector, center, dir):
        """vector pos = ToModelLine(object toolVector,vector center,vector dir)"""
        ...

    def ToModelPlane(self, toolVector, center, normal):
        """vector pos = ToModelPlane(object toolVector,vector center,vector normal)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ExternalRender(object):
    def __init__(self, *args, **kwargs):
        ...

    def Pause(self):
        """Pause()"""
        ...

    def Reset(self):
        """Reset()"""
        ...

    def SetBufferQueue(self, bufferQueue):
        """SetBufferQueue(object bufferQueue)"""
        ...

    def SetNotifier(self, notifier):
        """SetNotifier(object notifier)"""
        ...

    def Start(self):
        """Start()"""
        ...

    def Stop(self):
        """Stop()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ExternalRenderBufferQueue(object):
    def __init__(self, *args, **kwargs):
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ExternalRenderNotifier(object):
    def __init__(self, *args, **kwargs):
        ...

    def SetStatusText(self, text):
        """SetStatusText(string text)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Factory(object):
    def __init__(self, *args, **kwargs):
        ...

    def InfoTag(self, type):
        """string value = InfoTag(string type)"""
        ...

    def Module(self):
        """string module = Module()"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def Spawn(self):
        """Unknown object = Spawn()"""
        ...

    def TagByIndex(self, index):
        """(string type,string value) = TagByIndex(integer index)"""
        ...

    def TagCount(self):
        """integer count = TagCount()"""
        ...

    def UserName(self):
        """string userName = UserName()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Falloff(object):
    def __init__(self, *args, **kwargs):
        ...

    def Bounds(self):
        """bounds box = Bounds()"""
        ...

    def SetMesh(self, mesh):
        """matrix xfrm = SetMesh(object mesh)"""
        ...

    def WeightF(self, position, point, polygon):
        """float = WeightF(vector position,id point,id polygon)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class FalloffPacket(object):
    def __init__(self, *args, **kwargs):
        ...

    def Screen(self, vts, x, y):
        """float = Screen(object vts,integer x,integer y)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class FileRedirect(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddSearchPath(self, path):
        """AddSearchPath(string path)"""
        ...

    def Locate(self, path, type):
        """string = Locate(string path,string type)"""
        ...

    def LocateSequence(self, pattern, type):
        """(integer first,integer last,string) = LocateSequence(string pattern,string type)"""
        ...

    def NeutralFormat(self, allow):
        """NeutralFormat(integer allow)"""
        ...

    def Reference(self, path):
        """string = Reference(string path)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class FileReference(object):
    def __init__(self, *args, **kwargs):
        ...

    def Mode(self):
        """integer mode = Mode()"""
        ...

    def NiceName(self):
        """string = NiceName()"""
        ...

    def Path(self):
        """string path = Path()"""
        ...

    def SubByIndex(self, index):
        """FileReference object = SubByIndex(integer index)"""
        ...

    def SubCount(self):
        """integer count = SubCount()"""
        ...

    def Type(self):
        """integer type = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class FileSysDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def AsDir(self):
        """string dir = AsDir()"""
        ...

    def IsDir(self):
        """boolean = IsDir()"""
        ...

    def Path(self):
        """string path = Path()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Force(object):
    def __init__(self, *args, **kwargs):
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def Force(self, pos):
        """vector force = Force(vector pos)"""
        ...

    def ForceM(self, pos, mass):
        """vector force = ForceM(vector pos,float mass)"""
        ...

    def ForceV(self, pos, velocity):
        """vector force = ForceV(vector pos,vector velocity)"""
        ...

    def ForceVM(self, pos, velocity, mass):
        """vector force = ForceVM(vector pos,vector velocity,float mass)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class FormDeleteEntryDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Delete(self, hash):
        """Delete(string hash)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class FormEntryDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def ControlHash(self):
        """string hash = ControlHash()"""
        ...

    def FormHash(self):
        """string hash = FormHash()"""
        ...

    def Position(self):
        """integer pos = Position()"""
        ...

    def SyntheticIndex(self):
        """integer index = SyntheticIndex()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class FormEntryDropPreview(object):
    def __init__(self, *args, **kwargs):
        ...

    def MarkControl(self, hash, syntheticIndex, pos):
        """MarkControl(string hash,integer syntheticIndex,integer pos)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class FrameBuffer(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddAttribute(self, name, type):
        """integer index = AddAttribute(string name,string type)"""
        ...

    def Alpha(self, index):
        """object = Alpha(integer index)"""
        ...

    def AlphaIndex(self, index):
        """integer = AlphaIndex(integer index)"""
        ...

    def AreaProcessingActive(self, bufferIndex):
        """integer active = AreaProcessingActive(integer bufferIndex)"""
        ...

    def BucketsOnDisk(self, index):
        """integer = BucketsOnDisk(integer index)"""
        ...

    def ByIndex(self, index):
        """object = ByIndex(integer index)"""
        ...

    def Count(self):
        """integer = Count()"""
        ...

    def CreateFrameBufferTargetImage(self, type, w, h):
        """Unknown object = CreateFrameBufferTargetImage(integer type,integer w,integer h)"""
        ...

    def GetBloomEnabled(self, bufferIndex):
        """integer = GetBloomEnabled(integer bufferIndex)"""
        ...

    def GetBloomRadius(self, bufferIndex):
        """float = GetBloomRadius(integer bufferIndex)"""
        ...

    def GetBloomThreshold(self, bufferIndex):
        """float = GetBloomThreshold(integer bufferIndex)"""
        ...

    def GetColorization(self, bufferIndex):
        """float = GetColorization(integer bufferIndex)"""
        ...

    def GetExpType(self, bufferIndex):
        """integer = GetExpType(integer bufferIndex)"""
        ...

    def GetHueOffset(self, bufferIndex):
        """float = GetHueOffset(integer bufferIndex)"""
        ...

    def GetISO(self, bufferIndex):
        """float = GetISO(integer bufferIndex)"""
        ...

    def GetInputBlackLevel(self, bufferIndex):
        """float = GetInputBlackLevel(integer bufferIndex)"""
        ...

    def GetInputBlueGrayLevel(self, bufferIndex):
        """float = GetInputBlueGrayLevel(integer bufferIndex)"""
        ...

    def GetInputGrayLevel(self, bufferIndex):
        """float = GetInputGrayLevel(integer bufferIndex)"""
        ...

    def GetInputGreenGrayLevel(self, bufferIndex):
        """float = GetInputGreenGrayLevel(integer bufferIndex)"""
        ...

    def GetInputMaxBlueLevel(self, bufferIndex):
        """float = GetInputMaxBlueLevel(integer bufferIndex)"""
        ...

    def GetInputMaxGreenLevel(self, bufferIndex):
        """float = GetInputMaxGreenLevel(integer bufferIndex)"""
        ...

    def GetInputMaxRedLevel(self, bufferIndex):
        """float = GetInputMaxRedLevel(integer bufferIndex)"""
        ...

    def GetInputMinBlueLevel(self, bufferIndex):
        """float = GetInputMinBlueLevel(integer bufferIndex)"""
        ...

    def GetInputMinGreenLevel(self, bufferIndex):
        """float = GetInputMinGreenLevel(integer bufferIndex)"""
        ...

    def GetInputMinRedLevel(self, bufferIndex):
        """float = GetInputMinRedLevel(integer bufferIndex)"""
        ...

    def GetInputRedGrayLevel(self, bufferIndex):
        """float = GetInputRedGrayLevel(integer bufferIndex)"""
        ...

    def GetInputWhiteLevel(self, bufferIndex):
        """float = GetInputWhiteLevel(integer bufferIndex)"""
        ...

    def GetInvInputBlueGrayLevel(self, bufferIndex):
        """float = GetInvInputBlueGrayLevel(integer bufferIndex)"""
        ...

    def GetInvInputGrayLevel(self, bufferIndex):
        """float = GetInvInputGrayLevel(integer bufferIndex)"""
        ...

    def GetInvInputGreenGrayLevel(self, bufferIndex):
        """float = GetInvInputGreenGrayLevel(integer bufferIndex)"""
        ...

    def GetInvInputRedGrayLevel(self, bufferIndex):
        """float = GetInvInputRedGrayLevel(integer bufferIndex)"""
        ...

    def GetOutputBlackLevel(self, bufferIndex):
        """float = GetOutputBlackLevel(integer bufferIndex)"""
        ...

    def GetOutputColorspace(self):
        """string = GetOutputColorspace()"""
        ...

    def GetOutputGamma(self, bufferIndex):
        """float = GetOutputGamma(integer bufferIndex)"""
        ...

    def GetOutputInvGamma(self, bufferIndex):
        """float = GetOutputInvGamma(integer bufferIndex)"""
        ...

    def GetOutputMaxBlueLevel(self, bufferIndex):
        """float = GetOutputMaxBlueLevel(integer bufferIndex)"""
        ...

    def GetOutputMaxGreenLevel(self, bufferIndex):
        """float = GetOutputMaxGreenLevel(integer bufferIndex)"""
        ...

    def GetOutputMaxRedLevel(self, bufferIndex):
        """float = GetOutputMaxRedLevel(integer bufferIndex)"""
        ...

    def GetOutputMinBlueLevel(self, bufferIndex):
        """float = GetOutputMinBlueLevel(integer bufferIndex)"""
        ...

    def GetOutputMinGreenLevel(self, bufferIndex):
        """float = GetOutputMinGreenLevel(integer bufferIndex)"""
        ...

    def GetOutputMinRedLevel(self, bufferIndex):
        """float = GetOutputMinRedLevel(integer bufferIndex)"""
        ...

    def GetOutputWhiteLevel(self, bufferIndex):
        """float = GetOutputWhiteLevel(integer bufferIndex)"""
        ...

    def GetRenderPassName(self, name):
        """GetRenderPassName(byte[] name)"""
        ...

    def GetSaturation(self, bufferIndex):
        """float = GetSaturation(integer bufferIndex)"""
        ...

    def GetSaveProcessed(self, bufferIndex):
        """integer = GetSaveProcessed(integer bufferIndex)"""
        ...

    def GetStereoComposite(self):
        """integer composite = GetStereoComposite()"""
        ...

    def GetStereoEyeDisplay(self):
        """integer eyeDisplay = GetStereoEyeDisplay()"""
        ...

    def GetTargetColor(self, bufferIndex):
        """float color = GetTargetColor(integer bufferIndex)"""
        ...

    def GetToneAmt(self, bufferIndex):
        """float = GetToneAmt(integer bufferIndex)"""
        ...

    def GetToneMap(self, bufferIndex):
        """integer = GetToneMap(integer bufferIndex)"""
        ...

    def GetVignetteAmount(self, bufferIndex):
        """float = GetVignetteAmount(integer bufferIndex)"""
        ...

    def IsStereo(self):
        """integer isStereo = IsStereo()"""
        ...

    def Lookup(self, name, item):
        """object = Lookup(string name,object item)"""
        ...

    def LookupByIdentity(self, identity):
        """object = LookupByIdentity(string identity)"""
        ...

    def SetBloomEnabled(self, bufferIndex, enabled):
        """SetBloomEnabled(integer bufferIndex,integer enabled)"""
        ...

    def SetBloomRadius(self, bufferIndex, radius):
        """SetBloomRadius(integer bufferIndex,float radius)"""
        ...

    def SetBloomThreshold(self, bufferIndex, threshold):
        """SetBloomThreshold(integer bufferIndex,float threshold)"""
        ...

    def SetColorization(self, bufferIndex, colorization):
        """SetColorization(integer bufferIndex,float colorization)"""
        ...

    def SetExpType(self, bufferIndex, expType):
        """SetExpType(integer bufferIndex,integer expType)"""
        ...

    def SetEyeSide(self, eyeSide):
        """SetEyeSide(integer eyeSide)"""
        ...

    def SetHueOffset(self, bufferIndex, hueOffset):
        """SetHueOffset(integer bufferIndex,float hueOffset)"""
        ...

    def SetISO(self, bufferIndex, iso):
        """SetISO(integer bufferIndex,float iso)"""
        ...

    def SetInputBlackLevel(self, bufferIndex, blackLevel):
        """SetInputBlackLevel(integer bufferIndex,float blackLevel)"""
        ...

    def SetInputBlueGrayLevel(self, bufferIndex, gamma):
        """SetInputBlueGrayLevel(integer bufferIndex,float gamma)"""
        ...

    def SetInputGrayLevel(self, bufferIndex, gamma):
        """SetInputGrayLevel(integer bufferIndex,float gamma)"""
        ...

    def SetInputGreenGrayLevel(self, bufferIndex, gamma):
        """SetInputGreenGrayLevel(integer bufferIndex,float gamma)"""
        ...

    def SetInputMaxBlueLevel(self, bufferIndex, level):
        """SetInputMaxBlueLevel(integer bufferIndex,float level)"""
        ...

    def SetInputMaxGreenLevel(self, bufferIndex, level):
        """SetInputMaxGreenLevel(integer bufferIndex,float level)"""
        ...

    def SetInputMaxRedLevel(self, bufferIndex, level):
        """SetInputMaxRedLevel(integer bufferIndex,float level)"""
        ...

    def SetInputMinBlueLevel(self, bufferIndex, level):
        """SetInputMinBlueLevel(integer bufferIndex,float level)"""
        ...

    def SetInputMinGreenLevel(self, bufferIndex, level):
        """SetInputMinGreenLevel(integer bufferIndex,float level)"""
        ...

    def SetInputMinRedLevel(self, bufferIndex, level):
        """SetInputMinRedLevel(integer bufferIndex,float level)"""
        ...

    def SetInputRedGrayLevel(self, bufferIndex, gamma):
        """SetInputRedGrayLevel(integer bufferIndex,float gamma)"""
        ...

    def SetInputWhiteLevel(self, bufferIndex, whiteLevel):
        """SetInputWhiteLevel(integer bufferIndex,float whiteLevel)"""
        ...

    def SetOutputBlackLevel(self, bufferIndex, blackLevel):
        """SetOutputBlackLevel(integer bufferIndex,float blackLevel)"""
        ...

    def SetOutputColormapping(self, colormapping):
        """SetOutputColormapping(object colormapping)"""
        ...

    def SetOutputColorspace(self, colorspace):
        """SetOutputColorspace(string colorspace)"""
        ...

    def SetOutputGamma(self, bufferIndex, gamma):
        """SetOutputGamma(integer bufferIndex,float gamma)"""
        ...

    def SetOutputMaxBlueLevel(self, bufferIndex, whiteLevel):
        """SetOutputMaxBlueLevel(integer bufferIndex,float whiteLevel)"""
        ...

    def SetOutputMaxGreenLevel(self, bufferIndex, whiteLevel):
        """SetOutputMaxGreenLevel(integer bufferIndex,float whiteLevel)"""
        ...

    def SetOutputMaxRedLevel(self, bufferIndex, whiteLevel):
        """SetOutputMaxRedLevel(integer bufferIndex,float whiteLevel)"""
        ...

    def SetOutputMinBlueLevel(self, bufferIndex, blackLevel):
        """SetOutputMinBlueLevel(integer bufferIndex,float blackLevel)"""
        ...

    def SetOutputMinGreenLevel(self, bufferIndex, blackLevel):
        """SetOutputMinGreenLevel(integer bufferIndex,float blackLevel)"""
        ...

    def SetOutputMinRedLevel(self, bufferIndex, blackLevel):
        """SetOutputMinRedLevel(integer bufferIndex,float blackLevel)"""
        ...

    def SetOutputWhiteLevel(self, bufferIndex, whiteLevel):
        """SetOutputWhiteLevel(integer bufferIndex,float whiteLevel)"""
        ...

    def SetRenderPassName(self, name):
        """SetRenderPassName(string name)"""
        ...

    def SetSaturation(self, bufferIndex, saturation):
        """SetSaturation(integer bufferIndex,float saturation)"""
        ...

    def SetSaveProcessed(self, bufferIndex, enabled):
        """SetSaveProcessed(integer bufferIndex,integer enabled)"""
        ...

    def SetStereoComposite(self, composite):
        """SetStereoComposite(integer composite)"""
        ...

    def SetStereoEyeDisplay(self, eyeDisplay):
        """SetStereoEyeDisplay(integer eyeDisplay)"""
        ...

    def SetTargetColor(self, bufferIndex, color):
        """SetTargetColor(integer bufferIndex,double[] color)"""
        ...

    def SetToneAmt(self, bufferIndex, toneAmt):
        """SetToneAmt(integer bufferIndex,float toneAmt)"""
        ...

    def SetToneMap(self, bufferIndex, toneMap):
        """SetToneMap(integer bufferIndex,integer toneMap)"""
        ...

    def SetVignetteAmount(self, bufferIndex, radius):
        """SetVignetteAmount(integer bufferIndex,float radius)"""
        ...

    def Size(self, index):
        """(integer width,integer height) = Size(integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GLImage(object):
    def __init__(self, *args, **kwargs):
        ...

    def SetImage(self, image):
        """SetImage(object image)"""
        ...

    def Size(self):
        """(float w,float h) = Size()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GLMaterial(object):
    def __init__(self, *args, **kwargs):
        ...

    def Alpha(self):
        """float alpha = Alpha()"""
        ...

    def Color(self):
        """vector color = Color()"""
        ...

    def DiffuseAmount(self):
        """float amount = DiffuseAmount()"""
        ...

    def DiffuseColor(self):
        """vector color = DiffuseColor()"""
        ...

    def Glossiness(self):
        """float amount = Glossiness()"""
        ...

    def LuminosityColor(self):
        """vector color = LuminosityColor()"""
        ...

    def ReflectionColor(self):
        """vector color = ReflectionColor()"""
        ...

    def SpecularAmount(self):
        """float amount = SpecularAmount()"""
        ...

    def SpecularColor(self):
        """vector color = SpecularColor()"""
        ...

    def TwoSide(self):
        """integer value = TwoSide()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GLShadingListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def DisplacementUpdate(self, item):
        """DisplacementUpdate(object item)"""
        ...

    def FurUpdate(self, item):
        """FurUpdate(object item)"""
        ...

    def ShadingUpdate(self, item):
        """ShadingUpdate(object item)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GLViewport(object):
    def __init__(self, *args, **kwargs):
        ...

    def Draw(self):
        """Draw()"""
        ...

    def DropDestination(self, x, y):
        """Unknown object = DropDestination(integer x,integer y)"""
        ...

    def Initialize(self, client):
        """Initialize(object client)"""
        ...

    def MouseEvent(self, event):
        """MouseEvent(integer event)"""
        ...

    def SelectViewport(self):
        """SelectViewport()"""
        ...

    def SetSize(self, w, h):
        """SetSize(integer w,integer h)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GLViewportClient(object):
    def __init__(self, *args, **kwargs):
        ...

    def Invalidate(self):
        """Invalidate()"""
        ...

    def MouseButton(self):
        """integer button = MouseButton()"""
        ...

    def MouseCount(self):
        """integer count = MouseCount()"""
        ...

    def MousePosition(self):
        """(integer x,integer y) = MousePosition()"""
        ...

    def TabletPressure(self):
        """float press = TabletPressure()"""
        ...

    def TabletTilt(self):
        """float tilt = TabletTilt()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GeoCacheSegment(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetBBox(self):
        """bounds bbox = GetBBox()"""
        ...

    def GetPolygonVertexFeature(self, feature, featureData, count, start):
        """GetPolygonVertexFeature(integer feature,pointer featureData,integer count,integer start)"""
        ...

    def GetPolygonVertexInds(self, count, start):
        """integer polyVertexInds = GetPolygonVertexInds(integer count,integer start)"""
        ...

    def GetVertexFeature(self, feature, featureData, count, start):
        """GetVertexFeature(integer feature,pointer featureData,integer count,integer start)"""
        ...

    def PolygonCount(self):
        """integer count = PolygonCount()"""
        ...

    def VertexCount(self):
        """integer count = VertexCount()"""
        ...

    def VertexFeatureCount(self, feature):
        """integer count = VertexFeatureCount(integer feature)"""
        ...

    def VertsPerPoly(self):
        """integer count = VertsPerPoly()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GeoCacheSurface(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetBBox(self):
        """bounds bbox = GetBBox()"""
        ...

    def GetXfrm(self, endpoint):
        """(vector pos,matrix rot,vector scl) = GetXfrm(integer endpoint)"""
        ...

    def ID(self):
        """integer = ID()"""
        ...

    def InstanceIndex(self):
        """integer = InstanceIndex()"""
        ...

    def IsInstanced(self):
        """integer = IsInstanced()"""
        ...

    def IsValid(self):
        """integer = IsValid()"""
        ...

    def LoadSegments(self):
        """LoadSegments()"""
        ...

    def MaterialPTag(self):
        """string = MaterialPTag()"""
        ...

    def PartPTag(self):
        """string = PartPTag()"""
        ...

    def PickPTag(self):
        """string = PickPTag()"""
        ...

    def PolygonCount(self):
        """integer count = PolygonCount()"""
        ...

    def SegmentCount(self):
        """integer count = SegmentCount()"""
        ...

    def ShaderLayerCount(self):
        """integer count = ShaderLayerCount()"""
        ...

    def ShaderMaskName(self):
        """string name = ShaderMaskName()"""
        ...

    def ShaderMaskType(self):
        """integer = ShaderMaskType()"""
        ...

    def SourceItem(self):
        """Unknown object = SourceItem()"""
        ...

    def SourceSurface(self):
        """Unknown object = SourceSurface()"""
        ...

    def UnloadSegments(self):
        """UnloadSegments()"""
        ...

    def VertexCount(self):
        """integer count = VertexCount()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GradientFilter(object):
    def __init__(self, *args, **kwargs):
        ...

    def Evaluate(self, time, value):
        """float = Evaluate(float time,float value)"""
        ...

    def Generate(self, time):
        """float = Generate(float time)"""
        ...

    def MultiSample(self, time, other):
        """float = MultiSample(float time,object other)"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GroupDeformer(object):
    def __init__(self, *args, **kwargs):
        ...

    def DeformerByIndex(self, index):
        """Item object = DeformerByIndex(integer index)"""
        ...

    def DeformerCount(self):
        """integer = DeformerCount()"""
        ...

    def PointEffect(self, meshIndex, point, deformer, weight, max):
        """integer count = PointEffect(integer meshIndex,id point,unsigned[] deformer,float[] weight,integer max)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GroupDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Group(self):
        """Item object = Group()"""
        ...

    def Location(self):
        """integer = Location()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GroupEnumerator(object):
    def __init__(self, *args, **kwargs):
        ...

    def Channel(self):
        """(Item object,integer index) = Channel()"""
        ...

    def Enumerate(self, visitor, mask):
        """Enumerate(object visitor,integer mask)"""
        ...

    def Item(self):
        """Item object = Item()"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GroupItem(object):
    def __init__(self, *args, **kwargs):
        ...

    def Enumerator(self):
        """GroupEnumerator object = Enumerator()"""
        ...

    def SetType(self, type):
        """SetType(integer type)"""
        ...

    def Type(self):
        """integer type = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GroupMemberChanDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Channel(self):
        """Unknown object = Channel()"""
        ...

    def Group(self):
        """Unknown object = Group()"""
        ...

    def Location(self):
        """integer = Location()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class GroupMemberItemDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Group(self):
        """Unknown object = Group()"""
        ...

    def Item(self):
        """Unknown object = Item()"""
        ...

    def Location(self):
        """integer = Location()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class HandleDraw(object):
    def __init__(self, *args, **kwargs):
        ...

    def AxisHandle(self, pos, mat, axis, part, len, flags):
        """AxisHandle(vector pos,matrix mat,integer axis,integer part,float len,integer flags)"""
        ...

    def CrossHandle(self, pos, mat, part, flags):
        """CrossHandle(vector pos,matrix mat,integer part,integer flags)"""
        ...

    def Handle(self, pos, mat, part, flags):
        """Handle(vector pos,matrix mat,integer part,integer flags)"""
        ...

    def LineHandleHilight(self, pos, dir, part, flags):
        """LineHandleHilight(vector pos,vector dir,integer part,integer flags)"""
        ...

    def MoveHandle(self, pos, mat, axis, part, flags):
        """MoveHandle(vector pos,matrix mat,integer axis,integer part,integer flags)"""
        ...

    def PlaneHandle(self, pos, mat, axis, part, flags):
        """PlaneHandle(vector pos,matrix mat,integer axis,integer part,integer flags)"""
        ...

    def PlaneHandleHilight(self, pos, norm, part, flags):
        """PlaneHandleHilight(vector pos,vector norm,integer part,integer flags)"""
        ...

    def PointHandle(self, pos, part, flags):
        """PointHandle(vector pos,integer part,integer flags)"""
        ...

    def RotateHandle(self, pos, mat, axis, part, sAngle, eAngle, facing, flags):
        """RotateHandle(vector pos,matrix mat,integer axis,integer part,float sAngle,float eAngle,integer facing,integer flags)"""
        ...

    def RotateMouseHandle(self, center, pos, mat, axis, part, flags):
        """RotateMouseHandle(vector center,vector pos,matrix mat,integer axis,integer part,integer flags)"""
        ...

    def ScaleHandle(self, pos, mat, axis, part, offset, line, flags):
        """ScaleHandle(vector pos,matrix mat,integer axis,integer part,float offset,integer line,integer flags)"""
        ...

    def XHandle(self, pos, mat, part, flags):
        """XHandle(vector pos,matrix mat,integer part,integer flags)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Image(object):
    def __init__(self, *args, **kwargs):
        ...

    def Format(self):
        """integer = Format()"""
        ...

    def GetLine(self, y, type, buf):
        """data[] = GetLine(integer y,integer type,data[] buf)"""
        ...

    def GetPixel(self, x, y, type, pixel):
        """GetPixel(integer x,integer y,integer type,data[] pixel)"""
        ...

    def Size(self):
        """(integer w,integer h) = Size()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ImageFilter(object):
    def __init__(self, *args, **kwargs):
        ...

    def Generate(self, width, height, monitor):
        """Image object = Generate(integer width,integer height,object monitor)"""
        ...

    def MultiSample(self, monitor, image):
        """Image object = MultiSample(object monitor,object image)"""
        ...

    def SingleSample(self, src):
        """vector dest = SingleSample(vector src)"""
        ...

    def SingleSampleN(self, src, num):
        """float dest = SingleSampleN(float[] src,integer num)"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ImageFilterMetrics(object):
    def __init__(self, *args, **kwargs):
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ImageLevelSample(object):
    def __init__(self, *args, **kwargs):
        ...

    def Count(self):
        """integer = Count()"""
        ...

    def GetLevelSize(self, level):
        """(integer width,integer height) = GetLevelSize(integer level)"""
        ...

    def GetLine(self, level, y, buf):
        """float[] = GetLine(integer level,integer y,float[] buf)"""
        ...

    def GetPixel(self, level, x, y, type, pixel):
        """GetPixel(integer level,integer x,integer y,integer type,data[] pixel)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ImageLoaderTarget(object):
    def __init__(self, *args, **kwargs):
        ...

    def SetColorspace(self, colorspace):
        """SetColorspace(string colorspace)"""
        ...

    def SetColorspaceDepth(self, depth):
        """SetColorspaceDepth(integer depth)"""
        ...

    def SetMap(self, ncolor):
        """SetMap(integer ncolor)"""
        ...

    def SetSize(self, type, width, height):
        """SetSize(integer type,integer width,integer height)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ImageMonitor(object):
    def __init__(self, *args, **kwargs):
        ...

    def AspectRange(self):
        """(float minAspect,float maxAspect,float idealAspect) = AspectRange()"""
        ...

    def Draw(self, imageForDrawing):
        """Draw(object imageForDrawing)"""
        ...

    def Image(self, imageToAnalyze, frameBufferToAnalyze, bufferIndex, x1, y1, x2, y2, imageProcessingRead, processedThumbnail):
        """Image(object imageToAnalyze,object frameBufferToAnalyze,integer bufferIndex,float x1,float y1,float x2,float y2,object imageProcessingRead,object processedThumbnail)"""
        ...

    def ImageProcChanged(self):
        """ImageProcChanged()"""
        ...

    def ImageSource(self, source):
        """ImageSource(string source)"""
        ...

    def MouseDown(self, startx, starty, w, h):
        """MouseDown(integer startx,integer starty,integer w,integer h)"""
        ...

    def MouseMove(self, startx, starty, cx, cy, w, h):
        """MouseMove(integer startx,integer starty,integer cx,integer cy,integer w,integer h)"""
        ...

    def MouseTrack(self, cx, cy, w, h):
        """MouseTrack(integer cx,integer cy,integer w,integer h)"""
        ...

    def MouseTrackEnter(self):
        """MouseTrackEnter()"""
        ...

    def MouseTrackExit(self):
        """MouseTrackExit()"""
        ...

    def MouseUp(self, startx, starty, cx, cy, w, h):
        """MouseUp(integer startx,integer starty,integer cx,integer cy,integer w,integer h)"""
        ...

    def ToolTip(self, cx, cy, w, h):
        """string = ToolTip(integer cx,integer cy,integer w,integer h)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ImageProcessing(object):
    def __init__(self, *args, **kwargs):
        ...

    def ApplyToFrameBuffer(self, frameBuffer, bufferIndex):
        """ApplyToFrameBuffer(object frameBuffer,integer bufferIndex)"""
        ...

    def ApplyToFrameBufferOverride(self, frameBuffer, bufferIndex, opOverride):
        """ApplyToFrameBufferOverride(object frameBuffer,integer bufferIndex,integer opOverride)"""
        ...

    def ApplyToImage(self, srcImage, dstImage):
        """ApplyToImage(object srcImage,object dstImage)"""
        ...

    def ApplyToImageFromFrameBuffer(self, frameBuffer, bufferIndex, image, xOffset, yOffset, zoom):
        """ApplyToImageFromFrameBuffer(object frameBuffer,integer bufferIndex,object image,float xOffset,float yOffset,float zoom)"""
        ...

    def ApplyToImageFromFrameBufferOverride(self, frameBuffer, bufferIndex, image, xOffset, yOffset, zoom, opOverride):
        """ApplyToImageFromFrameBufferOverride(object frameBuffer,integer bufferIndex,object image,float xOffset,float yOffset,float zoom,integer opOverride)"""
        ...

    def ApplyToImageOverride(self, srcImage, dstImage, opOverride):
        """ApplyToImageOverride(object srcImage,object dstImage,integer opOverride)"""
        ...

    def AreaProcessingActive(self):
        """integer active = AreaProcessingActive()"""
        ...

    def CopySettingsFromFrameBuffer(self, frameBuffer, bufferIndex):
        """CopySettingsFromFrameBuffer(object frameBuffer,integer bufferIndex)"""
        ...

    def CopySettingsToFrameBuffer(self, frameBuffer, bufferIndex):
        """CopySettingsToFrameBuffer(object frameBuffer,integer bufferIndex)"""
        ...

    def GetAsReadOnly(self):
        """ImageProcessing object = GetAsReadOnly()"""
        ...

    def GetBloomEnabled(self):
        """integer enabled = GetBloomEnabled()"""
        ...

    def GetBloomRadius(self):
        """float radius = GetBloomRadius()"""
        ...

    def GetBloomThreshold(self):
        """float threshold = GetBloomThreshold()"""
        ...

    def GetColorSpaceEmbedding(self):
        """integer colorSpaceEmbedding = GetColorSpaceEmbedding()"""
        ...

    def GetColorization(self):
        """float colorization = GetColorization()"""
        ...

    def GetExpType(self):
        """integer expType = GetExpType()"""
        ...

    def GetHueOffset(self):
        """float hueOffset = GetHueOffset()"""
        ...

    def GetISO(self):
        """float iso = GetISO()"""
        ...

    def GetIdentifier(self):
        """string string = GetIdentifier()"""
        ...

    def GetImageProcessingOperators(self):
        """integer ops = GetImageProcessingOperators()"""
        ...

    def GetInputBlackLevel(self):
        """float inputBlackLevel = GetInputBlackLevel()"""
        ...

    def GetInputBlueGrayLevel(self):
        """float gamma = GetInputBlueGrayLevel()"""
        ...

    def GetInputGrayLevel(self):
        """float gamma = GetInputGrayLevel()"""
        ...

    def GetInputGreenGrayLevel(self):
        """float gamma = GetInputGreenGrayLevel()"""
        ...

    def GetInputMaxBlueLevel(self):
        """float inputLevel = GetInputMaxBlueLevel()"""
        ...

    def GetInputMaxGreenLevel(self):
        """float inputLevel = GetInputMaxGreenLevel()"""
        ...

    def GetInputMaxRedLevel(self):
        """float inputLevel = GetInputMaxRedLevel()"""
        ...

    def GetInputMinBlueLevel(self):
        """float inputLevel = GetInputMinBlueLevel()"""
        ...

    def GetInputMinGreenLevel(self):
        """float inputLevel = GetInputMinGreenLevel()"""
        ...

    def GetInputMinRedLevel(self):
        """float inputLevel = GetInputMinRedLevel()"""
        ...

    def GetInputRedGrayLevel(self):
        """float gamma = GetInputRedGrayLevel()"""
        ...

    def GetInputWhiteLevel(self):
        """float inputWhiteLevel = GetInputWhiteLevel()"""
        ...

    def GetInvInputBlueGrayLevel(self):
        """float invGamma = GetInvInputBlueGrayLevel()"""
        ...

    def GetInvInputGrayLevel(self):
        """float invGamma = GetInvInputGrayLevel()"""
        ...

    def GetInvInputGreenGrayLevel(self):
        """float invGamma = GetInvInputGreenGrayLevel()"""
        ...

    def GetInvInputRedGrayLevel(self):
        """float invGamma = GetInvInputRedGrayLevel()"""
        ...

    def GetOutputBlackLevel(self):
        """float outputBlackLevel = GetOutputBlackLevel()"""
        ...

    def GetOutputColorspace(self):
        """string = GetOutputColorspace()"""
        ...

    def GetOutputGamma(self):
        """float outputGamma = GetOutputGamma()"""
        ...

    def GetOutputInvGamma(self):
        """float outputInvGamma = GetOutputInvGamma()"""
        ...

    def GetOutputMaxBlueLevel(self):
        """float outputLevel = GetOutputMaxBlueLevel()"""
        ...

    def GetOutputMaxGreenLevel(self):
        """float outputLevel = GetOutputMaxGreenLevel()"""
        ...

    def GetOutputMaxRedLevel(self):
        """float outputLevel = GetOutputMaxRedLevel()"""
        ...

    def GetOutputMinBlueLevel(self):
        """float outputLevel = GetOutputMinBlueLevel()"""
        ...

    def GetOutputMinGreenLevel(self):
        """float outputLevel = GetOutputMinGreenLevel()"""
        ...

    def GetOutputMinRedLevel(self):
        """float outputLevel = GetOutputMinRedLevel()"""
        ...

    def GetOutputWhiteLevel(self):
        """float outputWhiteLevel = GetOutputWhiteLevel()"""
        ...

    def GetSaturation(self):
        """float saturation = GetSaturation()"""
        ...

    def GetSaveProcessed(self):
        """integer enabled = GetSaveProcessed()"""
        ...

    def GetSourceImageGamma(self):
        """float gamma = GetSourceImageGamma()"""
        ...

    def GetSourceImageIsStereoSideBySide(self):
        """integer isStereo = GetSourceImageIsStereoSideBySide()"""
        ...

    def GetStereoComposite(self):
        """integer mode = GetStereoComposite()"""
        ...

    def GetStereoEye(self):
        """integer eye = GetStereoEye()"""
        ...

    def GetTargetColor(self):
        """float color = GetTargetColor()"""
        ...

    def GetToneAmt(self):
        """float toneAmt = GetToneAmt()"""
        ...

    def GetToneMap(self):
        """integer toneMap = GetToneMap()"""
        ...

    def GetVignetteAmount(self):
        """float amount = GetVignetteAmount()"""
        ...

    def Reset(self):
        """Reset()"""
        ...

    def SetBloomEnabled(self, enabled):
        """SetBloomEnabled(integer enabled)"""
        ...

    def SetBloomRadius(self, radius):
        """SetBloomRadius(float radius)"""
        ...

    def SetBloomThreshold(self, threshold):
        """SetBloomThreshold(float threshold)"""
        ...

    def SetColorization(self, colorization):
        """SetColorization(float colorization)"""
        ...

    def SetExpType(self, expType):
        """SetExpType(integer expType)"""
        ...

    def SetHueOffset(self, hueOffset):
        """SetHueOffset(float hueOffset)"""
        ...

    def SetISO(self, iso):
        """SetISO(float iso)"""
        ...

    def SetIdentifier(self, string):
        """SetIdentifier(string string)"""
        ...

    def SetImageProcessingOperators(self, ops):
        """SetImageProcessingOperators(integer ops)"""
        ...

    def SetInputBlackLevel(self, blackLevel):
        """SetInputBlackLevel(float blackLevel)"""
        ...

    def SetInputBlueGrayLevel(self, gamma):
        """SetInputBlueGrayLevel(float gamma)"""
        ...

    def SetInputGrayLevel(self, gamma):
        """SetInputGrayLevel(float gamma)"""
        ...

    def SetInputGreenGrayLevel(self, gamma):
        """SetInputGreenGrayLevel(float gamma)"""
        ...

    def SetInputMaxBlueLevel(self, level):
        """SetInputMaxBlueLevel(float level)"""
        ...

    def SetInputMaxGreenLevel(self, level):
        """SetInputMaxGreenLevel(float level)"""
        ...

    def SetInputMaxRedLevel(self, level):
        """SetInputMaxRedLevel(float level)"""
        ...

    def SetInputMinBlueLevel(self, level):
        """SetInputMinBlueLevel(float level)"""
        ...

    def SetInputMinGreenLevel(self, level):
        """SetInputMinGreenLevel(float level)"""
        ...

    def SetInputMinRedLevel(self, level):
        """SetInputMinRedLevel(float level)"""
        ...

    def SetInputRedGrayLevel(self, gamma):
        """SetInputRedGrayLevel(float gamma)"""
        ...

    def SetInputWhiteLevel(self, whiteLevel):
        """SetInputWhiteLevel(float whiteLevel)"""
        ...

    def SetOutputBlackLevel(self, blackLevel):
        """SetOutputBlackLevel(float blackLevel)"""
        ...

    def SetOutputColormapping(self, colormapping):
        """SetOutputColormapping(object colormapping)"""
        ...

    def SetOutputColorspace(self, colorspace):
        """SetOutputColorspace(string colorspace)"""
        ...

    def SetOutputGamma(self, gamma):
        """SetOutputGamma(float gamma)"""
        ...

    def SetOutputMaxBlueLevel(self, outputLevel):
        """SetOutputMaxBlueLevel(float outputLevel)"""
        ...

    def SetOutputMaxGreenLevel(self, outputLevel):
        """SetOutputMaxGreenLevel(float outputLevel)"""
        ...

    def SetOutputMaxRedLevel(self, outputLevel):
        """SetOutputMaxRedLevel(float outputLevel)"""
        ...

    def SetOutputMinBlueLevel(self, outputLevel):
        """SetOutputMinBlueLevel(float outputLevel)"""
        ...

    def SetOutputMinGreenLevel(self, outputLevel):
        """SetOutputMinGreenLevel(float outputLevel)"""
        ...

    def SetOutputMinRedLevel(self, outputLevel):
        """SetOutputMinRedLevel(float outputLevel)"""
        ...

    def SetOutputWhiteLevel(self, whiteLevel):
        """SetOutputWhiteLevel(float whiteLevel)"""
        ...

    def SetSaturation(self, saturation):
        """SetSaturation(float saturation)"""
        ...

    def SetSaveProcessed(self, enabled):
        """SetSaveProcessed(integer enabled)"""
        ...

    def SetSourceImageGamma(self, gamma):
        """SetSourceImageGamma(float gamma)"""
        ...

    def SetSourceImageIsStereoSideBySide(self, isStereo):
        """SetSourceImageIsStereoSideBySide(integer isStereo)"""
        ...

    def SetStereoComposite(self, mode):
        """SetStereoComposite(integer mode)"""
        ...

    def SetStereoEye(self, eye):
        """SetStereoEye(integer eye)"""
        ...

    def SetTargetColor(self, color):
        """SetTargetColor(double[] color)"""
        ...

    def SetToneAmt(self, toneAmt):
        """SetToneAmt(float toneAmt)"""
        ...

    def SetToneMap(self, toneMap):
        """SetToneMap(integer toneMap)"""
        ...

    def SetVignetteAmount(self, amount):
        """SetVignetteAmount(float amount)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ImageProcessingListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def Changed(self, identifier, eventCode):
        """Changed(string identifier,integer eventCode)"""
        ...

    def Reset(self, identifier):
        """Reset(string identifier)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ImageProcessingRead(object):
    def __init__(self, *args, **kwargs):
        ...

    def ApplyToFrameBuffer(self, frameBuffer, bufferIndex):
        """ApplyToFrameBuffer(object frameBuffer,integer bufferIndex)"""
        ...

    def ApplyToFrameBufferOverride(self, frameBuffer, bufferIndex, opOverride):
        """ApplyToFrameBufferOverride(object frameBuffer,integer bufferIndex,integer opOverride)"""
        ...

    def ApplyToImage(self, srcImage, dstImage):
        """ApplyToImage(object srcImage,object dstImage)"""
        ...

    def ApplyToImageFromFrameBuffer(self, frameBuffer, bufferIndex, image, xOffset, yOffset, zoom):
        """ApplyToImageFromFrameBuffer(object frameBuffer,integer bufferIndex,object image,float xOffset,float yOffset,float zoom)"""
        ...

    def ApplyToImageFromFrameBufferOverride(self, frameBuffer, bufferIndex, image, xOffset, yOffset, zoom, opOverride):
        """ApplyToImageFromFrameBufferOverride(object frameBuffer,integer bufferIndex,object image,float xOffset,float yOffset,float zoom,integer opOverride)"""
        ...

    def ApplyToImageOverride(self, srcImage, dstImage, opOverride):
        """ApplyToImageOverride(object srcImage,object dstImage,integer opOverride)"""
        ...

    def AreaProcessingActive(self):
        """integer active = AreaProcessingActive()"""
        ...

    def CopySettingsToFrameBuffer(self, frameBuffer, bufferIndex):
        """CopySettingsToFrameBuffer(object frameBuffer,integer bufferIndex)"""
        ...

    def GetBloomEnabled(self):
        """integer enabled = GetBloomEnabled()"""
        ...

    def GetBloomRadius(self):
        """float radius = GetBloomRadius()"""
        ...

    def GetBloomThreshold(self):
        """float threshold = GetBloomThreshold()"""
        ...

    def GetColorization(self):
        """float colorization = GetColorization()"""
        ...

    def GetExpType(self):
        """integer expType = GetExpType()"""
        ...

    def GetHueOffset(self):
        """float hueOffset = GetHueOffset()"""
        ...

    def GetISO(self):
        """float iso = GetISO()"""
        ...

    def GetIdentifier(self):
        """string string = GetIdentifier()"""
        ...

    def GetImageProcessingOperators(self):
        """integer ops = GetImageProcessingOperators()"""
        ...

    def GetInputBlackLevel(self):
        """float inputLevel = GetInputBlackLevel()"""
        ...

    def GetInputBlueGrayLevel(self):
        """float gamma = GetInputBlueGrayLevel()"""
        ...

    def GetInputGrayLevel(self):
        """float gamma = GetInputGrayLevel()"""
        ...

    def GetInputGreenGrayLevel(self):
        """float gamma = GetInputGreenGrayLevel()"""
        ...

    def GetInputMaxBlueLevel(self):
        """float inputLevel = GetInputMaxBlueLevel()"""
        ...

    def GetInputMaxGreenLevel(self):
        """float inputLevel = GetInputMaxGreenLevel()"""
        ...

    def GetInputMaxRedLevel(self):
        """float inputLevel = GetInputMaxRedLevel()"""
        ...

    def GetInputMinBlueLevel(self):
        """float inputLevel = GetInputMinBlueLevel()"""
        ...

    def GetInputMinGreenLevel(self):
        """float inputLevel = GetInputMinGreenLevel()"""
        ...

    def GetInputMinRedLevel(self):
        """float inputLevel = GetInputMinRedLevel()"""
        ...

    def GetInputRedGrayLevel(self):
        """float gamma = GetInputRedGrayLevel()"""
        ...

    def GetInputWhiteLevel(self):
        """float inputLevel = GetInputWhiteLevel()"""
        ...

    def GetInvInputBlueGrayLevel(self):
        """float invGamma = GetInvInputBlueGrayLevel()"""
        ...

    def GetInvInputGrayLevel(self):
        """float invGamma = GetInvInputGrayLevel()"""
        ...

    def GetInvInputGreenGrayLevel(self):
        """float invGamma = GetInvInputGreenGrayLevel()"""
        ...

    def GetInvInputRedGrayLevel(self):
        """float invGamma = GetInvInputRedGrayLevel()"""
        ...

    def GetOutputBlackLevel(self):
        """float outputLevel = GetOutputBlackLevel()"""
        ...

    def GetOutputColorspace(self):
        """string = GetOutputColorspace()"""
        ...

    def GetOutputGamma(self):
        """float outputGamma = GetOutputGamma()"""
        ...

    def GetOutputInvGamma(self):
        """float outputInvGamma = GetOutputInvGamma()"""
        ...

    def GetOutputMaxBlueLevel(self):
        """float outputLevel = GetOutputMaxBlueLevel()"""
        ...

    def GetOutputMaxGreenLevel(self):
        """float outputLevel = GetOutputMaxGreenLevel()"""
        ...

    def GetOutputMaxRedLevel(self):
        """float outputLevel = GetOutputMaxRedLevel()"""
        ...

    def GetOutputMinBlueLevel(self):
        """float outputLevel = GetOutputMinBlueLevel()"""
        ...

    def GetOutputMinGreenLevel(self):
        """float outputLevel = GetOutputMinGreenLevel()"""
        ...

    def GetOutputMinRedLevel(self):
        """float outputLevel = GetOutputMinRedLevel()"""
        ...

    def GetOutputWhiteLevel(self):
        """float outputLevel = GetOutputWhiteLevel()"""
        ...

    def GetSaturation(self):
        """float saturation = GetSaturation()"""
        ...

    def GetSaveProcessed(self):
        """integer enabled = GetSaveProcessed()"""
        ...

    def GetSourceImageGamma(self):
        """float gamma = GetSourceImageGamma()"""
        ...

    def GetSourceImageIsStereoSideBySide(self):
        """integer isStereo = GetSourceImageIsStereoSideBySide()"""
        ...

    def GetStereoComposite(self):
        """integer mode = GetStereoComposite()"""
        ...

    def GetStereoEye(self):
        """integer eye = GetStereoEye()"""
        ...

    def GetTargetColor(self):
        """float color = GetTargetColor()"""
        ...

    def GetToneAmt(self):
        """float toneAmt = GetToneAmt()"""
        ...

    def GetToneMap(self):
        """integer toneMap = GetToneMap()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ImageSegment(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetSegment(self, y, left, right, rgba):
        """GetSegment(integer y,integer left,integer right,float[] rgba)"""
        ...

    def SetSegment(self, y, left, right, type, line):
        """SetSegment(integer y,integer left,integer right,integer type,data[] line)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ImageWrite(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddAttribute(self, name, type):
        """integer index = AddAttribute(string name,string type)"""
        ...

    def Format(self):
        """integer = Format()"""
        ...

    def SetLine(self, y, type, line):
        """SetLine(integer y,integer type,data[] line)"""
        ...

    def SetPixel(self, x, y, type, pixel):
        """SetPixel(integer x,integer y,integer type,data[] pixel)"""
        ...

    def Size(self):
        """(integer w,integer h) = Size()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class IndexImage(object):
    def __init__(self, *args, **kwargs):
        ...

    def Format(self):
        """integer = Format()"""
        ...

    def GetIndex(self, x, y):
        """integer index = GetIndex(integer x,integer y)"""
        ...

    def GetMap(self, index, type, pixel):
        """GetMap(integer index,integer type,data[] pixel)"""
        ...

    def MapSize(self):
        """integer numColors = MapSize()"""
        ...

    def Size(self):
        """(integer w,integer h) = Size()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class IndexImageWrite(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddAttribute(self, name, type):
        """integer index = AddAttribute(string name,string type)"""
        ...

    def Format(self):
        """integer = Format()"""
        ...

    def SetIndex(self, x, y, index):
        """SetIndex(integer x,integer y,integer index)"""
        ...

    def SetMap(self, index, type, pixel):
        """SetMap(integer index,integer type,data[] pixel)"""
        ...

    def Size(self):
        """(integer w,integer h) = Size()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class InputDeviceInstance(object):
    def __init__(self, *args, **kwargs):
        ...

    def AnalogCount(self):
        """integer = AnalogCount()"""
        ...

    def AnalogMetrics(self, index):
        """(integer isAbsolute,integer isDirectional) = AnalogMetrics(integer index)"""
        ...

    def AnalogName(self, index):
        """string = AnalogName(integer index)"""
        ...

    def AnalogUserName(self, index):
        """string = AnalogUserName(integer index)"""
        ...

    def AnalogValue(self, index):
        """float value = AnalogValue(integer index)"""
        ...

    def ButtonCount(self):
        """integer = ButtonCount()"""
        ...

    def ButtonIsDown(self, index):
        """boolean = ButtonIsDown(integer index)"""
        ...

    def ButtonName(self, index):
        """string = ButtonName(integer index)"""
        ...

    def ButtonUserName(self, index):
        """string = ButtonUserName(integer index)"""
        ...

    def IsConnected(self):
        """IsConnected()"""
        ...

    def Name(self, name):
        """Name(string name)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class InputDevices(object):
    def __init__(self, *args, **kwargs):
        ...

    def DeviceCount(self):
        """integer = DeviceCount()"""
        ...

    def DeviceInstanceByIndex(self, index):
        """InputDeviceInstance object = DeviceInstanceByIndex(integer index)"""
        ...

    def DeviceNameByIndex(self, index, name):
        """DeviceNameByIndex(integer index,string name)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class InstanceAssets(object):
    def __init__(self, *args, **kwargs):
        ...

    def Category(self, index):
        """string = Category(integer index)"""
        ...

    def Count(self):
        """integer count = Count()"""
        ...

    def GetPath(self, ident):
        """string = GetPath(string ident)"""
        ...

    def IdentByIndex(self, index):
        """(integer isSeq,string fileType,string) = IdentByIndex(integer index)"""
        ...

    def SetPath(self, ident, newPath):
        """SetPath(string ident,string newPath)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Instanceable(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddElements(self, tableau, instT0, instT1):
        """AddElements(object tableau,object instT0,object instT1)"""
        ...

    def Compare(self, other):
        """integer = Compare(object other)"""
        ...

    def GetSurface(self):
        """Unknown object = GetSurface()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class IntRange(object):
    def __init__(self, *args, **kwargs):
        ...

    def AllAfter(self):
        """boolean = AllAfter()"""
        ...

    def AllBefore(self):
        """boolean = AllBefore()"""
        ...

    def Current(self):
        """integer current = Current()"""
        ...

    def First(self):
        """integer first = First()"""
        ...

    def Last(self):
        """integer last = Last()"""
        ...

    def Max(self):
        """integer max = Max()"""
        ...

    def Min(self):
        """integer min = Min()"""
        ...

    def Next(self):
        """integer i = Next()"""
        ...

    def Prev(self):
        """integer i = Prev()"""
        ...

    def Test(self, i):
        """boolean = Test(integer i)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Interviewer(object):
    def __init__(self, *args, **kwargs):
        ...

    def ButtonCommand(self):
        """string = ButtonCommand()"""
        ...

    def ButtonLabel(self):
        """string = ButtonLabel()"""
        ...

    def Description(self):
        """string = Description()"""
        ...

    def Title(self):
        """string = Title()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Item(object):
    def __init__(self, *args, **kwargs):
        ...

    def BaseName(self):
        """string name = BaseName()"""
        ...

    def ChannelAdd(self):
        """Unknown object = ChannelAdd()"""
        ...

    def ChannelCount(self):
        """integer count = ChannelCount()"""
        ...

    def ChannelEvalType(self, index):
        """string type = ChannelEvalType(integer index)"""
        ...

    def ChannelGradient(self, index):
        """(string input,string output) = ChannelGradient(integer index)"""
        ...

    def ChannelIntHint(self, index):
        """hints hints = ChannelIntHint(integer index)"""
        ...

    def ChannelIsDriven(self, index):
        """boolean = ChannelIsDriven(integer index)"""
        ...

    def ChannelLookup(self, name):
        """integer index = ChannelLookup(string name)"""
        ...

    def ChannelName(self, index):
        """string name = ChannelName(integer index)"""
        ...

    def ChannelPackage(self, index):
        """string package = ChannelPackage(integer index)"""
        ...

    def ChannelStorageType(self, index):
        """string type = ChannelStorageType(integer index)"""
        ...

    def ChannelType(self, index):
        """integer type = ChannelType(integer index)"""
        ...

    def ChannelVectorMode(self, index):
        """(integer mode,integer components) = ChannelVectorMode(integer index)"""
        ...

    def Context(self):
        """Scene object = Context()"""
        ...

    def Delete(self):
        """Delete()"""
        ...

    def GetTag(self, type):
        """string = GetTag(integer type)"""
        ...

    def Ident(self):
        """string ident = Ident()"""
        ...

    def InvalidateName(self):
        """InvalidateName()"""
        ...

    def IsReferenced(self):
        """boolean = IsReferenced()"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def PackageAdd(self, package):
        """PackageAdd(string package)"""
        ...

    def PackageRemove(self, package):
        """PackageRemove(string package)"""
        ...

    def PackageStartIndex(self, package):
        """integer index = PackageStartIndex(string package)"""
        ...

    def PackageTest(self, package):
        """boolean = PackageTest(string package)"""
        ...

    def Parent(self):
        """Item object = Parent()"""
        ...

    def Reference(self):
        """Item object = Reference()"""
        ...

    def Root(self):
        """Item object = Root()"""
        ...

    def SetIdent(self, ident):
        """SetIdent(string ident)"""
        ...

    def SetName(self, name):
        """SetName(string name)"""
        ...

    def SetParent(self, parent):
        """SetParent(object parent)"""
        ...

    def SetParentAndPosition(self, parent, pos):
        """SetParentAndPosition(object parent,integer pos)"""
        ...

    def SetSource(self, source):
        """SetSource(object source)"""
        ...

    def SetTag(self, type, tag):
        """SetTag(integer type,string tag)"""
        ...

    def SetUniqueIndex(self, index):
        """SetUniqueIndex(integer index)"""
        ...

    def Source(self):
        """Item object = Source()"""
        ...

    def SubByIndex(self, index):
        """Item object = SubByIndex(integer index)"""
        ...

    def SubCount(self):
        """integer count = SubCount()"""
        ...

    def TestType(self, type):
        """boolean = TestType(integer type)"""
        ...

    def TestTypes(self, types):
        """boolean = TestTypes(int[] types)"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def UniqueIndex(self):
        """integer index = UniqueIndex()"""
        ...

    def UniqueName(self):
        """string name = UniqueName()"""
        ...

    def WasLoaded(self, test):
        """boolean = WasLoaded(integer test)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ItemChannel(object):
    def __init__(self, *args, **kwargs):
        ...

    def ChannelIndex(self):
        """integer = ChannelIndex()"""
        ...

    def Item(self):
        """Item object = Item()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ItemCollection(object):
    def __init__(self, *args, **kwargs):
        ...

    def Add(self, item):
        """Add(object item)"""
        ...

    def ByIndex(self, type, index):
        """Item object = ByIndex(integer type,integer index)"""
        ...

    def Count(self, type):
        """integer count = Count(integer type)"""
        ...

    def Test(self, item):
        """boolean = Test(object item)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ItemGraph(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddLink(self, from_obj, to_obj):
        """AddLink(object from_obj,object to_obj)"""
        ...

    def DeleteLink(self, from_obj, to_obj):
        """DeleteLink(object from_obj,object to_obj)"""
        ...

    def FwdByIndex(self, item, index):
        """Item object = FwdByIndex(object item,integer index)"""
        ...

    def FwdCount(self, item):
        """integer count = FwdCount(object item)"""
        ...

    def RevByIndex(self, item, index):
        """Item object = RevByIndex(object item,integer index)"""
        ...

    def RevCount(self, item):
        """integer count = RevCount(object item)"""
        ...

    def SetLink(self, from_obj, fromIndex, to_obj, toIndex):
        """SetLink(object from_obj,integer fromIndex,object to_obj,integer toIndex)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ItemInfluence(object):
    def __init__(self, *args, **kwargs):
        ...

    def AllowTransform(self, index):
        """integer flags = AllowTransform(integer index)"""
        ...

    def Enumerate(self, visitor):
        """Enumerate(object visitor)"""
        ...

    def GetItem(self):
        """Item object = GetItem()"""
        ...

    def HasItems(self):
        """boolean = HasItems()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ItemListType(object):
    def __init__(self, *args, **kwargs):
        ...

    def GenerateList(self, scene, collection):
        """GenerateList(object scene,object collection)"""
        ...

    def SetArgument(self, arg):
        """SetArgument(string arg)"""
        ...

    def SetRootItem(self, item):
        """SetRootItem(object item)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ItemPacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Item(self, packet):
        """Item object = Item(pointer packet)"""
        ...

    def Packet(self, item):
        """pointer = Packet(object item)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ItemReplacement(object):
    def __init__(self, *args, **kwargs):
        ...

    def NotifierByIndex(self, itemType, channelName, index):
        """string = NotifierByIndex(string itemType,string channelName,integer index)"""
        ...

    def NotifierCount(self, itemType, channelName):
        """integer count = NotifierCount(string itemType,string channelName)"""
        ...

    def ReplaceItems(self, current, replacement, targetType):
        """ReplaceItems(object current,object replacement,integer targetType)"""
        ...

    def Types(self, curType):
        """string repTypes = Types(string curType)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ItemTypeDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Item(self):
        """Item object = Item()"""
        ...

    def Location(self):
        """integer = Location()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Keyframe(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddF(self, time, value):
        """AddF(float time,float value)"""
        ...

    def AddI(self, time, value):
        """AddI(float time,integer value)"""
        ...

    def Delete(self):
        """Delete()"""
        ...

    def Find(self, time, side):
        """Find(float time,integer side)"""
        ...

    def First(self):
        """First()"""
        ...

    def GetBroken(self):
        """(integer breaks,integer side) = GetBroken()"""
        ...

    def GetSlope(self, side):
        """float slope = GetSlope(integer side)"""
        ...

    def GetSlopeType(self, side):
        """(integer type,integer weighted) = GetSlopeType(integer side)"""
        ...

    def GetTime(self):
        """float time = GetTime()"""
        ...

    def GetValueF(self, side):
        """float value = GetValueF(integer side)"""
        ...

    def GetValueI(self, side):
        """integer value = GetValueI(integer side)"""
        ...

    def GetWeight(self, side):
        """float weight = GetWeight(integer side)"""
        ...

    def Last(self):
        """Last()"""
        ...

    def Next(self):
        """Next()"""
        ...

    def Previous(self):
        """Previous()"""
        ...

    def SetSlope(self, slope, side):
        """SetSlope(float slope,integer side)"""
        ...

    def SetSlopeType(self, type, side):
        """SetSlopeType(integer type,integer side)"""
        ...

    def SetTime(self, time):
        """SetTime(float time)"""
        ...

    def SetValueF(self, value, side):
        """SetValueF(float value,integer side)"""
        ...

    def SetValueI(self, value, side):
        """SetValueI(integer value,integer side)"""
        ...

    def SetWeight(self, weight, reset, side):
        """SetWeight(float weight,integer reset,integer side)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Kit(object):
    def __init__(self, *args, **kwargs):
        ...

    def IsEnabled(self):
        """boolean = IsEnabled()"""
        ...

    def IsVisible(self):
        """boolean = IsVisible()"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def SetEnabled(self, enabled):
        """SetEnabled(integer enabled)"""
        ...

    def Version(self):
        """string version = Version()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...


class LayerScan(object):
    """ The LayerScan interface is the main way to do mesh edits. It can also be
    used in a non-edit mode to confirm what will happen when editing. 

    """
    def __init__(self, *args, **kwargs):
        ...

    def Apply(self) -> None:
        """Apply()"""
        ...

    def Count(self) -> int:
        """integer count = Count()"""
        ...

    def GetState(self, index: int) -> int:
        """ Query the state of a given layer. The state is a combination of the
        ACTIVE, BACKGROUND or PRIMARY layer scan flags.

        integer state = GetState(integer index)

        """
        ...

    def MeshAction(self, index: int) -> ChannelRead:
        """ChannelRead object = MeshAction(integer index)"""
        ...

    def MeshBase(self, index: int) -> Mesh:
        """Mesh object = MeshBase(integer index)"""
        ...

    def MeshEdit(self, index: int) -> Mesh:
        """Mesh object = MeshEdit(integer index)"""
        ...

    def MeshInstance(self, index: int) -> Mesh:
        """Mesh object = MeshInstance(integer index)"""
        ...

    def MeshItem(self, index: int) -> Item:
        """Item object = MeshItem(integer index)"""
        ...

    def MeshTransform(self, index: int) -> Matrix4:
        """ returns a Matrix4 representing the world transform of the mesh item. 

        matrix matrix = MeshTransform(integer index)

        """
        ...

    def SetMeshChange(self, index: int, edits: int) -> None:
        """SetMeshChange(integer index,integer edits)"""
        ...

    def Update(self) -> None:
        """Update()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class LayeredImage(object):
    def __init__(self, *args, **kwargs):
        ...

    def Blend(self, index):
        """(float opacity,integer mode) = Blend(integer index)"""
        ...

    def ChannelName(self, layerIndex, channelIndex):
        """string name = ChannelName(integer layerIndex,integer channelIndex)"""
        ...

    def Count(self):
        """integer = Count()"""
        ...

    def Image(self, index):
        """Image object = Image(integer index)"""
        ...

    def IsGroup(self, layerIndex):
        """integer isGroup = IsGroup(integer layerIndex)"""
        ...

    def Name(self, index):
        """string name = Name(integer index)"""
        ...

    def Offset(self, index):
        """(integer x,integer y) = Offset(integer index)"""
        ...

    def Parent(self, layerIndex):
        """integer parentIndex = Parent(integer layerIndex)"""
        ...

    def Size(self):
        """(integer w,integer h) = Size()"""
        ...

    def Type(self, index):
        """(integer flags,string type) = Type(integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class LayeredImageWrite(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddAttribute(self, name, type):
        """integer index = AddAttribute(string name,string type)"""
        ...

    def AddLayer(self, image, name):
        """string channelNames = AddLayer(object image,string name)"""
        ...

    def SetBlending(self, index, blend, mode):
        """SetBlending(integer index,float blend,string mode)"""
        ...

    def SetOffset(self, index, x, y):
        """SetOffset(integer index,integer x,integer y)"""
        ...

    def SetType(self, index, flags, type):
        """SetType(integer index,integer flags,string type)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class LightSample(object):
    def __init__(self, *args, **kwargs):
        ...

    def Vertex(self, vertex):
        """Vertex(float[] vertex)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Lighting(object):
    def __init__(self, *args, **kwargs):
        ...

    def EnvironmentEvaluate(self, vector, samples, flags):
        """vector lum = EnvironmentEvaluate(object vector,integer samples,integer flags)"""
        ...

    def GIRequired(self, vector):
        """integer = GIRequired(object vector)"""
        ...

    def LightSourceCount(self, vector):
        """integer num = LightSourceCount(object vector)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class LineExecution(object):
    def __init__(self, *args, **kwargs):
        ...

    def CookedLine(self, text):
        """CookedLine(string text)"""
        ...

    def Info(self, text):
        """Info(string text)"""
        ...

    def Message(self, message):
        """Message(object message)"""
        ...

    def ResultHints(self, hints):
        """ResultHints(hints hints)"""
        ...

    def Results(self, valArray):
        """Results(object valArray)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class LineInterpreter(object):
    def __init__(self, *args, **kwargs):
        ...

    def Execute(self, line, execFlags, execution):
        """Execute(string line,integer execFlags,object execution)"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def Prompt(self, type):
        """string prompt = Prompt(integer type)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class LinkPacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def From(self, packet):
        """(integer channel,Item object) = From(pointer packet)"""
        ...

    def Packet(self, fromItem, fromChannel, toItem, toChannel):
        """pointer = Packet(object fromItem,integer fromChannel,object toItem,integer toChannel)"""
        ...

    def To(self, packet):
        """(integer channel,Item object) = To(pointer packet)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ListenerPort(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddListener(self, object):
        """AddListener(object object)"""
        ...

    def RemoveListener(self, object):
        """RemoveListener(object object)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Loader(object):
    def __init__(self, *args, **kwargs):
        ...

    def Cleanup(self):
        """Cleanup()"""
        ...

    def LoadInstance(self, loadInfo, monitor):
        """Unknown object = LoadInstance(object loadInfo,object monitor)"""
        ...

    def LoadObject(self, loadInfo, monitor, dest):
        """LoadObject(object loadInfo,object monitor,object dest)"""
        ...

    def Recognize(self, filename, loadInfo):
        """Recognize(string filename,object loadInfo)"""
        ...

    def SpawnOptions(self):
        """Unknown object = SpawnOptions()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class LoaderInfo(object):
    def __init__(self, *args, **kwargs):
        ...

    def SetClass(self, clsGUID):
        """SetClass(string clsGUID)"""
        ...

    def SetFlags(self, flags):
        """SetFlags(integer flags)"""
        ...

    def SetFormat(self, format):
        """SetFormat(string format)"""
        ...

    def TestClass(self, clsGUID):
        """integer priority = TestClass(string clsGUID)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Locator(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddPostTransformItem(self, chanWrite, type, value):
        """(Item object,integer index) = AddPostTransformItem(object chanWrite,integer type,vector value)"""
        ...

    def AddPreTransformItem(self, chanWrite, type, value):
        """(Item object,integer index) = AddPreTransformItem(object chanWrite,integer type,vector value)"""
        ...

    def AddTransformItem(self, type):
        """(Item object,integer index) = AddTransformItem(integer type)"""
        ...

    def AppendTransformItem(self, chanWrite, type, value):
        """(Item object,integer index) = AppendTransformItem(object chanWrite,integer type,vector value)"""
        ...

    def ExtractLocalPosition(self, chanRead):
        """vector pos = ExtractLocalPosition(object chanRead)"""
        ...

    def ExtractLocalRotation(self, chanRead):
        """matrix m3 = ExtractLocalRotation(object chanRead)"""
        ...

    def GetTransformItem(self, type):
        """Item object = GetTransformItem(integer type)"""
        ...

    def LocalTransform(self, chanRead):
        """(matrix xfrm,vector pos) = LocalTransform(object chanRead)"""
        ...

    def LocalTransform4(self, chanRead):
        """matrix xfrm4 = LocalTransform4(object chanRead)"""
        ...

    def PrependTransformItem(self, chanWrite, type, value):
        """(Item object,integer index) = PrependTransformItem(object chanWrite,integer type,vector value)"""
        ...

    def SetPosition(self, chanRead, chanWrite, pos, type, comp):
        """SetPosition(object chanRead,object chanWrite,vector pos,integer type,integer comp)"""
        ...

    def SetRotation(self, chanRead, chanWrite, m3, type, comp):
        """SetRotation(object chanRead,object chanWrite,matrix m3,integer type,integer comp)"""
        ...

    def SetScale(self, chanRead, chanWrite, m4, type, comp):
        """SetScale(object chanRead,object chanWrite,matrix m4,integer type,integer comp)"""
        ...

    def SetTarget(self, target):
        """Item object = SetTarget(object target)"""
        ...

    def SetTransformVector(self, chanWrite, type, value):
        """SetTransformVector(object chanWrite,integer type,vector value)"""
        ...

    def Visible(self, chanRead):
        """boolean = Visible(object chanRead)"""
        ...

    def WorldInvertTransform(self, chanRead):
        """(matrix xfrm,vector pos) = WorldInvertTransform(object chanRead)"""
        ...

    def WorldTransform(self, chanRead):
        """(matrix xfrm,vector pos) = WorldTransform(object chanRead)"""
        ...

    def WorldTransform4(self, chanRead):
        """matrix xfrm4 = WorldTransform4(object chanRead)"""
        ...

    def ZeroTransform(self, chanRead, chanWrite, type):
        """ZeroTransform(object chanRead,object chanWrite,integer type)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class LocatorDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Item(self):
        """Item object = Item()"""
        ...

    def Location(self):
        """integer = Location()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Log(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddEntry(self, entry):
        """AddEntry(object entry)"""
        ...

    def ClearAll(self):
        """ClearAll()"""
        ...

    def EntryByIndex(self, index):
        """LogEntry object = EntryByIndex(integer index)"""
        ...

    def EntryCount(self):
        """integer count = EntryCount()"""
        ...

    def GetCurrentEntry(self):
        """LogEntry object = GetCurrentEntry()"""
        ...

    def GetMaxEntries(self):
        """integer max = GetMaxEntries()"""
        ...

    def GetRolling(self):
        """LogEntry object = GetRolling()"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def PeekEntryByIndex(self, index):
        """object = PeekEntryByIndex(integer index)"""
        ...

    def RollClear(self):
        """RollClear()"""
        ...

    def RollEntry(self, entry):
        """RollEntry(object entry)"""
        ...

    def SetMaxEntries(self, max):
        """SetMaxEntries(integer max)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class LogEntry(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddEntry(self, entry):
        """AddEntry(object entry)"""
        ...

    def AddPair(self, name, value):
        """AddPair(string name,string value)"""
        ...

    def ChildByIndex(self, index):
        """LogEntry object = ChildByIndex(integer index)"""
        ...

    def ChildCount(self):
        """integer count = ChildCount()"""
        ...

    def Class(self):
        """integer classType = Class()"""
        def __init__(self, *args, **kwargs):
            ...

        ...

    def Desc(self):
        """string desc = Desc()"""
        ...

    def InfoBlock(self):
        """LogInfoBlock object = InfoBlock()"""
        ...

    def InfoBlockValue(self, name, index):
        """Unknown object = InfoBlockValue(string name,integer index)"""
        ...

    def Message(self):
        """string message = Message()"""
        ...

    def PairCount(self):
        """integer count = PairCount()"""
        ...

    def PairName(self, index):
        """string name = PairName(integer index)"""
        ...

    def PairValue(self, index):
        """string value = PairValue(integer index)"""
        ...

    def PeekChildByIndex(self, index):
        """object = PeekChildByIndex(integer index)"""
        ...

    def SetDesc(self, desc):
        """SetDesc(string desc)"""
        ...

    def SetTitle(self, title):
        """SetTitle(string title)"""
        ...

    def SetValue(self, name, index, value):
        """SetValue(string name,integer index,object value)"""
        ...

    def SubSystemByIndex(self, index):
        """Unknown object = SubSystemByIndex(integer index)"""
        ...

    def SubSystemCount(self):
        """integer count = SubSystemCount()"""
        ...

    def TimeString(self):
        """string string = TimeString()"""
        ...

    def Title(self):
        """string title = Title()"""
        ...

    def Type(self):
        """integer type = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class LogInfoBlock(object):
    def __init__(self, *args, **kwargs):
        ...

    def FieldCount(self):
        """integer count = FieldCount()"""
        ...

    def FieldName(self, index):
        """string name = FieldName(integer index)"""
        ...

    def FieldType(self, index):
        """string type = FieldType(integer index)"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class LogListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def ChildEntryAdded(self, entry, parentEntry):
        """ChildEntryAdded(object entry,object parentEntry)"""
        ...

    def EntryAdded(self, system, entry):
        """EntryAdded(object system,object entry)"""
        ...

    def EntryDropped(self, system, entry):
        """EntryDropped(object system,object entry)"""
        ...

    def RollingChildEntryAdded(self, entry, parentEntry):
        """RollingChildEntryAdded(object entry,object parentEntry)"""
        ...

    def RollingEntryAdded(self, system, entry):
        """RollingEntryAdded(object system,object entry)"""
        ...

    def RollingEntryDropped(self, system, entry):
        """RollingEntryDropped(object system,object entry)"""
        ...

    def SystemAdded(self, system):
        """SystemAdded(object system)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Matrix(object):
    def __init__(self, *args, **kwargs):
        ...

    def Get3(self):
        """matrix mat3 = Get3()"""
        ...

    def Get4(self):
        """matrix mat4 = Get4()"""
        ...

    def GetOffset(self):
        """vector offset = GetOffset()"""
        ...

    def Invert(self):
        """Invert()"""
        ...

    def Multiply3(self, mat3):
        """Multiply3(matrix mat3)"""
        ...

    def Multiply4(self, mat4):
        """Multiply4(matrix mat4)"""
        ...

    def MultiplyVector(self, vector):
        """vector result = MultiplyVector(vector vector)"""
        ...

    def Set3(self, mat3):
        """Set3(matrix mat3)"""
        ...

    def Set4(self, mat4):
        """Set4(matrix mat4)"""
        ...

    def SetIdentity(self):
        """SetIdentity()"""
        ...

    def SetOffset(self, offset):
        """SetOffset(vector offset)"""
        ...

    def Transpose(self):
        """Transpose()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MergedDirCacheEntry(object):
    def __init__(self, *args, **kwargs):
        ...

    def EntryByIndex(self, index):
        """DirCacheEntry object = EntryByIndex(integer index)"""
        ...

    def EntryCount(self):
        """integer count = EntryCount()"""
        ...

    def Parent(self):
        """DirCacheEntry object = Parent()"""
        ...

    def Path(self):
        """string = Path()"""
        ...

    def UserPath(self):
        """string = UserPath()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MergedFileSysDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def EntryByIndex(self, index):
        """Unknown object = EntryByIndex(integer index)"""
        ...

    def EntryCount(self):
        """integer count = EntryCount()"""
        ...

    def MergedEntry(self):
        """Unknown object = MergedEntry()"""
        ...

    def Path(self):
        """string = Path()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Mesh(object):
    def __init__(self, *args, **kwargs):
        ...

    def BeginEditBatch(self):
        """BeginEditBatch()"""
        ...

    def BoundingBox(self, pick):
        """bounds bbox = BoundingBox(integer pick)"""
        ...

    def ChangeEvent(self, event):
        """ChangeEvent(integer event)"""
        ...

    def Clear(self):
        """Clear()"""
        ...

    def EdgeAccessor(self):
        """Edge object = EdgeAccessor()"""
        ...

    def EdgeCount(self):
        """integer count = EdgeCount()"""
        ...

    def EndEditBatch(self):
        """EndEditBatch()"""
        ...

    def MapCount(self):
        """integer count = MapCount()"""
        ...

    def MaxPointPolygons(self, pick):
        """integer count = MaxPointPolygons(integer pick)"""
        ...

    def MaxPolygonSize(self, pick):
        """integer count = MaxPolygonSize(integer pick)"""
        ...

    def Merge(self, other, flags):
        """Merge(object other,integer flags)"""
        ...

    def MergeWithTransform(self, other, xfrm, flags):
        """MergeWithTransform(object other,matrix xfrm,integer flags)"""
        ...

    def MeshMapAccessor(self):
        """MeshMap object = MeshMapAccessor()"""
        ...

    def PSUBDispLayerCurrent(self):
        """integer index = PSUBDispLayerCurrent()"""
        ...

    def PSUBDispLayerEnable(self, index):
        """integer enable = PSUBDispLayerEnable(integer index)"""
        ...

    def PSUBDispLayerLookupByName(self, name):
        """integer index = PSUBDispLayerLookupByName(string name)"""
        ...

    def PSUBDispLayerName(self, index):
        """string = PSUBDispLayerName(integer index)"""
        ...

    def PSUBDispLayerOpacity(self, index):
        """float opacity = PSUBDispLayerOpacity(integer index)"""
        ...

    def PSUBDispLayerSetOpacity(self, index, opacity):
        """PSUBDispLayerSetOpacity(integer index,float opacity)"""
        ...

    def PSUBDispNumLayer(self):
        """integer num = PSUBDispNumLayer()"""
        ...

    def PSUBGetBoundRule(self):
        """integer bound = PSUBGetBoundRule()"""
        ...

    def PSUBGetCurrentLevel(self):
        """integer n = PSUBGetCurrentLevel()"""
        ...

    def PSUBGetLevel(self):
        """integer n = PSUBGetLevel()"""
        ...

    def PSUBSetBoundRule(self, bound):
        """PSUBSetBoundRule(integer bound)"""
        ...

    def PSUBSetCurrentLevel(self, n):
        """PSUBSetCurrentLevel(integer n)"""
        ...

    def PSUBSetLevel(self, n):
        """PSUBSetLevel(integer n)"""
        ...

    def PSUBSetSubdivObj(self, subObj):
        """PSUBSetSubdivObj(object subObj)"""
        ...

    def PTagByIndex(self, type, index):
        """string tag = PTagByIndex(integer type,integer index)"""
        ...

    def PTagCount(self, type):
        """integer = PTagCount(integer type)"""
        ...

    def PointAccessor(self):
        """Point object = PointAccessor()"""
        ...

    def PointCount(self):
        """integer count = PointCount()"""
        ...

    def PolyTagSetDefault(self, type, tag):
        """PolyTagSetDefault(integer type,string tag)"""
        ...

    def PolygonAccessor(self):
        """Polygon object = PolygonAccessor()"""
        ...

    def PolygonCount(self):
        """integer count = PolygonCount()"""
        ...

    def SUBDGetLevel(self):
        """integer n = SUBDGetLevel()"""
        ...

    def SUBDGetLinearUV(self):
        """integer isLinear = SUBDGetLinearUV()"""
        ...

    def SUBDSetLevel(self, n):
        """SUBDSetLevel(integer n)"""
        ...

    def SUBDSetLinearUV(self, isLinear):
        """SUBDSetLinearUV(integer isLinear)"""
        ...

    def SetMeshEdits(self, edits):
        """SetMeshEdits(integer edits)"""
        ...

    def TestSameMesh(self, other):
        """boolean = TestSameMesh(object other)"""
        ...

    def TrackChanges(self):
        """Unknown object = TrackChanges()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshBlend(object):
    def __init__(self, *args, **kwargs):
        ...

    def BlendMesh(self, t):
        """Unknown object = BlendMesh(float t)"""
        ...

    def EnumeratePoints(self, source, target, visitor):
        """EnumeratePoints(object source,object target,object visitor)"""
        ...

    def EnumeratePolygons(self, source, target, visitor):
        """EnumeratePolygons(object source,object target,object visitor)"""
        ...

    def GetPoint(self, source):
        """id target = GetPoint(id source)"""
        ...

    def GetPolygon(self, source):
        """id target = GetPolygon(id source)"""
        ...

    def SetPoint(self, source, target):
        """SetPoint(id source,id target)"""
        ...

    def SetPolygon(self, source, target):
        """SetPolygon(id source,id target)"""
        ...

    def SourceMesh(self):
        """Unknown object = SourceMesh()"""
        ...

    def TargetMesh(self):
        """Unknown object = TargetMesh()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def HitNormal(self):
        """vector nrm = HitNormal()"""
        ...

    def HitPosition(self):
        """vector pos = HitPosition()"""
        ...

    def Item(self):
        """Item object = Item()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshElementGroup(object):
    def __init__(self, *args, **kwargs):
        ...

    def GroupCount(self):
        """integer count = GroupCount()"""
        ...

    def GroupName(self, index):
        """string name = GroupName(integer index)"""
        ...

    def GroupUserName(self, index):
        """string username = GroupUserName(integer index)"""
        ...

    def TestEdge(self, index, edge):
        """boolean = TestEdge(integer index,id edge)"""
        ...

    def TestPoint(self, index, point):
        """boolean = TestPoint(integer index,id point)"""
        ...

    def TestPolygon(self, index, polygon):
        """boolean = TestPolygon(integer index,id polygon)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshFilter(object):
    def __init__(self, *args, **kwargs):
        ...

    def Evaluate(self, mesh, tracker):
        """Evaluate(object mesh,object tracker)"""
        ...

    def Generate(self):
        """Mesh object = Generate()"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshFilterBBox(object):
    def __init__(self, *args, **kwargs):
        ...

    def Evaluate(self):
        """bounds box = Evaluate()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshFilterBlend(object):
    def __init__(self, *args, **kwargs):
        ...

    def Evaluate(self, other, blend):
        """Evaluate(object other,object blend)"""
        ...

    def Generate(self, other):
        """MeshBlend object = Generate(object other)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshFilterIdent(object):
    def __init__(self, *args, **kwargs):
        ...

    def Generate(self, ident):
        """Mesh object = Generate(string ident)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshInfluence(object):
    def __init__(self, *args, **kwargs):
        ...

    def MeshByIndex(self, index):
        """Item object = MeshByIndex(integer index)"""
        ...

    def MeshChange(self, index, change):
        """MeshChange(integer index,integer change)"""
        ...

    def MeshCount(self):
        """integer = MeshCount()"""
        ...

    def PartitionIndex(self, index):
        """integer = PartitionIndex(integer index)"""
        ...

    def SetMesh(self, index, mesh, item):
        """SetMesh(integer index,object mesh,object item)"""
        ...

    def SetTransform(self, index):
        """matrix xfrm = SetTransform(integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshLayerPreDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Mesh(self):
        """Mesh object = Mesh()"""
        ...

    def ShaderDest(self):
        """ShaderPreDest object = ShaderDest()"""
        ...

    def Transform(self):
        """matrix xform = Transform()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshMap(object):
    def __init__(self, *args, **kwargs):
        ...

    def Clear(self):
        """Clear()"""
        ...

    def Dimension(self):
        """integer dimension = Dimension()"""
        ...

    def Enumerate(self, mode, visitor, monitor):
        """Enumerate(integer mode,object visitor,object monitor)"""
        ...

    def EnumerateContinuous(self, visitor, point):
        """EnumerateContinuous(object visitor,object point)"""
        ...

    def EnumerateDiscontinuous(self, visitor, point, poly):
        """EnumerateDiscontinuous(object visitor,object point,object poly)"""
        ...

    def EnumerateEdges(self, visitor, edge):
        """EnumerateEdges(object visitor,object edge)"""
        ...

    def EnumerateUVSeamEdges(self, visitor, edge, poly):
        """EnumerateUVSeamEdges(object visitor,object edge,object poly)"""
        ...

    def FilterByType(self, type):
        """FilterByType(integer type)"""
        ...

    def ID(self):
        """id = ID()"""
        ...

    def IsContinuous(self):
        """boolean = IsContinuous()"""
        ...

    def IsEdgeMap(self):
        """boolean = IsEdgeMap()"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def New(self, type, name):
        """id mapID = New(integer type,string name)"""
        ...

    def Remove(self):
        """Remove()"""
        ...

    def Select(self, map):
        """Select(id map)"""
        ...

    def SelectByName(self, type, name):
        """SelectByName(integer type,string name)"""
        ...

    def SetName(self, name):
        """SetName(string name)"""
        ...

    def Spawn(self):
        """MeshMap object = Spawn()"""
        ...

    def Type(self):
        """integer type = Type()"""
        ...

    def UVBoundingBox(self):
        """bounds bbox = UVBoundingBox()"""
        ...

    def UVSeamOppositeEdge(self, originalEdge, originalPoly):
        """(id opppositePoly,integer isReverse) = UVSeamOppositeEdge(id originalEdge,id originalPoly)"""
        ...

    def ZeroDefault(self):
        """boolean = ZeroDefault()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshOpDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Graph(self):
        """string = Graph()"""
        ...

    def Item(self):
        """Item object = Item()"""
        ...

    def ItemDeformer(self):
        """Item object = ItemDeformer()"""
        ...

    def Location(self):
        """integer = Location()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshOperation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Blend(self, other, blend):
        """Blend(object other,object blend)"""
        ...

    def Clone(self, target, source):
        """Unknown object = Clone(object target,object source)"""
        ...

    def Compare(self, other):
        """integer = Compare(object other)"""
        ...

    def Convert(self, other):
        """Convert(object other)"""
        ...

    def Evaluate(self, mesh, type, mode):
        """Evaluate(object mesh,integer type,integer mode)"""
        ...

    def ReEvaluate(self, mesh, type):
        """ReEvaluate(object mesh,integer type)"""
        ...

    def SetTransform(self, matrix):
        """SetTransform(matrix matrix)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshTracker(object):
    def __init__(self, *args, **kwargs):
        ...

    def Active(self):
        """Active()"""
        ...

    def AddPoint(self, point, change):
        """AddPoint(id point,integer change)"""
        ...

    def AddPolygon(self, poly, change):
        """AddPolygon(id poly,integer change)"""
        ...

    def Changes(self):
        """integer edit = Changes()"""
        ...

    def EnumeratePoints(self, change, visitor, point):
        """EnumeratePoints(integer change,object visitor,object point)"""
        ...

    def EnumeratePolygons(self, change, visitor, poly):
        """EnumeratePolygons(integer change,object visitor,object poly)"""
        ...

    def Filter(self):
        """integer filter = Filter()"""
        ...

    def Mesh(self):
        """Unknown object = Mesh()"""
        ...

    def Reset(self):
        """Reset()"""
        ...

    def SetChange(self, change):
        """SetChange(integer change)"""
        ...

    def SetFilter(self, filter):
        """SetFilter(integer filter)"""
        ...

    def Start(self):
        """Start()"""
        ...

    def Stop(self):
        """Stop()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class MeshXtraData(object):
    def __init__(self, *args, **kwargs):
        ...

    def ClearPoint(self, point):
        """ClearPoint(id point)"""
        ...

    def ClearPolygon(self, poly):
        """ClearPolygon(id poly)"""
        ...

    def GetPointObject(self, point):
        """Unknown object = GetPointObject(id point)"""
        ...

    def GetPolygonObject(self, poly):
        """Unknown object = GetPolygonObject(id poly)"""
        ...

    def SetPointData(self, point, data):
        """SetPointData(id point,pointer data)"""
        ...

    def SetPointObject(self, point, obj):
        """SetPointObject(id point,object obj)"""
        ...

    def SetPolygonData(self, poly, data):
        """SetPolygonData(id poly,pointer data)"""
        ...

    def SetPolygonObject(self, poly, obj):
        """SetPolygonObject(id poly,object obj)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Message(object):
    def __init__(self, *args, **kwargs):
        ...

    def Code(self):
        """Code()"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def Reset(self):
        """Reset()"""
        ...

    def SetArgumentFloat(self, arg, value):
        """SetArgumentFloat(integer arg,float value)"""
        ...

    def SetArgumentInt(self, arg, value):
        """SetArgumentInt(integer arg,integer value)"""
        ...

    def SetArgumentObject(self, arg, object):
        """SetArgumentObject(integer arg,object object)"""
        ...

    def SetArgumentString(self, arg, string):
        """SetArgumentString(integer arg,string string)"""
        ...

    def SetCode(self, code):
        """SetCode(integer code)"""
        ...

    def SetMessage(self, table, name, id):
        """SetMessage(string table,string name,integer id)"""
        ...

    def SetMessageResult(self, id):
        """SetMessageResult(integer id)"""
        ...

    def Table(self):
        """string table = Table()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Modifier(object):
    def __init__(self, *args, **kwargs):
        ...

    def Evaluate(self):
        """Evaluate()"""
        ...

    def Free(self, cache):
        """Free(pointer cache)"""
        ...

    def Invalidate(self, item, index):
        """boolean = Invalidate(object item,integer index)"""
        ...

    def Required(self, index):
        """(integer attr,Item object) = Required(integer index)"""
        ...

    def RequiredCount(self):
        """integer = RequiredCount()"""
        ...

    def Test(self, item, index):
        """boolean = Test(object item,integer index)"""
        ...

    def Validate(self, item, index, rc):
        """Validate(object item,integer index,integer rc)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Module(object):
    def __init__(self, *args, **kwargs):
        ...

    def Generate(self, name, iid):
        """Unknown object = Generate(string name,string iid)"""
        ...

    def GetTags(self, name, iid):
        """StringTag object = GetTags(string name,string iid)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Monitor(object):
    def __init__(self, *args, **kwargs):
        ...

    def Increment(self, count):
        """Increment(integer count)"""
        ...

    def Initialize(self, count):
        """Initialize(integer count)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class NavigationListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def Delta(self, view, item, hot, pos, rot, zoom):
        """Delta(object view,object item,integer hot,vector pos,matrix rot,float zoom)"""
        ...

    def Down(self, view, item):
        """Down(object view,object item)"""
        ...

    def HotSyncPost(self, view, item):
        """HotSyncPost(object view,object item)"""
        ...

    def HotSyncPre(self, view, item):
        """HotSyncPre(object view,object item)"""
        ...

    def Move(self, view, item, hot, pos, rot, zoom):
        """Move(object view,object item,integer hot,vector pos,matrix rot,float zoom)"""
        ...

    def Up(self, view, item):
        """Up(object view,object item)"""
        ...

    def Wheel(self, view, item):
        """Wheel(object view,object item)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class NeedContext(object):
    def __init__(self, *args, **kwargs):
        ...

    def SetContext(self, app):
        """SetContext(object app)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class NodePacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Node(self, packet):
        """Node object = Node(pointer packet)"""
        ...

    def Packet(self, node):
        """pointer = Packet(object node)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Notifier(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddClient(self, object):
        """AddClient(object object)"""
        ...

    def Args(self):
        """string args = Args()"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def RemoveClient(self, object):
        """RemoveClient(object object)"""
        ...

    def SetArgs(self, args):
        """SetArgs(string args)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Object(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddObserver(self, visitor):
        """AddObserver(object visitor)"""
        ...

    def Identifier(self):
        """string id = Identifier()"""
        ...

    def InterfaceByIndex(self, index):
        """string guid = InterfaceByIndex(integer index)"""
        ...

    def InterfaceCount(self):
        """integer count = InterfaceCount()"""
        ...

    def RemoveObserver(self, visitor):
        """RemoveObserver(object visitor)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Package(object):
    def __init__(self, *args, **kwargs):
        ...

    def Attach(self):
        """Unknown object = Attach()"""
        ...

    def CollectItems(self, collection, mode):
        """CollectItems(object collection,integer mode)"""
        ...

    def PostLoad(self, scene):
        """PostLoad(object scene)"""
        ...

    def SetupChannels(self, addChan):
        """SetupChannels(object addChan)"""
        ...

    def TestInterface(self, guid):
        """boolean = TestInterface(string guid)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PackageInstance(object):
    def __init__(self, *args, **kwargs):
        ...

    def Add(self):
        """Add()"""
        ...

    def AfterLoad(self):
        """AfterLoad()"""
        ...

    def Cleanup(self):
        """Cleanup()"""
        ...

    def Doomed(self):
        """Doomed()"""
        ...

    def DupType(self):
        """integer = DupType()"""
        ...

    def Initialize(self, item, super):
        """Initialize(object item,object super)"""
        ...

    def Loading(self):
        """Loading()"""
        ...

    def Newborn(self, original, flags):
        """Newborn(object original,integer flags)"""
        ...

    def Remove(self):
        """Remove()"""
        ...

    def SynthName(self):
        """string = SynthName()"""
        ...

    def TestParent(self, item):
        """boolean = TestParent(object item)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PacketEffect(object):
    def __init__(self, *args, **kwargs):
        ...

    def ByIndex(self, index):
        """(string name,string typeName,integer type) = ByIndex(integer index)"""
        ...

    def Count(self):
        """integer = Count()"""
        ...

    def Get(self, index, packet, item):
        """float val = Get(integer index,pointer packet,pointer item)"""
        ...

    def Packet(self):
        """string packet = Packet()"""
        ...

    def Set(self, index, packet, val, item):
        """Set(integer index,pointer packet,float[] val,pointer item)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PaintBrushPacket(object):
    def __init__(self, *args, **kwargs):
        ...

    def BBox(self, toolVector, center, size):
        """(integer,bounds bbox) = BBox(object toolVector,vector center,float size)"""
        ...

    def Eval3D(self, toolVector, center, wpos, bpos, rad):
        """(float,float rgba) = Eval3D(object toolVector,vector center,vector wpos,vector bpos,float rad)"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def Size(self):
        """float = Size()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PaintInkPacket(object):
    def __init__(self, *args, **kwargs):
        ...

    def Color(self, toolVector, flags):
        """(integer,vector rgba) = Color(object toolVector,integer flags)"""
        ...

    def Flags(self, toolVector):
        """integer = Flags(object toolVector)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PaintNozzlePacket(object):
    def __init__(self, *args, **kwargs):
        ...

    def Jitter(self, toolVector, brushSize):
        """(integer,integer xj,integer yj) = Jitter(object toolVector,float brushSize)"""
        ...

    def Nozzle(self, toolVector):
        """(integer,float strength,float size,float rotation) = Nozzle(object toolVector)"""
        ...

    def Paint(self, toolVector, brushSize):
        """integer = Paint(object toolVector,float brushSize)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ParticleCoOperator(object):
    def __init__(self, *args, **kwargs):
        ...

    def Cleanup(self):
        """Cleanup()"""
        ...

    def Initialize(self, eval):
        """Initialize(object eval)"""
        ...

    def Particle(self):
        """Particle()"""
        ...

    def Step(self, dT):
        """Step(float dT)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ParticleEvalFrame(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddParticle(self, state):
        """integer index = AddParticle(float[] state)"""
        ...

    def AliveCount(self):
        """integer = AliveCount()"""
        ...

    def GetVector(self, index):
        """float vector = GetVector(integer index)"""
        ...

    def IsAlive(self, index):
        """integer = IsAlive(integer index)"""
        ...

    def KillParticle(self, index):
        """KillParticle(integer index)"""
        ...

    def MaxCount(self):
        """integer = MaxCount()"""
        ...

    def Neighbors(self, maxDist, maxCount):
        """(vector pos,integer index,float dist,integer count) = Neighbors(float maxDist,integer maxCount)"""
        ...

    def SetVector(self, index, vector):
        """SetVector(integer index,float[] vector)"""
        ...

    def VertexDescription(self):
        """object = VertexDescription()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ParticleFilter(object):
    def __init__(self, *args, **kwargs):
        ...

    def Cleanup(self):
        """Cleanup()"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def Frame(self, stage):
        """Frame(integer stage)"""
        ...

    def Initialize(self, vertex, frame, time):
        """Initialize(object vertex,object frame,float time)"""
        ...

    def Particle(self, stage, vertex):
        """Particle(integer stage,float[] vertex)"""
        ...

    def Step(self, other, dt):
        """Step(object other,float dt)"""
        ...

    def Vertex(self, full):
        """object = Vertex(object full)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ParticleGeneratorPacket(object):
    def __init__(self, *args, **kwargs):
        ...

    def Count(self, vts):
        """integer = Count(object vts)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ParticleItem(object):
    def __init__(self, *args, **kwargs):
        ...

    def Evaluate(self, attr, index):
        """Unknown object = Evaluate(object attr,integer index)"""
        ...

    def Prepare(self, eval):
        """integer index = Prepare(object eval)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PathGeneratorPacket(object):
    def __init__(self, *args, **kwargs):
        ...

    def Bank(self, vts, t):
        """float = Bank(object vts,float t)"""
        ...

    def Count(self, vts):
        """integer = Count(object vts)"""
        ...

    def Current(self, vts):
        """integer = Current(object vts)"""
        ...

    def KnotDataSet(self, gen):
        """KnotDataSet(object gen)"""
        ...

    def Length(self, vts, t0, t1):
        """float = Length(object vts,float t0,float t1)"""
        ...

    def Tangent(self, vts, t):
        """float tan = Tangent(object vts,float t)"""
        ...

    def Value(self, vts, t):
        """vector pos = Value(object vts,float t)"""
        ...

    def Walk(self, vts, pathStep, angle, ti, tf):
        """integer = Walk(object vts,object pathStep,float angle,float ti,float tf)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PathStep(object):
    def __init__(self, *args, **kwargs):
        ...

    def CleanUp(self):
        """CleanUp()"""
        ...

    def Setup(self):
        """Setup()"""
        ...

    def Step(self, t):
        """(integer,vector pos) = Step(float t)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Pattern(object):
    def __init__(self, *args, **kwargs):
        ...

    def GenerateSequenceString(self, start, end):
        """string = GenerateSequenceString(integer start,integer end)"""
        ...

    def Test(self, index, offset):
        """boolean = Test(integer index,integer offset)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PersistenceClient(object):
    def __init__(self, *args, **kwargs):
        ...

    def Setup(self):
        """Setup()"""
        ...

    def SyncRead(self):
        """SyncRead()"""
        ...

    def SyncWrite(self):
        """SyncWrite()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PersistentEntry(object):
    def __init__(self, *args, **kwargs):
        ...

    def Append(self):
        """Append()"""
        ...

    def Clear(self):
        """Clear()"""
        ...

    def Count(self):
        """integer count = Count()"""
        ...

    def Delete(self):
        """Delete()"""
        ...

    def Hash(self):
        """string key = Hash()"""
        ...

    def Insert(self, key):
        """Insert(string key)"""
        ...

    def Lookup(self, key):
        """Lookup(string key)"""
        ...

    def Select(self, index):
        """Select(integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PivotPacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Item(self, packet):
        """Item object = Item(pointer packet)"""
        ...

    def Packet(self, item, type):
        """pointer = Packet(object item,integer type)"""
        ...

    def Type(self, packet):
        """integer = Type(pointer packet)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Point(object):
    def __init__(self, *args, **kwargs):
        ...

    def ClearMapValue(self, map):
        """ClearMapValue(id map)"""
        ...

    def Copy(self):
        """id pointID = Copy()"""
        ...

    def Corner(self):
        """vector pos = Corner()"""
        ...

    def EdgeByIndex(self, index):
        """id edgeID = EdgeByIndex(integer index)"""
        ...

    def EdgeCount(self):
        """integer count = EdgeCount()"""
        ...

    def Enumerate(self, mode, visitor, monitor):
        """Enumerate(integer mode,object visitor,object monitor)"""
        ...

    def ID(self):
        """id = ID()"""
        ...

    def Index(self):
        """integer index = Index()"""
        ...

    def MapEvaluate(self, map, value):
        """boolean = MapEvaluate(id map,float[] value)"""
        ...

    def MapValue(self, map, value):
        """boolean = MapValue(id map,float[] value)"""
        ...

    def Mesh(self):
        """Unknown object = Mesh()"""
        ...

    def New(self, pos):
        """id pointID = New(vector pos)"""
        ...

    def NewOnEdge(self, A, B, percent):
        """id newPoint = NewOnEdge(id A,id B,float percent)"""
        ...

    def Normal(self, pol):
        """vector normal = Normal(id pol)"""
        ...

    def OnSymmetryCenter(self):
        """OnSymmetryCenter()"""
        ...

    def Part(self):
        """integer part = Part()"""
        ...

    def PointByIndex(self, index):
        """id pointID = PointByIndex(integer index)"""
        ...

    def PointCount(self):
        """integer count = PointCount()"""
        ...

    def PolygonByIndex(self, index):
        """id polygonID = PolygonByIndex(integer index)"""
        ...

    def PolygonCount(self):
        """integer count = PolygonCount()"""
        ...

    def Pos(self):
        """vector pos = Pos()"""
        ...

    def Remove(self):
        """Remove()"""
        ...

    def Select(self, point):
        """Select(id point)"""
        ...

    def SelectByIndex(self, index):
        """SelectByIndex(integer index)"""
        ...

    def SelectPolygonVertex(self, polygon, index):
        """SelectPolygonVertex(id polygon,integer index)"""
        ...

    def SetMapValue(self, map, value):
        """SetMapValue(id map,float[] value)"""
        ...

    def SetMarks(self, set):
        """SetMarks(integer set)"""
        ...

    def SetPos(self, pos):
        """SetPos(vector pos)"""
        ...

    def Spawn(self):
        """Point object = Spawn()"""
        ...

    def Symmetry(self):
        """id pointID = Symmetry()"""
        ...

    def TestMarks(self, mode):
        """boolean = TestMarks(integer mode)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PointCacheItem(object):
    def __init__(self, *args, **kwargs):
        ...

    def Cleanup(self):
        """Cleanup()"""
        ...

    def Initialize(self, vdesc, attr, index, time, sample):
        """Initialize(object vdesc,object attr,integer index,float time,float sample)"""
        ...

    def Prepare(self, eval):
        """integer index = Prepare(object eval)"""
        ...

    def SaveFrame(self, pobj, time):
        """SaveFrame(object pobj,float time)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Polygon(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddContourEdge(self, startPt, endPt):
        """AddContourEdge(id startPt,id endPt)"""
        ...

    def Area(self):
        """float area = Area()"""
        ...

    def ClearMapValue(self, point, map):
        """ClearMapValue(id point,id map)"""
        ...

    def ClearTriangles(self):
        """ClearTriangles()"""
        ...

    def Closest(self, maxDist, pos):
        """(boolean,vector hitPos,vector hitNorm,float hitDist) = Closest(float maxDist,vector pos)"""
        ...

    def EdgeIndex(self, edgeID):
        """integer index = EdgeIndex(id edgeID)"""
        ...

    def Enumerate(self, mode, visitor, monitor):
        """Enumerate(integer mode,object visitor,object monitor)"""
        ...

    def EnumerateBBox(self, mode, visitor, min, max):
        """EnumerateBBox(integer mode,object visitor,vector min,vector max)"""
        ...

    def EnumerateBin(self, mode, visitor, bin):
        """EnumerateBin(integer mode,object visitor,object bin)"""
        ...

    def EnumerateByPTag(self, mode, type, tag, visitor):
        """EnumerateByPTag(integer mode,integer type,string tag,object visitor)"""
        ...

    def EnumerateByUV(self, mode, vMapName, quality, uv, visitor):
        """EnumerateByUV(integer mode,string vMapName,integer quality,vector uv,object visitor)"""
        ...

    def EnumerateLine(self, mode, visitor, org, dir):
        """EnumerateLine(integer mode,object visitor,vector org,vector dir)"""
        ...

    def EnumerateRay(self, mode, visitor, org, ray):
        """EnumerateRay(integer mode,object visitor,vector org,vector ray)"""
        ...

    def FirstIsControlEndpoint(self):
        """boolean = FirstIsControlEndpoint()"""
        ...

    def GenerateContour(self, type):
        """id polygonID = GenerateContour(integer type)"""
        ...

    def GenerateContourProto(self):
        """id polygonID = GenerateContourProto()"""
        ...

    def GenerateTriangles(self):
        """integer count = GenerateTriangles()"""
        ...

    def GoodPoint(self, points, nPoints):
        """integer index = GoodPoint(id[] points,integer nPoints)"""
        ...

    def ID(self):
        """id = ID()"""
        ...

    def Index(self):
        """integer index = Index()"""
        ...

    def IntersectRay(self, pos, dir):
        """(boolean,vector hitNorm,float hitDist) = IntersectRay(vector pos,vector dir)"""
        ...

    def IsBorder(self):
        """boolean = IsBorder()"""
        ...

    def LastIsControlEndpoint(self):
        """boolean = LastIsControlEndpoint()"""
        ...

    def MapEvaluate(self, map, point, value):
        """boolean = MapEvaluate(id map,id point,float[] value)"""
        ...

    def MapValue(self, map, point, value):
        """boolean = MapValue(id map,id point,float[] value)"""
        ...

    def Mesh(self):
        """Unknown object = Mesh()"""
        ...

    def New(self, type, vertices, numVert, rev):
        """id polygonID = New(integer type,id[] vertices,integer numVert,integer rev)"""
        ...

    def NewCurveFill(self, polygons, numPols):
        """id polygonID = NewCurveFill(id[] polygons,integer numPols)"""
        ...

    def NewProto(self, type, vertices, numVert, rev):
        """id polygonID = NewProto(integer type,id[] vertices,integer numVert,integer rev)"""
        ...

    def Normal(self):
        """vector normal = Normal()"""
        ...

    def Part(self):
        """integer part = Part()"""
        ...

    def PointIndex(self, pointID):
        """integer index = PointIndex(id pointID)"""
        ...

    def Remove(self):
        """Remove()"""
        ...

    def RepresentativePosition(self):
        """vector pos = RepresentativePosition()"""
        ...

    def Select(self, polygon):
        """Select(id polygon)"""
        ...

    def SelectByIndex(self, index):
        """SelectByIndex(integer index)"""
        ...

    def SetFirstIsControlEndpoint(self, state):
        """SetFirstIsControlEndpoint(integer state)"""
        ...

    def SetLastIsControlEndpoint(self, state):
        """SetLastIsControlEndpoint(integer state)"""
        ...

    def SetMapValue(self, point, map, value):
        """SetMapValue(id point,id map,float[] value)"""
        ...

    def SetMarks(self, set):
        """SetMarks(integer set)"""
        ...

    def SetVertexList(self, vertices, numVert, rev):
        """SetVertexList(id[] vertices,integer numVert,integer rev)"""
        ...

    def SharedEdge(self, polygonID):
        """id edgeID = SharedEdge(id polygonID)"""
        ...

    def Spawn(self):
        """Polygon object = Spawn()"""
        ...

    def StartContour(self):
        """StartContour()"""
        ...

    def Symmetry(self):
        """id polygonID = Symmetry()"""
        ...

    def TestMarks(self, mode):
        """boolean = TestMarks(integer mode)"""
        ...

    def TriangleByIndex(self, index):
        """(id point0,id point1,id point2) = TriangleByIndex(integer index)"""
        ...

    def Type(self):
        """integer type = Type()"""
        ...

    def UVLookup(self, vMapName, uv):
        """(vector surfacePosition,vector surfaceNormal,vector surfaceDPDU,vector surfaceDPDV) = UVLookup(string vMapName,vector uv)"""
        ...

    def UVPart(self, map):
        """integer part = UVPart(id map)"""
        ...

    def VertexByIndex(self, index):
        """id point = VertexByIndex(integer index)"""
        ...

    def VertexCount(self):
        """integer count = VertexCount()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PolygonPacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Item(self, packet):
        """Item object = Item(pointer packet)"""
        ...

    def Mesh(self, packet):
        """Mesh object = Mesh(pointer packet)"""
        ...

    def Packet(self, polygon, mesh):
        """pointer = Packet(id polygon,object mesh)"""
        ...

    def Polygon(self, packet):
        """id polygon = Polygon(pointer packet)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PolygonSlice(object):
    def __init__(self, *args, **kwargs):
        ...

    def ByLine(self, pos0, pos1):
        """ByLine(vector pos0,vector pos1)"""
        ...

    def Done(self):
        """integer = Done()"""
        ...

    def SetAxis(self, axis):
        """SetAxis(integer axis)"""
        ...

    def SetAxisByVector(self, axis):
        """SetAxisByVector(vector axis)"""
        ...

    def Start(self, meshObj, pol, setAxis):
        """Start(object meshObj,id pol,integer setAxis)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PoseItem(object):
    def __init__(self, *args, **kwargs):
        ...

    def Create(self):
        """Create()"""
        ...

    def GetFloat(self, item, channelIndex):
        """float value = GetFloat(object item,integer channelIndex)"""
        ...

    def GetInt(self, item, channelIndex):
        """integer value = GetInt(object item,integer channelIndex)"""
        ...

    def SetFloat(self, item, channelIndex, value):
        """SetFloat(object item,integer channelIndex,float value)"""
        ...

    def SetInt(self, item, channelIndex, value):
        """SetInt(object item,integer channelIndex,integer value)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PresetBrowserSource(object):
    def __init__(self, *args, **kwargs):
        ...

    def ViewportHash(self):
        """string = ViewportHash()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PresetDo(object):
    def __init__(self, *args, **kwargs):
        ...

    def Do(self, path):
        """Do(string path)"""
        ...

    def Test(self, path):
        """Test(string path)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PresetLoaderTarget(object):
    def __init__(self, *args, **kwargs):
        ...

    def CategoryByIndex(self, index):
        """string category = CategoryByIndex(integer index)"""
        ...

    def CategoryCount(self):
        """integer count = CategoryCount()"""
        ...

    def ServerName(self):
        """string = ServerName()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PresetMetrics(object):
    def __init__(self, *args, **kwargs):
        ...

    def Flags(self):
        """integer flags = Flags()"""
        ...

    def Markup(self):
        """Attributes object = Markup()"""
        ...

    def Metadata(self):
        """Attributes object = Metadata()"""
        ...

    def ThumbnailIdealSize(self):
        """(integer idealW,integer idealH) = ThumbnailIdealSize()"""
        ...

    def ThumbnailImage(self):
        """Image object = ThumbnailImage()"""
        ...

    def ThumbnailResource(self):
        """string resourceName = ThumbnailResource()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PresetPathPacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Identifier(self, packet):
        """string identifier = Identifier(pointer packet)"""
        ...

    def Packet(self, path, identifier):
        """pointer = Packet(string path,string identifier)"""
        ...

    def Path(self, packet):
        """string path = Path(pointer packet)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PresetType(object):
    def __init__(self, *args, **kwargs):
        ...

    def Apply(self, path, destination):
        """Apply(string path,object destination)"""
        ...

    def BaseAspect(self):
        """float aspect = BaseAspect()"""
        ...

    def DefaultThumbnail(self, path):
        """DefaultThumbnail(string path)"""
        ...

    def Do(self, path):
        """Do(string path)"""
        ...

    def DoCommandFlags(self, path):
        """integer flags = DoCommandFlags(string path)"""
        ...

    def GenericThumbnailResource(self, path):
        """string resourceName = GenericThumbnailResource(string path)"""
        ...

    def Metrics(self, path, flags, w, h, prevMetrics):
        """PresetMetrics object = Metrics(string path,integer flags,integer w,integer h,object prevMetrics)"""
        ...

    def Recognize(self, path):
        """string category = Recognize(string path)"""
        ...

    def StoreMarkup(self, path, attr):
        """StoreMarkup(string path,object attr)"""
        ...

    def StoreThumbnail(self, path, image):
        """StoreThumbnail(string path,object image)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Preview(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetBuffer(self):
        """Image object = GetBuffer()"""
        ...

    def GetCurrentTime(self):
        """float = GetCurrentTime()"""
        ...

    def GetResHeight(self):
        """integer = GetResHeight()"""
        ...

    def GetResWidth(self):
        """integer = GetResWidth()"""
        ...

    def IsComplete(self):
        """boolean = IsComplete()"""
        ...

    def Pause(self):
        """Pause()"""
        ...

    def Reset(self):
        """Reset()"""
        ...

    def SetAlpha(self, enable):
        """SetAlpha(integer enable)"""
        ...

    def SetCameraOverrideApertureX(self, apertureX):
        """SetCameraOverrideApertureX(float apertureX)"""
        ...

    def SetCameraOverrideApertureY(self, apertureY):
        """SetCameraOverrideApertureY(float apertureY)"""
        ...

    def SetCameraOverrideFocalLength(self, focalLength):
        """SetCameraOverrideFocalLength(float focalLength)"""
        ...

    def SetCameraOverrideProjectionType(self, projectionType):
        """SetCameraOverrideProjectionType(integer projectionType)"""
        ...

    def SetCameraOverrideTransform(self, transform):
        """SetCameraOverrideTransform(matrix transform)"""
        ...

    def SetMotionBlur(self, enable):
        """SetMotionBlur(integer enable)"""
        ...

    def SetNotifier(self, notifier):
        """SetNotifier(object notifier)"""
        ...

    def SetQuality(self, quality, samples):
        """SetQuality(integer quality,integer samples)"""
        ...

    def SetRenderAllOutputs(self, enable):
        """SetRenderAllOutputs(integer enable)"""
        ...

    def SetRenderTime(self, time):
        """SetRenderTime(float time)"""
        ...

    def SetRes(self, width, height):
        """SetRes(integer width,integer height)"""
        ...

    def SetStereo(self, enable, eye):
        """SetStereo(integer enable,integer eye)"""
        ...

    def SetUseAllThreads(self, enable):
        """SetUseAllThreads(integer enable)"""
        ...

    def Start(self):
        """Start()"""
        ...

    def Stop(self):
        """Stop()"""
        ...

    def UseCameraOverride(self, useCameraOverride):
        """UseCameraOverride(integer useCameraOverride)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class PreviewNotifier(object):
    def __init__(self, *args, **kwargs):
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Profile1DPreDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Box(self):
        """bounds box = Box()"""
        ...

    def Count(self):
        """integer = Count()"""
        ...

    def CurveTo(self, x0, y0, x1, y1, x2, y2):
        """CurveTo(float x0,float y0,float x1,float y1,float x2,float y2)"""
        ...

    def Evaluate(self, t, flags, axis):
        """float = Evaluate(float t,integer flags,integer axis)"""
        ...

    def LineTo(self, x, y):
        """LineTo(float x,float y)"""
        ...

    def MoveTo(self, x, y):
        """MoveTo(float x,float y)"""
        ...

    def PathSteps(self, tol, flags, x, y, nstep):
        """integer = PathSteps(float tol,integer flags,double[] x,double[] y,integer nstep)"""
        ...

    def SelectByIndex(self, index):
        """SelectByIndex(integer index)"""
        ...

    def SelectByParameter(self, t):
        """SelectByParameter(float t)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Profile2DPreDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Box(self):
        """bounds box = Box()"""
        ...

    def Closed(self, closed):
        """Closed(integer closed)"""
        ...

    def Count(self):
        """integer = Count()"""
        ...

    def CurveTo(self, x0, y0, x1, y1, x2, y2):
        """CurveTo(float x0,float y0,float x1,float y1,float x2,float y2)"""
        ...

    def LineTo(self, x, y):
        """LineTo(float x,float y)"""
        ...

    def MoveTo(self, x, y):
        """MoveTo(float x,float y)"""
        ...

    def NewPath(self):
        """NewPath()"""
        ...

    def SelectByIndex(self, index):
        """SelectByIndex(integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ProjDirOverride(object):
    def __init__(self, *args, **kwargs):
        ...

    def OverrideWith(self, originalPath):
        """string = OverrideWith(string originalPath)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ProxyOptions(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddItem(self, type, internal_name, user_name):
        """AddItem(integer type,string internal_name,string user_name)"""
        ...

    def LoadList(self):
        """LoadList()"""
        ...

    def LoadNone(self):
        """LoadNone()"""
        ...

    def SetFlags(self, flags):
        """SetFlags(integer flags)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Quaternion(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetAngleAxis(self):
        """(float ang,vector axis) = GetAngleAxis()"""
        ...

    def GetMatrix(self):
        """matrix mat3 = GetMatrix()"""
        ...

    def GetQuaternion(self):
        """quaternion q = GetQuaternion()"""
        ...

    def SetAngleAxis(self, ang, axis):
        """SetAngleAxis(float ang,vector axis)"""
        ...

    def SetMatrix(self, mat3):
        """SetMatrix(matrix mat3)"""
        ...

    def SetQuaternion(self, q):
        """SetQuaternion(quaternion q)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Raycast(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetSurfaceType(self, vector):
        """integer = GetSurfaceType(object vector)"""
        ...

    def InternalShade(self, vector):
        """InternalShade(object vector)"""
        ...

    def RayPop(self, vector):
        """RayPop(object vector)"""
        ...

    def Raycast(self, vector, pos, dir):
        """float = Raycast(object vector,vector pos,vector dir)"""
        ...

    def Raytrace(self, vector, pos, dir, flags):
        """float = Raytrace(object vector,vector pos,vector dir,integer flags)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class RaycastPacket(object):
    def __init__(self, *args, **kwargs):
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Raymarch(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetOpacity(self, vector, dist):
        """float opa = GetOpacity(object vector,float dist)"""
        ...

    def Jitter1D(self, vector):
        """float offset = Jitter1D(object vector)"""
        ...

    def ShaderEvaluate(self, vector, shader):
        """ShaderEvaluate(object vector,object shader)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class RenderBucket(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetGIBounce(self):
        """integer = GetGIBounce()"""
        ...

    def GetPixel(self):
        """(integer x,integer y) = GetPixel()"""
        ...

    def GetSubPixel(self):
        """(float x,float y) = GetSubPixel()"""
        ...

    def GetTimeOffset(self):
        """float = GetTimeOffset()"""
        ...

    def PopRay(self):
        """PopRay()"""
        ...

    def PushRay(self):
        """PushRay()"""
        ...

    def SampleVec(self):
        """Unknown object = SampleVec()"""
        ...

    def Thread(self):
        """integer = Thread()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class RenderCache(object):
    def __init__(self, *args, **kwargs):
        ...

    def Clear(self):
        """Clear()"""
        ...

    def GeoSurfaceCount(self):
        """integer count = GeoSurfaceCount()"""
        ...

    def Time(self):
        """(float time,float timeOffsets) = Time()"""
        ...

    def Update(self, time, force):
        """Update(float time,integer force)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class RenderJob(object):
    def __init__(self, *args, **kwargs):
        ...

    def ActionName(self):
        """string action = ActionName()"""
        ...

    def FrameBufferRegionBackgroundSlot(self):
        """(integer slotIndex,integer ...Index) = FrameBufferRegionBackgroundSlot()"""
        ...

    def FrameBufferSlot(self):
        """integer index = FrameBufferSlot()"""
        ...

    def GroupName(self):
        """string group = GroupName()"""
        ...

    def Options(self):
        """integer options = Options()"""
        ...

    def OutputFilename(self):
        """string filename = OutputFilename()"""
        ...

    def OutputFormat(self):
        """string format = OutputFormat()"""
        ...

    def ProgressAborted(self):
        """ProgressAborted()"""
        ...

    def ProgressBegin(self, renderStats):
        """ProgressBegin(object renderStats)"""
        ...

    def ProgressBucketBegin(self, row, col):
        """ProgressBucketBegin(integer row,integer col)"""
        ...

    def ProgressBucketEnd(self, row, col, code):
        """ProgressBucketEnd(integer row,integer col,integer code)"""
        ...

    def ProgressEnd(self, finalFrameBuffer, finalStats):
        """ProgressEnd(object finalFrameBuffer,object finalStats)"""
        ...

    def ProgressFrameBegin(self, frame, w, h):
        """ProgressFrameBegin(integer frame,integer w,integer h)"""
        ...

    def ProgressFrameEnd(self, frame, stats):
        """ProgressFrameEnd(integer frame,object stats)"""
        ...

    def ProgressFramePassBegin(self, frame, renderPass, eye, ..._int):
        """ProgressFramePassBegin(integer frame,integer renderPass,integer eye,integer ..._int)"""
        ...

    def ProgressFramePassEnd(self, frame, renderPass, eye, ..._int):
        """ProgressFramePassEnd(integer frame,integer renderPass,integer eye,integer ..._int)"""
        ...

    def ProgressImage(self, img):
        """ProgressImage(object img)"""
        ...

    def ProgressImageMetrics(self, resX, resH):
        """(integer w,integer h,float zoom,integer panX,integer panY,integer output) = ProgressImageMetrics(integer resX,integer resH)"""
        ...

    def ProgressImageUpdated(self):
        """ProgressImageUpdated()"""
        ...

    def ProgressPercentDone(self, progressScene, progressFrame, progressRenderPass):
        """ProgressPercentDone(float progressScene,float progressFrame,float progressRenderPass)"""
        ...

    def ProgressRenderPassBegin(self, frameIndex, renderPassIndex, renderPassName, eye):
        """ProgressRenderPassBegin(integer frameIndex,integer renderPassIndex,string renderPassName,integer eye)"""
        ...

    def ProgressRenderPassEnd(self, frame, renderPassIndex, renderPassName, eye, frameBuffer, stats):
        """ProgressRenderPassEnd(integer frame,integer renderPassIndex,string renderPassName,integer eye,object frameBuffer,object stats)"""
        ...

    def ProgressString(self, infoString, userString):
        """ProgressString(string infoString,string userString)"""
        ...

    def ProgressTickle(self):
        """ProgressTickle()"""
        ...

    def RenderAs(self):
        """integer mode = RenderAs()"""
        ...

    def RenderAtTime(self):
        """float time = RenderAtTime()"""
        ...

    def RenderBakeCageVMap(self):
        """string vmap = RenderBakeCageVMap()"""
        ...

    def RenderBakeEffect(self):
        """string effect = RenderBakeEffect()"""
        ...

    def RenderBakeFromRGBA(self):
        """integer mode = RenderBakeFromRGBA()"""
        ...

    def RenderBakeImage(self):
        """Image object = RenderBakeImage()"""
        ...

    def RenderBakeLookDistance(self):
        """float distance = RenderBakeLookDistance()"""
        ...

    def RenderBakeToRGBA(self):
        """integer mode = RenderBakeToRGBA()"""
        ...

    def RenderBakeVMap(self):
        """string vmap = RenderBakeVMap()"""
        ...

    def RenderItem(self):
        """Item object = RenderItem()"""
        ...

    def RenderTurntableFPS(self):
        """integer fps = RenderTurntableFPS()"""
        ...

    def RenderTurntableNumFrames(self):
        """integer numFrames = RenderTurntableNumFrames()"""
        ...

    def TestItem(self, item, eval):
        """TestItem(object item,object eval)"""
        ...

    def UDIM(self):
        """integer udim = UDIM()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class RenderProgressListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def Begin(self):
        """Begin()"""
        ...

    def End(self, stats):
        """End(object stats)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class RenderStats(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetFrameStats(self, frameIndex):
        """Unknown object = GetFrameStats(integer frameIndex)"""
        ...

    def GetPassStats(self, frameIndex, ...Index):
        """Unknown object = GetPassStats(integer frameIndex,integer ...Index)"""
        ...

    def GetSceneStats(self):
        """Unknown object = GetSceneStats()"""
        ...

    def NumFrames(self):
        """integer count = NumFrames()"""
        ...

    def NumPasses(self, frameIndex):
        """integer count = NumPasses(integer frameIndex)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ReplicatorEnumerator(object):
    def __init__(self, *args, **kwargs):
        ...

    def Dissolve(self):
        """float = Dissolve()"""
        ...

    def Enumerate(self, visitor, chan, localXform):
        """Enumerate(object visitor,object chan,integer localXform)"""
        ...

    def Geometry(self):
        """Unknown object = Geometry()"""
        ...

    def GroupId(self):
        """float = GroupId()"""
        ...

    def Id(self):
        """float = Id()"""
        ...

    def Item(self):
        """Item object = Item()"""
        ...

    def Orientation(self):
        """matrix mx = Orientation()"""
        ...

    def Position(self):
        """vector pos = Position()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Saver(object):
    def __init__(self, *args, **kwargs):
        ...

    def Save(self, source, filename, monitor):
        """Save(object source,string filename,object monitor)"""
        ...

    def Verify(self, source, message):
        """Verify(object source,object message)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Scene(object):
    def __init__(self, *args, **kwargs):
        ...

    def AllocAssets(self):
        """SceneAssets object = AllocAssets()"""
        ...

    def AnyItemOfType(self, type):
        """Item object = AnyItemOfType(integer type)"""
        ...

    def BatchCopyAbort(self):
        """BatchCopyAbort()"""
        ...

    def BatchCopyBegin(self, destination):
        """BatchCopyBegin(object destination)"""
        ...

    def BatchCopyEnd(self):
        """BatchCopyEnd()"""
        ...

    def BatchCreateAbort(self):
        """BatchCreateAbort()"""
        ...

    def BatchCreateBegin(self):
        """BatchCreateBegin()"""
        ...

    def BatchCreateEnd(self):
        """BatchCreateEnd()"""
        ...

    def Changed(self, changed):
        """Changed(integer changed)"""
        ...

    def Channels(self, name, time):
        """ChannelRead object = Channels(string name,float time)"""
        ...

    def CustomLoad(self, visitor):
        """CustomLoad(object visitor)"""
        ...

    def DeleteCollection(self, collection, closeMode):
        """DeleteCollection(object collection,integer closeMode)"""
        ...

    def EvalModInvalidate(self, modName):
        """EvalModInvalidate(string modName)"""
        ...

    def EvalModReset(self, modName):
        """EvalModReset(string modName)"""
        ...

    def FileFormat(self):
        """string format = FileFormat()"""
        ...

    def Filename(self):
        """string filename = Filename()"""
        ...

    def FriendlyFilename(self, flags):
        """string filename = FriendlyFilename(integer flags)"""
        ...

    def GeneralCollection(self, typeName, arg, rootItem):
        """Unknown object = GeneralCollection(string typeName,string arg,object rootItem)"""
        ...

    def GeneralCollectionRaw(self, typeName, arg, rootItem):
        """Unknown object = GeneralCollectionRaw(string typeName,string arg,object rootItem)"""
        ...

    def GraphByIndex(self, index):
        """SceneGraph object = GraphByIndex(integer index)"""
        ...

    def GraphCount(self):
        """integer count = GraphCount()"""
        ...

    def GraphLookup(self, name):
        """SceneGraph object = GraphLookup(string name)"""
        ...

    def HasChanged(self):
        """integer numChanges = HasChanged()"""
        ...

    def Import(self, path, monitor):
        """Import(string path,object monitor)"""
        ...

    def ItemAdd(self, type):
        """Item object = ItemAdd(integer type)"""
        ...

    def ItemAddReference(self, item):
        """Item object = ItemAddReference(object item)"""
        ...

    def ItemByIndex(self, type, index):
        """Item object = ItemByIndex(integer type,integer index)"""
        ...

    def ItemByIndexByTypes(self, types, index):
        """Item object = ItemByIndexByTypes(int[] types,integer index)"""
        ...

    def ItemCopy(self, item):
        """Item object = ItemCopy(object item)"""
        ...

    def ItemCount(self, type):
        """integer count = ItemCount(integer type)"""
        ...

    def ItemCountByTypes(self, types):
        """integer count = ItemCountByTypes(int[] types)"""
        ...

    def ItemInstance(self, item):
        """Item object = ItemInstance(object item)"""
        ...

    def ItemLocalize(self, item):
        """Item object = ItemLocalize(object item)"""
        ...

    def ItemLookup(self, id):
        """Item object = ItemLookup(string id)"""
        ...

    def ItemLookupIdent(self, id):
        """Item object = ItemLookupIdent(string id)"""
        ...

    def ItemLookupImported(self, id):
        """Item object = ItemLookupImported(string id)"""
        ...

    def ItemRemove(self, item):
        """ItemRemove(object item)"""
        ...

    def ItemReplace(self, item, type):
        """Item object = ItemReplace(object item,integer type)"""
        ...

    def ItemRootType(self):
        """integer = ItemRootType()"""
        ...

    def LoadFlags(self):
        """integer = LoadFlags()"""
        ...

    def Parent(self):
        """Item object = Parent()"""
        ...

    def RenderCameraByIndex(self, index):
        """Item object = RenderCameraByIndex(integer index)"""
        ...

    def RenderCameraCount(self):
        """integer count = RenderCameraCount()"""
        ...

    def RenderCameraIndex(self, eval):
        """integer index = RenderCameraIndex(object eval)"""
        ...

    def SetupChannels(self):
        """ChannelRead object = SetupChannels()"""
        ...

    def SetupMode(self):
        """boolean = SetupMode()"""
        ...

    def SubSceneByIndex(self, type, index):
        """Scene object = SubSceneByIndex(integer type,integer index)"""
        ...

    def SubSceneCount(self, type):
        """integer count = SubSceneCount(integer type)"""
        ...

    def TextureCopy(self, item):
        """Item object = TextureCopy(object item)"""
        ...

    def WorkPlanePosition(self, chanRead):
        """vector pos = WorkPlanePosition(object chanRead)"""
        ...

    def WorkPlaneRotation(self, chanRead):
        """matrix m3 = WorkPlaneRotation(object chanRead)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SceneAssets(object):
    def __init__(self, *args, **kwargs):
        ...

    def Category(self, index):
        """string category = Category(integer index)"""
        ...

    def Count(self):
        """integer count = Count()"""
        ...

    def FileType(self, index):
        """string type = FileType(integer index)"""
        ...

    def GetPath(self, item, ident):
        """string = GetPath(object item,string ident)"""
        ...

    def Ident(self, index):
        """string ident = Ident(integer index)"""
        ...

    def IsSequence(self, index):
        """boolean = IsSequence(integer index)"""
        ...

    def Item(self, index):
        """Item object = Item(integer index)"""
        ...

    def SetPath(self, item, ident, newPath):
        """SetPath(object item,string ident,string newPath)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SceneContents(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddLink(self, type, internal_name, user_name):
        """AddLink(integer type,string internal_name,string user_name)"""
        ...

    def BBox(self, index):
        """bounds box = BBox(integer index)"""
        ...

    def ByInternalName(self, internal_name):
        """integer index = ByInternalName(string internal_name)"""
        ...

    def ByUserName(self, user_name):
        """integer index = ByUserName(string user_name)"""
        ...

    def Count(self):
        """integer = Count()"""
        ...

    def InternalName(self, index):
        """string = InternalName(integer index)"""
        ...

    def Item(self, type, internal_name, user_name):
        """Item(integer type,string internal_name,string user_name)"""
        ...

    def LinkCount(self, index):
        """integer = LinkCount(integer index)"""
        ...

    def Reset(self):
        """Reset()"""
        ...

    def SetBBox(self, min_X, min_Y, min_Z, max_X, max_Y, max_Z):
        """SetBBox(float min_X,float min_Y,float min_Z,float max_X,float max_Y,float max_Z)"""
        ...

    def Type(self, index):
        """integer type = Type(integer index)"""
        ...

    def UserName(self, index):
        """string = UserName(integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SceneEvalListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def ChannelPostValue(self):
        """ChannelPostValue()"""
        ...

    def ChannelPreValue(self):
        """ChannelPreValue()"""
        ...

    def ChannelValue(self, item, index):
        """ChannelValue(object item,integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SceneGraph(object):
    def __init__(self, *args, **kwargs):
        ...

    def Context(self):
        """Scene object = Context()"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def RootByIndex(self, index):
        """Item object = RootByIndex(integer index)"""
        ...

    def RootCount(self):
        """integer count = RootCount()"""
        ...

    def RootFirst(self):
        """Item object = RootFirst()"""
        ...

    def RootNext(self):
        """Item object = RootNext()"""
        ...

    def RootRemove(self, item):
        """RootRemove(object item)"""
        ...

    def RootSetPos(self, item, pos):
        """RootSetPos(object item,integer pos)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SceneItemListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def ChanLinkAdd(self, graph, itemFrom, chanFrom, itemTo, chanTo):
        """ChanLinkAdd(string graph,object itemFrom,integer chanFrom,object itemTo,integer chanTo)"""
        ...

    def ChanLinkRemAfter(self, graph, itemFrom, chanFrom, itemTo, chanTo):
        """ChanLinkRemAfter(string graph,object itemFrom,integer chanFrom,object itemTo,integer chanTo)"""
        ...

    def ChanLinkRemBefore(self, graph, itemFrom, chanFrom, itemTo, chanTo):
        """ChanLinkRemBefore(string graph,object itemFrom,integer chanFrom,object itemTo,integer chanTo)"""
        ...

    def ChanLinkSet(self, graph, itemFrom, chanFrom, itemTo, chanTo):
        """ChanLinkSet(string graph,object itemFrom,integer chanFrom,object itemTo,integer chanTo)"""
        ...

    def ChannelValue(self, action, item, index):
        """ChannelValue(string action,object item,integer index)"""
        ...

    def ItemAdd(self, item):
        """ItemAdd(object item)"""
        ...

    def ItemAddChannel(self, item):
        """ItemAddChannel(object item)"""
        ...

    def ItemChannelDefault(self, item, index):
        """ItemChannelDefault(object item,integer index)"""
        ...

    def ItemChannelMinMax(self, item, index):
        """ItemChannelMinMax(object item,integer index)"""
        ...

    def ItemChannelName(self, item, index):
        """ItemChannelName(object item,integer index)"""
        ...

    def ItemChannelType(self, item, index):
        """ItemChannelType(object item,integer index)"""
        ...

    def ItemChild(self, item):
        """ItemChild(object item)"""
        ...

    def ItemLocal(self, item):
        """ItemLocal(object item)"""
        ...

    def ItemName(self, item):
        """ItemName(object item)"""
        ...

    def ItemPackage(self, item):
        """ItemPackage(object item)"""
        ...

    def ItemParent(self, item):
        """ItemParent(object item)"""
        ...

    def ItemPostDelete(self, scene):
        """ItemPostDelete(object scene)"""
        ...

    def ItemPreChange(self, scene):
        """ItemPreChange(object scene)"""
        ...

    def ItemRemove(self, item):
        """ItemRemove(object item)"""
        ...

    def ItemRemoveChannel(self, item):
        """ItemRemoveChannel(object item)"""
        ...

    def ItemSource(self, item):
        """ItemSource(object item)"""
        ...

    def ItemTag(self, item):
        """ItemTag(object item)"""
        ...

    def LinkAdd(self, graph, itemFrom, itemTo):
        """LinkAdd(string graph,object itemFrom,object itemTo)"""
        ...

    def LinkRemAfter(self, graph, itemFrom, itemTo):
        """LinkRemAfter(string graph,object itemFrom,object itemTo)"""
        ...

    def LinkRemBefore(self, graph, itemFrom, itemTo):
        """LinkRemBefore(string graph,object itemFrom,object itemTo)"""
        ...

    def LinkSet(self, graph, itemFrom, itemTo):
        """LinkSet(string graph,object itemFrom,object itemTo)"""
        ...

    def SceneClear(self, scene):
        """SceneClear(object scene)"""
        ...

    def SceneCreate(self, scene):
        """SceneCreate(object scene)"""
        ...

    def SceneDestroy(self, scene):
        """SceneDestroy(object scene)"""
        ...

    def SceneFilename(self, scene, filename):
        """SceneFilename(object scene,string filename)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SceneItemPreDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def ContainerItem(self):
        """Item object = ContainerItem()"""
        ...

    def Item(self):
        """(integer mode,Item object) = Item()"""
        ...

    def Orientation(self):
        """matrix xfrm = Orientation()"""
        ...

    def Position(self):
        """vector pos = Position()"""
        ...

    def Scene(self):
        """Scene object = Scene()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SceneLoaderTarget(object):
    def __init__(self, *args, **kwargs):
        ...

    def ClearFlags(self, flags):
        """ClearFlags(integer flags)"""
        ...

    def SetFlags(self, flags):
        """SetFlags(integer flags)"""
        ...

    def SetRootType(self, typeName):
        """SetRootType(string typeName)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ScenePacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Packet(self, scene):
        """pointer = Packet(object scene)"""
        ...

    def Scene(self, packet):
        """Scene object = Scene(pointer packet)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SceneSubset(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetCollection(self):
        """ItemCollection object = GetCollection()"""
        ...

    def GetScene(self):
        """Scene object = GetScene()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SchemaDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Channel(self):
        """Unknown object = Channel()"""
        ...

    def Graph(self):
        """Unknown object = Graph()"""
        ...

    def Group(self):
        """Item object = Group()"""
        ...

    def Item(self):
        """Item object = Item()"""
        ...

    def Link(self):
        """Unknown object = Link()"""
        ...

    def Node(self):
        """Item object = Node()"""
        ...

    def Position(self):
        """vector pos = Position()"""
        ...

    def ViewType(self):
        """integer = ViewType()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SchematicConnection(object):
    def __init__(self, *args, **kwargs):
        ...

    def AllowConnect(self, from_obj, to_obj):
        """boolean = AllowConnect(object from_obj,object to_obj)"""
        ...

    def AllowConnectType(self, to_obj, type):
        """boolean = AllowConnectType(object to_obj,integer type)"""
        ...

    def BaseFlags(self):
        """integer = BaseFlags()"""
        ...

    def ByIndex(self, item, index):
        """Item object = ByIndex(object item,integer index)"""
        ...

    def ChannelAllowConnect(self, from_obj, fromIndex, to_obj, toIndex):
        """boolean = ChannelAllowConnect(object from_obj,integer fromIndex,object to_obj,integer toIndex)"""
        ...

    def ChannelByIndex(self, xItem, fromIndex, index):
        """(Item object,integer toIndex) = ChannelByIndex(object xItem,integer fromIndex,integer index)"""
        ...

    def ChannelConnect(self, from_obj, fromIndex, to_obj, toIndex):
        """ChannelConnect(object from_obj,integer fromIndex,object to_obj,integer toIndex)"""
        ...

    def ChannelCount(self, xItem, fromIndex):
        """integer count = ChannelCount(object xItem,integer fromIndex)"""
        ...

    def ChannelDisconnect(self, from_obj, fromIndex, to_obj, toIndex):
        """ChannelDisconnect(object from_obj,integer fromIndex,object to_obj,integer toIndex)"""
        ...

    def ChannelIOType(self):
        """integer ioType = ChannelIOType()"""
        ...

    def Connect(self, from_obj, to_obj, toIndex):
        """Connect(object from_obj,object to_obj,integer toIndex)"""
        ...

    def Count(self, item):
        """integer count = Count(object item)"""
        ...

    def Disconnect(self, from_obj, to_obj):
        """Disconnect(object from_obj,object to_obj)"""
        ...

    def GraphName(self):
        """string name = GraphName()"""
        ...

    def ItemFlags(self, item):
        """integer flags = ItemFlags(object item)"""
        ...

    def ItemFlagsValid(self):
        """integer = ItemFlagsValid()"""
        ...

    def PerItemFlags(self, item):
        """integer flags = PerItemFlags(object item)"""
        ...

    def PresetBrowserHash(self, item):
        """string hash = PresetBrowserHash(object item)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SchematicGroup(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddItem(self, item):
        """SchematicNode object = AddItem(object item)"""
        ...

    def Group(self):
        """Item object = Group()"""
        ...

    def InputNode(self):
        """SchematicNode object = InputNode()"""
        ...

    def IsWorkspace(self):
        """boolean = IsWorkspace()"""
        ...

    def NodeByIndex(self, index):
        """SchematicNode object = NodeByIndex(integer index)"""
        ...

    def NodeCount(self):
        """integer count = NodeCount()"""
        ...

    def OutputNode(self):
        """SchematicNode object = OutputNode()"""
        ...

    def RemoveItem(self, item):
        """RemoveItem(object item)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SchematicNode(object):
    def __init__(self, *args, **kwargs):
        ...

    def AbsoluteSize(self):
        """(float width,float height) = AbsoluteSize()"""
        ...

    def AddChannel(self, index):
        """AddChannel(integer index)"""
        ...

    def ChannelByIndex(self, index, type):
        """SchematicNodeChannel object = ChannelByIndex(integer index,integer type)"""
        ...

    def ChannelCount(self):
        """integer count = ChannelCount()"""
        ...

    def ConnectionByIndex(self, index, type):
        """SchematicNodeConnection object = ConnectionByIndex(integer index,integer type)"""
        ...

    def ConnectionCount(self):
        """integer count = ConnectionCount()"""
        ...

    def Expanded(self):
        """boolean = Expanded()"""
        ...

    def Group(self):
        """Item object = Group()"""
        ...

    def IsRoot(self):
        """boolean = IsRoot()"""
        ...

    def Item(self):
        """Item object = Item()"""
        ...

    def Position(self):
        """(float x,float y) = Position()"""
        ...

    def RemoveChannel(self, index):
        """RemoveChannel(integer index)"""
        ...

    def RootNode(self):
        """SchematicNode object = RootNode()"""
        ...

    def SetPosition(self, x, y):
        """SetPosition(float x,float y)"""
        ...

    def Size(self):
        """(float width,float height) = Size()"""
        ...

    def SubNodeByIndex(self, index):
        """SchematicNode object = SubNodeByIndex(integer index)"""
        ...

    def SubNodeCount(self):
        """integer count = SubNodeCount()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SchematicNodeChannel(object):
    def __init__(self, *args, **kwargs):
        ...

    def ByIndex(self, index):
        """SchematicNodeChannel object = ByIndex(integer index)"""
        ...

    def Count(self):
        """integer count = Count()"""
        ...

    def Flags(self):
        """integer flags = Flags()"""
        ...

    def Index(self):
        """integer index = Index()"""
        ...

    def Node(self):
        """SchematicNode object = Node()"""
        ...

    def Position(self):
        """(float x,float y) = Position()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SchematicNodeConnection(object):
    def __init__(self, *args, **kwargs):
        ...

    def ByIndex(self, index):
        """SchematicNodeConnection object = ByIndex(integer index)"""
        ...

    def Count(self):
        """integer count = Count()"""
        ...

    def Flags(self):
        """integer flags = Flags()"""
        ...

    def Node(self):
        """SchematicNode object = Node()"""
        ...

    def Position(self, index):
        """(float x,float y) = Position(integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Script(object):
    def __init__(self, *args, **kwargs):
        ...

    def Desc(self):
        """string desc = Desc()"""
        ...

    def GetBuffer(self):
        """(string buffer,integer bufferLength) = GetBuffer()"""
        ...

    def Hash(self):
        """string hash = Hash()"""
        ...

    def HelpKey(self, args):
        """string key = HelpKey(string args)"""
        ...

    def Icon(self):
        """string icon = Icon()"""
        ...

    def Manager(self):
        """Unknown object = Manager()"""
        ...

    def SetBuffer(self, buffer, bufferLength):
        """SetBuffer(string buffer,integer bufferLength)"""
        ...

    def SetDesc(self, desc):
        """SetDesc(string desc)"""
        ...

    def SetUserName(self, userName):
        """SetUserName(string userName)"""
        ...

    def UserName(self):
        """string userName = UserName()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ScriptLineEvent(object):
    def __init__(self, *args, **kwargs):
        ...

    def Index(self):
        """integer index = Index()"""
        ...

    def Script(self):
        """Script object = Script()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ScriptManager(object):
    def __init__(self, *args, **kwargs):
        ...

    def ByIndex(self, index, write):
        """Unknown object = ByIndex(integer index,integer write)"""
        ...

    def Count(self):
        """integer count = Count()"""
        ...

    def Flags(self):
        """integer flags = Flags()"""
        ...

    def Lookup(self, hash, write, tryAsUserName):
        """Unknown object = Lookup(string hash,integer write,integer tryAsUserName)"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def New(self, name):
        """Unknown object = New(string name)"""
        ...

    def ReadWrite(self, hash, index):
        """ReadWrite(string hash,integer index)"""
        ...

    def Remove(self, script):
        """Remove(object script)"""
        ...

    def Run(self, script, execFlags, args, msg):
        """Run(object script,integer execFlags,string args,object msg)"""
        ...

    def Validate(self, script, msg):
        """Validate(object script,object msg)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ScriptQuery(object):
    def __init__(self, *args, **kwargs):
        ...

    def Query(self, attribute, query):
        """Query(string attribute,object query)"""
        ...

    def Select(self, attribute, which):
        """Select(string attribute,string which)"""
        ...

    def Type(self, attribute):
        """integer type = Type(string attribute)"""
        ...

    def TypeName(self, attribute):
        """string type = TypeName(string attribute)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SelectionListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def Add(self, type, subtType):
        """Add(integer type,integer subtType)"""
        ...

    def Current(self, type):
        """Current(integer type)"""
        ...

    def Remove(self, type, subtType):
        """Remove(integer type,integer subtType)"""
        ...

    def Time(self, time):
        """Time(float time)"""
        ...

    def TimeRange(self, type):
        """TimeRange(integer type)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SelectionOperation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Evaluate(self, type, state):
        """Evaluate(integer type,object state)"""
        ...

    def SetMesh(self, mesh):
        """SetMesh(object mesh)"""
        ...

    def SetTransform(self):
        """matrix xfrm = SetTransform()"""
        ...

    def TestEdge(self, edge):
        """boolean = TestEdge(id edge)"""
        ...

    def TestPoint(self, point):
        """boolean = TestPoint(id point)"""
        ...

    def TestPolygon(self, polygon):
        """boolean = TestPolygon(id polygon)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SelectionState(object):
    def __init__(self, *args, **kwargs):
        ...

    def SetEdge(self, edge, state):
        """SetEdge(id edge,integer state)"""
        ...

    def SetPoint(self, point, state):
        """SetPoint(id point,integer state)"""
        ...

    def SetPolygon(self, polygon, state):
        """SetPolygon(id polygon,integer state)"""
        ...

    def TestEdge(self, edge):
        """boolean = TestEdge(id edge)"""
        ...

    def TestPoint(self, point):
        """boolean = TestPoint(id point)"""
        ...

    def TestPolygon(self, polygon):
        """boolean = TestPolygon(id polygon)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SelectionType(object):
    def __init__(self, *args, **kwargs):
        ...

    def Compare(self, pkey, pelt):
        """integer = Compare(pointer pkey,pointer pelt)"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def MessageTable(self):
        """string = MessageTable()"""
        ...

    def Size(self):
        """integer = Size()"""
        ...

    def SubType(self, pkt):
        """integer = SubType(pointer pkt)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SessionListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def BeforeStartupCommands(self):
        """BeforeStartupCommands()"""
        ...

    def CheckQuitUI(self, quitWasAborted):
        """boolean = CheckQuitUI(integer quitWasAborted)"""
        ...

    def FirstWindowOpening(self):
        """FirstWindowOpening()"""
        ...

    def LastWindowClosed(self):
        """LastWindowClosed()"""
        ...

    def QuittingUI(self):
        """QuittingUI()"""
        ...

    def ShuttingDown(self):
        """ShuttingDown()"""
        ...

    def SystemReady(self):
        """SystemReady()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Shader(object):
    def __init__(self, *args, **kwargs):
        ...

    def Enumerate(self, visitor):
        """Enumerate(object visitor)"""
        ...

    def ShaderItemGet(self):
        """Item object = ShaderItemGet()"""
        ...

    def Spawn(self):
        """Shader object = Spawn()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ShaderDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def Item(self):
        """Unknown object = Item()"""
        ...

    def Location(self):
        """integer = Location()"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ShaderPreDest(object):
    def __init__(self, *args, **kwargs):
        ...

    def ContainerItem(self):
        """Item object = ContainerItem()"""
        ...

    def GetTag(self, type):
        """string tag = GetTag(integer type)"""
        ...

    def HitItem(self):
        """Item object = HitItem()"""
        ...

    def Item(self):
        """(integer mode,Item object) = Item()"""
        ...

    def Mode(self):
        """integer mode = Mode()"""
        ...

    def Scene(self):
        """Scene object = Scene()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ShaderSlice(object):
    def __init__(self, *args, **kwargs):
        ...

    def Evaluate(self, vecstack):
        """Evaluate(object vecstack)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ShapeDraw(object):
    def __init__(self, *args, **kwargs):
        ...

    def Arc(self, col, alpha, pos, rad, start, end, axis, flags):
        """Arc(vector col,float alpha,vector pos,float rad,float start,float end,integer axis,integer flags)"""
        ...

    def Arrow(self, col, pos, size, axis, flags):
        """Arrow(vector col,vector pos,float size,integer axis,integer flags)"""
        ...

    def Axis(self, col, pos, size, flags):
        """Axis(vector col,vector pos,vector size,integer flags)"""
        ...

    def BBox(self, col, size, flags):
        """BBox(vector col,float size,integer flags)"""
        ...

    def Bone(self, col, rlen, active):
        """Bone(vector col,float rlen,integer active)"""
        ...

    def BoxShape(self, colW, colF, pos, size, flags):
        """BoxShape(vector colW,vector colF,vector pos,vector size,integer flags)"""
        ...

    def CSeg(self, cen, offset, screen, col, flags):
        """CSeg(vector cen,vector offset,float screen,vector col,integer flags)"""
        ...

    def Circle(self, col, alpha, pos, rad, axis, flags):
        """Circle(vector col,float alpha,vector pos,float rad,integer axis,integer flags)"""
        ...

    def CircleShape(self, colW, colF, pos, radius, axis, flags):
        """CircleShape(vector colW,vector colF,vector pos,float radius,integer axis,integer flags)"""
        ...

    def Cone(self, col, pos, rad, height, axis, flags):
        """Cone(vector col,vector pos,float rad,float height,integer axis,integer flags)"""
        ...

    def ConeShape(self, colW, colF, pos, radius, height, axis, flags):
        """ConeShape(vector colW,vector colF,vector pos,float radius,float height,integer axis,integer flags)"""
        ...

    def Cross(self, col, pos, rad, flags):
        """Cross(vector col,vector pos,vector rad,integer flags)"""
        ...

    def CrossHair(self, col, alpha, pos, flags):
        """CrossHair(vector col,float alpha,vector pos,integer flags)"""
        ...

    def Cube(self, col, pos, size, flags):
        """Cube(vector col,vector pos,vector size,integer flags)"""
        ...

    def CubeFill(self, col, alpha, pos, size, flags):
        """CubeFill(vector col,float alpha,vector pos,vector size,integer flags)"""
        ...

    def Cylinder(self, col, pos, rad, height, axis, flags):
        """Cylinder(vector col,vector pos,float rad,float height,integer axis,integer flags)"""
        ...

    def CylinderShape(self, colW, colF, pos, radius, height, axis, flags):
        """CylinderShape(vector colW,vector colF,vector pos,float radius,float height,integer axis,integer flags)"""
        ...

    def Dimension(self, col, A, B, format, top, flags):
        """Dimension(vector col,vector A,vector B,string format,integer top,integer flags)"""
        ...

    def Distance(self, col, pos, dist, axis, flags):
        """Distance(vector col,vector pos,float dist,integer axis,integer flags)"""
        ...

    def Ellipse(self, col, alpha, pos, rad, axis, flags):
        """Ellipse(vector col,float alpha,vector pos,vector rad,integer axis,integer flags)"""
        ...

    def Ellipsoid(self, col, alpha, pos, rad, flags):
        """Ellipsoid(vector col,float alpha,vector pos,vector rad,integer flags)"""
        ...

    def Grid(self, col, pos, siz, divX, divY, divZ, axis, flags):
        """Grid(vector col,vector pos,vector siz,integer divX,integer divY,integer divZ,integer axis,integer flags)"""
        ...

    def Line(self, v0, v1, col, alpha, flags):
        """Line(vector v0,vector v1,vector col,float alpha,integer flags)"""
        ...

    def Link(self, col, posS, posE, solid, flags):
        """Link(vector col,vector posS,vector posE,integer solid,integer flags)"""
        ...

    def Pill(self, col, alpha, pos, width, height, rad, axis, flags):
        """Pill(vector col,float alpha,vector pos,float width,float height,float rad,integer axis,integer flags)"""
        ...

    def Plane(self, col, pos, size, axis, flags):
        """Plane(vector col,vector pos,vector size,integer axis,integer flags)"""
        ...

    def PlaneIndicator(self, col, alpha, pos, rad, axis, flags):
        """PlaneIndicator(vector col,float alpha,vector pos,float rad,integer axis,integer flags)"""
        ...

    def PlaneShape(self, colW, colF, pos, size, axis, flags):
        """PlaneShape(vector colW,vector colF,vector pos,vector size,integer axis,integer flags)"""
        ...

    def PreciseHandle(self, col, alpha, pos, size, flags):
        """PreciseHandle(vector col,float alpha,vector pos,vector size,integer flags)"""
        ...

    def Pyramid(self, col, pos, size, axis, flags):
        """Pyramid(vector col,vector pos,vector size,integer axis,integer flags)"""
        ...

    def PyramidShape(self, colW, colF, pos, size, axis, flags):
        """PyramidShape(vector colW,vector colF,vector pos,vector size,integer axis,integer flags)"""
        ...

    def RadialMap(self, image, col, cen, size, sel, flags):
        """RadialMap(object image,vector col,vector cen,float size,integer sel,integer flags)"""
        ...

    def RadialRays(self, image, col, cen, size, sel, flags):
        """RadialRays(object image,vector col,vector cen,float size,integer sel,integer flags)"""
        ...

    def Rhombus(self, col, pos, size, axis, flags):
        """Rhombus(vector col,vector pos,vector size,integer axis,integer flags)"""
        ...

    def RhombusShape(self, colW, colF, pos, size, axis, flags):
        """RhombusShape(vector colW,vector colF,vector pos,vector size,integer axis,integer flags)"""
        ...

    def Ruler(self, col, pos, xfrm, len, axis, flags):
        """Ruler(vector col,vector pos,matrix xfrm,float len,integer axis,integer flags)"""
        ...

    def SphereShape(self, colW, colF, pos, radius, axis, flags):
        """SphereShape(vector colW,vector colF,vector pos,float radius,integer axis,integer flags)"""
        ...

    def Star(self, col, pos, rad, flags):
        """Star(vector col,vector pos,vector rad,integer flags)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SharedWork(object):
    def __init__(self, *args, **kwargs):
        ...

    def Evaluate(self):
        """Evaluate()"""
        ...

    def Share(self, other, split):
        """Share(object other,integer split)"""
        ...

    def Spawn(self):
        """SharedWork object = Spawn()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SimulationListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def End(self):
        """End()"""
        ...

    def Invalidate(self):
        """Invalidate()"""
        ...

    def Start(self, channels):
        """Start(object channels)"""
        ...

    def Time(self, time):
        """Time(float time)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SimulationModifier(object):
    def __init__(self, *args, **kwargs):
        ...

    def Bake(self, time):
        """Bake(float time)"""
        ...

    def Cleanup(self):
        """Cleanup()"""
        ...

    def Enabled(self, chanRead):
        """boolean = Enabled(object chanRead)"""
        ...

    def Initialize(self, time, sample):
        """Initialize(float time,float sample)"""
        ...

    def Step(self, dt):
        """Step(float dt)"""
        ...

    def StepSize(self):
        """float stepSize = StepSize()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SolidDrill(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddMesh(self, meshObj, xfrm):
        """AddMesh(object meshObj,matrix xfrm)"""
        ...

    def Clear(self):
        """Clear()"""
        ...

    def Execute(self, meshObj, xfrm, pick, mode, sten, monitor):
        """Execute(object meshObj,matrix xfrm,integer pick,integer mode,string sten,object monitor)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class StackFilter(object):
    def __init__(self, *args, **kwargs):
        ...

    def Compare(self, other):
        """integer = Compare(object other)"""
        ...

    def Convert(self, other):
        """Convert(object other)"""
        ...

    def Identifier(self):
        """string identifier = Identifier()"""
        ...

    def Type(self):
        """string = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class StreamIO(object):
    def __init__(self, *args, **kwargs):
        ...

    def Read(self, stream):
        """Read(object stream)"""
        ...

    def Write(self, stream):
        """Write(object stream)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class StringConversion(object):
    def __init__(self, *args, **kwargs):
        ...

    def Decode(self, buf):
        """Decode(string buf)"""
        ...

    def Encode(self):
        """string = Encode()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class StringConversionNice(object):
    def __init__(self, *args, **kwargs):
        ...

    def Decode(self, buf):
        """Decode(string buf)"""
        ...

    def Encode(self):
        """string = Encode()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class StringTag(object):
    def __init__(self, *args, **kwargs):
        ...

    def ByIndex(self, index):
        """(integer type,string tag) = ByIndex(integer index)"""
        ...

    def Count(self):
        """integer count = Count()"""
        ...

    def Get(self, type):
        """string tag = Get(integer type)"""
        ...

    def Set(self, type, tag):
        """Set(integer type,string tag)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class StrokeDraw(object):
    def __init__(self, *args, **kwargs):
        ...

    def Begin(self, type, color, alpha):
        """Begin(integer type,vector color,float alpha)"""
        ...

    def BeginI(self, texture, type, color, alpha):
        """BeginI(object texture,integer type,vector color,float alpha)"""
        ...

    def BeginPoints(self, size, color, alpha):
        """BeginPoints(float size,vector color,float alpha)"""
        ...

    def BeginPolygons(self, type, color, alpha, stip, offsetX, offsetY, fill, cull):
        """BeginPolygons(integer type,vector color,float alpha,float stip,float offsetX,float offsetY,integer fill,integer cull)"""
        ...

    def BeginW(self, type, color, alpha, width):
        """BeginW(integer type,vector color,float alpha,float width)"""
        ...

    def BeginWD(self, type, color, alpha, width, dashPattern):
        """BeginWD(integer type,vector color,float alpha,float width,integer dashPattern)"""
        ...

    def Image(self, texID, just):
        """Image(integer texID,integer just)"""
        ...

    def PopTransform(self):
        """PopTransform()"""
        ...

    def PushTransform(self, v, m):
        """PushTransform(vector v,matrix m)"""
        ...

    def SetPart(self, part):
        """SetPart(integer part)"""
        ...

    def Text(self, text, just):
        """Text(string text,integer just)"""
        ...

    def TextureUV(self, u, v):
        """TextureUV(float u,float v)"""
        ...

    def Vertex(self, pos, flags):
        """Vertex(vector pos,integer flags)"""
        ...

    def Vertex3(self, x, y, z, flags):
        """Vertex3(float x,float y,float z,integer flags)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Subdivision(object):
    def __init__(self, *args, **kwargs):
        ...

    def Adaptive(self):
        """integer = Adaptive()"""
        ...

    def AddUVMap(self, name):
        """integer = AddUVMap(string name)"""
        ...

    def Backend(self):
        """integer = Backend()"""
        ...

    def BoundaryRule(self):
        """integer = BoundaryRule()"""
        ...

    def ChildFace(self, faceIndex, vertOfFace):
        """integer = ChildFace(integer faceIndex,integer vertOfFace)"""
        ...

    def FaceDepth(self, faceIndex):
        """integer = FaceDepth(integer faceIndex)"""
        ...

    def FirstFaceOffset(self, level):
        """integer = FirstFaceOffset(integer level)"""
        ...

    def FirstVertexOffset(self, level):
        """integer = FirstVertexOffset(integer level)"""
        ...

    def GetUV(self, mapIndex, faceIndex, vertOfFace):
        """float[] = GetUV(integer mapIndex,integer faceIndex,integer vertOfFace)"""
        ...

    def InvalidatePosition(self):
        """InvalidatePosition()"""
        ...

    def InvalidateTopology(self):
        """InvalidateTopology()"""
        ...

    def LookupUVMap(self, name):
        """integer = LookupUVMap(string name)"""
        ...

    def MaxLevel(self):
        """integer = MaxLevel()"""
        ...

    def NumFaces(self):
        """integer = NumFaces()"""
        ...

    def NumLevelFaces(self, level):
        """integer = NumLevelFaces(integer level)"""
        ...

    def NumLevelVertices(self, level):
        """integer = NumLevelVertices(integer level)"""
        ...

    def NumUVMap(self):
        """integer = NumUVMap()"""
        ...

    def NumVertices(self):
        """integer = NumVertices()"""
        ...

    def NumVerticesOfFace(self, faceIndex):
        """integer = NumVerticesOfFace(integer faceIndex)"""
        ...

    def ParentFace(self, faceIndex):
        """integer = ParentFace(integer faceIndex)"""
        ...

    def ParentVertex(self, vertIndex):
        """integer = ParentVertex(integer vertIndex)"""
        ...

    def Refine(self, mesh):
        """Refine(object mesh)"""
        ...

    def Scheme(self):
        """integer = Scheme()"""
        ...

    def SetAdaptive(self, adaptive):
        """integer = SetAdaptive(integer adaptive)"""
        ...

    def SetBackend(self, backend):
        """integer = SetBackend(integer backend)"""
        ...

    def SetBoundaryRule(self, bound):
        """integer = SetBoundaryRule(integer bound)"""
        ...

    def SetMaxLevel(self, level):
        """integer = SetMaxLevel(integer level)"""
        ...

    def SetScheme(self, scheme):
        """integer = SetScheme(integer scheme)"""
        ...

    def SetUVBoundaryRule(self, bound):
        """integer = SetUVBoundaryRule(integer bound)"""
        ...

    def Status(self):
        """integer = Status()"""
        ...

    def UVBoundaryRule(self):
        """integer = UVBoundaryRule()"""
        ...

    def UVMapName(self, mapIndex):
        """string = UVMapName(integer mapIndex)"""
        ...

    def Validate(self, mesh):
        """Validate(object mesh)"""
        ...

    def VertexNormal(self, vertIndex):
        """float[] = VertexNormal(integer vertIndex)"""
        ...

    def VertexOfFace(self, faceIndex, vertofface):
        """integer = VertexOfFace(integer faceIndex,integer vertofface)"""
        ...

    def VertexPosition(self, vertIndex):
        """float[] = VertexPosition(integer vertIndex)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Subject2Packet(object):
    def __init__(self, *args, **kwargs):
        ...

    def ScanAllocate(self, flags):
        """LayerScan object = ScanAllocate(integer flags)"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Surface(object):
    def __init__(self, *args, **kwargs):
        ...

    def BinByIndex(self, index):
        """SurfaceBin object = BinByIndex(integer index)"""
        ...

    def BinCount(self):
        """integer count = BinCount()"""
        ...

    def FrontBBox(self, pos, dir):
        """bounds bbox = FrontBBox(vector pos,vector dir)"""
        ...

    def GLCount(self):
        """integer count = GLCount()"""
        ...

    def GetBBox(self):
        """bounds bbox = GetBBox()"""
        ...

    def TagByIndex(self, type, index):
        """string stag = TagByIndex(integer type,integer index)"""
        ...

    def TagCount(self, type):
        """integer count = TagCount(integer type)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SurfaceBin(object):
    def __init__(self, *args, **kwargs):
        ...

    def FrontBBox(self, pos, dir):
        """bounds bbox = FrontBBox(vector pos,vector dir)"""
        ...

    def GetBBox(self):
        """bounds bbox = GetBBox()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SurfaceItem(object):
    def __init__(self, *args, **kwargs):
        ...

    def Evaluate(self, attr, index):
        """Surface object = Evaluate(object attr,integer index)"""
        ...

    def GetSurface(self, chanRead, morph):
        """Surface object = GetSurface(object chanRead,integer morph)"""
        ...

    def Prepare(self, eval):
        """integer index = Prepare(object eval)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class SymmetryPacket(object):
    def __init__(self, *args, **kwargs):
        ...

    def Active(self):
        """integer = Active()"""
        ...

    def Axis(self):
        """(integer,vector axvec,float offset) = Axis()"""
        ...

    def BaseSide(self):
        """integer = BaseSide()"""
        ...

    def Position(self, pos):
        """(integer,vector sv) = Position(vector pos)"""
        ...

    def SetBase(self, pos):
        """SetBase(vector pos)"""
        ...

    def TestSide(self, pos, useBase):
        """integer = TestSide(vector pos,integer useBase)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Tableau(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddElement(self, element, shader):
        """AddElement(object element,object shader)"""
        ...

    def AddInstance(self, inst, element, shader):
        """AddInstance(object inst,object element,object shader)"""
        ...

    def AddInstanceItem(self, instItem, fromItem, inst, vdesc, vertex):
        """AddInstanceItem(object instItem,object fromItem,object inst,object vdesc,float[] vertex)"""
        ...

    def AddInstanceableElement(self, elt, tags):
        """AddInstanceableElement(object elt,object tags)"""
        ...

    def Channels(self, type):
        """ChannelRead object = Channels(integer type)"""
        ...

    def EltNotify(self, element, event):
        """EltNotify(object element,integer event)"""
        ...

    def FindShader(self, item, tags):
        """TableauShader object = FindShader(object item,object tags)"""
        ...

    def InstNotify(self, instance, event):
        """InstNotify(object instance,integer event)"""
        ...

    def InstanceItem(self):
        """object = InstanceItem()"""
        ...

    def Time(self):
        """(float t0,float interval) = Time()"""
        ...

    def Update(self, visitor, immediate):
        """Update(object visitor,integer immediate)"""
        ...

    def UpdateAll(self):
        """UpdateAll()"""
        ...

    def Visible(self, item):
        """boolean = Visible(object item)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TableauElement(object):
    def __init__(self, *args, **kwargs):
        ...

    def Bound(self):
        """bounds bbox = Bound()"""
        ...

    def FeatureByIndex(self, type, index):
        """string name = FeatureByIndex(integer type,integer index)"""
        ...

    def FeatureCount(self, type):
        """integer = FeatureCount(integer type)"""
        ...

    def SetVertex(self, vdesc):
        """SetVertex(object vdesc)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TableauInstance(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetDissolve(self):
        """float dissolve = GetDissolve()"""
        ...

    def GetTransform(self, endPoint):
        """(vector offset,matrix xfrm) = GetTransform(integer endPoint)"""
        ...

    def ParticleArray(self):
        """float vector = ParticleArray()"""
        ...

    def ParticleDescription(self):
        """Unknown object = ParticleDescription()"""
        ...

    def Properties(self, vecstack):
        """Properties(object vecstack)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TableauLight(object):
    def __init__(self, *args, **kwargs):
        ...

    def Bound(self):
        """bounds bbox = Bound()"""
        ...

    def FeatureByIndex(self, type, index):
        """string name = FeatureByIndex(integer type,integer index)"""
        ...

    def FeatureCount(self, type):
        """integer = FeatureCount(integer type)"""
        ...

    def Geometry(self, gc):
        """integer = Geometry(pointer gc)"""
        ...

    def Sample(self, u, v, dir, t):
        """(vector wPos,vector oPos,vector norm) = Sample(float u,float v,vector dir,float t)"""
        ...

    def SetVertex(self, vdesc):
        """SetVertex(object vdesc)"""
        ...

    def ShadowMap(self):
        """(integer,Unknown object) = ShadowMap()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TableauProxy(object):
    def __init__(self, *args, **kwargs):
        ...

    def Bound(self):
        """bounds bbox = Bound()"""
        ...

    def FeatureByIndex(self, type, index):
        """string name = FeatureByIndex(integer type,integer index)"""
        ...

    def FeatureCount(self, type):
        """integer = FeatureCount(integer type)"""
        ...

    def Sample(self, bbox, tableau):
        """Sample(bounds bbox,object tableau)"""
        ...

    def SetVertex(self, vdesc):
        """SetVertex(object vdesc)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TableauShader(object):
    def __init__(self, *args, **kwargs):
        ...

    def Select(self, teElt, tvDesc):
        """Select(object teElt,object tvDesc)"""
        ...

    def Slice(self, vtOutput, tvDesc):
        """ShaderSlice object = Slice(object vtOutput,object tvDesc)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TableauSource(object):
    def __init__(self, *args, **kwargs):
        ...

    def ElementType(self, type):
        """integer supported = ElementType(integer type)"""
        ...

    def Elements(self, tableau):
        """Elements(object tableau)"""
        ...

    def GetCurves(self, tableau, tags):
        """Unknown object = GetCurves(object tableau,object tags)"""
        ...

    def Instance(self, tableau, instance):
        """Instance(object tableau,object instance)"""
        ...

    def Preview(self, tableau):
        """Preview(object tableau)"""
        ...

    def PreviewUpdate(self, chanIndex):
        """integer update = PreviewUpdate(integer chanIndex)"""
        ...

    def SubShader(self, tableau):
        """Unknown object = SubShader(object tableau)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TableauSurface(object):
    def __init__(self, *args, **kwargs):
        ...

    def Bound(self):
        """bounds bbox = Bound()"""
        ...

    def FeatureByIndex(self, type, index):
        """string name = FeatureByIndex(integer type,integer index)"""
        ...

    def FeatureCount(self, type):
        """integer = FeatureCount(integer type)"""
        ...

    def Padding(self):
        """float dist = Padding()"""
        ...

    def Sample(self, bbox, scale, trisoup):
        """Sample(bounds bbox,float scale,object trisoup)"""
        ...

    def SegmentBox(self, segID):
        """bounds bbox = SegmentBox(integer segID)"""
        ...

    def SetVertex(self, vdesc):
        """SetVertex(object vdesc)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TableauVertex(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddFeature(self, type, name):
        """integer index = AddFeature(integer type,string name)"""
        ...

    def ByIndex(self, index):
        """(integer type,string name,integer offset) = ByIndex(integer index)"""
        ...

    def Count(self):
        """integer = Count()"""
        ...

    def Lookup(self, type, name):
        """integer offset = Lookup(integer type,string name)"""
        ...

    def Size(self):
        """integer = Size()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TableauVolume(object):
    def __init__(self, *args, **kwargs):
        ...

    def Bound(self):
        """bounds bbox = Bound()"""
        ...

    def Density(self, densitySlice, sv, raycastObj, pos, worldPos):
        """float dens = Density(object densitySlice,object sv,object raycastObj,vector pos,integer worldPos)"""
        ...

    def FeatureByIndex(self, type, index):
        """string name = FeatureByIndex(integer type,integer index)"""
        ...

    def FeatureCount(self, type):
        """integer = FeatureCount(integer type)"""
        ...

    def RayCast(self, densitySlice, sv, raycastObj):
        """(float dist,integer localShader) = RayCast(object densitySlice,object sv,object raycastObj)"""
        ...

    def RaySample(self, densitySlice, shadingSlice, sv, raycastObj, raymarchObj):
        """RaySample(object densitySlice,object shadingSlice,object sv,object raycastObj,object raymarchObj)"""
        ...

    def RenderInit(self, sv):
        """RenderInit(object sv)"""
        ...

    def SetVertex(self, vdesc):
        """SetVertex(object vdesc)"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TagDescription(object):
    def __init__(self, *args, **kwargs):
        ...

    def Count(self):
        """integer = Count()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TextEncoding(object):
    def __init__(self, *args, **kwargs):
        ...

    def Convert(self, src, buf, max):
        """Convert(string src,byte[] buf,integer max)"""
        ...

    def Default(self):
        """integer = Default()"""
        ...

    def NumChar(self, string, target):
        """integer = NumChar(string string,integer target)"""
        ...

    def PullChar(self, string, target):
        """(string,integer code,integer len) = PullChar(string string,integer target)"""
        ...

    def SetSource(self, encoding):
        """SetSource(integer encoding)"""
        ...

    def SetTarget(self, encoding):
        """SetTarget(integer encoding)"""
        ...

    def Source(self):
        """integer = Source()"""
        ...

    def Target(self):
        """integer = Target()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TextScriptInterpreter(object):
    def __init__(self, *args, **kwargs):
        ...

    def Run(self, script, execFlags, args, msg):
        """Run(object script,integer execFlags,string args,object msg)"""
        ...

    def Validate(self, script, msg):
        """boolean = Validate(object script,object msg)"""
        ...

    def ValidateFileType(self, script, firstLine):
        """boolean = ValidateFileType(object script,string firstLine)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Texture(object):
    def __init__(self, *args, **kwargs):
        ...

    def Effect(self):
        """string = Effect()"""
        ...

    def EvalImage(self, scene):
        """Image object = EvalImage(object scene)"""
        ...

    def Image(self):
        """Item object = Image()"""
        ...

    def ImageName(self):
        """string = ImageName()"""
        ...

    def Locator(self):
        """Item object = Locator()"""
        ...

    def LocatorProjectionAxis(self, time):
        """integer = LocatorProjectionAxis(float time)"""
        ...

    def LocatorProjectionMode(self, time):
        """integer = LocatorProjectionMode(float time)"""
        ...

    def SetEffect(self, effect):
        """SetEffect(string effect)"""
        ...

    def SetImage(self, img):
        """SetImage(object img)"""
        ...

    def SetLocator(self, tloc):
        """SetLocator(object tloc)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TextureEffect(object):
    def __init__(self, *args, **kwargs):
        ...

    def Get(self, sv, item):
        """float val = Get(object sv,pointer item)"""
        ...

    def Set(self, sv, val, item):
        """Set(object sv,float[] val,pointer item)"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def TypeName(self):
        """string = TypeName()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TexturePacket(object):
    def __init__(self, *args, **kwargs):
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ThreadGroup(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddJob(self, job):
        """AddJob(object job)"""
        ...

    def Clear(self):
        """Clear()"""
        ...

    def Execute(self):
        """Execute()"""
        ...

    def Kill(self):
        """Kill()"""
        ...

    def NumJobs(self):
        """integer = NumJobs()"""
        ...

    def Running(self):
        """boolean = Running()"""
        ...

    def Wait(self):
        """Wait()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ThreadJob(object):
    def __init__(self, *args, **kwargs):
        ...

    def Execute(self):
        """Execute()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ThreadMutex(object):
    def __init__(self, *args, **kwargs):
        ...

    def Enter(self):
        """Enter()"""
        ...

    def Leave(self):
        """Leave()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ThreadRangeWorker(object):
    def __init__(self, *args, **kwargs):
        ...

    def Execute(self, index, sharedData):
        """Execute(integer index,pointer sharedData)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ThreadSlot(object):
    def __init__(self, *args, **kwargs):
        ...

    def Clear(self):
        """Clear()"""
        ...

    def Set(self, value):
        """Set(pointer value)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ThreadSlotClient(object):
    def __init__(self, *args, **kwargs):
        ...

    def Free(self, value):
        """Free(pointer value)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TileImage(object):
    def __init__(self, *args, **kwargs):
        ...

    def DeterminePixel(self, level, x, y):
        """(integer adjX,integer adjY) = DeterminePixel(integer level,integer x,integer y)"""
        ...

    def DetermineTile(self, level, x, y):
        """(integer tileX,integer tileY) = DetermineTile(integer level,integer x,integer y)"""
        ...

    def GetLevelSize(self, level):
        """(integer width,integer height,integer tilesWidth,integer tilesHeight) = GetLevelSize(integer level)"""
        ...

    def GetTile(self, level, tileX, tileY):
        """Image object = GetTile(integer level,integer tileX,integer tileY)"""
        ...

    def GetTileSize(self, level, tileX, tileY):
        """(integer width,integer height) = GetTileSize(integer level,integer tileX,integer tileY)"""
        ...

    def LevelCount(self):
        """integer = LevelCount()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Tool(object):
    def __init__(self, *args, **kwargs):
        ...

    def CompareOp(self, vts, toolop):
        """integer = CompareOp(object vts,object toolop)"""
        ...

    def Evaluate(self, vts):
        """Evaluate(object vts)"""
        ...

    def GetOp(self, flags):
        """Unknown object = GetOp(integer flags)"""
        ...

    def Order(self):
        """string = Order()"""
        ...

    def Reset(self):
        """Reset()"""
        ...

    def Sequence(self, seq):
        """Sequence(object seq)"""
        ...

    def ShouldBeAttribute(self, task):
        """integer = ShouldBeAttribute(integer task)"""
        ...

    def Task(self):
        """integer = Task()"""
        ...

    def UpdateOp(self, toolop):
        """UpdateOp(object toolop)"""
        ...

    def VectorType(self):
        """object = VectorType()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ToolModel(object):
    def __init__(self, *args, **kwargs):
        ...

    def AllowOverride(self, attrName, mouseInput, haulAxis):
        """AllowOverride(string attrName,integer mouseInput,integer haulAxis)"""
        ...

    def Down(self, vts, adjust):
        """Down(object vts,object adjust)"""
        ...

    def Draw(self, vts, stroke, flags):
        """Draw(object vts,object stroke,integer flags)"""
        ...

    def Drop(self):
        """Drop()"""
        ...

    def Enable(self, msg):
        """Enable(object msg)"""
        ...

    def Filter(self, vts, adjust):
        """Filter(object vts,object adjust)"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def Haul(self, index):
        """string = Haul(integer index)"""
        ...

    def Help(self, vts):
        """string = Help(object vts)"""
        ...

    def Initialize(self, vts, adjust, flags):
        """Initialize(object vts,object adjust,integer flags)"""
        ...

    def Move(self, vts, adjust):
        """Move(object vts,object adjust)"""
        ...

    def Post(self, vts):
        """Post(object vts)"""
        ...

    def Test(self, vts, stroke, flags):
        """Test(object vts,object stroke,integer flags)"""
        ...

    def TestType(self, type):
        """TestType(integer type)"""
        ...

    def Tooltip(self, vts, part):
        """string = Tooltip(object vts,integer part)"""
        ...

    def Track(self, vts, eventType):
        """Track(object vts,integer eventType)"""
        ...

    def TrackFlags(self):
        """integer flags = TrackFlags()"""
        ...

    def Up(self, vts, adjust):
        """Up(object vts,object adjust)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ToolOperation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Blend(self, other, blend):
        """Blend(object other,object blend)"""
        ...

    def Evaluate(self, vts):
        """Evaluate(object vts)"""
        ...

    def ReEvaluate(self, vts):
        """ReEvaluate(object vts)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TransformScan(object):
    def __init__(self, *args, **kwargs):
        ...

    def AlternateAxis(self):
        """(matrix matrix,matrix inverse) = AlternateAxis()"""
        ...

    def AlternateCenter(self):
        """vector center = AlternateCenter()"""
        ...

    def Enumerate(self, visitor):
        """Enumerate(object visitor)"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def Position(self):
        """float[] = Position()"""
        ...

    def SetPosition(self):
        """vector pos = SetPosition()"""
        ...

    def Weight(self):
        """float = Weight()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Tree(object):
    def __init__(self, *args, **kwargs):
        ...

    def ChildIsLeaf(self):
        """boolean = ChildIsLeaf()"""
        ...

    def Count(self):
        """integer count = Count()"""
        ...

    def Current(self):
        """integer index = Current()"""
        ...

    def IsRoot(self):
        """boolean = IsRoot()"""
        ...

    def ItemState(self, guid):
        """integer state = ItemState(string guid)"""
        ...

    def SetCurrent(self, index):
        """SetCurrent(integer index)"""
        ...

    def SetItemState(self, guid, state):
        """SetItemState(string guid,integer state)"""
        ...

    def Spawn(self, mode):
        """Tree object = Spawn(integer mode)"""
        ...

    def ToChild(self):
        """ToChild()"""
        ...

    def ToParent(self):
        """ToParent()"""
        ...

    def ToRoot(self):
        """ToRoot()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TreeListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def ClearAllCachedThumbnails(self):
        """ClearAllCachedThumbnails()"""
        ...

    def ClearCachedThumbnail(self, ident):
        """ClearCachedThumbnail(string ident)"""
        ...

    def NewAttributes(self):
        """NewAttributes()"""
        ...

    def NewShape(self):
        """NewShape()"""
        ...

    def NewShowDescriptionText(self):
        """NewShowDescriptionText()"""
        ...

    def NewSpaceForThumbnails(self):
        """NewSpaceForThumbnails()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TreeView(object):
    def __init__(self, *args, **kwargs):
        ...

    def BadgeDetail(self, columnIndex, badgeIndex, badgeDetail):
        """string = BadgeDetail(integer columnIndex,integer badgeIndex,integer badgeDetail)"""
        ...

    def BadgeType(self, columnIndex, badgeIndex):
        """integer badgeType = BadgeType(integer columnIndex,integer badgeIndex)"""
        ...

    def BadgeType2(self, columnIndex, badgeIndex):
        """integer badgeType = BadgeType2(integer columnIndex,integer badgeIndex)"""
        ...

    def BatchCommand(self, columnIndex):
        """string = BatchCommand(integer columnIndex)"""
        ...

    def CanFilter(self):
        """boolean = CanFilter()"""
        ...

    def CellCommand(self, columnIndex):
        """string = CellCommand(integer columnIndex)"""
        ...

    def ColumnByIndex(self, columnIndex):
        """(string,integer columnWidth) = ColumnByIndex(integer columnIndex)"""
        ...

    def ColumnCount(self):
        """integer colCount = ColumnCount()"""
        ...

    def ColumnIconResource(self, columnIndex):
        """string = ColumnIconResource(integer columnIndex)"""
        ...

    def ColumnInternalName(self, columnIndex):
        """string = ColumnInternalName(integer columnIndex)"""
        ...

    def ColumnJustification(self, columnIndex):
        """integer justification = ColumnJustification(integer columnIndex)"""
        ...

    def DescriptionText(self, columnIndex):
        """string = DescriptionText(integer columnIndex)"""
        ...

    def Filter(self):
        """integer flags = Filter()"""
        ...

    def GetDragDropDestinationObject(self, columnIndex, location):
        """Unknown object = GetDragDropDestinationObject(integer columnIndex,integer location)"""
        ...

    def GetDragDropSourceObject(self, columnIndex, type):
        """Unknown object = GetDragDropSourceObject(integer columnIndex,string type)"""
        ...

    def IconResource(self, columnIndex, width, height):
        """string = IconResource(integer columnIndex,integer width,integer height)"""
        ...

    def IsDescendantSelected(self):
        """boolean = IsDescendantSelected()"""
        ...

    def IsInputRegion(self, columnIndex, regionID):
        """boolean = IsInputRegion(integer columnIndex,integer regionID)"""
        ...

    def IsSelected(self):
        """boolean = IsSelected()"""
        ...

    def PrimaryColumnPosition(self):
        """integer index = PrimaryColumnPosition()"""
        ...

    def ReservedSpaceForIcons(self):
        """(integer columnIndex,integer width,integer height,integer iconAsValue) = ReservedSpaceForIcons()"""
        ...

    def ReservedSpaceForThumbnails(self):
        """(integer columnIndex,integer width,integer height) = ReservedSpaceForThumbnails()"""
        ...

    def RestoreState(self, uid):
        """RestoreState(string uid)"""
        ...

    def Select(self, mode):
        """Select(integer mode)"""
        ...

    def ShowDescriptionText(self):
        """ShowDescriptionText()"""
        ...

    def StoreState(self, uid):
        """StoreState(string uid)"""
        ...

    def StyleHints(self):
        """integer flags = StyleHints()"""
        ...

    def SupportedDragDropSourceTypes(self, columnIndex):
        """string = SupportedDragDropSourceTypes(integer columnIndex)"""
        ...

    def Thumbnail(self, columnIndex, width, height):
        """(Image object,string) = Thumbnail(integer columnIndex,integer width,integer height)"""
        ...

    def ToPrimary(self):
        """boolean = ToPrimary()"""
        ...

    def ToolTip(self, columnIndex):
        """string = ToolTip(integer columnIndex)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TriangleGroup(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddSurface(self):
        """TriangleSurface object = AddSurface()"""
        ...

    def Cleanup(self):
        """Cleanup()"""
        ...

    def GetSurface(self, index):
        """TriangleSurface object = GetSurface(integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TriangleSoup(object):
    def __init__(self, *args, **kwargs):
        ...

    def Connect(self, type):
        """Connect(integer type)"""
        ...

    def Polygon(self, v0, v1, v2):
        """Polygon(integer v0,integer v1,integer v2)"""
        ...

    def Segment(self, segID, type):
        """Segment(integer segID,integer type)"""
        ...

    def TestBox(self, bbox):
        """integer = TestBox(bounds bbox)"""
        ...

    def Vertex(self, vertex):
        """integer index = Vertex(float[] vertex)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class TriangleSurface(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddVector(self, type, name):
        """integer index = AddVector(integer type,string name)"""
        ...

    def FixNormals(self):
        """unsigned[] = FixNormals()"""
        ...

    def GetSize(self):
        """(integer nvrt,integer ntri) = GetSize()"""
        ...

    def SetEdge(self, edge):
        """unsigned[] = SetEdge(integer edge)"""
        ...

    def SetEdgeCount(self, nedge):
        """SetEdgeCount(integer nedge)"""
        ...

    def SetSize(self, nvrt, ntri):
        """SetSize(integer nvrt,integer ntri)"""
        ...

    def SetTriangle(self, tri):
        """unsigned[] = SetTriangle(integer tri)"""
        ...

    def SetVector(self, index, vrt):
        """float[] = SetVector(integer index,integer vrt)"""
        ...

    def Triangles(self):
        """unsigned[] = Triangles()"""
        ...

    def Vector(self, index):
        """float[] = Vector(integer index)"""
        ...

    def VectorInfo(self, index):
        """(integer type,string name,integer dim) = VectorInfo(integer index)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class UIHints(object):
    def __init__(self, *args, **kwargs):
        ...

    def BooleanStyle(self, style):
        """BooleanStyle(integer style)"""
        ...

    def ButtonHasPopoverDecoration(self, state):
        """ButtonHasPopoverDecoration(integer state)"""
        ...

    def ChannelFlags(self, flags):
        """ChannelFlags(integer flags)"""
        ...

    def Class(self, c):
        """Class(string c)"""
        ...

    def ClipChoiceSupportsGroups(self, flags):
        """ClipChoiceSupportsGroups(integer flags)"""
        ...

    def ForceUpdate(self):
        """ForceUpdate()"""
        ...

    def FormFilterPriority(self, priority):
        """FormFilterPriority(integer priority)"""
        ...

    def InfoTextUseSmallFont(self, state):
        """InfoTextUseSmallFont(integer state)"""
        ...

    def Label(self, label):
        """Label(string label)"""
        ...

    def MaxFloat(self, max):
        """MaxFloat(float max)"""
        ...

    def MaxInt(self, max):
        """MaxInt(integer max)"""
        ...

    def MinFloat(self, min):
        """MinFloat(float min)"""
        ...

    def MinInt(self, min):
        """MinInt(integer min)"""
        ...

    def StepFloat(self, step):
        """StepFloat(float step)"""
        ...

    def StepInt(self, step):
        """StepInt(integer step)"""
        ...

    def StringList(self):
        """string strings = StringList()"""
        ...

    def TextFixedWidthFont(self, state):
        """TextFixedWidthFont(integer state)"""
        ...

    def TextLines(self, lines):
        """TextLines(integer lines)"""
        ...

    def TextPasswordMode(self, state):
        """TextPasswordMode(integer state)"""
        ...

    def Track(self, state):
        """Track(integer state)"""
        ...

    def ValuePresetCookie(self, cookie):
        """ValuePresetCookie(string cookie)"""
        ...

    def VertmapAllowNone(self, state):
        """VertmapAllowNone(integer state)"""
        ...

    def VertmapItemMode(self, state):
        """VertmapItemMode(integer state)"""
        ...

    def VertmapType(self, type):
        """VertmapType(integer type)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class UIHintsRead(object):
    def __init__(self, *args, **kwargs):
        ...

    def BooleanStyle(self):
        """integer style = BooleanStyle()"""
        ...

    def ButtonHasPopoverDecoration(self):
        """integer state = ButtonHasPopoverDecoration()"""
        ...

    def ChannelFlags(self):
        """integer flags = ChannelFlags()"""
        ...

    def Class(self):
        """string = Class()"""
        ...

    def ClipChoiceSupportsGroups(self):
        """integer flags = ClipChoiceSupportsGroups()"""
        ...

    def ForceUpdate(self):
        """integer state = ForceUpdate()"""
        ...

    def FormFilterPriority(self):
        """integer priority = FormFilterPriority()"""
        ...

    def InfoTextUseSmallFont(self):
        """integer state = InfoTextUseSmallFont()"""
        ...

    def Label(self):
        """string = Label()"""
        ...

    def MaxFloat(self):
        """float max = MaxFloat()"""
        ...

    def MaxInt(self):
        """integer max = MaxInt()"""
        ...

    def MinFloat(self):
        """float min = MinFloat()"""
        ...

    def MinInt(self):
        """integer min = MinInt()"""
        ...

    def StepFloat(self):
        """float step = StepFloat()"""
        ...

    def StepInt(self):
        """integer step = StepInt()"""
        ...

    def StringListByIndex(self, index):
        """string = StringListByIndex(integer index)"""
        ...

    def StringListCount(self):
        """integer count = StringListCount()"""
        ...

    def TextFixedWidthFont(self):
        """integer state = TextFixedWidthFont()"""
        ...

    def TextLines(self):
        """integer lines = TextLines()"""
        ...

    def TextPasswordMode(self):
        """integer state = TextPasswordMode()"""
        ...

    def Track(self):
        """integer state = Track()"""
        ...

    def ValuePresetCookie(self):
        """string = ValuePresetCookie()"""
        ...

    def VertmapAllowNone(self):
        """integer state = VertmapAllowNone()"""
        ...

    def VertmapItemMode(self):
        """integer state = VertmapItemMode()"""
        ...

    def VertmapType(self):
        """integer type = VertmapType()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class UIValueHints(object):
    def __init__(self, *args, **kwargs):
        ...

    def ColorPickerCommands(self, rgb, alpha, rgbAlt, alphaAlt, useAlt, bufLens):
        """ColorPickerCommands(byte[] rgb,byte[] alpha,byte[] rgbAlt,byte[] alphaAlt,byte[] useAlt,integer bufLens)"""
        ...

    def CueText(self):
        """string = CueText()"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def FormCommandListByIndex(self, index):
        """string command = FormCommandListByIndex(integer index)"""
        ...

    def FormCommandListCount(self):
        """integer count = FormCommandListCount()"""
        ...

    def ItemTest(self, item):
        """boolean = ItemTest(object item)"""
        ...

    def NotifierByIndex(self, index):
        """(string name,string args) = NotifierByIndex(integer index)"""
        ...

    def NotifierCount(self):
        """integer count = NotifierCount()"""
        ...

    def PopCategory(self):
        """string category = PopCategory()"""
        ...

    def PopCount(self):
        """integer = PopCount()"""
        ...

    def PopFlags(self, index):
        """integer flags = PopFlags(integer index)"""
        ...

    def PopIconImage(self, index):
        """Image object = PopIconImage(integer index)"""
        ...

    def PopIconResource(self, index):
        """string iconResource = PopIconResource(integer index)"""
        ...

    def PopIconSize(self):
        """(integer,integer w,integer h) = PopIconSize()"""
        ...

    def PopInternalName(self, index):
        """string = PopInternalName(integer index)"""
        ...

    def PopToolTip(self, index):
        """string = PopToolTip(integer index)"""
        ...

    def PopUserName(self, index):
        """string = PopUserName(integer index)"""
        ...

    def TextValidate(self, value):
        """string = TextValidate(string value)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Undo(object):
    def __init__(self, *args, **kwargs):
        ...

    def Forward(self):
        """Forward()"""
        ...

    def Reverse(self):
        """Reverse()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Unknown(object):
    def __init__(self, *args, **kwargs):
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class UserValue(object):
    def __init__(self, *args, **kwargs):
        ...

    def Action(self):
        """string action = Action()"""
        ...

    def ArgType(self):
        """string argType = ArgType()"""
        ...

    def AsUI(self):
        """boolean = AsUI()"""
        ...

    def DefaultValue(self):
        """Unknown object = DefaultValue()"""
        ...

    def DeferAction(self):
        """boolean = DeferAction()"""
        ...

    def DialogUserName(self):
        """string username = DialogUserName()"""
        ...

    def EnableCommand(self):
        """string command = EnableCommand()"""
        ...

    def FloatRange(self):
        """(integer hasMin,float min,integer hasMax,float max) = FloatRange()"""
        ...

    def GetFlt(self):
        """float val = GetFlt()"""
        ...

    def GetInt(self):
        """integer val = GetInt()"""
        ...

    def GetString(self):
        """string = GetString()"""
        ...

    def IntRange(self):
        """(integer hasMin,integer min,integer hasMax,integer max) = IntRange()"""
        ...

    def InvertEnableCommandTest(self):
        """boolean = InvertEnableCommandTest()"""
        ...

    def IsTransient(self):
        """(boolean,integer isTransient) = IsTransient()"""
        ...

    def Lifespan(self):
        """integer life = Lifespan()"""
        ...

    def List(self):
        """string list = List()"""
        ...

    def ListNames(self):
        """string listNames = ListNames()"""
        ...

    def Name(self):
        """string name = Name()"""
        ...

    def Notifier(self):
        """string notifier = Notifier()"""
        ...

    def Type(self):
        """integer type = Type()"""
        ...

    def TypeName(self):
        """string tname = TypeName()"""
        ...

    def UIMode(self):
        """integer uiMode = UIMode()"""
        ...

    def UserName(self):
        """string username = UserName()"""
        ...

    def ValuePresetCookie(self):
        """string cookie = ValuePresetCookie()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class UserValueListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def Added(self, userValue):
        """Added(object userValue)"""
        ...

    def DefChanged(self, userValue):
        """DefChanged(object userValue)"""
        ...

    def Deleted(self, name):
        """Deleted(string name)"""
        ...

    def ValueChanged(self, userValue):
        """ValueChanged(object userValue)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VMapPacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Name(self, packet):
        """string name = Name(pointer packet)"""
        ...

    def Packet(self, type, name):
        """pointer = Packet(integer type,string name)"""
        ...

    def Type(self, packet):
        """integer type = Type(pointer packet)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Value(object):
    def __init__(self, *args, **kwargs):
        ...

    def Clone(self):
        """Value object = Clone()"""
        ...

    def Compare(self, other):
        """integer diff = Compare(object other)"""
        ...

    def Copy(self, from_obj):
        """Copy(object from_obj)"""
        ...

    def GetFlt(self):
        """float val = GetFlt()"""
        ...

    def GetInt(self):
        """integer val = GetInt()"""
        ...

    def GetString(self):
        """string = GetString()"""
        ...

    def Intrinsic(self):
        """pointer = Intrinsic()"""
        ...

    def SetFlt(self, val):
        """SetFlt(float val)"""
        ...

    def SetInt(self, val):
        """SetInt(integer val)"""
        ...

    def SetString(self, val):
        """SetString(string val)"""
        ...

    def SubTypeName(self):
        """string name = SubTypeName()"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def TypeName(self):
        """string name = TypeName()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ValueArray(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddEmptyValue(self):
        """Value object = AddEmptyValue()"""
        ...

    def AddFloat(self, value):
        """AddFloat(float value)"""
        ...

    def AddInt(self, value):
        """AddInt(integer value)"""
        ...

    def AddString(self, value):
        """AddString(string value)"""
        ...

    def AddValue(self, value):
        """AddValue(object value)"""
        ...

    def Count(self):
        """integer = Count()"""
        ...

    def FirstUnique(self):
        """integer uniqueIndex = FirstUnique()"""
        ...

    def GetFloat(self, index):
        """float value = GetFloat(integer index)"""
        ...

    def GetInt(self, index):
        """integer value = GetInt(integer index)"""
        ...

    def GetString(self, index):
        """string = GetString(integer index)"""
        ...

    def GetValue(self, index):
        """Value object = GetValue(integer index)"""
        ...

    def Remove(self, index):
        """Remove(integer index)"""
        ...

    def Reset(self):
        """Reset()"""
        ...

    def SetFloat(self, index, value):
        """SetFloat(integer index,float value)"""
        ...

    def SetInt(self, index, value):
        """SetInt(integer index,integer value)"""
        ...

    def SetString(self, index, value):
        """SetString(integer index,string value)"""
        ...

    def SetValue(self, index, value):
        """SetValue(integer index,object value)"""
        ...

    def Type(self):
        """integer type = Type()"""
        ...

    def TypeName(self):
        """string name = TypeName()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ValueConversion(object):
    def __init__(self, *args, **kwargs):
        ...

    def Convert(self, from_obj, fromType, to_obj, toType):
        """Convert(object from_obj,string fromType,object to_obj,string toType)"""
        ...

    def Test(self, fromType, toType):
        """Test(string fromType,string toType)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ValueMath(object):
    def __init__(self, *args, **kwargs):
        ...

    def Add(self, delta):
        """Add(float delta)"""
        ...

    def Blend(self, other, blend):
        """Blend(object other,float blend)"""
        ...

    def Detent(self):
        """integer = Detent()"""
        ...

    def Multiply(self, factor):
        """Multiply(float factor)"""
        ...

    def Step(self, direction):
        """Step(integer direction)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ValueReference(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetObject(self):
        """Unknown object = GetObject()"""
        ...

    def IsSet(self):
        """boolean = IsSet()"""
        ...

    def SetObject(self, obj):
        """SetObject(object obj)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ValueTexture(object):
    def __init__(self, *args, **kwargs):
        ...

    def Cleanup(self, data):
        """Cleanup(pointer data)"""
        ...

    def IsSampleDriven(self):
        """(integer,integer idx) = IsSampleDriven()"""
        ...

    def LinkChannels(self, eval, item):
        """LinkChannels(object eval,object item)"""
        ...

    def LinkSampleChannels(self, nodalEtor, item):
        """integer idx = LinkSampleChannels(object nodalEtor,object item)"""
        ...

    def Setup(self, data):
        """Setup(pointer data)"""
        ...

    def SetupChannels(self, addChan):
        """SetupChannels(object addChan)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ValueTextureCustom(object):
    def __init__(self, *args, **kwargs):
        ...

    def AddFeature(self, type, name):
        """AddFeature(integer type,string name)"""
        ...

    def AddPacket(self, name):
        """AddPacket(string name)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Variation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Do(self, x, y):
        """Do(float x,float y)"""
        ...

    def Initialize(self, item, chanRead):
        """(float x,float y) = Initialize(object item,object chanRead)"""
        ...

    def RangeX(self):
        """(float min,float max) = RangeX()"""
        ...

    def RangeY(self):
        """(float min,float max) = RangeY()"""
        ...

    def TestItem(self, item, chanRead):
        """boolean = TestItem(object item,object chanRead)"""
        ...

    def Thumb(self, x, y, size, chanRead):
        """Unknown object = Thumb(float x,float y,integer size,object chanRead)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VectorCanvas(object):
    def __init__(self, *args, **kwargs):
        ...

    def BeginEditBatch(self):
        """BeginEditBatch()"""
        ...

    def EndEditBatch(self):
        """EndEditBatch()"""
        ...

    def GetItem(self):
        """Item object = GetItem()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VectorKnotPacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Canvas(self, packet):
        """VectorCanvas object = Canvas(pointer packet)"""
        ...

    def Item(self, packet):
        """Item object = Item(pointer packet)"""
        ...

    def Path(self, packet):
        """VectorPath object = Path(pointer packet)"""
        ...

    def Shape(self, packet):
        """VectorShape object = Shape(pointer packet)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VectorList(object):
    def __init__(self, *args, **kwargs):
        ...

    def Append(self):
        """integer index = Append()"""
        ...

    def Clear(self):
        """Clear()"""
        ...

    def Count(self):
        """integer = Count()"""
        ...

    def Current(self):
        """integer = Current()"""
        ...

    def Optional(self, offset):
        """pointer = Optional(integer offset)"""
        ...

    def SetCurrent(self, index):
        """SetCurrent(integer index)"""
        ...

    def SetPacket(self, offset, pdat):
        """SetPacket(integer offset,pointer pdat)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VectorListener(object):
    def __init__(self, *args, **kwargs):
        ...

    def Destroy(self):
        """Destroy()"""
        ...

    def KnotPosition(self, shape, path):
        """KnotPosition(object shape,object path)"""
        ...

    def PathAdd(self, shape, path):
        """PathAdd(object shape,object path)"""
        ...

    def PathRemove(self, shape, path):
        """PathRemove(object shape,object path)"""
        ...

    def ShapeAdd(self, shape):
        """ShapeAdd(object shape)"""
        ...

    def ShapeRemove(self, shape):
        """ShapeRemove(object shape)"""
        ...

    def ShapeStyle(self, shape, name):
        """ShapeStyle(object shape,string name)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VectorPath(object):
    def __init__(self, *args, **kwargs):
        ...

    def ID(self):
        """id = ID()"""
        ...

    def IsPathClosed(self):
        """boolean = IsPathClosed()"""
        ...

    def KnotCount(self):
        """integer count = KnotCount()"""
        ...

    def KnotEnumerate(self, visitor):
        """KnotEnumerate(object visitor)"""
        ...

    def Pos(self):
        """(float x,float y) = Pos()"""
        ...

    def SelectKnot(self, knot):
        """SelectKnot(id knot)"""
        ...

    def SelectKnotByIndex(self, index):
        """SelectKnotByIndex(integer index)"""
        ...

    def SetPathClosed(self, closed):
        """SetPathClosed(integer closed)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VectorPathPacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Canvas(self, packet):
        """VectorCanvas object = Canvas(pointer packet)"""
        ...

    def Item(self, packet):
        """Item object = Item(pointer packet)"""
        ...

    def Packet(self, path):
        """pointer = Packet(object path)"""
        ...

    def Path(self, packet):
        """VectorPath object = Path(pointer packet)"""
        ...

    def Shape(self, packet):
        """VectorShape object = Shape(pointer packet)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VectorShape(object):
    def __init__(self, *args, **kwargs):
        ...

    def Parent(self):
        """VectorShape object = Parent()"""
        ...

    def PathByIndex(self, index):
        """VectorPath object = PathByIndex(integer index)"""
        ...

    def PathCount(self):
        """integer count = PathCount()"""
        ...

    def ShapeByIndex(self, index):
        """VectorShape object = ShapeByIndex(integer index)"""
        ...

    def ShapeCount(self):
        """integer count = ShapeCount()"""
        ...

    def Transform(self, matrix):
        """Transform(matrix matrix)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VectorShapePacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Canvas(self, packet):
        """VectorCanvas object = Canvas(pointer packet)"""
        ...

    def Item(self, packet):
        """Item object = Item(pointer packet)"""
        ...

    def Packet(self, shape):
        """pointer = Packet(object shape)"""
        ...

    def Shape(self, packet):
        """VectorShape object = Shape(pointer packet)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VectorStack(object):
    def __init__(self, *args, **kwargs):
        ...

    def Optional(self, offset):
        """pointer = Optional(integer offset)"""
        ...

    def Pop(self):
        """Pop()"""
        ...

    def Push(self):
        """Push()"""
        ...

    def SetPacket(self, offset, pdat):
        """SetPacket(integer offset,pointer pdat)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VectorType(object):
    def __init__(self, *args, **kwargs):
        ...

    def ByIndex(self, type, index):
        """(integer,integer flags) = ByIndex(integer type,integer index)"""
        ...

    def Category(self):
        """string = Category()"""
        ...

    def Count(self, type):
        """integer = Count(integer type)"""
        ...

    def Test(self, offset):
        """integer = Test(integer offset)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VertexPacketTranslation(object):
    def __init__(self, *args, **kwargs):
        ...

    def Item(self, packet):
        """Item object = Item(pointer packet)"""
        ...

    def Mesh(self, packet):
        """Mesh object = Mesh(pointer packet)"""
        ...

    def Packet(self, vertex, polygon, mesh):
        """pointer = Packet(id vertex,id polygon,object mesh)"""
        ...

    def Polygon(self, packet):
        """id polygon = Polygon(pointer packet)"""
        ...

    def Vertex(self, packet):
        """id vertex = Vertex(pointer packet)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VideoClipItem(object):
    def __init__(self, *args, **kwargs):
        ...

    def AllocFilter(self, attr, cache):
        """ImageFilter object = AllocFilter(object attr,pointer cache)"""
        ...

    def Cleanup(self, cache):
        """Cleanup(pointer cache)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class View(object):
    def __init__(self, *args, **kwargs):
        ...

    def Aspect(self):
        """float = Aspect()"""
        ...

    def Axis(self):
        """integer = Axis()"""
        ...

    def Center(self):
        """vector center = Center()"""
        ...

    def Dimensions(self):
        """(integer w,integer h) = Dimensions()"""
        ...

    def EyeVector(self, pos):
        """(float,vector eye) = EyeVector(vector pos)"""
        ...

    def Focal(self):
        """(float flen,float fdist) = Focal()"""
        ...

    def GridSize(self):
        """float = GridSize()"""
        ...

    def GridSnap(self):
        """float = GridSnap()"""
        ...

    def InvMatrix(self):
        """matrix xfrm = InvMatrix()"""
        ...

    def Matrix(self):
        """matrix xfrm = Matrix()"""
        ...

    def Ortho(self):
        """(integer index,integer spin) = Ortho()"""
        ...

    def PixelScale(self):
        """float = PixelScale()"""
        ...

    def Scale(self):
        """float = Scale()"""
        ...

    def ScreenNormals(self, pos):
        """(vector ax,vector ay,vector az) = ScreenNormals(vector pos)"""
        ...

    def ToModel(self, x, y, snap):
        """vector pos = ToModel(integer x,integer y,integer snap)"""
        ...

    def ToScreen(self, pos):
        """(integer,float x,float y) = ToScreen(vector pos)"""
        ...

    def ToScreen3(self, pos):
        """(integer,vector vp) = ToScreen3(vector pos)"""
        ...

    def Type(self):
        """integer = Type()"""
        ...

    def WorkPlane(self):
        """(integer,vector center) = WorkPlane()"""
        ...

    def Zoom(self):
        """float = Zoom()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class View3D(object):
    def __init__(self, *args, **kwargs):
        ...

    def Angles(self):
        """vector hpb = Angles()"""
        ...

    def Axis(self):
        """(integer,integer cam,vector axis) = Axis()"""
        ...

    def BackdropAspect(self):
        """(integer,float asp) = BackdropAspect()"""
        ...

    def BackdropLook(self):
        """(integer,float brit,float cont,float trns) = BackdropLook()"""
        ...

    def BackdropName(self):
        """string = BackdropName()"""
        ...

    def BackdropOrient(self):
        """(integer,float ang) = BackdropOrient()"""
        ...

    def BackdropPlace(self):
        """(float cx,float cy,float w,float h) = BackdropPlace()"""
        ...

    def BackdropRender(self):
        """(integer,integer resolution,integer blend) = BackdropRender()"""
        ...

    def Bounds(self):
        """(integer x,integer y,integer w,integer h) = Bounds()"""
        ...

    def Center(self):
        """vector center = Center()"""
        ...

    def Deformers(self):
        """Deformers()"""
        ...

    def EyeVector(self):
        """(float,vector pos,vector dir) = EyeVector()"""
        ...

    def FrameRate(self):
        """float = FrameRate()"""
        ...

    def GridSize(self):
        """float = GridSize()"""
        ...

    def InvalidateSurface(self, item):
        """InvalidateSurface(object item)"""
        ...

    def ItemIsVisible(self, item):
        """ItemIsVisible(object item)"""
        ...

    def ItemShade(self, item):
        """integer shade = ItemShade(object item)"""
        ...

    def Matrix(self, inverse):
        """matrix mat = Matrix(integer inverse)"""
        ...

    def PixelSize(self):
        """float = PixelSize()"""
        ...

    def SetCenter(self, vec):
        """SetCenter(vector vec)"""
        ...

    def SetMatrix(self, mat):
        """SetMatrix(matrix mat)"""
        ...

    def SetScale(self, scl):
        """SetScale(float scl)"""
        ...

    def Space(self):
        """integer = Space()"""
        ...

    def Style(self, option):
        """integer = Style(integer option)"""
        ...

    def To3D(self, x, y, flags):
        """vector pos = To3D(float x,float y,integer flags)"""
        ...

    def To3DHit(self, x, y):
        """(vector pos,vector nrm) = To3DHit(float x,float y)"""
        ...

    def ToUVHit(self, name, x, y, layer):
        """(float u,float v) = ToUVHit(string name,float x,float y,integer layer)"""
        ...

    def WorkPlane(self):
        """(integer,vector center) = WorkPlane()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ViewItem3D(object):
    def __init__(self, *args, **kwargs):
        ...

    def Draw(self, chanRead, strokeDraw, selectionFlags, itemColor):
        """Draw(object chanRead,object strokeDraw,integer selectionFlags,vector itemColor)"""
        ...

    def DrawBackground(self, chanRead, strokeDraw, itemColor):
        """DrawBackground(object chanRead,object strokeDraw,vector itemColor)"""
        ...

    def HandleChannel(self, handleIndex):
        """integer chanIndex = HandleChannel(integer handleIndex)"""
        ...

    def HandleCount(self):
        """integer count = HandleCount()"""
        ...

    def HandleMotion(self, handleIndex):
        """(integer handleFlags,float min,float max,vector plane,vector offset) = HandleMotion(integer handleIndex)"""
        ...

    def HandlePositionToValue(self, handleIndex, position):
        """float chanValue = HandlePositionToValue(integer handleIndex,vector position)"""
        ...

    def HandleValueToPosition(self, handleIndex, chanValue):
        """vector position = HandleValueToPosition(integer handleIndex,double[] chanValue)"""
        ...

    def Test(self, chanRead, strokeDraw, selectionFlags, itemColor):
        """Test(object chanRead,object strokeDraw,integer selectionFlags,vector itemColor)"""
        ...

    def WorldSpace(self):
        """boolean = WorldSpace()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class ViewObject(object):
    def __init__(self, *args, **kwargs):
        ...

    def ByIndex(self, type, index):
        """ViewObject object = ByIndex(integer type,integer index)"""
        ...

    def ByView(self, view):
        """ViewObject object = ByView(object view)"""
        ...

    def Count(self, type):
        """integer = Count(integer type)"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def Generate(self, type):
        """Generate(integer type)"""
        ...

    def TestMode(self, type):
        """TestMode(integer type)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VirtualDevice(object):
    def __init__(self, *args, **kwargs):
        ...

    def Date(self):
        """string = Date()"""
        ...

    def Extract(self, dest):
        """Extract(string dest)"""
        ...

    def Initialize(self, path):
        """Initialize(string path)"""
        ...

    def Name(self):
        """string = Name()"""
        ...

    def Scan(self, visitor):
        """Scan(object visitor)"""
        ...

    def Select(self, sub):
        """Select(string sub)"""
        ...

    def Size(self):
        """float bytes = Size()"""
        ...

    def Type(self):
        """integer type = Type()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class VirtualModel(object):
    def __init__(self, *args, **kwargs):
        ...

    def Down(self, vts):
        """Down(object vts)"""
        ...

    def Draw(self, stroke):
        """Draw(object stroke)"""
        ...

    def Flags(self):
        """integer = Flags()"""
        ...

    def Move(self, vts):
        """Move(object vts)"""
        ...

    def Test(self, stroke):
        """Test(object stroke)"""
        ...

    def Tooltip(self, part):
        """string = Tooltip(integer part)"""
        ...

    def Track(self, part):
        """Track(integer part)"""
        ...

    def Up(self, vts):
        """Up(object vts)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Visitor(object):
    def __init__(self, *args, **kwargs):
        ...

    def Evaluate(self):
        """Evaluate()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Voxel(object):
    def __init__(self, *args, **kwargs):
        ...

    def BBox(self):
        """bounds bbox = BBox()"""
        ...

    def FeatureByIndex(self, index):
        """string name = FeatureByIndex(integer index)"""
        ...

    def FeatureCount(self):
        """integer num = FeatureCount()"""
        ...

    def NextPos(self, currentPos, currentSegment, stride):
        """(float segmentList,integer nextSegment,float nextPos) = NextPos(float currentPos,integer currentSegment,float stride)"""
        ...

    def Sample(self, pos, index):
        """float val = Sample(vector pos,integer index)"""
        ...

    def VDBData(self):
        """Unknown object = VDBData()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class Waterfall(object):
    def __init__(self, *args, **kwargs):
        ...

    def Advance(self):
        """Advance()"""
        ...

    def GetWork(self):
        """GetWork()"""
        ...

    def ProcessWork(self):
        """ProcessWork()"""
        ...

    def Spawn(self):
        """Waterfall object = Spawn()"""
        ...

    def State(self):
        """integer = State()"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class WeightMapDeformerItem(object):
    def __init__(self, *args, **kwargs):
        ...

    def GetColor(self, chanRead):
        """vector col = GetColor(object chanRead)"""
        ...

    def GetMapName(self, chanRead):
        """string = GetMapName(object chanRead)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class WorkList(object):
    def __init__(self, *args, **kwargs):
        ...

    def Clear(self):
        """Clear()"""
        ...

    def IsEmpty(self):
        """boolean = IsEmpty()"""
        ...

    def Next(self):
        """pointer = Next()"""
        ...

    def Split(self, mode):
        """WorkList object = Split(integer mode)"""
        ...

    def set(self, source: object) -> bool:
        """bool = set(object source)"""
        ...

    def test(self) -> bool:
        """bool = test()"""
        ...



class storage(object):
    def __init__(self, *args, **kwargs):
        ...

    def get(self):
        """Read out the contents of the buffer as a tuple, either the full length or the specified length"""
        ...

    def offset(self):
        """Set or read the offset in the buffer"""
        ...

    def set(self):
        """Assign a tuple to fill the buffer"""
        ...

    def setSize(self):
        """Set the number of elements in the buffer"""
        ...

    def setType(self):
        """Set the element type for buffer: float, double, int, byte, unsigned, pointer"""
        ...

    def size(self):
        """Return the size of the buffer"""
        ...

    def string(self):
        """Read out the contents of the buffer as a string"""
        ...



def info():
    ...

