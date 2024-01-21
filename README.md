# IronBuffer
Small simple reliable java like ```ByteBuffer```  
Written to be as simple and performant as possible

# Installation
To install run ```pip install git+https://github.com/IRONALEKS/IronBuffer.git```

# Usage

## Intro
A ByteBuffer has three variables(the fourth memoryview is only for performance):  
* The buffer itself(```bytearray```)  
* The position(```int```)  
* The limit(```int```)

When creating a ```ByteBuffer``` the position will be set 0 and the limit will be set to the capacity(the size of the internal ```bytearray```)  

## Import
To import ```from IronBuffer.ByteBuffer import ByteBuffer```

## Creation
To create a ```ByteBuffer``` you can use the constructor/```__init__``` which takes a ```bytearray``` as argument  
But the recommended way to create a ```ByteBuffer``` is to use it's static functions
```
ByteBuffer.createBufferEmpty() -> ByteBuffer
ByteBuffer.createBufferWithSize(size: int) -> ByteBuffer
ByteBuffer.createBufferFromByteArray(buffer: bytearray) -> ByteBuffer
ByteBuffer.createBufferFromMemoryView(buffer: memoryview) -> ByteBuffer
ByteBuffer.createBufferFromBytes(buffer: bytes) -> ByteBuffer
```




## Constants
You can use a lot of useful constants that have the prefix CONST:
```ByteBuffer.CONST_BITS_IN_BYTE: int = 8```

### Minimum and maximum value for data types
```
ByteBuffer.CONST_UINT_8_MIN: int = 0
ByteBuffer.CONST_UINT_8_MAX: int = 255
ByteBuffer.CONST_INT_8_MIN: int  = -128
ByteBuffer.CONST_INT_8_MAX: int  = 127


ByteBuffer.CONST_UINT_16_MIN: int = 0
ByteBuffer.CONST_UINT_16_MAX: int = 65535
ByteBuffer.CONST_INT_16_MIN: int  = -32768
ByteBuffer.CONST_INT_16_MAX: int  = 32767


ByteBuffer.CONST_UINT_32_MIN: int = 0
ByteBuffer.CONST_UINT_32_MAX: int = 4294967295
ByteBuffer.CONST_INT_32_MIN: int  = -2147483648
ByteBuffer.CONST_INT_32_MAX: int  = 2147483647

ByteBuffer.CONST_UINT_64_MIN: int  = 0
ByteBuffer.CONST_UINT_64_MAX: int  = 18446744073709551615
ByteBuffer.CONST_INT_64_MIN: int   = -9223372036854775808
ByteBuffer.CONST_INT_64_MAX: int   = 9223372036854775807
```

### Amount of values that a data type can store
```
ByteBuffer.CONST_UINT_8_VALUES_COUNT: int  = 256
ByteBuffer.CONST_INT_8_VALUES_COUNT: int   = 256

ByteBuffer.CONST_UINT_16_VALUES_COUNT: int = 65536
ByteBuffer.CONST_INT_16_VALUES_COUNT: int  = 65536

ByteBuffer.CONST_UINT_32_VALUES_COUNT: int = 4294967296
ByteBuffer.CONST_INT_32_VALUES_COUNT: int  = 4294967296

ByteBuffer.CONST_UINT_64_VALUES_COUNT: int = 18446744073709551616
ByteBuffer.CONST_INT_64_VALUES_COUNT: int  = 18446744073709551616
```

### Data type sizes in bytes
```
ByteBuffer.CONST_UINT_8_SIZE: int  = 1
ByteBuffer.CONST_INT_8_SIZE: int   = 1

ByteBuffer.CONST_UINT_16_SIZE: int = 2
ByteBuffer.CONST_INT_16_SIZE: int  = 2

ByteBuffer.CONST_UINT_32_SIZE: int = 4
ByteBuffer.CONST_INT_32_SIZE: int  = 4

ByteBuffer.CONST_UINT_64_SIZE: int = 8
ByteBuffer.CONST_INT_64_SIZE: int  = 8

ByteBuffer.CONST_FLOAT_SIZE: int   = 4

ByteBuffer.CONST_DOUBLE_SIZE: int  = 8
```
