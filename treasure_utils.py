# name : Pierre Andre El Boustany
# McGill ID : 261076411

MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'

def get_nth_row_from_map (treasure_map_string, n, width, height):
    '''(str, int, int, int) -> str
    takes a treasure map string, integer n, width and height as inputs
    returns the n'th row of a treasure map
    
    >>> get_nth_row_from_map('^..>>>..v',1,3,3)
    '>>>'
    
    >>> get_nth_row_from_map('>>>..vv^<..v',2,4,3)
    '<..v'
    
    >>> get_nth_row_from_map('>>.<',3,1,2)
    '.'
    '''
    
    if 0 <= n <= height:
        return treasure_map_string[(n * width) : (n * width) + width]      
    else: 
         return (EMPTY_SYMBOL)


def print_treasure_map (treasure_map_string, width, height):
    '''(str, int, int) -> NoneType
    takes a treasure map string, integer n, width and height as inputs
    prints out the n'th row of a treasure map
    
    >>> print_treasure_map ('<..vvv..^', 3, 3)
    <..
    vvv
    ..^
    
    >>> print_treasure_map ('........', 2, 4)
    ..
    ..
    ..
    ..
    
    >>> print_treasure_map ('>>.<', 2, 2)
    >>
    .<
    '''
    n = 0
    while n < height:
        print (get_nth_row_from_map(treasure_map_string, n, width, height))
        n += 1
     

def change_char_in_map(treasure_map_string, row, column, character_c, width, height):
    '''(str, int, int, int, int, int) -> str
    takes a treasure map string, integer row and column index, character c, and integer width and hight as inputs
    returns a copy of the treasure map string with the character c at the given row and column index
    
    >>> change_char_in_map('.........', 1, 1, 'X', 3, 3)
    '....X....'
    
    >>> change_char_in_map('><..vv>^.<>>', 2, 1, 'X', 3, 4)
    '><..vv>X.<>>'
    
    >>> change_char_in_map('>vv.', 0, 0, 'X', 2, 2)
    'Xvv.'
    '''
    if 0 <= row < height and 0 <= column < width:
        select_index = (row * width) + column 
        text = treasure_map_string[:select_index] + character_c + treasure_map_string[select_index + 1:]
        return (text)  
    else:
        return (treasure_map_string)


def get_proportion_travelled(treasure_map_string):
    '''(str) -> str
    takes a treasure map string as input
    returns the percentage of the map travelled (float) rounded to 2 decimals
    
    >>> get_proportion_travelled('.X..X.XX.')
    0.44
    
    >>> get_proportion_travelled('XX...X..XX.XXX')
    0.57
    
    >>> get_proportion_travelled('XXXXX..XX')
    0.78
    '''
    passage = treasure_map_string.count ('X')
    percentage = passage / len(treasure_map_string)
    return round(percentage,2)

def get_nth_map_from_3D_map (treasure_map_string, n, width, height, depth):
    '''(str, int, int, int, int) -> str
    takes a treasure map string, integer n, width, height and depth as inputs
    returns the n'th row of a treasure map
    
    >>> get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 0, 3, 3, 2)
    '.X.XXX.X.'
    
    >>> get_nth_map_from_3D_map('.v...vvv..v.vX..', 2, 2, 2, 3)
    '..v.'
    
    >>> get_nth_map_from_3D_map('.........', 4, 3, 3, 2)
    '.'
    '''
    if 0 <= n < depth :
        map = treasure_map_string [n * width * height : n  * width * height + width * height]
        return map
    else:
        return EMPTY_SYMBOL

def print_3D_treasure_map(treasure_map_string, width, height, depth):
    '''(str, int, int, int) -> NoneType
    takes a treasure map string, integer n, width, height and depth as inputs
    prints out each row on its own line and each map separated by a blank
    
    >>> print_3D_treasure_map('.X.XXX.X..v.vXv.v.',3,3,2)
    .X.
    XXX
    .X.

    .v.
    vXv
    .v.
   
    >>> print_3D_treasure_map('..........',2,1,5)
    ..

    ..

    ..

    ..

    ..
    '''
    for n in range (depth):
        if n != 0:
            print('')
            
        map = get_nth_map_from_3D_map(treasure_map_string, n, width, height, depth)
        print_treasure_map(map, width, height)


def change_char_in_3D_map(treasure_map_string, row, column, depth_index, character_c, width, height, depth):
    '''(str, int, int, int, int, int, int, int) -> str
    takes a 3D treasure map string, integer row, column and depth index, character c, and integer width, height and depth as inputs
    returns a copy of the 3D treasure map string with the character c at the given row, column and depth index
    
    >>> change_char_in_3D_map('.X.XXX.X..v.vXv.v.', 0, 0, 0, '#', 3, 3, 2)
    '#X.XXX.X..v.vXv.v.'
    
    >>> change_char_in_3D_map('..................', 1, 1, 1, '#', 3, 3, 2)
    '.............#....'
    
    >>> change_char_in_3D_map('...............', 1, 1, 1, '%', 3, 5, 3)
    '...............%'
    '''
    map = ''
    for n in range (depth):
        if n != depth_index:
            map += get_nth_map_from_3D_map(treasure_map_string, n, width, height, depth)
        else:
            old_map = get_nth_map_from_3D_map(treasure_map_string, n, width, height, depth)
            map += change_char_in_map(old_map, row, column, character_c, width, height)

    return map




        
        

    
    