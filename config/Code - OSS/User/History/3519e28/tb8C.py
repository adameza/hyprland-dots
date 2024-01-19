#!/usr/bin/env python3
import random

# Define all tiles using official addition of scrabble
tile_BLANK_count = (' ', 2)
tile_A_count = ('A', 9)
tile_B_count = ('B', 2)
tile_C_count = ('C', 2) 
tile_D_count = ('D', 4)
tile_E_count = ('E', 12)
tile_F_count = ('F', 2)
tile_G_count = ('G', 3)
tile_H_count = ('H', 2)
tile_I_count = ('I', 9)
tile_J_count = ('J', 1)
tile_K_count = ('K', 1)
tile_L_count = ('L', 4)
tile_M_count = ('M', 2)
tile_N_count = ('N', 6)
tile_O_count = ('O', 8)
tile_P_count = ('P', 2)
tile_Q_count = ('Q', 1)
tile_R_count = ('R', 6)
tile_S_count = ('S', 4)
tile_T_count = ('T', 6)
tile_U_count = ('U', 4)
tile_V_count = ('V', 2)
tile_W_count = ('W', 2)
tile_X_count = ('X', 1)
tile_Y_count = ('Y', 2)
tile_Z_count = ('Z', 1)

#Define data structure to hold tiles counts
tile_counts_list = [
    tile_BLANK_count,
    tile_A_count,
    tile_B_count,
    tile_C_count, 
    tile_D_count,
    tile_E_count,
    tile_F_count,
    tile_G_count,
    tile_H_count,
    tile_I_count,
    tile_J_count,
    tile_K_count,
    tile_L_count,
    tile_M_count,
    tile_N_count,
    tile_O_count,
    tile_P_count,
    tile_Q_count,
    tile_R_count,
    tile_S_count,
    tile_T_count,
    tile_U_count,
    tile_V_count,
    tile_W_count,
    tile_X_count,
    tile_Y_count,
    tile_Z_count
]

tile_bag = []

def load_tiles(tile_tuple, tile_bag):
    tile_count = tile_tuple[1]
    tile_letter = tile_tuple[0]

    for x in range(tile_count):
        tile_bag.append(tile_letter)

def refreshTileBag(tile_bag):
    for tile_tuple in tile_counts_list:
        load_tiles(tile_tuple, tile_bag)
    print(tile_bag)

def drawTiles(tile_bag):
    # random number of tiles being drawn
    num_tiles_drawn = random.randint(2, 7)
    #randomly draw the tiles
    for x in range num_tiles_drawn:
        drawn_tile_index = random.randint(0, len(tile_bag))
        deleteTile(tile_bag, drawn_tile_index)



def main():
    """ Main entry point of the app """
    refreshTileBag()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()