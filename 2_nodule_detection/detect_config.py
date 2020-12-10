config = {
    'anchors': [ 10.0, 30.0, 60.], 
    'chanel': 1,
    'pad_value': 170,
    'stride': 4, 
    'max_stride': 16,
    
    'anchors': [ 10.0, 30.0, 60.], 
    'chanel': 1, 
    'crop_size': [128, 128, 128], 
    'margin': 32, 
    'sidelen': 144, 
    'num_neg': 800, 
    'th_neg': 0.02,
    'th_pos_train': 0.5, 
    'num_hard': 2, 
    'bound_size': 12, 
    'reso': 1, 
    'sizelim': 6., 
    'sizelim2': 30, 
    'sizelim3': 40, 
    'aug_scale': True, 
    'r_rand_crop': 0.3,
    'luna_raw': True,
    'cleanimg': True, 
    'augtype': {'flip':True,'swap':False,'scale':True,'rotate':False},
    'lr_stage': [50,100,120], 
    'lr': [0.01,0.001,0.0001],
    'blacklist': [],
}