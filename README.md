# IronBuffer
Small simple reliable java like ```ByteBuffer```  
Written to be as simple and performant as possible
If you are not familiar with the java ```ByteBuffer``` i highly encourage you to read this documentation or to refer to in when needed

# Installation
To install run ```pip install git+https://github.com/IRONALEKS/IronBuffer.git```

## Example
```python
buffer = ByteBuffer.createBufferWithSize(30)
#position: 0, limit: 30
buffer.insert_UINT_8(100)       #takes up 1 byte
#position: 1, limit: 30
buffer.insert_BOOL(True)        #takes up 1 byte
#position: 2, limit: 30
buffer.insert_UINT_64(1000000)  #takes up 8 bytes
#position: 10, limit: 30
buffer.insert_FLOAT(1.2345)     #takes up 4 bytes
#position: 14, limit: 30
buffer.insert_DOUBLE(2.3456789) #takes up 8 bytes
#position: 22, limit: 30

buffer.flip()
#position: 0, limit: 22

print(buffer.extract_UINT_8() #prints 100
#position: 1, limit: 22
print(buffer.extract_BOOL() #prints True
#position: 2, limit: 22
print(buffer.extract_UINT_64() #prints 1000000
#position: 10, limit: 22
print(buffer.extract_FLOAT() #prints ~1.2345
#position: 14, limit: 22
print(buffer.extract_DOUBLE() #prints ~2.3456789
#position: 22, limit: 22

buffer.clear() #resets buffer
#position: 0, limit: 30

buffer.insert_UINT_8(100) #takes up 1 byte
#position: 1, limit: 30

buffer.flip()
#position: 0, limit: 1


#You can peek data with peek_ functions, it will do the same thing as extract_ except it will not change the current position
print(buffer.peek_UINT_8())
#position: 0, limit: 1

#You can remove data with remove functions, it will do the same thing as extract_ except it will not return the data
buffer.remove_UINT_8()
#position: 1, limit: 1

#You can set and get data in the whole buffer no matter where the position and limit are with set_ and get_ functions without affecting the position and the limit
buffer.set_UINT_(10, 100)
buffer.set_UINT_(10) #prints 100
```

# Usage

## Intro
Everything in the ```ByteBuffer``` is stored in big-endian, for now there i have no plan to add little-endian support, anyone is welcome to create a pull request with the functionality

A ```ByteBuffer``` has three variables(the fourth memoryview is only for performance):  
* The buffer itself(```bytearray```)  
* The position(```int```)  
* The limit(```int```)


When creating a ```ByteBuffer``` the position will be set 0 and the limit will be set to the capacity(the size of the internal ```bytearray```)

## Import
```python
from IronBuffer.ByteBuffer import ByteBuffer
```

## Creation
To create a ```ByteBuffer``` you can use the constructor/```__init__``` which takes a ```bytearray``` as argument  
But the recommended way to create a ```ByteBuffer``` is to use it's static functions
```python
ByteBuffer.createBufferEmpty() -> ByteBuffer
ByteBuffer.createBufferWithSize(size: int) -> ByteBuffer
ByteBuffer.createBufferFromByteArray(buffer: bytearray) -> ByteBuffer
ByteBuffer.createBufferFromMemoryView(buffer: memoryview) -> ByteBuffer
ByteBuffer.createBufferFromBytes(buffer: bytes) -> ByteBuffer
```




## Constants
You can use a lot of useful constants that have the prefix CONST:
```python
ByteBuffer.CONST_BITS_IN_BYTE: int = 8
```

### Minimum and maximum value for data types
```python
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
```python
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
```python
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

### General functionality
To set and get the current position in the buffer
```python
  ByteBuffer.setPosition(position: int)
  ByteBuffer.getPosition() -> int
```
To set and get the current limit in the buffer
```python
  ByteBuffer.setLimit(limit: int)
  ByteBuffer.getLimit() -> int
```
