from __future__ import annotations
from struct import Struct

class ByteBuffer:
    CONST_BITS_IN_BYTE: int = 8


    CONST_UINT_8_MIN: int = 0
    CONST_UINT_8_MAX: int = 255
    CONST_INT_8_MIN: int  = -128
    CONST_INT_8_MAX: int  = 127

    CONST_UINT_8_SIZE: int = 1
    CONST_INT_8_SIZE: int  = 1

    CONST_UINT_8_VALUES_COUNT: int = 256
    CONST_INT_8_VALUES_COUNT: int  = 256


    CONST_UINT_16_MIN: int = 0
    CONST_UINT_16_MAX: int = 65535
    CONST_INT_16_MIN: int  = -32768
    CONST_INT_16_MAX: int  = 32767

    CONST_UINT_16_SIZE: int = 2
    CONST_INT_16_SIZE: int  = 2

    CONST_UINT_16_VALUES_COUNT: int = 65536
    CONST_INT_16_VALUES_COUNT: int  = 65536


    CONST_UINT_32_MIN: int = 0
    CONST_UINT_32_MAX: int = 4294967295
    CONST_INT_32_MIN: int  = -2147483648
    CONST_INT_32_MAX: int  = 2147483647

    CONST_UINT_32_SIZE: int = 4
    CONST_INT_32_SIZE: int  = 4

    CONST_UINT_32_VALUES_COUNT: int = 4294967296
    CONST_INT_32_VALUES_COUNT: int  = 4294967296

    CONST_UINT_64_MIN: int  = 0
    CONST_UINT_64_MAX: int  = 18446744073709551615
    CONST_INT_64_MIN: int   = -9223372036854775808
    CONST_INT_64_MAX: int   = 9223372036854775807


    CONST_UINT_64_SIZE: int = 8
    CONST_INT_64_SIZE: int  = 8

    CONST_UINT_64_VALUES_COUNT: int = 18446744073709551616
    CONST_INT_64_VALUES_COUNT: int  = 18446744073709551616

    CONST_FLOAT_SIZE: int   = 4
    CONST_DOUBLE_SIZE: int  = 8



    converterUINT16: Struct = Struct('>H')
    converterINT16: Struct  = Struct('>h')

    converterUINT32: Struct = Struct('>I')
    converterINT32: Struct  = Struct('>i')

    converterUINT64: Struct = Struct('>Q')
    converterINT64: Struct  = Struct('>q')

    converterFloat: Struct  = Struct('>f')
    converterDouble: Struct = Struct('>d')



    buffer:           bytearray
    bufferMemoryView: memoryview
    position: int
    limit:    int



    def __init__(self, buffer: bytearray):
        self.buffer           = buffer
        self.bufferMemoryView = memoryview(self.buffer)

        self.position = 0
        self.limit    = 0

        self.clear()
    
    @staticmethod
    def createBufferEmpty() -> ByteBuffer:
        return ByteBuffer(bytearray())
    
    @staticmethod
    def createBufferWithSize(size: int) -> ByteBuffer:
        return ByteBuffer(bytearray(size))
    
    @staticmethod
    def createBufferFromByteArray(buffer: bytearray) -> ByteBuffer:
        return ByteBuffer(buffer)
    
    @staticmethod
    def createBufferFromMemoryView(buffer: memoryview) -> ByteBuffer:
        return ByteBuffer(bytearray(buffer))
    
    @staticmethod
    def createBufferFromBytes(buffer: bytes) -> ByteBuffer:
        return ByteBuffer(bytearray(buffer))
    


    def getCapacity(self) -> int:
        return len(self.buffer)
    

    def setPosition(self, position: int):
        # assert position <= self.getLimit()
        self.position = position
    
    def getPosition(self) -> int:
        return self.position


    def setLimit(self, limit: int):
        # assert limit <= self.getCapacity()
        self.limit = limit

    def getLimit(self) -> int:
        return self.limit


    def hasRemaining(self) -> bool:
        return self.getRemaining() > 0

    def getRemaining(self) -> int:
        return self.getLimit() - self.getPosition()
    
    def getRemainingMemoryView(self) -> memoryview:
        return self.bufferMemoryView[self.getPosition():self.getPosition()+self.getRemaining()]



    def clear(self):
        self.setPosition(0)
        self.setLimit(self.getCapacity())

    def flip(self):
        position = self.getPosition()

        self.setPosition(0)
        self.setLimit(position)
    
    def rewing(self):
        self.setPosition(0)
    
    def compact(self):
        remaining = self.getRemaining()
        
        if remaining > 0:
            position = self.getPosition()

            if position != 0:
                self.bufferMemoryView[0:remaining] = self.bufferMemoryView[position:position + remaining]

        self.setPosition(remaining)
        self.setLimit(self.getCapacity())

    def insertBuffer(self, buffer: ByteBuffer):
        thisPosition  = self.getPosition()
        thisRemaining = self.getRemaining()
        
        bufferPosition  = buffer.getPosition()
        bufferRemaining = buffer.getRemaining()
        
        bytesToCopy = min(thisRemaining, bufferRemaining)
        
        if bytesToCopy > 0:
            self.bufferMemoryView[thisPosition:thisPosition+bytesToCopy] = buffer.bufferMemoryView[bufferPosition:bufferPosition+bytesToCopy]
            
            self.setPosition(thisPosition + bytesToCopy)
            buffer.setPosition(bufferPosition + bytesToCopy)
    

    
    def set_UINT_8(self, position: int, uint_8: int):
        self.buffer[position] = uint_8

    def get_UINT_8(self, position: int) -> int:
        return self.buffer[position]
    
    def insert_UINT_8(self, uint_8: int):
        self.set_UINT_8(self.getPosition(), uint_8)
        self.setPosition(self.getPosition() + ByteBuffer.CONST_UINT_8_SIZE)
    
    def extract_UINT_8(self) -> int:
        result = self.peek_UINT_8()
        self.remove_UINT_8()

        return result
    
    def peek_UINT_8(self) -> int:
        return self.get_UINT_8(self.getPosition())
    
    def remove_UINT_8(self):
        self.setPosition(self.getPosition() + ByteBuffer.CONST_UINT_8_SIZE)
        

    def set_INT_8(self, position: int, int_8: int):
        self.buffer[position] = int_8 + (-ByteBuffer.CONST_INT_8_MIN)

    def get_INT_8(self, position: int) -> int:
        return self.buffer[position] + ByteBuffer.CONST_INT_8_MIN
    
    def insert_INT_8(self, int_8: int):
        self.set_INT_8(self.getPosition(), int_8)
        self.setPosition(self.getPosition() + ByteBuffer.CONST_INT_8_SIZE)
    
    def extract_INT_8(self) -> int:
        result = self.peek_INT_8()
        self.remove_INT_8()

        return result
    
    def peek_INT_8(self) -> int:
        return self.get_INT_8(self.getPosition())
    
    def remove_INT_8(self):
        self.setPosition(self.getPosition() + ByteBuffer.CONST_INT_8_SIZE)
    


    def set_UINT_16(self, position: int, uint_16: int):
        ByteBuffer.converterUINT16.pack_into(self.buffer, position, uint_16)

    def get_UINT_16(self, position: int) -> int:
        return ByteBuffer.converterUINT16.unpack_from(self.buffer, position)[0]

    def insert_UINT_16(self, uint_16: int):
        self.set_UINT_16(self.getPosition(), uint_16)
        self.setPosition(self.getPosition() + ByteBuffer.CONST_UINT_16_SIZE)
    
    def extract_UINT_16(self) -> int:
        result = self.peek_UINT_16()
        self.remove_UINT_16()

        return result
    
    def peek_UINT_16(self) -> int:
        return self.get_UINT_16(self.getPosition())
    
    def remove_UINT_16(self):
        self.setPosition(self.getPosition() + ByteBuffer.CONST_UINT_16_SIZE)
    

    def set_INT_16(self, position: int, int_16: int):
        ByteBuffer.converterINT16.pack_into(self.buffer, position, int_16)

    def get_INT_16(self, position: int) -> int:
        return ByteBuffer.converterINT16.unpack_from(self.buffer, position)[0]

    def insert_INT_16(self, int_16: int):
        self.set_INT_16(self.getPosition(), int_16)
        self.setPosition(self.getPosition() + ByteBuffer.CONST_INT_16_SIZE)
    
    def extract_INT_16(self) -> int:
        result = self.peek_INT_16()
        self.remove_INT_16()

        return result
    
    def peek_INT_16(self) -> int:
        return self.get_INT_16(self.getPosition())
    
    def remove_INT_16(self):
        self.setPosition(self.getPosition() + ByteBuffer.CONST_INT_16_SIZE)
    


    def set_UINT_32(self, position: int, uint_32: int):
        ByteBuffer.converterUINT32.pack_into(self.buffer, position, uint_32)

    def get_UINT_32(self, position: int) -> int:
        return ByteBuffer.converterUINT32.unpack_from(self.buffer, position)[0]

    def insert_UINT_32(self, uint_32: int):
        self.set_UINT_32(self.getPosition(), uint_32)
        self.setPosition(self.getPosition() + ByteBuffer.CONST_UINT_32_SIZE)
    
    def extract_UINT_32(self) -> int:
        result = self.peek_UINT_32()
        self.remove_UINT_32()

        return result
    
    def peek_UINT_32(self) -> int:
        return self.get_UINT_32(self.getPosition())
    
    def remove_UINT_32(self):
        self.setPosition(self.getPosition() + ByteBuffer.CONST_UINT_32_SIZE)
    

    def set_INT_32(self, position: int, int_32: int):
        ByteBuffer.converterINT32.pack_into(self.buffer, position, int_32)

    def get_INT_32(self, position: int) -> int:
        return ByteBuffer.converterINT32.unpack_from(self.buffer, position)[0]

    def insert_INT_32(self, int_32: int):
        self.set_INT_32(self.getPosition(), int_32)
        self.setPosition(self.getPosition() + ByteBuffer.CONST_INT_32_SIZE)
    
    def extract_INT_32(self) -> int:
        result = self.peek_INT_32()
        self.remove_INT_32()

        return result
    
    def peek_INT_32(self) -> int:
        return self.get_INT_32(self.getPosition())
    
    def remove_INT_32(self):
        self.setPosition(self.getPosition() + ByteBuffer.CONST_INT_32_SIZE)
    


    def set_UINT_64(self, position: int, uint_64: int):
        ByteBuffer.converterUINT64.pack_into(self.buffer, position, uint_64)

    def get_UINT_64(self, position: int) -> int:
        return ByteBuffer.converterUINT64.unpack_from(self.buffer, position)[0]

    def insert_UINT_64(self, uint_64: int):
        self.set_UINT_64(self.getPosition(), uint_64)
        self.setPosition(self.getPosition() + ByteBuffer.CONST_UINT_64_SIZE)
    
    def extract_UINT_64(self) -> int:
        result = self.peek_UINT_64()
        self.remove_UINT_64()

        return result
    
    def peek_UINT_64(self) -> int:
        return self.get_UINT_64(self.getPosition())
    
    def remove_UINT_64(self):
        self.setPosition(self.getPosition() + ByteBuffer.CONST_UINT_64_SIZE)
    

    def set_INT_64(self, position: int, int_64: int):
        ByteBuffer.converterINT64.pack_into(self.buffer, position, int_64)

    def get_INT_64(self, position: int) -> int:
        return ByteBuffer.converterINT64.unpack_from(self.buffer, position)[0]

    def insert_INT_64(self, int_64: int):
        self.set_INT_64(self.getPosition(), int_64)
        self.setPosition(self.getPosition() + ByteBuffer.CONST_INT_64_SIZE)
    
    def extract_INT_64(self) -> int:
        result = self.peek_INT_64()
        self.remove_INT_64()

        return result
    
    def peek_INT_64(self) -> int:
        return self.get_INT_64(self.getPosition())
    
    def remove_INT_64(self):
        self.setPosition(self.getPosition() + ByteBuffer.CONST_INT_64_SIZE)
    


    def set_FLOAT(self, position: int, number: float):
        ByteBuffer.converterFloat.pack_into(self.buffer, position, number)

    def get_FLOAT(self, position: int) -> float:
        return ByteBuffer.converterFloat.unpack_from(self.buffer, position)[0]

    def insert_FLOAT(self, number: float):
        self.set_FLOAT(self.getPosition(), number)
        self.setPosition(self.getPosition() + ByteBuffer.CONST_FLOAT_SIZE)
    
    def extract_FLOAT(self) -> float:
        result = self.peek_FLOAT()
        self.remove_FLOAT()

        return result
    
    def peek_FLOAT(self) -> float:
        return self.get_FLOAT(self.getPosition())
    
    def remove_FLOAT(self):
        self.setPosition(self.getPosition() + ByteBuffer.CONST_FLOAT_SIZE)
    


    def set_DOUBLE(self, position: int, number: float):
        ByteBuffer.converterDouble.pack_into(self.buffer, position, number)

    def get_DOUBLE(self, position: int) -> float:
        return ByteBuffer.converterDouble.unpack_from(self.buffer, position)[0]

    def insert_DOUBLE(self, number: float):
        self.set_DOUBLE(self.getPosition(), number)
        self.setPosition(self.getPosition() + ByteBuffer.CONST_DOUBLE_SIZE)
    
    def extract_DOUBLE(self) -> float:
        result = self.peek_DOUBLE()
        self.remove_DOUBLE()

        return result
    
    def peek_DOUBLE(self) -> float:
        return self.get_DOUBLE(self.getPosition())
    
    def remove_DOUBLE(self):
        self.setPosition(self.getPosition() + ByteBuffer.CONST_DOUBLE_SIZE)
    


    def set_BOOL(self, position: int, value: bool):
        if value is True:
            self.set_UINT_8(position, 1)
        else:
            self.set_UINT_8(position, 0)

    def get_BOOL(self, position: int) -> bool:
        result = self.get_UINT_8(position)
        
        if result == 1:
            return True
        else:
            return False

    def insert_BOOL(self, value: bool):
        if value is True:
            self.insert_UINT_8(1)
        else:
            self.insert_UINT_8(0)
    
    def extract_BOOL(self) -> bool:
        result = self.extract_UINT_8()
        
        if result == 1:
            return True
        else:
            return False
    
    def peek_BOOL(self) -> bool:
        result = self.peek_UINT_8()
        
        if result == 1:
            return True
        else:
            return False
    
    def remove_BOOL(self):
        self.remove_UINT_8()
    


    def set_BYTEARRAY(self, position: int, array: bytearray):
        self.bufferMemoryView[position:position+len(array)] = array

    def get_BYTEARRAY(self, position: int, length: int) -> bytearray:
        return self.buffer[position:position+length]

    def insert_BYTEARRAY(self, array: bytearray):
        self.set_BYTEARRAY(self.getPosition(), array)
        self.setPosition(self.getPosition() + len(array))
    
    def extract_BYTEARRAY(self, length: int) -> bytearray:
        result = self.peek_BYTEARRAY(length)
        self.remove_BYTEARRAY(length)

        return result
    
    def peek_BYTEARRAY(self, length: int) -> bytearray:
        return self.get_BYTEARRAY(self.getPosition(), length)
    
    def remove_BYTEARRAY(self, length: int):
        self.setPosition(self.getPosition() + length)
    


    def set_BYTES(self, position: int, array: bytes):
        self.bufferMemoryView[position:position+len(array)] = array

    def get_BYTES(self, position: int, length: int) -> bytes:
        return bytes(self.buffer[position:position+length])

    def insert_BYTES(self, array: bytes):
        self.set_BYTES(self.getPosition(), array)
        self.setPosition(self.getPosition() + len(array))
    
    def extract_BYTES(self, length: int) -> bytes:
        result = self.peek_BYTES(length)
        self.remove_BYTES(length)

        return result
    
    def peek_BYTES(self, length: int) -> bytes:
        return self.get_BYTES(self.getPosition(), length)
    
    def remove_BYTES(self, length: int):
        self.setPosition(self.getPosition() + length)

        

    def copyBytes(self) -> bytes:
        return self.copyBytesAbsolute(self.getPosition(), self.getRemaining())
    
    def copyBytesAbsolute(self, position: int, length: int) -> bytes:
        return self.get_BYTES(position, length)
    

    def copyByteArray(self) -> bytearray:
        return self.copyByteArrayAbsolute(self.getPosition(), self.getRemaining())
    
    def copyByteArrayAbsolute(self, position: int, length: int) -> bytearray:
        return self.get_BYTEARRAY(position, length)
    

    def copyBuffer(self) -> ByteBuffer:
        return self.copyBufferAbsolute(self.getPosition(), self.getRemaining())
    
    def copyBufferAbsolute(self, position: int, length: int) -> ByteBuffer:
        return ByteBuffer.createBufferFromByteArray(self.copyByteArrayAbsolute(position, length))




    def __str__(self) -> str:
        return 'Capacity: {capacity} Remaining: {remaining} Position: {position} Limit: {limit} '.format(capacity=self.getCapacity(), remaining=self.getRemaining(), position=self.getPosition(), limit=self.getLimit())