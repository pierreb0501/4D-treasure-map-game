# name : Pierre Andre El Boustany
# McGill ID : 261076411

import random
import treasure_utils



def generate_treasure_map_row(width, boolean):
    '''(int, bool) -> str
    takes a positive integer width and a boolean as inputs
    creates and returns a single row given of a treasure map

    >>> random.seed(9001)
    >>> generate_treasure_map_row(10, True)
    '.v*v>vv>^<'
    
    >>> random.seed(150)
    >>> generate_treasure_map_row(6, False)
    '^<^<>v'
    
    >>> random.seed(100)
    >>> generate_treasure_map_row(8, True)
    '^*^v>>.^'
    '''
    create_map = ''   
    for i in range (width):                
         if random.randint(0, 5) == 0:
            create_map += treasure_utils.EMPTY_SYMBOL
         else:
            create_map += treasure_utils.MOVEMENT_SYMBOLS[random.randint(0, 3)]
            
    if boolean :
         for c in range (width):
             if random.randint(0, 1) == 0:
                 return treasure_utils.change_char_in_map (create_map, 0, c, treasure_utils.MOVEMENT_SYMBOLS_3D[random.randint(0, 1)], width, 1)
             
    return create_map



def generate_treasure_map (width, height, boolean):
    '''(int, int, bool) -> str
    takes a positive integer width and height, and a boolean as inputs
    creates and returns a treasure map of the given width and height

    >>> generate_treasure_map(3,3,False)
    '><.<v><<v'
    
    >>> generate_treasure_map(3,3,True)
    '>^>..|*^<'
    
    >>> generate_treasure_map(4,3,True)
    '><^^|>v^>*>>'
    '''
    map = ''
    for i in range (height):
        map += generate_treasure_map_row(width, boolean)
    return treasure_utils.MOVEMENT_SYMBOLS[0] + map[1:]
    

def generate_3D_treasure_map(width, height, depth):
    '''(int, int, int) -> str
    takes a positive integer width, height and depth as inputs
    creates and returns a treasure map of the given width, height and depth
    
    >>> generate_3D_treasure_map(3,3,3)
    '>.^>|>>^.>^>*v><<|>v>*>.|><'
    
    >>> generate_3D_treasure_map(4,6,2)
    '>.vv*<vv*.vv<*<v*^^<v|^v>v.^|v<^<.^*|>^v|<.<|v<.'
    
    >>> generate_3D_treasure_map(5,10,2)
    '><.v.>v*<<|^<v^..*^.>|.^.<v*^<*><><^*<v..<|.^*vv<^>|v<^>>*..|<.>.*vv.^|.vv^>|<v.>|<<<>v.|^^|>^>*^><>'
    '''
    map = ''
    for i in range (depth):
        map += generate_treasure_map(width, height, True)
    
    return map

def follow_trail(treasure_map_string, row, column, depth_index, width, height, depth, number_tiles):
    '''(str, int, int, int, int, int, int, int) -> str
    takes a 3D treasure map string, starting row, column, depth index (int), width, height, depth (int), and the number of tiles to travel (int) as inputs,
    follows the trail in the map, starting at the given position,
    stops when the encountering a tile that has been previously encountered, or when the specified number of tiles has been travelled,
    prints the number of treasure collected and the number of symbols visited,
    returns the travelled map

    >>> follow_trail('>+....', 0, 0, 0, 3, 2, 1, 3)
    Treasures collected : 1
    Symbols visited : 3
    'X+....'
    '''

    treasure_found = 0
    position = row * width + width  * height * depth_index + column
    moves = 0
    initial_pos = ''
    information_1 = treasure_map_string, treasure_found
    information_2 = row, height, depth_index, moves
    
    def pos (row, column, depth_index, moves):

        position = row * width + width * height * depth_index + column

        if treasure_map_string [position] == treasure_utils.MOVEMENT_SYMBOLS[0]:
            position += 1 
            column += 1 
            moves += 1

        
        elif treasure_map_string [position] == treasure_utils.MOVEMENT_SYMBOLS[1]:
            position -= 1 
            column -= 1 
            moves += 1
            
        
        elif treasure_map_string [position] == treasure_utils.MOVEMENT_SYMBOLS[2]:
            position += (row + 1) * width
            row += 1
            moves += 1
           
        
        elif treasure_map_string [position] == treasure_utils.MOVEMENT_SYMBOLS[3]:
            position += (row - 1) * width
            row -= 1
            moves += 1
            
        
        elif treasure_map_string [position] == treasure_utils.MOVEMENT_SYMBOLS_3D[0]:
            position += (width  * height * (depth_index + 1) )
            depth_index += 1
            moves += 1
            
        
        elif treasure_map_string [position] == treasure_utils.MOVEMENT_SYMBOLS_3D[1]:
            position += (width  * height * (depth_index - 1) )
            depthp_index -= 1
            moves += 1
            
        
        else:
            pass

        moves += 1
        return information_2

    
    def passage (treasure_map_string, position, initial_pos, treasure_found):


        if treasure_map_string [position] == treasure_utils.MOVEMENT_SYMBOLS :
            return information_1, initial_pos
        
        elif treasure_map_string [position] == treasure_utils.TREASURE_SYMBOL :
            treasure_found += 1      
            return information_1, initial_pos
        
        elif treasure_map_string [position] != treasure_utils.TREASURE_SYMBOL :
            treasure_map_string = treasure_map_string[:position] + treasure_utils.BREADCRUMB_SYMBOL + treasure_map_string[position + 1 :]
            return information_1, initial_pos

    
    
    
    while not (0 > column > width or 0 > row > height or 0 > depth_index > depth) :

        information_1, initial_pos = passage(treasure_map_string, position, initial_pos, treasure_found) 
        information_2 = pos(row, column, depth_index, moves)

        if treasure_map_string[position] == treasure_utils.BREADCRUMB_SYMBOL or (moves == number_tiles and number_tiles > -1):
            print("Treasures collected", treasure_found)
            print("Symbols visited", moves)
            return treasure_map_string
        
        


