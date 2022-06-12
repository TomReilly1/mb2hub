# id="simple_back_sword_t2"
# name="{=IK2Z9zWk}Simple Scimitar"

# <Piece id="khuzait_blade_7" Type="Blade" scale_factor="90" />
#     scale_factor="90"
#     length="82.5"
#     weight="0.85">
#     stack_amount="3"
#     <Thrust damage_type="Pierce" damage_factor="2.1" />
#     <Swing damage_type="Cut" damage_factor="3.1" />

# <Piece id="sturgian_guard_7" Type="Guard" scale_factor="100" />
#     scale_factor="100"
#     length="2.4"
#     weight="0.22">

# <Piece id="khuzait_grip_16" Type="Handle" scale_factor="100" />
    # scale_factor="100"
#     length="27"
#     weight="0.1">
# <Piece id="cleaver_pommel_1" Type="Pommel" scale_factor="100" />
#     scale_factor="100"
#     length="5.255"
#     weight="0.14">

# scaled = 82.5 * 0.9
# blade = {'length': 82.5 * 0.9, 'weight': 0.85 * 0.9}
# guard = {'length': 2.4, 'weight': 0.22}
# handle = {'length': 27, 'weight': 0.1}
# pommel = {'length': 5.255, 'weight': 0.14}
# parts = (blade, guard, handle, pommel)

# length = 0
# weight = 0
# for part in parts:
#     length += part['length']
#     weight += part['weight']

# print(length)
# print(weight)


# try:
#     x = '5'
#     y = 'hello'
#     x = int(x)
#     y = int(y)
# except:
#     print('error')

import re
 
# Initialising string
ini_str = 'Crossbow'
 
# Printing Initial string
print ("Initial String", ini_str)
 

res_list = []
res_list = re.findall('[A-Z][^A-Z]*', ini_str)
res_list = '_'.join(res_list).lower()

print('Python Case', res_list)
