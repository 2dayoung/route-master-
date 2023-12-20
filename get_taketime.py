import requests

def get_travel_time(api_key, secretcode,start, destination):
    base_url = "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving"

    params = {
        "start": start,          # 출발지 주소 또는 좌표
        "goal": destination,     # 목적지 주소 또는 좌표
    }
    
    headers = {
        "X-NCP-APIGW-API-KEY-ID": api_key,
        "X-NCP-APIGW-API-KEY": secretcode
    }

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        route = data["route"]
        path = route["traoptimal"][0]  # 가장 최적의 경로를 선택
        distance = path["summary"]["distance"]  #meter
        duration = path["summary"]["duration"]  #millisecond(1/1000초)

            # 밀리초를 초로 변환
        seconds = duration / 1000

        return distance, seconds
    else:
        print("API 요청 실패:", response.status_code)
        return None

# if __name__ == "__main__":
#     naver_api_key = "a986bwktfz"
#     secretcode= "uEQ7c34iw9s6XQNeIzcRungn858UJNL79g3ifFth"
#     start_location = "127.1058342,37.359708"
#     destination_location = "129.075986,35.179470"

#     distance, duration = get_travel_time(naver_api_key, start_location, destination_location)

#     if duration:
#         print(f"출발지에서 목적지까지 {distance}m 거리이며, 약 {duration}분 소요됩니다.")
