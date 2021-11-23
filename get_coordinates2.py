import os
import cv2
import cv2.aruco as aruco


### --- aruco設定 --- ###
dict_aruco = aruco.Dictionary_get(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters_create()
img_path_name = "test.png"  # 対象画像の名前
bace = os.path.dirname(os.path.abspath(__file__))  # 実行ファイルのディレクトリ名
target_path = os.path.join(bace, img_path_name)  # パスの連結
image = cv2.imread(target_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
height, width, channels = image.shape[:3]
ColorCyan = (255, 255, 0)

# #マーカーの四隅の座標を配列に格納する。
# def getMarkerMean(corners):
#     v = np.mean(corners,axis=0) # マーカーの四隅の座標から中心の座標を取得する
#     return [corners[0], corners[1], corners[2], corners[3]]


def getMarkerCoordinates(ids, corners):
    identification = []
    coordinates = []
    for i, id in enumerate(ids):
        identification.append(id[0])
        coordinates.append(corners[i][0].tolist())
    return identification, coordinates


def show(image):
    # 0.5倍のサイズで表示する
    magnification = 0.5
    image = cv2.resize(image, (int(width * magnification),
                       int(height * magnification)))
    cv2.imshow('image', image)
    cv2.waitKey(0)


def main(path: str = "test.png"):
    corners, ids, _rejectedImgPoints = aruco.detectMarkers(image, dict_aruco)
    # マーカーのIDと座標を取得)
    marker_ids, marker_coords = getMarkerCoordinates(ids, corners)
    # print(corners)
    aruco.drawDetectedMarkers(image, corners, ids, ColorCyan)
    # show(image)
    # print(marker_ids)
    # print(marker_coords)
    return marker_ids, marker_coords


cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
