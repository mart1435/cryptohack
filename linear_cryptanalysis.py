
def int2vector(unsigned_int):
    hex_string = f'{unsigned_int:032x}'
    arr = [int(hex_string[i:i+2], 16) for i in range(0, 32, 2)]
    return arr

def int2hex(unsigned_int):
    return hex(unsigned_int)

def hex2int(hex_str):
    return int(hex_str,16)

def hex2vector(hex_str):
    if len(hex_str) != 32:
        raise ValueError("Hex string must be exactly 32 characters long.")
    arr = [int(hex_str[i:i+2], 16) for i in range(0, 32, 2)]
    return arr

def vector2hex(arr):
    if len(arr) != 16:
        raise ValueError("Array must be exactly 16 integers long.")
    hex_string = ''.join(f'{num:02x}' for num in arr)
    return hex_string

def vector2int(arr):
    if len(arr) != 16:
        raise ValueError("Array must be exactly 16 integers long.")
    unsigned_int = 0
    for num in arr:
        unsigned_int = (unsigned_int << 8) | num
    return unsigned_int


inv_sbox = (1, 153, 42, 178, 87, 207, 124, 228, 173, 53, 134, 30, 251, 99, 208,
            72, 66, 218, 105, 241, 20, 140, 63, 167, 238, 118, 197, 93, 184, 32,
            147, 11, 135, 31, 172, 52, 209, 73, 250, 98, 43, 179, 0, 152, 125, 
            229, 86, 206, 196, 92, 239, 119, 146, 10, 185, 33, 104, 240, 67, 219,
            62, 166, 21, 141, 22, 142, 61, 165, 64, 216, 107, 243, 186, 34, 145,
            9, 236, 116, 199, 95, 85, 205, 126, 230, 3, 155, 40, 176, 249, 97,
            210, 74, 175, 55, 132, 28, 144, 8, 187, 35, 198, 94, 237, 117, 60,
            164, 23, 143, 106, 242, 65, 217, 211, 75, 248, 96, 133, 29, 174, 54,
            127, 231, 84, 204, 41, 177, 2, 154, 47, 183, 4, 156, 121, 225, 82,
            202, 131, 27, 168, 48, 213, 77, 254, 102, 108, 244, 71, 223, 58, 162,
            17, 137, 192, 88, 235, 115, 150, 14, 189, 37, 169, 49, 130, 26, 255,
            103, 212, 76, 5, 157, 46, 182, 83, 203, 120, 224, 234, 114, 193, 89, 
            188, 36, 151, 15, 70, 222, 109, 245, 16, 136, 59, 163, 56, 160, 19,
            139, 110, 246, 69, 221, 148, 12, 191, 39, 194, 90, 233, 113, 123, 227,
            80, 200, 45, 181, 6, 158, 215, 79, 252, 100, 129, 25, 170, 50, 190, 
            38, 149, 13, 232, 112, 195, 91, 18, 138, 57, 161, 68, 220, 111, 247,
            253, 101, 214, 78, 171, 51, 128, 24, 81, 201, 122, 226, 7, 159, 44, 180)

