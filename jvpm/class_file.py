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

            self.access_flags = self.data[self.offset : self.offset + 2]
            self.offset += 2
            self.this_class = self.data[self.offset : self.offset + 2]
            self.offset += 2
            self.super_class = self.data[self.offset : self.offset + 2]
            self.offset += 2
            self.interfaces_count = self.data[self.offset : self.offset + 2]
            self.offset += 2
            self.interfaces = self.data[self.offset : self.offset + 2]
            # Ask Beaty or Luke: Is this an array of only 2 bytes,
            # or an array of 0+ 2-byte items?
            self.offset += 2
            
            self.fields_count = self.data[self.offset : self.offset + 2]
            self.offset += 2
            self.fields_begin = self.offset
            self.fields = get_info(self, self.fields_count)

            self.methods_count = self.data[self.offset : self.offset + 2]
            self.offset += 2
            self.methods_begin = self.offset
            self.methods = get_info(self, self.methods_count)

            self.class_attributes_count = (self.data[self.offset] << 8) + self.data[self.offset + 1]
            self.offset += 1
            self.class_attributes = get_attributes(self, self.class_attributes_count)

def get_constant_pool(self):
    tag_table = {
        1: {'type': 'utf-8', 'default_size': 3, 'value': get_extended(self).decode('utf-8')},
        3: {'type': 'Integer',  'default_size': 5, 'value': numpy.int32(get_u4(self))},
        4: {'type': 'Float', 'default_size': 5, 'value': numpy.float32(get_u4(self))},
        5: {'type': 'Long', 'default_size': 9, 'value': numpy.int64(get_u8(self))},
        6: {'type': 'Double', 'default_size': 9, 'value': numpy.float64(get_u8(self))},
        7: {'type': 'Class', 'default_size': 3, 'name_index': int(get_u2(self))},
        8: {'type': 'String', 'default_size': 3, 'string_index': int(get_u2(self))},
        9: {'type': 'Fieldref', 'default_size': 5, 'class_index': int(get_u2(self)), 'name_and_type_index': int(get_u2(self))},
        10: {'type': 'Methodref', 'default_size': 5, 'class_index': int(get_u2(self)), 'name_and_type_index': int(get_u2(self))},
        11: {'type': 'InterfaceMethodref', 'default_size': 5, 'class_index': int(get_u2(self)), 'name_and_type_index': int(get_u2(self))},
        12: {'type': 'NameAndType', 'default_size': 5, 'name_index': int(get_u2(self)), 'descriptor_index': int(get_u2(self))},
        15: {'type': 'MethodHandle', 'default_size': 4, 'reference_kind': int(get_u1(self)), 'reference_index': int(get_u2(self))},
        16: {'type': 'MethodType', 'default_size': 3, 'descriptor_index': int(get_u2(self))},
        18: {'type': 'InvokeDynamic', 'default_size': 5, 'bootstrap_method_attr_index': int(get_u2(self)), 'name_and_type_index': int(get_u2(self))}
    }
    pool = {0: []}
    pool[0] = (self.data[8] << 8) + self.data[9]
    for index in range(1, pool[0] - 1):
        tag = (self.data[self.offset])
        #const_size = tag_table[tag]['default_size']
        #if tag == 1:
        #    const_size += (self.data[self.offset + 1] << 8) + self.data[self.offset + 2]
        #constant = self.data[self.offset + 1 : self.offset + const_size]
        #self.offset += const_size
        #if tag in [5,6]:
        #    index += 1
    return pool
    
def get_info(self, count):
    info = {0: {'values_count': count} }
    for val in range(1, count):
        info[val]['access_flags'] = self.data[self.offset : self.offset + 2]
        self.offset += 2
        info[val]['name_index'] = self.data[self.offset : self.offset + 2]
        self.offset += 2
        info[val]['descriptor_index'] = self.data[self.offset : self.offset + 2]
        self.offset += 2
        info[val]['attributes_count'] = self.data[self.offset : self.offset + 2]
        self.offset += 2
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
    attribute['num_bytes'] = 0
    attribute['name_index'] = (self.data[self.offset] << 8) + self.data[self.offset + 1]
    attribute['num_bytes'] += 2
    attribute['length'] = (self.data[self.offset + bytes] << 24) + (self.data[self.offset + bytes + 1] << 16) + (self.data[self.offset + bytes + 2] << 8) + self.data[self.offset + bytes + 3]
    attribute['num_bytes'] += 4
    attribute['info'] = self.data[self.offset + bytes : self.offset + bytes + self.length]
    attribute['num_bytes'] += attribute['length']
    self.offset += attribute['num_bytes']
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

def get_extended(self):
    length = (int(self.data[self.offset] << 8) + self.data[self.offset + 1])
    value = self.data[self.offset + 2 : self.offset + length]
    self.offset += 2 + length
    return value
