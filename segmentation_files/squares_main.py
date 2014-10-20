import math
import cv2.cv as cv
import Image
import numpy as np
import glob
import os
import shutil
import wx

#filename=build1_1.png
def crop_img(filename,image):
    with open(r"C:\3d-Model\bin\a.txt",'w') as f:
        f.write(str(filename) + "  " + str(image) )
    flag=0
    pic_name=filename[:filename.find("_")] # pic_name=build1
    print pic_name 
    text_name=filename[:filename.find(".")]+".txt" # text_name= build1_1.txt
    src="C:\\3d-Model\\bin\\segmentation_files\\"+text_name # src=C:\\3d-Model\\bin\\segmentation_files\\build1_1.txt
    #fil = open(src,'w+') #to create file if not exists
    #fil.close()
    with open("C:\\3d-Model\\bin\\curr_proj.txt","r") as f: #Read whole file into data
        proj_name = f.read()  #proj_name= C:\\3d-Model\\projects\\Ashish
    main_directory=proj_name+"\\input"  #main_directory=C:\\3d-Model\\projects\\Ashish\\input
    print main_directory  
    image_data = np.asarray(image) #Input data, in any form that can be converted to an array. This includes lists, lists of tuples, tuples, tuples of tuples, tuples of lists and ndarrays.
    image_data_bw = image_data.max(axis=2)
    non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
    non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
    cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))
    image1=Image.open("C:\\3d-Model\\bin\\segmentation_files\\pic.jpg")
    image1.load()
    image_data1=np.asarray(image1)
    image_data_new = image_data1[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 , :]
    new_image = Image.fromarray(image_data_new) 
    folders=os.listdir(main_directory) #main_directory=C:\\3d-Model\\projects\\Ashish\\input
    print folders
    #this loop will traverse all files in the folders of the input folder
    if os.path.isdir(main_directory+"\\"+pic_name) == True:
        print main_directory+"\\"+pic_name
        dst=main_directory+"\\"+pic_name
        new_image.save(main_directory+"\\"+pic_name+"\\"+filename)
        shutil.copy (src, dst)
        os.remove(src)
        print "save"

    #flag=0 means that the folder of the building was not found in the input folder, hence we will create that folder
    else:
        os.mkdir(main_directory+"\\"+pic_name)
        dst=main_directory+"\\"+pic_name
        new_image.save(main_directory+"\\"+pic_name+"\\"+filename)
        shutil.copy (src, dst)
        os.remove(src)
        print "made" 
     
def angle(pt1, pt2, pt0):
    "calculate angle contained by 3 points(x, y)"
    dx1 = pt1[0] - pt0[0]
    dy1 = pt1[1] - pt0[1]
    dx2 = pt2[0] - pt0[0]
    dy2 = pt2[1] - pt0[1]

    nom = dx1*dx2 + dy1*dy2
    denom = math.sqrt( (dx1*dx1 + dy1*dy1) * (dx2*dx2 + dy2*dy2) + 1e-10 )
    ang = nom / denom
    print ang
    return ang

def is_square(contour):
    """
    Squareness checker

    Square contours should:
        -have 4 vertices after approximation,
        -have relatively large area (to filter out noisy contours)
        -be convex.
        -have angles between sides close to 90deg (cos(ang) ~0 )
    Note: absolute value of an area is used because area may be
    positive or negative - in accordance with the contour orientation
    """

    area = math.fabs( cv.ContourArea(contour) )
    isconvex = cv.CheckContourConvexity(contour)
    s = 0
    if len(contour) == 4 and area > 100 and isconvex:
        for i in range(1, 4):
            # find minimum angle between joint edges (maximum of cosine)
            pt1 = contour[i]
            pt2 = contour[i-1]
            pt0 = contour[i-2]
            
           
            t = math.fabs(angle(pt0, pt1, pt2))
            if s <= t :
                s = t
                

        # if cosines of all angles are small (all angles are ~90 degree)
        # then its a square
        if s < .6 :
            return True
                
    return False

def find_squares_from_binary( gray ):
    """
    use contour search to find squares in binary image
    returns list of numpy arrays containing 4 points
    """
    squares = []
    storage = cv.CreateMemStorage(0)
    contours = cv.FindContours(gray, storage, cv.CV_RETR_TREE, cv.CV_CHAIN_APPROX_SIMPLE, (0,0))
    storage = cv.CreateMemStorage(0)
    while contours:
        #approximate contour with accuracy proportional to the contour perimeter
        arclength = cv.ArcLength(contours)
        polygon = cv.ApproxPoly( contours, storage, cv.CV_POLY_APPROX_DP, arclength * 0.02, 0)
        if is_square(polygon):
            squares.append(polygon[0:4])
        contours = contours.h_next()

    return squares