sbox = ( 0x2a, 0x00, 0x7e, 0x54, 0x82, 0xa8, 0xd6, 0xfc, 0x61, 0x4b, 0x35, 0x1f, 0xc9, 0xe3, 0x9d, 0xb7,
    0xbc, 0x96, 0xe8, 0xc2, 0x14, 0x3e, 0x40, 0x6a, 0xf7, 0xdd, 0xa3, 0x89, 0x5f, 0x75, 0x0b, 0x21,
    0x1d, 0x37, 0x49, 0x63, 0xb5, 0x9f, 0xe1, 0xcb, 0x56, 0x7c, 0x02, 0x28, 0xfe, 0xd4, 0xaa, 0x80,
    0x8b, 0xa1, 0xdf, 0xf5, 0x23, 0x09, 0x77, 0x5d, 0xc0, 0xea, 0x94, 0xbe, 0x68, 0x42, 0x3c, 0x16,
    0x44, 0x6e, 0x10, 0x3a, 0xec, 0xc6, 0xb8, 0x92, 0x0f, 0x25, 0x5b, 0x71, 0xa7, 0x8d, 0xf3, 0xd9, 
    0xd2, 0xf8, 0x86, 0xac, 0x7a, 0x50, 0x2e, 0x04, 0x99, 0xb3, 0xcd, 0xe7, 0x31, 0x1b, 0x65, 0x4f,
    0x73, 0x59, 0x27, 0x0d, 0xdb, 0xf1, 0x8f, 0xa5, 0x38, 0x12, 0x6c, 0x46, 0x90, 0xba, 0xc4, 0xee,
    0xe5, 0xcf, 0xb1, 0x9b, 0x4d, 0x67, 0x19, 0x33, 0xae, 0x84, 0xfa, 0xd0, 0x06, 0x2c, 0x52, 0x78,
    0xf6, 0xdc, 0xa2, 0x88, 0x5e, 0x74, 0x0a, 0x20, 0xbd, 0x97, 0xe9, 0xc3, 0x15, 0x3f, 0x41, 0x6b,
    0x60, 0x4a, 0x34, 0x1e, 0xc8, 0xe2, 0x9c, 0xb6, 0x2b, 0x01, 0x7f, 0x55, 0x83, 0xa9, 0xd7, 0xfd,
    0xc1, 0xeb, 0x95, 0xbf, 0x69, 0x43, 0x3d, 0x17, 0x8a, 0xa0, 0xde, 0xf4, 0x22, 0x08, 0x76, 0x5c,
    0x57, 0x7d, 0x03, 0x29, 0xff, 0xd5, 0xab, 0x81, 0x1c, 0x36, 0x48, 0x62, 0xb4, 0x9e, 0xe0, 0xca,
    0x98, 0xb2, 0xcc, 0xe6, 0x30, 0x1a, 0x64, 0x4e, 0xd3, 0xf9, 0x87, 0xad, 0x7b, 0x51, 0x2f, 0x05,
    0x0e, 0x24, 0x5a, 0x70, 0xa6, 0x8c, 0xf2, 0xd8, 0x45, 0x6f, 0x11, 0x3b, 0xed, 0xc7, 0xb9, 0x93, 
    0xaf, 0x85, 0xfb, 0xd1, 0x07, 0x2d, 0x53, 0x79, 0xe4, 0xce, 0xb0, 0x9a, 0x4c, 0x66, 0x18, 0x32, 
    0x39, 0x13, 0x6d, 0x47, 0x91, 0xbb, 0xc5, 0xef, 0x72, 0x58, 0x26, 0x0c, 0xda, 0xf0, 0x8e, 0xa4
)

rcon = (0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36)

gmul2 = ( 0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e, 
    0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e, 
    0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e, 
    0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e, 
    0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e, 
    0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae, 0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe, 
    0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde, 
    0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee, 0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe, 
    0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15, 0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05, 
    0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35, 0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25, 
    0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55, 0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45, 
    0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75, 0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65, 
    0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95, 0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85, 
    0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5, 0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5, 
    0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5, 0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5, 
    0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5, 0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5
)

