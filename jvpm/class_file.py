import numpy

class ClassFile():
    """This class reads in a Java .class file and parses its values"""
    def __init__(self, name):
        """this is the constructor"""
        with open(name, 'rb') as binary_file:
            self.data = binary_file.read()
            self.run_code = []
            self.magic = self.data[0:4]
            self.minor = self.data[4:6]
            self.major = self.data[6:8]
            self.pool_count = self.data[8:10]
            self.offset = 10
            
            self.cp_begin = self.offset
            self.constant_pool = get_constant_pool(self)

            self.access_flags = get_u2(self)
            self.this_class = get_u2(self)
            self.super_class = get_u2(self)
            self.interfaces_count = get_u2(self)
            self.interfaces = get_u2(self)
            # Ask Beaty or Luke: Is this an array of only 2 bytes,
            # or an array of 0+ 2-byte items?
            
            self.fields_count = get_u2(self)
            self.fields_begin = self.offset
            self.fields = get_info(self, self.fields_count)

            self.methods_count = get_u2(self)
            self.methods_begin = self.offset
            self.methods = get_info(self, self.methods_count)

            self.class_attributes_count = get_u2(self)
            self.class_attributes = get_attributes(self, self.class_attributes_count)

def get_constant_pool(self):
    tag_table = {
        1: {'type': 'utf-8', 'value': get_extended(self).decode('utf-8')},
        3: {'type': 'Integer',  'value': numpy.int32(get_u4(self))},
        4: {'type': 'Float', 'value': numpy.float32(get_u4(self))},
        5: {'type': 'Long', 'value': numpy.int64(get_u8(self))},
        6: {'type': 'Double', 'value': numpy.float64(get_u8(self))},
        7: {'type': 'Class', 'name_index': int(get_u2(self))},
        8: {'type': 'String', 'string_index': int(get_u2(self))},
        9: {'type': 'Fieldref', 'class_index': int(get_u2(self)), 'name_and_type_index': int(get_u2(self))},
        10: {'type': 'Methodref', 'class_index': int(get_u2(self)), 'name_and_type_index': int(get_u2(self))},
        11: {'type': 'InterfaceMethodref', 'class_index': int(get_u2(self)), 'name_and_type_index': int(get_u2(self))},
        12: {'type': 'NameAndType', 'name_index': int(get_u2(self)), 'descriptor_index': int(get_u2(self))},
        15: {'type': 'MethodHandle', 'reference_kind': int(get_u1(self)), 'reference_index': int(get_u2(self))},
        16: {'type': 'MethodType', 'descriptor_index': int(get_u2(self))},
        18: {'type': 'InvokeDynamic', 'bootstrap_method_attr_index': int(get_u2(self)), 'name_and_type_index': int(get_u2(self))}
    }
    pool = {0: []}
    pool[0] = (self.data[8] << 8) + self.data[9]
    for index in range(1, pool[0] - 1):
        tag = int.from_bytes(get_u1(self), byteorder='big')
        constant = tag_table[tag]
        for aspect in constant:
            aspect
        if tag in [5,6]:
            index += 1
    return pool
    
def get_info(self, count):
    info = {0: {'values_count': count} }
    for val in range(1, count):
        info[val]['access_flags'] = get_u2(self)
        info[val]['name_index'] = get_u2(self)
        info[val]['descriptor_index'] = get_u2(self)
        info[val]['attributes_count'] = get_u2(self)
        info[val]['attributes'] = get_attributes(self, info[val]['attributes_count'])
    return info

def get_attributes(self, count):
    attributes = []
    attributes[0] = 0
    for attr in range(1, count):
        attributes[attr] = get_an_attribute(self)
        attributes[0] += attributes[len(attributes)]['bytes']
    return attributes

def get_an_attribute(self):
    attribute = {}
    attribute['name_index'] = get_u2(self)
    attribute['length'] = get_u4(self)
    attribute['info'] = get_extended(self, length=attribute['length'])
    # # WANGLE OUT CODE ATTRIBUTES
    return attribute

def get_u1(self):
    value =self.data[self.offset]
    self.offset += 1
    return value

def get_u2(self):
    value = (self.data[self.offset] << 8) + self.data[self.offset + 1]
    self.offset += 2
    return value

def get_u4(self):
    value = (self.data[self.offset] << 24) + (self.data[self.offset + 1] << 16) + (self.data[self.offset + 2] << 8) + self.data[self.offset + 3]
    self.offset += 4
    return value

def get_u8(self):
    value = (self.data[self.offset] << 56) + (self.data[self.offset + 1] << 48) + (self.data[self.offset + 2] << 40) + (self.data[self.offset + 3] << 32) + (self.data[self.offset + 4] << 24) + (self.data[self.offset + 5] << 16) + (self.data[self.offset + 6] << 8) + self.data[self.offset + 7]
    self.offset += 8
    return value

def get_extended(self, length=0):
    if not length:
        length = get_u2(self)
    value = self.data[self.offset : self.offset + length]
    self.offset += length
    return value
