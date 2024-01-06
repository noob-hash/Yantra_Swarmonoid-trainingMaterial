import cv2
import numpy as np

def generate_aruco_image(marker_id, marker_size=50):
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
    marker_image = cv2.aruco.drawMarker(aruco_dict, marker_id, marker_size)
    marker_image_bgr = cv2.cvtColor(marker_image, cv2.COLOR_GRAY2BGR)
    return marker_image_bgr

# Create an image to place ArUco markers
aurco_size = 50 #also equals grid size
no_of_grid = 22
image_size = aurco_size * no_of_grid
canvas = np.ones((image_size, image_size, 3), dtype=np.uint8) * 255

# Positions for markers 0-3 from top-left to bottom-right corners and waste collection 4 & 5
positions = {
    0: (aurco_size, aurco_size), #topleft
    1: (aurco_size, image_size - aurco_size*2),#topright
    2: (image_size - aurco_size*2, aurco_size), #bottomleft
    3: (image_size - aurco_size*2, image_size - aurco_size*2), #bottomright
    4: (11*aurco_size,aurco_size), #nororganic waste center
    5: (aurco_size, 11*aurco_size) #organic waste center
}

# Generate markers with IDs 0-5 and place them on the canvas
for marker_id, position in positions.items():
    marker = generate_aruco_image(marker_id)
    x, y = position
    canvas[y:y + 50, x:x + 50] = marker

positions_bot_waste_y = {
    6: [(14*aurco_size, 9*aurco_size)], #bot 1
    7: [(11*aurco_size, 11*aurco_size)], #bot 2
    8: [ #8 is non organic
        (7*aurco_size,7*aurco_size),
        (7*aurco_size,14*aurco_size),
        (14*aurco_size,15*aurco_size),
        (11*aurco_size,18*aurco_size),
        (18*aurco_size,7*aurco_size)
        ],
    9: [ #9 is organic
        (8*aurco_size,9*aurco_size),
        (12*aurco_size,9*aurco_size),
        (9*aurco_size,13*aurco_size),
        (8*aurco_size,18*aurco_size),
        (18*aurco_size,13*aurco_size)
        ],
}

# Generate markers with IDs 6 and 9 and place them in playable grid
for marker_id, positions_list in positions_bot_waste_y.items():
    for position in positions_list:
        marker = generate_aruco_image(marker_id)
        x, y = position
        canvas[y:y + aurco_size, x:x + aurco_size] = marker

# Display the image with ArUco markers
cv2.imshow("ArUco Markers", canvas)
cv2.imwrite("images/TestGround.png", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
