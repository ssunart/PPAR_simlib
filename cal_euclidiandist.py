### 2개의 PDB 파일에서 원자 좌표를 읽어들인 후, 
##각 분자의 좌표 중심(center of mass)을 계산하고 두 중심 간의 유클리드 거리를 계산.

import numpy as np

def read_pdb(filename):
    """ PDB 파일에서 좌표를 읽어 numpy 배열로 반환하는 함수 """
    coordinates = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                x, y, z = map(float, line[30:54].split())
                coordinates.append([x, y, z])
    return np.array(coordinates)

def calculate_center_of_mass(coordinates):
    """ 원자 좌표들의 중심을 계산하는 함수 """
    return np.mean(coordinates, axis=0)

def calculate_distance(center1, center2):
    """ 두 중심간의 유클리드 거리를 계산하는 함수 """
    return np.linalg.norm(center1 - center2)

# 두 PDB 파일 읽기
coordinates1 = read_pdb("6c5t_xlig.pdb")
coordinates2 = read_pdb("Z56777699_top.pdb")

# 각 분자의 좌표 중심 계산
center1 = calculate_center_of_mass(coordinates1)
center2 = calculate_center_of_mass(coordinates2)

# 두 중심간 거리 계산
distance = calculate_distance(center1, center2)
print(f"Distance between centers: {distance} Å")