gmul3 = ( 0x00, 0x03, 0x06, 0x05, 0x0c, 0x0f, 0x0a, 0x09, 0x18, 0x1b, 0x1e, 0x1d, 0x14, 0x17, 0x12, 0x11, 
    0x30, 0x33, 0x36, 0x35, 0x3c, 0x3f, 0x3a, 0x39, 0x28, 0x2b, 0x2e, 0x2d, 0x24, 0x27, 0x22, 0x21, 
    0x60, 0x63, 0x66, 0x65, 0x6c, 0x6f, 0x6a, 0x69, 0x78, 0x7b, 0x7e, 0x7d, 0x74, 0x77, 0x72, 0x71, 
    0x50, 0x53, 0x56, 0x55, 0x5c, 0x5f, 0x5a, 0x59, 0x48, 0x4b, 0x4e, 0x4d, 0x44, 0x47, 0x42, 0x41, 
    0xc0, 0xc3, 0xc6, 0xc5, 0xcc, 0xcf, 0xca, 0xc9, 0xd8, 0xdb, 0xde, 0xdd, 0xd4, 0xd7, 0xd2, 0xd1, 
    0xf0, 0xf3, 0xf6, 0xf5, 0xfc, 0xff, 0xfa, 0xf9, 0xe8, 0xeb, 0xee, 0xed, 0xe4, 0xe7, 0xe2, 0xe1, 
    0xa0, 0xa3, 0xa6, 0xa5, 0xac, 0xaf, 0xaa, 0xa9, 0xb8, 0xbb, 0xbe, 0xbd, 0xb4, 0xb7, 0xb2, 0xb1, 
    0x90, 0x93, 0x96, 0x95, 0x9c, 0x9f, 0x9a, 0x99, 0x88, 0x8b, 0x8e, 0x8d, 0x84, 0x87, 0x82, 0x81, 
    0x9b, 0x98, 0x9d, 0x9e, 0x97, 0x94, 0x91, 0x92, 0x83, 0x80, 0x85, 0x86, 0x8f, 0x8c, 0x89, 0x8a, 
    0xab, 0xa8, 0xad, 0xae, 0xa7, 0xa4, 0xa1, 0xa2, 0xb3, 0xb0, 0xb5, 0xb6, 0xbf, 0xbc, 0xb9, 0xba, 
    0xfb, 0xf8, 0xfd, 0xfe, 0xf7, 0xf4, 0xf1, 0xf2, 0xe3, 0xe0, 0xe5, 0xe6, 0xef, 0xec, 0xe9, 0xea, 
    0xcb, 0xc8, 0xcd, 0xce, 0xc7, 0xc4, 0xc1, 0xc2, 0xd3, 0xd0, 0xd5, 0xd6, 0xdf, 0xdc, 0xd9, 0xda, 
    0x5b, 0x58, 0x5d, 0x5e, 0x57, 0x54, 0x51, 0x52, 0x43, 0x40, 0x45, 0x46, 0x4f, 0x4c, 0x49, 0x4a, 
    0x6b, 0x68, 0x6d, 0x6e, 0x67, 0x64, 0x61, 0x62, 0x73, 0x70, 0x75, 0x76, 0x7f, 0x7c, 0x79, 0x7a, 
    0x3b, 0x38, 0x3d, 0x3e, 0x37, 0x34, 0x31, 0x32, 0x23, 0x20, 0x25, 0x26, 0x2f, 0x2c, 0x29, 0x2a, 
    0x0b, 0x08, 0x0d, 0x0e, 0x07, 0x04, 0x01, 0x02, 0x13, 0x10, 0x15, 0x16, 0x1f, 0x1c, 0x19, 0x1a
)

