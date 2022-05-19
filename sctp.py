# UDP
hex_stream = ['13','55','b6','76','79','88','29','5e','00','00','00','00','00','03','00','00','34','7e','58','1e','36','00','00',',00','00','00','00','00','00']
scale =16


def decode_nibble(nibble_string):
    binary_string = ''
    
    for i in nibble_string:
        b_s = str(bin(int('0x'+i,scale)))[2:].zfill(4)
        # padd the left with zeros
        
        binary_string += b_s
    
    
    return binary_string


source_string = ''      
for i in range(2):
    source_string +=hex_stream[i]
    

#print(source_string)
Source_Port = decode_nibble(source_string)
print(f"Source Port: {int(Source_Port,2)}")

dest_string = ''      
for i in range(2,4):
    dest_string +=hex_stream[i]
    
#print(dest_string)

destination_port = decode_nibble(dest_string)
print(f"Dest_port: {int(destination_port,2)}")

ver_string = ''      
for i in range(4,8):
    ver_string +=hex_stream[i]

ver_tag = decode_nibble(dest_string)
print(f"verificatioon_tag: {int(ver_tag,2)}")

# Type
type_string = ''      
for i in range(1):
    type_string +=hex_stream[i]

type2 = decode_nibble(type_string)
print(f"Type: {int(type2,2)}")

# Type
string = ''      
for i in range(12,14):
    string +=hex_stream[i]
b_flag = decode_nibble(string)
print(f"B flag: {int(b_flag,2)}")




