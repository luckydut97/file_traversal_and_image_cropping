import os
import cv2

#폴더 순회
for folder_name, subfolders, filenames in os.walk('.\\Image'):
    print('\n')
    print('상위 디렉토리 : ' + folder_name)
    for subfolder in subfolders:
        print('하위 디렉토리 : ' + folder_name + ': ' + subfolder)

    for filename in filenames:
        print('파일명 : ' + folder_name + ': ' + filename)
        if os.path.splitext(filename)[1] == '.jpg': #jpg 파일만 처리
            img = cv2.imread(folder_name + '\\' + filename)

            # cutting
            cut_image = img[180:1000, 670:1300]

            # resizing
            scaleX = 0.6
            scaleY = 0.6
            scaledown_img = cv2.resize(cut_image, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)

            # scaledown 한 img 저장 및 삭제
            save_file = ''+filename+'.jpg'  # 저장할 이름 지정
            cv2.imwrite(folder_name + '\\' + save_file, scaledown_img)  # 파일저장
            os.remove(folder_name + '\\' + filename) #파일 삭제