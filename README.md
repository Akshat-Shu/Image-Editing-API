## Image Editing "API"

This web service allows users to edit images just by modifying the URL and providing a Base Image

It currently has the following functionality:
* resize images
* crop images
* mirror images
* rotate images
* overlay images

### Resize Images:
provide the width and height parameters with values in pixels to resize, TODO: implement scaling

### Crop images
specify the crop_right, crop_left, crop_top and crop_bottom parameters in pixels to crop images

### Mirror images
specify the value of transpose parameter as one of the following: mirror, bottom_mirror, transpose or transverse
