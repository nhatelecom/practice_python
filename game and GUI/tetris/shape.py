import numpy as np

class Shape:
    def __init__(self, rotations):
        self._rotations = rotations

def generate_shapes(self):
    # shape I
    shape_i_rot1 =  np.array([[1,0],[1,1],[1,2],[1,3]], np.int32)
    shape_i_rot2 =  np.array([[0,1],[1,1],[2,1],[3,1]], np.int32)
    shape_i =  Shape(np.array([shape_i_rot1,shape_i_rot2]))

    # shape L
    shape_l_rot1 = np.array([], np.int32)
    shape_l_rot2 = np.array([], np.int32)
    shape_l_rot3 = np.array([], np.int32)
    shape_l_rot4 = np.array([], np.int32)
    shape_l =  Shape(np.array([shape_l_rot1,shape_l_rot2,shape_l_rot3,shape_l_rot4]))

    # shape J
    shape_j_rot1 = np.array([], np.int32)
    shape_j_rot2 = np.array([], np.int32)
    shape_j_rot3 = np.array([], np.int32)
    shape_j_rot4 = np.array([], np.int32)
    shape_j =  Shape(np.array([shape_j_rot1,shape_j_rot2,shape_j_rot3,shape_j_rot4]))

    # shape O
    shape_o_rot1 =  np.array([[0,0],[0,1],[1,0],[1,1]], np.int32)
    shape_o =  Shape(np.array([shape_o_rot1]))

    # shape Z

    # shape S

    # shape T
    shape_t_rot1 = np.array([[1,0],[1,1],[1,2],[1,3]], np.int32)
    shape_t_rot2 = np.array([], np.int32)
    shape_t_rot3 = np.array([], np.int32)
    shape_t_rot4 = np.array([], np.int32)
    shape_t =  Shape(np.array([shape_t_rot1,shape_t_rot2,shape_t_rot3,shape_t_rot4]))

    return list(shape_i,shape_l,shape_t)

def generate_colors():
    RED = [255,50,21]
    ORANGE = [255,151,29]
    YELLOW = [255,213,4]
    GREEN = [114,203,59]
    BLUE = [4,65,174]
    OLIVE = [128,128,0]
    WHITE = [125,125,125]
    CYAN = [0,255,255]
    PURPLE = [128,0,128]
    return list([WHITE,BLUE,RED,ORANGE,YELLOW,GREEN,OLIVE,CYAN,PURPLE])


