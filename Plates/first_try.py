abc = 'abcdefghijklmnopqrstuvwxyz'

def next_plate(i):
    for letter in abc:
        i += 1
        yield letter, i

num_plates = 10000
i = 0
all_plates = {}

for plate,i in next_plate(i):
    if i > num_plates:
        break
    all_plates[i] = plate
    
if i < num_plates:
    for plate_1, _ in next_plate(i):
        for plate_2,i in next_plate(i):
            if i > num_plates:
                break
            all_plates[i] = plate_1 + plate_2
            
if i < num_plates:
    for plate_1, _ in next_plate(i):
        for plate_2, _ in next_plate(i):
            for plate_3,i in next_plate(i):
                if i > num_plates:
                    break
                all_plates[i] = plate_1 + plate_2 + plate_3
            
