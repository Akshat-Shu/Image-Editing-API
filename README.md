## Image Editing "API"

This web service allows users to edit images just by modifying the URL and providing a Base Image

It currently has the following functionality:
* Resize Images
* Crop Images
* Mirror Images
* Rotate Images
* Overlay Images

### Resize Images:
provide the width and height parameters with values in pixels to resize, TODO: implement scaling

### Crop Images
specify the crop_right, crop_left, crop_top and crop_bottom parameters in pixels to crop images

### Mirror Images
specify the value of transpose parameter as one of the following: mirror, bottom_mirror, transpose or transverse

### Rotate Images
you can rotate the images by specifying the rotate parameter in degrees (can be a floating point number).
Further, you can specify the rotate_expand parameter as true or false 
TODO: specify rotate_background_color in hex

### Overlay Images


Images are not stored as files or temp files on the Hard Disk of any system. They are only stored as variables on the RAM. Using the Pillow library secures against decompression bombs