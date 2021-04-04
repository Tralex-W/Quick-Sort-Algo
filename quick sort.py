def quick_sort(li):
    if len(li) <= 1:
        return li
    else:
        pivot = li.pop()
    
    items_higher = []
    items_lower = []

    for item in li:
        if item > pivot:
            items_higher.append(item)
        else:
            items_lower.append(item)
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_higher)

if __name__ == '__main__':
    li = [378, -364, 369, -200, 376, 368, -499, -22, -71, 10, 335, 260, 160, 314, 4, 122, 19, 384, 403, -101, 456, 296, -56, -216, -461, -262, -215, -276, 328, 295, -259, -62, -463, -219, 200, 310, -281, 250, -59, -492, -81, -491, -14, 64, 397, 492, -41, -414, -199, 136, 212, 199, -423, -330, -1, 300, 406, -391, 336, 457, -101, 292, 153, 413, 229, -143, 74, -74, 306, -333, -445, 273, 18, -135, -253, -295, -377, -479, 5, -20, -150, 146, -284, 165, 383, 55, 268, -145, 84, -326, 223, 26, 136, -241, 57, -166, -215, -331, 151, 295, -317, -323, 321, -170, -410, -352, -293, 157, -481, 423, 317, 327, 234, 357, -131, -368, 490, -96, 481, -37, 157, 295, 113, 406, 60, -479, -95, -121, 102, -248, 320, 498, 147, -55, -39, 399, 346, -144, -109, -464, -444, -402, -192, 81, 483, -28, -217, 319, -208, -315, -321, -358, 267, 430, 445, 56, -491, 268, 411, -495, 124, 204, 180, 166, 65, -441, 34, -119, -5, 102, -401, 143, -96, 85, -169, 220, 306, -75, 254, -175, 422, 355, 182, 7, 387, 458, -16, -155, 89, -449, -258, -41, -176, 77, 70, -391, 195, -230, 256, 191, 491, 475, 133, -160, 261, -307, 271, -203, -216, 412, 469, 295, 219, 359, -211, -359, -358, -100, -406, 203, -42, -476, -45, -418, -73, -17, 393, -74, 335, 372, -29, 443, -465, -377, -287, 42, 214, 262, 145, 149, -416, -357, 247, -70, -299, 405, 7, -80, -363, 368, -390, 369, 41, -136, -383, -223, 380, -28, -428, -139, -404, -498, -453, 248, 68, -121, -48, 475, -346, 421, -227, 94, 331, -491, -37, 94, 348, -339, 30, 31, 157, -290, 105, -436, -218, 448, 244, 40, -418, 348, 435, -128, -75, -43, -447, 414, 231, 334, -341, -79, -207, -140, -461, 444, -257, 234, 131, -78, 391, -429, 369, 337, -318, -213, -464, -252, -251, 224, -388, -346, 325, -182, 441, -215, 304, 324, 177, 21, -169, -91, 2, 379, -482, 28, -237, 251, 328, -438, -295, 35, -79, 51, 
        -445, -84, -405, -386, -311, 357, 236, 172, 468, -492, 101, 442, 317, -9, -453, -276, -213, 437, 395, 320, 109, -457, -448, -334, -333, -54, 392, 395, 83, 134, 253, 426, -230, 42, -274, -349, 51, -434, -294, -10, 309, 449, -291, -125, -157, -349, 264, -408, 1, 306, -215, 237, 363, 21, 73, 242, -130, -253, -118, 69, -330, 73, 73, 304, -104, -145, 47, -183, -121, 68, 210, -282, -200, 238, 47, -218, -239, -447, -147, -260, 328, -250, 351, 112, -411, -29, -388, 114, -301, 363, -94, 236, 358, -210, -78, 205, -77, 406, 74, -409, 218, -473, 307, -404, 115, 213, 421, 206, 474, 91, 188, -227, -369, -371, -271, 145, -174, 170, 128, -378, 319, 58, -298, -482, 330, 190, 102, -248, -82, -178, -460, 100, -454, 287, 339, 240, 57, -432, -491, -73, -477, -165, 354, 12, 47, -54, 220, 224, 193, 180, 385, -162, -25, 164, 95, -325, 27, -65, 336, 40, 136, 66, -134, 230, 101, 270, 467, 200, -209, -21, 259, -284, -495, 113, -31, -273, 19, -242, -412, -286, -267, 41, 33, -135, -232, 104, 413, -414, -447, 117, 479, -151, -119, -176, -264, 61, -444, -57, -120, -130, 296, -423, 479, -142, -157, 418, 223, -260, 312, -134, 71, 218, 354, 
        474, 191, -295, -357, 341, -487, -29, -238, -356, -418, 429, 172, 176, -15, 411, -8, 280, 118, -89, -408, -154, -359, -420, 330, -423, -187, 103, 446, 202, 206, -497, 398, 467, 246, 358, 72, -361, 182, 41, -408, 488, -494, -209, -125, -331, -141, -398, 343, -11, -132, -48, -342, -6, -89, -73, -303, 232, -297, -366, 457, 82, -67, -95, -471, 377, 295, 274, 349, -434, -299, -121, -268, 404, -326, 363, -481, -149, 89, -38, 224, -242, 215, -138, -332, -484, -463, -135, -4, -252, -46, -251, -411, -309, 14, 351, 226, -214, 314, 285, 103, 277, -24, 423, -72, -82, 257, 95, -492, -136, 428, 82, -386, -155, 270, 100, 67, -286, -244, 32, 155, 17, 35, -301, -337, -253, -410, -21, -334, 4, 238, -70, -309, 263, -363, 248, -340, 116, 6, 102, -287, 120, 372, 471, 203, 309, -445, -364, 344, 494, 117, 137, -496, -198, 162, -155, -444, -43, -210, -242, -404, -354, -291, 427, 268, -380, -284, 8, 458, 138, 348, -271, -40, 226, -8, -487, 172, -464, -463, -37, 127, -193, 23, 122, 194, -76, 403, -166, -224, -173, 444, -453, 106, -255, -444, -134, -26, -422, 403, 172, 126, -470, -250, -410, 332, 357, -281, 64, -482, 119, -399, 81, 450, -57, -433, 306, 262, -365, -269, -425, 15, -5, -425, -226, -107, -313, 186, -51, -381, -255, 225, -109, -101, 442, -26, -334, -370, 62, 29, 373, 64, 373, -292, -224, -242, -124, 353, -170, 60, -114, 116, -497, 160, -204, -132, 320, -194, -331, -293, 400, 207, 71, 431, -358, 191, -34, 306, 83, -420, -365, -308, 476, 468, 226, -1, 225, 11, -120, 138, 459, 28, 80, -268, 41, -278, -327, -150, -212, 389, -445, -193, -171, -457, -286, -128, 355, -171, 307, -187, 164, -346, -109, -202, 438, 25, 450, 422, 175, -76, -474, 0, 29, 19, 157, -283, 477, 124, -260, -345, -66, 419, 407, -130, 352, -406, 7, -349, -125, -209, 44, -77, 393, 185, -9, -305, -412, -341, -251, 208, -363, 492, -62, -363, 221, 181, -278, 289, -63, 104, 139, -359, 422, -306, 115, 8, -269, 395, 329, 446, -306, -264, 118, 28, -141, 80, -219, -263, 363, -103, 122, 115, 101, -105, -377, -351, 487, 157, 299, 349, -137, 50, 283, -382, 378, 414, 82, 48, -15, 327, 140, -333, 8, 351, 346, -348, -147, 143, 304, 356, -267, 282, 293, 258, 93, 327, 80, -382, 239, -225, 413, 290, 449, -200, -381, 429, 318, -128, -270, -299, -469, 80, -226, 337, -409, -497, 496, -65, -206, 72, -151, -481, -49, 36, 276, -262, 373, -225, 184, -351, 320, 345, -231, -321, -318, 353, -104]
    print(quick_sort(li))