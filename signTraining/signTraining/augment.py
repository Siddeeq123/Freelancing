import Augmentor
p = Augmentor.Pipeline(r"C:\Users\safwa\Desktop\signTraining\NewDataSet\E")
p.zoom(probability=0.3,min_factor=0.8,max_factor=1.4)
p.flip_left_right(probability=0.5)
p.random_brightness(probability=0.3,min_factor=0.3,max_factor=1.2)
p.random_distortion(probability=0.5,grid_width=4,grid_height=4,magnitude=8)
p.zoom_random(probability=0.2, percentage_area=0.9)
p.sample(285)