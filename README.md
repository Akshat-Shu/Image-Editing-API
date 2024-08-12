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
You can specify an Image URL for image to be overlayed using the overlay_image_url parameter, supports images with transparent backgrounds. You can optionally specify the overlay_image_x and overlay_image_y coordinate parameters.

The project's automated design makes it easy to create a new parameter that modifies the Images in wanted ways.

for base_image, you can even specify one of the encoded URL of this service itself. This means that overlay_image can be modified before overlaying on base_image. This also implies that one can create multiple layers of overlaying and multiple overlayed images.

This project is meant for use in those services which do not have the liberty to use image editing tools but can generate a URL based on their needs.


Images are not stored as files or temp files on the Hard Disk of any system. They are only stored as variables on the RAM. Using the Pillow library secures against decompression bombs

Currently, this project only serves PNG Images But it may serve JPEG images too in the future depending on parameter value

Developed for Google Project IDX Hackathon

**NOTE:** /edit_image?base_image=base.jpg&overlay_image_url=overlay.png&rotate=45
and 
/edit_image?base_image=base.jpg&rotate=45&overlay_image_url=overlay.png
return different images. This is done to enable more functionality
