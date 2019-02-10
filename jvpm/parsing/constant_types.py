#this file contains all classes that represent the types of constants discussed in section 4.4 of the java language specification (relating to the constant pool of the class file format)
#the class Constant is the class from which all constant types will derive
class Constant:
    def __init__(self):
        pass
class ConstClass(Constant):
    def __init__(self,name_index):
        self.name_index = name_index
class ConstFieldRef(Constant):
    def __init__(self,class_index,name_and_type_index):
        self.class_index = class_index
        self.name_and_type_index = name_and_type_index
class ConstMethodRef(Constant):
    def __init__(self,class_index,name_and_type_index):
        self.class_index = class_index
        self.name_and_type_index = name_and_type_index
class ConstInterfaceMethodRef(Constant):
    def __init__(self,class_index,name_and_type_index):
        self.class_index = class_index
        self.name_and_type_index = name_and_type_index
class ConstString(Constant):
    def __init__(self,string_index):
        self.string_index = string_index
class ConstInteger(Constant):
    def __init__(self,chars): #I'm doing this to avoid potential name conflicts with the python bytes type
        self.chars = chars
class ConstFloat(Constant):
    def __init__(self,chars):
        self.chars = chars
class ConstLong(Constant):
    def __init__(self,high_bytes,low_bytes):
        self.high_bytes = high_bytes
        self.low_bytes = low_bytes
class ConstDouble(Constant):
    def __init__(self,high_bytes,low_bytes):
        self.high_bytes = high_bytes
        self.low_bytes = low_bytes
class ConstNameAndType(Constant):
    def __init__(self,name_index,descriptor_index):
        self.name_index = name_index
        self.descriptor_index = descriptor_index
class ConstUtf8(Constant):
    def __init__(self,length,chars):
        self.length = length
        self.chars = chars
class ConstMethodHandle(Constant):
    def __init__(self, reference_kind, reference_index):
        self.reference_kind = reference_kind
        self.reference_index = reference_index
class ConstMethodType(Constant):
    def __init__(self,descriptor_index):
        self.descriptor_index = descriptor_index
class ConstInvokeDynamic(Constant):
    def __init__(self,bootstrap_method_attr_index,name_and_type_index):
        self.bootstrap_method_attr_index = bootstrap_method_attr_index
        self.name_and_type_index = name_and_type_index
