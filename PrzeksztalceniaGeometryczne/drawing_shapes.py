import numpy as np
import cv2 as cv
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
# mouse callback function
mouse_event = ['EVENT_MOUSEMOVE', 'EVENT_LBUTTONDOWN', 'EVENT_RBUTTONDOWN',
               'EVENT_MBUTTONDOWN', 'EVENT_LBUTTONUP','EVENT_RBUTTONUP',
               'EVENT_MBUTTONUP', 'EVENT_LBUTTONDBLCLK', 'EVENT_RBUTTONDBLCLK',
               'EVENT_MBUTTONDBLCLK', 'EVENT_MOUSEWHEEL', 'EVENT_MOUSEHWHEEL']
int_to_event = dict(zip((range(len(mouse_event))), mouse_event))
def draw_circle(event,x,y,flags,param):
    print(f'Event : {int_to_event[event]}')
    print(x, y)
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 5, (255, 0, 0), thickness=2)
    if event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x, y), (x+50, y+50), (0, 255, 0), thickness=3)


if __name__ == '__main__':
    img = np.zeros((512,512,3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image',draw_circle)
    while(1):
        cv.imshow('image',img)
        k = cv.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break
    cv.destroyAllWindows()
