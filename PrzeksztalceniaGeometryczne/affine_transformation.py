import numpy as np
import cv2 as cv
path = "../images/"
# mouse callback function
mouse_event = ['EVENT_MOUSEMOVE', 'EVENT_LBUTTONDOWN', 'EVENT_RBUTTONDOWN',
               'EVENT_MBUTTONDOWN', 'EVENT_LBUTTONUP','EVENT_RBUTTONUP',
               'EVENT_MBUTTONUP', 'EVENT_LBUTTONDBLCLK', 'EVENT_RBUTTONDBLCLK',
               'EVENT_MBUTTONDBLCLK', 'EVENT_MOUSEWHEEL', 'EVENT_MOUSEHWHEEL']
int_to_event = dict(zip((range(len(mouse_event))), mouse_event))

picked_points = []
def draw_circle(event,x,y,flags,param):
    # print(f'Event : {int_to_event[event]}')
    if event == cv.EVENT_LBUTTONDOWN:
        picked_points.append( (x, y) )
        cv.circle(img, (x, y), 5, (255, 0, 0), thickness=2)
    if event == cv.EVENT_RBUTTONDOWN:
        if len(picked_points) > 0:
            picked_points.pop()
    if event == cv.EVENT_MBUTTONUP:
        pts = np.array( [0, 0])
        for p in picked_points:
            pts = np.vstack( (pts, np.array([p[0], p[1]])) )
        pts = pts[1:, :]
        cv.polylines(img, [pts], True, color=(0, 0, 255), thickness=1)
        pts = pts.astype(np.float32)
        m = cv.getPerspectiveTransform(pts, dstPts)
        dst = cv.warpPerspective(img,m,(img.shape[0],img.shape[1]))
        cv.imshow('dst image',dst)



if __name__ == '__main__':
    img = cv.imread(path + 'road.jpg')
    dstPts = np.array([ [0, img.shape[1]], [0,0], [img.shape[0], 0],[img.shape[0], img.shape[1]] ],np.float32)
    print(dstPts)
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
