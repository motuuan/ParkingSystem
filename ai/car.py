import requests
import base64
from datetime import datetime
import cv2 as cv

#车辆检测
def vehicle_detect(img, video_id):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image":base64_image}
    access_token = '24.9d9f90f4eee67ba6e17b661fa2007c74.2592000.1722755878.282335-90979262'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    vehicle_num = 0
    if response:
        #print('yes response')
        data = response.json()
        print(data)
        vehicle_num = data['vehicle_num']['car']
        for item in data['vehicle_info']:
            location = item['location']
            x1 = location['left']
            y1 = location['top']
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            cv.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            #print("运行到此了")

            #车牌识别api调用
            license_plate_request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
            license_plate_params = {"image": base64_image}
            license_plate_request_url = license_plate_request_url + "?access_token=" + access_token
            license_plate_response = requests.post(license_plate_request_url, data=license_plate_params,
                                                   headers=headers)
            if license_plate_response:
                plate_data = license_plate_response.json()
                #print(plate_data)
                plate_number = plate_data['words_result']['number']
                plate_color = plate_data['words_result']['color']

            #text = item['type']
            vehicle_type = item['type']
            text = f"{vehicle_type} - {plate_number} ({plate_color})"


            position = (x1, y1-10)
            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (0, 255, 0)
            thickness = 2
            img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)

            if video_id == 1:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 格式化当前时间
                with open('data/RecordIn.txt','a') as file:
                    file.write(f"'车辆' {vehicle_num}: '车牌号：' {plate_number},'车牌颜色：' {plate_color}'色','车型：'{vehicle_type},'入场时间': {current_time}\n")
            if video_id == 2:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open('data/RecordOut.txt','a') as file:
                    file.write(f"'车辆' {vehicle_num}: '车牌号：' {plate_number},'车牌颜色：' {plate_color}'色','车型：'{vehicle_type},'出场时间': {current_time}\n")
    return img, vehicle_num, plate_number,vehicle_type

    # # 等待按键，然后关闭窗口
    cv.waitKey(0)
    cv.destroyAllWindows()
