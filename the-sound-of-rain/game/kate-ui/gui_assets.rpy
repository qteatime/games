init offset = -2

init python:
  def im_invert(img):
    return im.MatrixColor(img, im.matrix.invert())

define kate_cancel_bare = Image("kate-ui/images/cancel-bare.png")
define kate_ok_bare = Image("kate-ui/images/ok-bare.png")
define kate_cancel = im_invert(Image("kate-ui/images/cancel.png"))
define kate_ok = im_invert(Image("kate-ui/images/ok.png"))
define kate_down = Image("kate-ui/images/down.png")
define kate_left = Image("kate-ui/images/left.png")
define kate_right = Image("kate-ui/images/right.png")
define kate_up = Image("kate-ui/images/up.png")
define kate_l = Image("kate-ui/images/l.png")
define kate_r = Image("kate-ui/images/r.png")
define kate_menu = Image("kate-ui/images/menu.png")
define kate_capture = Image("kate-ui/images/capture.png")

define kate_cancel_dark = im_invert(kate_cancel)
define kate_ok_dark = im_invert(kate_ok)
define kate_cancel_bare_dark = im_invert(kate_cancel_bare)
define kate_ok_bare_dark = im_invert(kate_ok_bare)
define kate_down_dark = im_invert(kate_down)
define kate_left_dark = im_invert(kate_left)
define kate_right_dark = im_invert(kate_right)
define kate_up_dark = im_invert(kate_up)
define kate_l_dark = im_invert(kate_l)
define kate_r_dark = im_invert(kate_r)
define kate_menu_dark = im_invert(kate_menu)
define kate_capture_dark = im_invert(kate_capture)