gmul9 = (
    0x00, 0x09, 0x12, 0x1b, 0x24, 0x2d, 0x36, 0x3f, 0x48, 0x41, 0x5a, 0x53, 0x6c, 0x65, 0x7e, 0x77,
    0x90, 0x99, 0x82, 0x8b, 0xb4, 0xbd, 0xa6, 0xaf, 0xd8, 0xd1, 0xca, 0xc3, 0xfc, 0xf5, 0xee, 0xe7,
    0x3b, 0x32, 0x29, 0x20, 0x1f, 0x16, 0x0d, 0x04, 0x73, 0x7a, 0x61, 0x68, 0x57, 0x5e, 0x45, 0x4c,
    0xab, 0xa2, 0xb9, 0xb0, 0x8f, 0x86, 0x9d, 0x94, 0xe3, 0xea, 0xf1, 0xf8, 0xc7, 0xce, 0xd5, 0xdc,
    0x76, 0x7f, 0x64, 0x6d, 0x52, 0x5b, 0x40, 0x49, 0x3e, 0x37, 0x2c, 0x25, 0x1a, 0x13, 0x08, 0x01,
    0xe6, 0xef, 0xf4, 0xfd, 0xc2, 0xcb, 0xd0, 0xd9, 0xae, 0xa7, 0xbc, 0xb5, 0x8a, 0x83, 0x98, 0x91,
    0x4d, 0x44, 0x5f, 0x56, 0x69, 0x60, 0x7b, 0x72, 0x05, 0x0c, 0x17, 0x1e, 0x21, 0x28, 0x33, 0x3a,
    0xdd, 0xd4, 0xcf, 0xc6, 0xf9, 0xf0, 0xeb, 0xe2, 0x95, 0x9c, 0x87, 0x8e, 0xb1, 0xb8, 0xa3, 0xaa,
    0xec, 0xe5, 0xfe, 0xf7, 0xc8, 0xc1, 0xda, 0xd3, 0xa4, 0xad, 0xb6, 0xbf, 0x80, 0x89, 0x92, 0x9b,
    0x7c, 0x75, 0x6e, 0x67, 0x58, 0x51, 0x4a, 0x43, 0x34, 0x3d, 0x26, 0x2f, 0x10, 0x19, 0x02, 0x0b,
    0xd7, 0xde, 0xc5, 0xcc, 0xf3, 0xfa, 0xe1, 0xe8, 0x9f, 0x96, 0x8d, 0x84, 0xbb, 0xb2, 0xa9, 0xa0,
    0x47, 0x4e, 0x55, 0x5c, 0x63, 0x6a, 0x71, 0x78, 0x0f, 0x06, 0x1d, 0x14, 0x2b, 0x22, 0x39, 0x30,
    0x9a, 0x93, 0x88, 0x81, 0xbe, 0xb7, 0xac, 0xa5, 0xd2, 0xdb, 0xc0, 0xc9, 0xf6, 0xff, 0xe4, 0xed,
    0x0a, 0x03, 0x18, 0x11, 0x2e, 0x27, 0x3c, 0x35, 0x42, 0x4b, 0x50, 0x59, 0x66, 0x6f, 0x74, 0x7d,
    0xa1, 0xa8, 0xb3, 0xba, 0x85, 0x8c, 0x97, 0x9e, 0xe9, 0xe0, 0xfb, 0xf2, 0xcd, 0xc4, 0xdf, 0xd6,
    0x31, 0x38, 0x23, 0x2a, 0x15, 0x1c, 0x07, 0x0e, 0x79, 0x70, 0x6b, 0x62, 0x5d, 0x54, 0x4f, 0x46
)

gmul11 = (
    0x00, 0x0b, 0x16, 0x1d, 0x2c, 0x27, 0x3a, 0x31, 0x58, 0x53, 0x4e, 0x45, 0x74, 0x7f, 0x62, 0x69,
    0xb0, 0xbb, 0xa6, 0xad, 0x9c, 0x97, 0x8a, 0x81, 0xe8, 0xe3, 0xfe, 0xf5, 0xc4, 0xcf, 0xd2, 0xd9,
    0x7b, 0x70, 0x6d, 0x66, 0x57, 0x5c, 0x41, 0x4a, 0x23, 0x28, 0x35, 0x3e, 0x0f, 0x04, 0x19, 0x12,
    0xcb, 0xc0, 0xdd, 0xd6, 0xe7, 0xec, 0xf1, 0xfa, 0x93, 0x98, 0x85, 0x8e, 0xbf, 0xb4, 0xa9, 0xa2,
    0xf6, 0xfd, 0xe0, 0xeb, 0xda, 0xd1, 0xcc, 0xc7, 0xae, 0xa5, 0xb8, 0xb3, 0x82, 0x89, 0x94, 0x9f,
    0x46, 0x4d, 0x50, 0x5b, 0x6a, 0x61, 0x7c, 0x77, 0x1e, 0x15, 0x08, 0x03, 0x32, 0x39, 0x24, 0x2f,
    0x8d, 0x86, 0x9b, 0x90, 0xa1, 0xaa, 0xb7, 0xbc, 0xd5, 0xde, 0xc3, 0xc8, 0xf9, 0xf2, 0xef, 0xe4,
    0x3d, 0x36, 0x2b, 0x20, 0x11, 0x1a, 0x07, 0x0c, 0x65, 0x6e, 0x73, 0x78, 0x49, 0x42, 0x5f, 0x54,
    0xf7, 0xfc, 0xe1, 0xea, 0xdb, 0xd0, 0xcd, 0xc6, 0xaf, 0xa4, 0xb9, 0xb2, 0x83, 0x88, 0x95, 0x9e,
    0x47, 0x4c, 0x51, 0x5a, 0x6b, 0x60, 0x7d, 0x76, 0x1f, 0x14, 0x09, 0x02, 0x33, 0x38, 0x25, 0x2e,
    0x8c, 0x87, 0x9a, 0x91, 0xa0, 0xab, 0xb6, 0xbd, 0xd4, 0xdf, 0xc2, 0xc9, 0xf8, 0xf3, 0xee, 0xe5,
    0x3c, 0x37, 0x2a, 0x21, 0x10, 0x1b, 0x06, 0x0d, 0x64, 0x6f, 0x72, 0x79, 0x48, 0x43, 0x5e, 0x55,
    0x01, 0x0a, 0x17, 0x1c, 0x2d, 0x26, 0x3b, 0x30, 0x59, 0x52, 0x4f, 0x44, 0x75, 0x7e, 0x63, 0x68,
    0xb1, 0xba, 0xa7, 0xac, 0x9d, 0x96, 0x8b, 0x80, 0xe9, 0xe2, 0xff, 0xf4, 0xc5, 0xce, 0xd3, 0xd8,
    0x7a, 0x71, 0x6c, 0x67, 0x56, 0x5d, 0x40, 0x4b, 0x22, 0x29, 0x34, 0x3f, 0x0e, 0x05, 0x18, 0x13,
    0xca, 0xc1, 0xdc, 0xd7, 0xe6, 0xed, 0xf0, 0xfb, 0x92, 0x99, 0x84, 0x8f, 0xbe, 0xb5, 0xa8, 0xa3
)

