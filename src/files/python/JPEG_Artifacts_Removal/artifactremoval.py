import os.path
import numpy as np
from collections import OrderedDict
import torch
import cv2
from PIL import Image, ImageOps
import utils_image as util
from network_fbcnn import FBCNN as net
import requests
import datetime
import sys
# import torch_directml
def inference(input_img, is_gray, input_quality):
    
    # #print("datetime:",datetime.datetime.utcnow())
    input_img_width, input_img_height = Image.fromarray(input_img).size
    # #print("img size:",(input_img_width,input_img_height))
    
    if (input_img_width > 1080) or (input_img_height > 1080):
        resize_ratio = min(1080/input_img_width, 1080/input_img_height)
        resized_input = Image.fromarray(input_img).resize((int(input_img_width*resize_ratio)+(input_img_width*resize_ratio < 1),
                                                           int(input_img_height*resize_ratio)+(input_img_height*resize_ratio < 1)),
                                                          resample=Image.BICUBIC)
        input_img = np.array(resized_input)
        # #print("input image resized to:", resized_input.size)
        # script_directory = os.path.dirname(os.path.realpath(__file__))
    if is_gray:
        n_channels = 1 # set 1 for grayscale image, set 3 for color image
        script_directory = os.path.dirname(os.path.realpath(__file__))
        model_name = script_directory+'/fbcnn_gray.pth'
    else:
        n_channels = 3 # set 1 for grayscale image, set 3 for color image
        script_directory = os.path.dirname(os.path.realpath(__file__))
        model_name = script_directory+'/fbcnn_color.pth'
    nc = [64,128,256,512]
    nb = 4
    

    input_quality = 100 - input_quality

    model_path = model_name

    if os.path.exists(model_path):
        print(f'{model_path} already exists.')
    # else:
    #     #print("downloading model")
    #     os.makedirs(os.path.dirname(model_path), exist_ok=True)
    #     url = 'https://github.com/jiaxi-jiang/FBCNN/releases/download/v1.0/{}'.format(os.path.basename(model_path))
    #     r = requests.get(url, allow_redirects=True)
    #     open(model_path, 'wb').write(r.content)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # device = torch_directml.device(torch_directml.default_device())
    #print("device:",device)

    # ----------------------------------------
    # load model
    # ----------------------------------------
    
    #print(f'loading model from {model_path}')
    
    model = net(in_nc=n_channels, out_nc=n_channels, nc=nc, nb=nb, act_mode='R')
    #print("#model.load_state_dict(torch.load(model_path), strict=True)")
    model.load_state_dict(torch.load(model_path), strict=True)
    #print("#model.eval()")
    model.eval()
    #print("#for k, v in model.named_parameters()")
    for k, v in model.named_parameters():
        v.requires_grad = False
    #print("#model.to(device)")
    model = model.to(device)
    #print("Model loaded.")

    test_results = OrderedDict()
    test_results['psnr'] = []
    test_results['ssim'] = []
    test_results['psnrb'] = []

    # ------------------------------------
    # (1) img_L
    # ------------------------------------

    #print("#if n_channels")
    if n_channels == 1:
        open_cv_image = Image.fromarray(input_img)
        open_cv_image = ImageOps.grayscale(open_cv_image)
        open_cv_image = np.array(open_cv_image) # PIL to open cv image
        img = np.expand_dims(open_cv_image, axis=2)  # HxWx1
    elif n_channels == 3:
        open_cv_image = np.array(input_img) # PIL to open cv image
        if open_cv_image.ndim == 2:
            open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_GRAY2RGB)  # GGG
        else:
            open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2RGB)  # RGB

    #print("#util.uint2tensor4(open_cv_image)")
    img_L = util.uint2tensor4(open_cv_image)
    
    #print("#img_L.to(device)")
    img_L = img_L.to(device)

    # ------------------------------------
    # (2) img_E
    # ------------------------------------
    
    #print("#model(img_L)")
    img_E,QF = model(img_L)
    #print("#util.tensor2single(img_E)")
    img_E = util.tensor2single(img_E)
    #print("#util.single2uint(img_E)")
    img_E = util.single2uint(img_E)
    
    #print("#torch.tensor([[1-input_quality/100]]).cuda() || torch.tensor([[1-input_quality/100]])")
    qf_input = torch.tensor([[1-input_quality/100]]).cuda() if device == torch.device('cuda') else torch.tensor([[1-input_quality/100]])
    #print("#util.single2uint(img_E)")
    img_E,QF = model(img_L, qf_input)  

    #print("#util.tensor2single(img_E)")
    img_E = util.tensor2single(img_E)
    #print("#util.single2uint(img_E)")
    img_E = util.single2uint(img_E)

    if img_E.ndim == 3:
        img_E = img_E[:, :, [2, 1, 0]]
    
    #print("--inference finished")

    out_img = Image.fromarray(img_E)
   
    
    #print("--generating preview finished")
    
    return out_img
if __name__ == "__main__":
   

    input_img = np.array(Image.open(sys.argv[1]))  # Load your input image here

    is_gray = False  # Set this based on your image
    input_quality = int(sys.argv[2])  # Set the input quality


    out_img = inference(input_img, is_gray, input_quality)
    directory, full_filename = os.path.split(sys.argv[1])
    filename, extension = os.path.splitext(full_filename)
    output = directory+"/"+filename+"_cleaned.png"
    out_img.save(output)