def find_squares4(color_img):
    """
    Finds multiple squares in image

    Steps:
    -Use Canny edge to highlight contours, and dilation to connect
    the edge segments.
    -Threshold the result to binary edge tokens
    -Use cv.FindContours: returns a cv.CvSequence of cv.CvContours
    -Filter each candidate: use Approx poly, keep only contours with 4 vertices,
    enough area, and ~90deg angles.

    Return all squares contours in one flat list of arrays, 4 x,y points each.
    """
    #select even sizes only
    width, height = (color_img.width & -2, color_img.height & -2 )
    timg = cv.CloneImage( color_img ) # make a copy of input image
    gray = cv.CreateImage( (width,height), 8, 1 )

    # select the maximum ROI in the image
    cv.SetImageROI( timg, (0, 0, width, height) )

    # down-scale and upscale the image to filter out the noise
    pyr = cv.CreateImage( (width/2, height/2), 8, 3 )
    cv.PyrDown( timg, pyr, 7 )
    cv.PyrUp( pyr, timg, 7 )

    tgray = cv.CreateImage( (width,height), 8, 1 )
    squares = []

    # Find squares in every color plane of the image
    # Two methods, we use both:
    # 1. Canny to catch squares with gradient shading. Use upper threshold
    # from slider, set the lower to 0 (which forces edges merging). Then
    # dilate canny output to remove potential holes between edge segments.
    # 2. Binary thresholding at multiple levels
    N = 11
    for c in [0, 1, 2]:
        #extract the c-th color plane
        cv.SetImageCOI( timg, c+1 );
        cv.Copy( timg, tgray, None );
        cv.Canny( tgray, gray, 0, 50, 5 )
        cv.Dilate( gray, gray)
        squares = squares + find_squares_from_binary( gray )

        # Look for more squares at several threshold levels
        for l in range(1, N):
            cv.Threshold( tgray, gray, (l+1)*255/N, 255, cv.CV_THRESH_BINARY )
            squares = squares + find_squares_from_binary( gray )

    return squares


RED = (0,0,255)
GREEN = (0,255,0)
def draw_squares( color_img, squares ):
    """
    Squares is py list containing 4-pt numpy arrays. Step through the list
    and draw a polygon for each 4-group
    """
    color, othercolor = RED, GREEN
    for square in squares:
        cv.PolyLine(color_img, [square], True, color, 3, cv.CV_AA, 0)
        color, othercolor = othercolor, color
    
    #cv.ShowImage(WNDNAME, color_img)
    cv.SaveImage('C:\\3d-Model\\bin\\segmentation_files\\pic_square.jpg', color_img) # save the image as jpg

#WNDNAME = "Squares Demo"
def main():
    """Open test color images, create display window, start the search"""
    #cv.NamedWindow(WNDNAME, 1)
    
    os.chdir("C:\\3d-Model\\bin\\segmentation_files")
    for fil in glob.glob("*.png"):
   
        img0 = cv.LoadImage(fil, cv.CV_LOAD_IMAGE_COLOR)
        try:
            img0
        except ValueError:
            print "Couldn't load %s\n" % fil
            continue
        # slider deleted from C version, same here and use fixed Canny param=50
        img = cv.CloneImage(img0)
        img1 = cv.CreateImage((img0.width, img0.height), 8, 3)

        #cv.ShowImage(WNDNAME, img1)

        # force the image processing

        draw_squares( img1, find_squares4( img ) )

        image=Image.open("C:\\3d-Model\\bin\\segmentation_files\\pic_square.jpg")
        image.load()

        crop_img(fil,image)

        directory="C:\\3d-Model\\bin\\segmentation_files\\"+ fil
        os.remove(directory)
        print "removed"
    try:
        os.remove("C:\\3d-Model\\bin\\segmentation_files\\pic.jpg")
    except:
        pass
    try:
        os.remove("C:\\3d-Model\\bin\\segmentation_files\\pic_blur.jpg")
    except:
        pass
    try:
        os.remove("C:\\3d-Model\\bin\\segmentation_files\\pic_contours.jpg")
    except:
        pass
    try:
        os.remove("C:\\3d-Model\\bin\\segmentation_files\\pic_resize.jpg")
    except:
        pass
    try:
        os.remove("C:\\3d-Model\\bin\\segmentation_files\\pic_seg.jpg")
    except:
        pass
    try:
        os.remove("C:\\3d-Model\\bin\\segmentation_files\\pic_square.jpg")
    except:
        pass

    print "DONE!!! Segmentation completed successfully"
    #log code contour to file for progress
    with open('C:\\3d-Model\\bin\\segmentation_files\\progress.txt', 'w') as myFile:
            myFile.write("crop")
    cv.DestroyAllWindows()

if __name__ == "__main__":
    main()