gmul13 = (
    0x00, 0x0d, 0x1a, 0x17, 0x34, 0x39, 0x2e, 0x23, 0x68, 0x65, 0x72, 0x7f, 0x5c, 0x51, 0x46, 0x4b,
    0xd0, 0xdd, 0xca, 0xc7, 0xe4, 0xe9, 0xfe, 0xf3, 0xb8, 0xb5, 0xa2, 0xaf, 0x8c, 0x81, 0x96, 0x9b,
    0xbb, 0xb6, 0xa1, 0xac, 0x8f, 0x82, 0x95, 0x98, 0xd3, 0xde, 0xc9, 0xc4, 0xe7, 0xea, 0xfd, 0xf0,
    0x6b, 0x66, 0x71, 0x7c, 0x5f, 0x52, 0x45, 0x48, 0x03, 0x0e, 0x19, 0x14, 0x37, 0x3a, 0x2d, 0x20,
    0x6d, 0x60, 0x77, 0x7a, 0x59, 0x54, 0x43, 0x4e, 0x05, 0x08, 0x1f, 0x12, 0x31, 0x3c, 0x2b, 0x26,
    0xbd, 0xb0, 0xa7, 0xaa, 0x89, 0x84, 0x93, 0x9e, 0xd5, 0xd8, 0xcf, 0xc2, 0xe1, 0xec, 0xfb, 0xf6,
    0xd6, 0xdb, 0xcc, 0xc1, 0xe2, 0xef, 0xf8, 0xf5, 0xbe, 0xb3, 0xa4, 0xa9, 0x8a, 0x87, 0x90, 0x9d,
    0x06, 0x0b, 0x1c, 0x11, 0x32, 0x3f, 0x28, 0x25, 0x6e, 0x63, 0x74, 0x79, 0x5a, 0x57, 0x40, 0x4d,
    0xda, 0xd7, 0xc0, 0xcd, 0xee, 0xe3, 0xf4, 0xf9, 0xb2, 0xbf, 0xa8, 0xa5, 0x86, 0x8b, 0x9c, 0x91,
    0x0a, 0x07, 0x10, 0x1d, 0x3e, 0x33, 0x24, 0x29, 0x62, 0x6f, 0x78, 0x75, 0x56, 0x5b, 0x4c, 0x41,
    0x61, 0x6c, 0x7b, 0x76, 0x55, 0x58, 0x4f, 0x42, 0x09, 0x04, 0x13, 0x1e, 0x3d, 0x30, 0x27, 0x2a,
    0xb1, 0xbc, 0xab, 0xa6, 0x85, 0x88, 0x9f, 0x92, 0xd9, 0xd4, 0xc3, 0xce, 0xed, 0xe0, 0xf7, 0xfa,
    0xb7, 0xba, 0xad, 0xa0, 0x83, 0x8e, 0x99, 0x94, 0xdf, 0xd2, 0xc5, 0xc8, 0xeb, 0xe6, 0xf1, 0xfc,
    0x67, 0x6a, 0x7d, 0x70, 0x53, 0x5e, 0x49, 0x44, 0x0f, 0x02, 0x15, 0x18, 0x3b, 0x36, 0x21, 0x2c,
    0x0c, 0x01, 0x16, 0x1b, 0x38, 0x35, 0x22, 0x2f, 0x64, 0x69, 0x7e, 0x73, 0x50, 0x5d, 0x4a, 0x47,
    0xdc, 0xd1, 0xc6, 0xcb, 0xe8, 0xe5, 0xf2, 0xff, 0xb4, 0xb9, 0xae, 0xa3, 0x80, 0x8d, 0x9a, 0x97
)

