import requests

def address_to_coordinates(api_key, secretcode, address):
    base_url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"

    params = {
        "query": address
    }
    
    headers = {
        "X-NCP-APIGW-API-KEY-ID": api_key,
        "X-NCP-APIGW-API-KEY": secretcode}

    response = requests.get(base_url, params=params, headers=headers)
    

    if response.status_code == 200:
        data = response.json()
        if data.get('addresses'):
            first_address = data['addresses'][0]
            longitude = first_address['x']  # 경도
            latitude = first_address['y']   # 위도
            
            return float(longitude),float(latitude)
        else:
            print("주소 정보를 찾을 수 없습니다.")
            return None
    else:
        print("API 요청 실패:", response.status_code)
        return None
    


# def get_coordinatelist(naver_api_key, secretcode, address_list) :
#     coordinate_list = []
#     for i in range(len(address_list)):
#         longitude,latitude =  address_to_coordinates(naver_api_key, secretcode, address_list[i])
#         print(i)
#         coordinate_list.append(str(longitude)+','+str(latitude))
#     print("coor" , coordinate_list)

#     return coordinate_list



# if __name__ == "__main__":
#     naver_api_key = "a986bwktfz"
#     secretcode= "uEQ7c34iw9s6XQNeIzcRungn858UJNL79g3ifFth"
#     address = "충청북도 청주시 서원구 모충로 32"  # 원하는 주소로 변경
#     address_list=["충청북도 청주시 서원구 사창동 367-7",
#                   "충청북도 청주시 서원구 1순환로680번길 13-11",
#                   "충청북도 청주시 서원구 모충로3번길 26",
#                   "충청북도 청주시 서원구 내수동로 140",
#                   "충청북도 청주시 서원구 창직로31번길 12-1"]

#     get_coordinatelist(naver_api_key, secretcode, address_list)



