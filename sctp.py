# UDP
hex_stream = ['13','55','b6','76','79','88','29','5e','00','00','00','00','00','03','00','34',
                '7e','58','1e','36','00','00',',00','00','00','00','00','00']
scale =16


def decode_nibble(nibble_string):
    '''This function decodes a string of nibbles
        Returns the byte stream'''
    binary_string = ''
    
    for i in nibble_string:
        b_s = str(bin(int('0x'+i,scale)))[2:].zfill(4)
        # padd the left with zeros
        
        binary_string += b_s
    
    
    return binary_string

def extract_nibbles(a,b):
    ''' This function extracts the appropriate nibble string
         Returns: The nibble string'''
    source_string = ''      
    for i in range(a,b):
        source_string +=hex_stream[i]
    
    return source_string

# Extract the first 16 bits, i.e 2 nibbles, 16 bits
Source_Port = decode_nibble(extract_nibbles(0,2))
print(f"Source Port: {int(Source_Port,2)}")


# Extract the corresponding 2 nibbles. 16 bits
destination_port = decode_nibble(extract_nibbles(2,4))
print(f"Dest_port: {int(destination_port,2)}")

# Verification tag: used by the receiver to validate the sender of the sctp packet: 32 bits
# During transmit, its value = Initiate Tag received from peer endpoint during the association initialization
ver_tag = decode_nibble(extract_nibbles(4,8))
print(f"verification_tag: {int(ver_tag,2)}")

# Checksum Contains the checksum of the sctp packet 32 bits
checksum = decode_nibble(extract_nibbles(8,12))
print(f"CheckSum: {int(checksum,2)}")


# CHUNK TYPE : 8 bits
chunk_type = decode_nibble(extract_nibbles(12,13))
print(f"Chunk_Type: {int(chunk_type,2)}")
print('This signifies a payload data chunk type\n')

# Chunk Flag: depends on the Chunk type: 8 bits
chunk_flag = decode_nibble(extract_nibbles(13,14))
print(f"Chunk_Flags: {chunk_flag}")

# chunk length;
chunk_length = decode_nibble(extract_nibbles(14,16))
print(f"Chunk_Length: {int(chunk_length,2)}")


# Chunk Value----This is specific to each chunk... 
# SCTP Data Chunk.
# Type
type1 = decode_nibble(extract_nibbles(16,17))
print(f"Type: {int(type1,2)}")

# Reserved, U-bit,B-bit,and E bit
rube = decode_nibble(extract_nibbles(16,17))
print(f"\nReserved bits: {rube[0:5]}")
# used to indicate if this is an unordered DATA chunk
print(f"U-bit: {rube[5:6]}")
# used to indicate the beginning of a fragmented DATA chunk
print(f"B-bit: {rube[6:7]}")
# used to indicate the ending of a fragmented DATA chunk
print(f"E-bit: {rube[7:]}\n")

# Length, 16 bits
length = decode_nibble(extract_nibbles(17,19))
print(f"Length: {int(length,2)}")

# Transmission Sequence Number,32 bits
#tsn = decode_nibble(extract_nibbles(19,23))
#print(f"TSN: {int(tsn,2)}")

# Stream Identifier, 16 bits
stream_i = decode_nibble(extract_nibbles(23,25))
print(f"Stream Identifier: {int(stream_i,2)}")

# Stream Sequence Number , 16 bit
ssn = decode_nibble(extract_nibbles(25,27))
print(f"Stream Sequence Number : {int(ssn,2)}")

# Payload Protocol Identifier


# User data