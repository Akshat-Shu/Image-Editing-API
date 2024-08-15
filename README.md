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
Multiple overlay images are supported since URLs allow for multiple values of the same parameters.
You can use the parameters: overlay_image_url, overlay_image_y, overlay_image_x, overlay_image_width and overlay_image_height to specify where you want to place the overlaying image and of what size.
overlay_image_url can be a URL of this very web service. Hence, an image edited from this web service can be pasted over another image.
<ins>EX:</ins> /edit_image?base_image=base.image?overlay_image_url=overlay_image_url1?overlay_image_url=overlay_image_url2 

Images are not stored as files or temp files on the Hard Disk of any system. They are only stored as variables on the RAM. Using the Pillow library secures against decompression bombs

Currently, this project only serves PNG Images But it may serve JPEG images too in the future depending on parameter value

Developed for Google Project IDX Hackathon

**NOTE:** /edit_image?base_image=base.jpg&overlay_image_url=overlay.png&rotate=45
and 
/edit_image?base_image=base.jpg&rotate=45&overlay_image_url=overlay.png
return different images. This is done to enable more functionality