gmul14 = (
    0x00, 0x0e, 0x1c, 0x12, 0x38, 0x36, 0x24, 0x2a, 0x70, 0x7e, 0x6c, 0x62, 0x48, 0x46, 0x54, 0x5a,
    0xe0, 0xee, 0xfc, 0xf2, 0xd8, 0xd6, 0xc4, 0xca, 0x90, 0x9e, 0x8c, 0x82, 0xa8, 0xa6, 0xb4, 0xba,
    0xdb, 0xd5, 0xc7, 0xc9, 0xe3, 0xed, 0xff, 0xf1, 0xab, 0xa5, 0xb7, 0xb9, 0x93, 0x9d, 0x8f, 0x81,
    0x3b, 0x35, 0x27, 0x29, 0x03, 0x0d, 0x1f, 0x11, 0x4b, 0x45, 0x57, 0x59, 0x73, 0x7d, 0x6f, 0x61,
    0xad, 0xa3, 0xb1, 0xbf, 0x95, 0x9b, 0x89, 0x87, 0xdd, 0xd3, 0xc1, 0xcf, 0xe5, 0xeb, 0xf9, 0xf7,
    0x4d, 0x43, 0x51, 0x5f, 0x75, 0x7b, 0x69, 0x67, 0x3d, 0x33, 0x21, 0x2f, 0x05, 0x0b, 0x19, 0x17,
    0x76, 0x78, 0x6a, 0x64, 0x4e, 0x40, 0x52, 0x5c, 0x06, 0x08, 0x1a, 0x14, 0x3e, 0x30, 0x22, 0x2c,
    0x96, 0x98, 0x8a, 0x84, 0xae, 0xa0, 0xb2, 0xbc, 0xe6, 0xe8, 0xfa, 0xf4, 0xde, 0xd0, 0xc2, 0xcc,
    0x41, 0x4f, 0x5d, 0x53, 0x79, 0x77, 0x65, 0x6b, 0x31, 0x3f, 0x2d, 0x23, 0x09, 0x07, 0x15, 0x1b,
    0xa1, 0xaf, 0xbd, 0xb3, 0x99, 0x97, 0x85, 0x8b, 0xd1, 0xdf, 0xcd, 0xc3, 0xe9, 0xe7, 0xf5, 0xfb,
    0x9a, 0x94, 0x86, 0x88, 0xa2, 0xac, 0xbe, 0xb0, 0xea, 0xe4, 0xf6, 0xf8, 0xd2, 0xdc, 0xce, 0xc0,
    0x7a, 0x74, 0x66, 0x68, 0x42, 0x4c, 0x5e, 0x50, 0x0a, 0x04, 0x16, 0x18, 0x32, 0x3c, 0x2e, 0x20,
    0xec, 0xe2, 0xf0, 0xfe, 0xd4, 0xda, 0xc8, 0xc6, 0x9c, 0x92, 0x80, 0x8e, 0xa4, 0xaa, 0xb8, 0xb6,
    0x0c, 0x02, 0x10, 0x1e, 0x34, 0x3a, 0x28, 0x26, 0x7c, 0x72, 0x60, 0x6e, 0x44, 0x4a, 0x58, 0x56,
    0x37, 0x39, 0x2b, 0x25, 0x0f, 0x01, 0x13, 0x1d, 0x47, 0x49, 0x5b, 0x55, 0x7f, 0x71, 0x63, 0x6d,
    0xd7, 0xd9, 0xcb, 0xc5, 0xef, 0xe1, 0xf3, 0xfd, 0xa7, 0xa9, 0xbb, 0xb5, 0x9f, 0x91, 0x83, 0x8d
)

