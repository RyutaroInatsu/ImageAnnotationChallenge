import os, glob


target_dir = "./inputs/avoid/rename"
output_dir = "./inputs/avoid/renamed"
saved_image_count = 0

for i in glob.glob(os.path.join(target_dir, "*.jpg")):
    os.rename(i, os.path.join(output_dir, f"1{str(saved_image_count).zfill(5)}.jpg"))
    saved_image_count +=1