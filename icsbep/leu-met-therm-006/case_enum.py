import copy

#############################################
# Benchmark:  LEU-MET-THERM-006 
# Cases:      1-30 
# Model by:   Nour Ali  
# Date:       26/08/2024
#############################################


w3 = 'w3'
f1 = 'f1'
f2 = 'f2'

class info:
    """
    c_no=case number\n
    w_h=critical water height\n
    pitch=assembly pitch\n
    beams_number_h=number of beams in horizontal direction\n
    beams_number_v=number of beams in vertical direction\n
    diag: number of diagonal moves from the corner pin to the center pin\n
    vert: number of vertical moves from the corner pin to the center pin\n
    lattice: lattice type, rectangular or hexagonal\n
    additional_plate: True if there is an additional plate in the assembly\n
    assembly_dict: dictionary of all possible assembly configurations"""

    START_IDX = 1

    #the indices are constant throughout for case numbers
    #for example, the parameters for case 1 are all at index 0
    c_no = [x for x in range(1,31)]
    w_h = [59.55,57.97,52.91,64.32,53.18,61.77,60.82,59.41,54.65,55.50,48.41,63.56,
           56.44,62.35,61.21,56.47,66.54,63.51,63.94,57.07,61.56,60.26,59.60,57.66,
           63.52,60.95,59.25,58.90,65.65,61.20]
    pitch = [10.2,10.2,10.2,10.7,10.7,11.2,11.2,11.2,11.2,11.2,11.2,11.7,11.7,12.2,
             12.2,12.2,12.7,12.7,9.7,9.7,10.2,10.2,10.2,10.2,10.7,10.7,10.7,10.7,
             11.2,11.2]
    beams_number_h = [7,7,8,6,7,6,6,6,6,6,7,6,6,7,7,7,8,8,
                      6,7,6,6,6,6,6,6,6,6,7,7]
    beams_number_v= [7]*30

    diag=[3,3,3,2,3,3,3,3,2,2,3,3,2,3,3,3,3,3]
    rec_d=[19]*12
    diag.extend(rec_d)

    vert=[1,2,2,2,1,1,1,1,2,2,1,1,2,1,1,1,1,2]
    rec_v=[20]*12
    vert.extend(rec_v)

    lattice=['hex']*18
    rect=['rect']*12
    lattice.extend(rect)

    additional_plate=[True]*30
    additional_plate[6:9]=[False]*3
    additional_plate[10]=False

    assembly_dict={}

    #case 1
    ring1_4 = [w3] + [f1]*3 + [w3]*5 + [f1] + [w3]*5 + [f1] + [w3]*5 +[f1]*3
    ring1_3= [f1] *9 + [w3] + [f1]*8
    ring1_2 = [f1]*12
    ring1_1 = [f1]*6
    ring1_0=[f1]

    hex_array1=[ring1_4, ring1_3, ring1_2, ring1_1, ring1_0]
    assembly_dict[1]=copy.deepcopy(hex_array1)

    #case2
    ring2_5=[w3]*30
    ring2_5[12]=ring2_5[18]=f1
    ring2_4=[w3]*24
    ring2_4[3]=ring2_4[9]=ring2_4[10]=ring2_4[11]=ring2_4[-3]=f1
    ring2_4[-9]=ring2_4[-10]=ring2_4[-11]=f1
    ring2_3= [w3] + [f1]*17
    ring2_2 = [f1]*12
    ring2_1 = [f1]*6
    ring2_0=[f1]
    hex_array2=[ring2_5, ring2_4, ring2_3, ring2_2, ring2_1, ring2_0]
    assembly_dict[2]=copy.deepcopy(hex_array2)

    # Case 3,18
    ring3_5=[w3]*30
    ring3_5[12]=ring3_5[18]=f1
    ring3_5[11]=f2
    ring3_4=[w3]*24
    ring3_4[3]=ring3_4[9]=ring3_4[10]=ring3_4[11]=f1
    ring3_4[-3]=ring3_4[-9]=ring3_4[-10]=ring3_4[-11]=f1
    ring3_4[4:9]=[f2]*5
    ring3_3= [w3] + [f1]*17
    ring3_2 = [f1]*12
    ring3_1 = [f1]*6
    ring3_0=[f1]
    hex_array3=[ring3_5, ring3_4, ring3_3, ring3_2, ring3_1, ring3_0]
    assembly_dict[3]=copy.deepcopy(hex_array3)
    assembly_dict[18]=copy.deepcopy(hex_array3)

    # Case 4,9,10,13
    ring4_4 = [w3]*24
    ring4_4[3]=ring4_4[9]=ring4_4[10]=ring4_4[14]=f1
    ring4_3= [w3]*18
    ring4_3[1:12]=[f1]*11
    ring4_3[16:18]=[f1]*2
    ring4_2 = [f1]*12
    ring4_1 = [f1]*6
    ring4_0=[f1]
    hex_array4=[ring4_4, ring4_3, ring4_2, ring4_1, ring4_0]
    assembly_dict[4]=copy.deepcopy(hex_array4)
    assembly_dict[9]=copy.deepcopy(hex_array4)
    assembly_dict[10]=copy.deepcopy(hex_array4)
    assembly_dict[13]=copy.deepcopy(hex_array4)

    # Case 5,11,16
    ring5_4 = [w3]*24
    ring5_4[2]=ring5_4[3]=ring5_4[-2]=ring5_4[-3]=ring5_4[9]=ring5_4[15]=f1
    ring5_3=[f1]*18
    ring5_3[9]=w3
    ring5_2 = [f1]*12
    ring5_1 = [f1]*6
    ring5_0=[f1]
    hex_array5=[ring5_4, ring5_3, ring5_2, ring5_1, ring5_0]
    assembly_dict[5]=copy.deepcopy(hex_array5)
    assembly_dict[11]=copy.deepcopy(hex_array5)
    assembly_dict[16]=copy.deepcopy(hex_array5)

    # Case 6,7,12
    ring6_4 = [w3]*24
    ring6_4[15]=f1
    ring6_3=[f1]*18
    ring6_3[0]=ring6_3[9]=w3
    ring6_3[3:7]=[w3]*4
    ring6_2 = [f1]*12
    ring6_1 = [f1]*6
    ring6_0=[f1]
    hex_array6=[ring6_4, ring6_3, ring6_2, ring6_1, ring6_0]
    assembly_dict[6]=copy.deepcopy(hex_array6)
    assembly_dict[7]=copy.deepcopy(hex_array6)
    assembly_dict[12]=copy.deepcopy(hex_array6)

    # Case 8
    ring8_4=[w3]*24
    ring8_4[15]=ring8_4[21]=f1
    ring8_3=[f1]*18
    ring8_3[0]=ring8_3[9]=w3
    ring8_3[3:7]=[w3]*4
    ring8_2 = [f1]*12
    ring8_1 = [f1]*6
    ring8_0=[f1]
    hex_array8=[ring8_4, ring8_3, ring8_2, ring8_1, ring8_0]
    assembly_dict[8]=copy.deepcopy(hex_array8)

    # Case 14
    ring14_4 = [w3]*24
    ring14_4[3]=ring14_4[9]=ring14_4[15]=f1
    ring14_3=[f1]*18
    ring14_3[0]=ring14_3[9]=w3
    ring14_2 = [f1]*12
    ring14_1 = [f1]*6
    ring14_0=[f1]
    hex_array14=[ring14_4, ring14_3, ring14_2, ring14_1, ring14_0]
    assembly_dict[14]=copy.deepcopy(hex_array14)

    # Case 15
    ring15_4 = [w3]*24
    ring15_4[3]=ring15_4[-3]=ring15_4[9]=ring15_4[-9]=f1
    ring15_3=[f1]*18
    ring15_3[0]=ring15_3[9]=w3
    ring15_2 = [f1]*12
    ring15_1 = [f1]*6
    ring15_0=[f1]
    hex_array15=[ring15_4, ring15_3, ring15_2, ring15_1, ring15_0]
    assembly_dict[15]=copy.deepcopy(hex_array15)

    #Case 17
    ring17_5=[w3]*30
    ring17_5[3]=ring17_5[-3]=f1
    ring17_4=[f1]*24
    ring17_4[4:9]=[f2]*5
    ring17_4[0]=w3
    ring17_4[10:15]=[w3]*5
    ring17_4[16:21]=[w3]*5
    ring17_3=[f1]*18
    ring17_3[9]=w3
    ring17_2 = [f1]*12
    ring17_1 = [f1]*6
    ring17_0=[f1]
    hex_array17=[ring17_5, ring17_4, ring17_3, ring17_2, ring17_1, ring17_0]
    assembly_dict[17]=copy.deepcopy(hex_array17)

    # Case 19, 24, 28
    rect_array19=[
        [w3,w3,w3,w3,w3,w3,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,w3,w3,w3,w3,w3,w3,w3]]
    
    assembly_dict[19]=copy.deepcopy(rect_array19)
    assembly_dict[24]=copy.deepcopy(rect_array19)
    assembly_dict[28]=copy.deepcopy(rect_array19)
    
    # Case 20
    rect_array20=[
        [w3,w3,w3,w3,w3,w3,w3,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3,w3],
        [w3,w3,w3,w3,w3,w3,w3,w3,w3]]
    
    assembly_dict[20]=copy.deepcopy(rect_array20)
    
    # Case 21
    rect_array21=[
        [w3,w3,w3,w3,w3,w3,w3,w3],
        [w3,w3,f2,f1,f1,w3,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,w3,w3,w3,w3,w3,w3,w3]]
    
    assembly_dict[21]=copy.deepcopy(rect_array21)

    #Case 22
    rect_array22=[
        [w3,w3,w3,w3,w3,w3,w3,w3],
        [w3,w3,f1,f1,f1,f1,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,w3,w3],
        [w3,w3,w3,w3,w3,w3,w3,w3]]
    
    assembly_dict[22]=copy.deepcopy(rect_array22)

    #Case23
    rect_array23=[
        [w3,w3,w3,w3,w3,w3,w3,w3],
        [w3,f1,f1,f1,f1,f1,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,w3,w3],
        [w3,w3,w3,w3,w3,w3,w3,w3]]

    assembly_dict[23]=copy.deepcopy(rect_array23)

    #Case 25
    rect_array25=[
        [w3,w3,w3,w3,w3,w3,w3,w3],
        [w3,w3,f1,f1,f1,w3,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,w3,w3,w3,w3,w3,w3,w3]]
    
    assembly_dict[25]=copy.deepcopy(rect_array25)

    # Case 26
    rect_array26=[
        [w3,w3,w3,w3,w3,w3,w3,w3],
        [w3,w3,f1,f1,f1,f1,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,w3,w3,w3,w3,w3,w3,w3]]
    
    assembly_dict[26]=copy.deepcopy(rect_array26)

    #case27
    rect_array27=[
        [w3,w3,w3,w3,w3,w3,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f2,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3],
        [w3,w3,w3,w3,w3,w3,w3,w3]]
    
    assembly_dict[27]=copy.deepcopy(rect_array27)

    #case 29
    rect_array29=[
        [w3,w3,w3,w3,w3,w3,w3,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,f1,w3],
        [w3,w3,w3,w3,w3,w3,w3,w3,w3]]
    
    assembly_dict[29]=copy.deepcopy(rect_array29)
    
    #case 30
    rect_array30=[
        [w3,w3,w3,w3,w3,w3,w3,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,f1,w3],
        [w3,f1,f1,f1,f1,f1,f1,f2,w3],
        [w3,f1,f1,f1,f1,f1,f1,w3,w3],
        [w3,f1,f1,f1,f1,f1,f1,f1,w3],
        [w3,w3,w3,w3,w3,w3,w3,w3,w3]]

    assembly_dict[30]=copy.deepcopy(rect_array30)


class case_enum:
    """
    This class assigns the parameters of each case to its corresponding case number.
    """
    def __init__(self, case_num) -> None:
        idx = case_num - info.START_IDX
        self.c_no = info.c_no[idx]
        self.w_h = info.w_h[idx]
        self.pitch=info.pitch[idx]
        self.beams_number_h=info.beams_number_h[idx]
        self.beams_number_v=info.beams_number_v[idx]
        self.diag=info.diag[idx]
        self.vert=info.vert[idx]
        self.lattice=info.lattice[idx]
        self.additional_plate=info.additional_plate[idx]
        self.assembly_lat=copy.deepcopy(info.assembly_dict[case_num])
        
    