def inv_mix_columns(state):
    s = [0] * 16
    for i in range(4):
        s[i] = gmul14[state[i]] ^ gmul11[state[i + 4]] ^ gmul13[state[i + 8]] ^ gmul9[state[i + 12]]
        s[i + 4] = gmul9[state[i]] ^ gmul14[state[i + 4]] ^ gmul11[state[i + 8]] ^ gmul13[state[i + 12]]
        s[i + 8] = gmul13[state[i]] ^ gmul9[state[i + 4]] ^ gmul14[state[i + 8]] ^ gmul11[state[i + 12]]
        s[i + 12] = gmul11[state[i]] ^ gmul13[state[i + 4]] ^ gmul9[state[i + 8]] ^ gmul14[state[i + 12]]
    return s


def mix_columns(state):
    s = [0] * 16
    for i in range(4):
        s[i] = gmul2[state[i]] ^ gmul3[state[i + 4]] ^ state[i + 8] ^ state[i + 12]
        s[i + 4] = state[i] ^ gmul2[state[i + 4]] ^ gmul3[state[i + 8]] ^ state[i + 12]
        s[i + 8] = state[i] ^ state[i + 4] ^ gmul2[state[i + 8]] ^ gmul3[state[i + 12]]
        s[i + 12] = gmul3[state[i]] ^ state[i + 4] ^ state[i + 8] ^ gmul2[state[i + 12]]
    return s

def shift_rows(state):
    s = [state[0], state[1], state[2], state[3],
        state[5], state[6], state[7], state[4],
        state[10], state[11], state[8], state[9],
        state[15], state[12], state[13], state[14]]
    return s

def inv_shift_rows(state):
    s = [state[0], state[1], state[2], state[3],
         state[7], state[4], state[5], state[6],
         state[10], state[11], state[8], state[9],
         state[13], state[14], state[15], state[12]]
    return s


def sub_bytes(state):
    s = [sbox[i] for i in state] 
    return s   

def inv_sub_bytes(state):
    s = [inv_sbox[i] for i in state] 
    return s 

def recover_key(plaintext, ciphertext):
    state = hex2vector(plaintext)
    for i in range(1,10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
    state = sub_bytes(state)
    state = shift_rows(state)
    K = int(ciphertext, 16) - vector2int(state)
    return hex(K) 


def revert(s):
    state = s
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state) 
    for i in range(1,10):
        state = inv_mix_columns(state)
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
    return state
    
def recover_flag(encrypted_flag, key):
    plaintext = ""
    key = int(key, 16)

    for i in range(0, len(encrypted_flag), 32):
        chunk = encrypted_flag[i:i+32]
        state = int2vector(int(chunk, 16) - key)
        state = revert(state) 
        plaintext += vector2hex(state)
    return plaintext     
        
def main():
    known_plaintext = "11112233445566778899aabbccddeeff"
    known_ciphertext = "d02d2593fb4bb75c4df6e5a74ffce9be"
    flag_encrypted = "b0123780b7d3e6cf3621a640e95f4dafd2e3c392f6cd1ccfed055e2160df382a79923392b9a84b6566ccde65f74f621d"
    k = recover_key(known_plaintext, known_ciphertext)
    print(k)
    print(recover_flag(flag_encrypted, k))


main()