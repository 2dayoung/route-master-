import json
import algori
def jjson() : 

    # 데이터 생성 및 초기화
    min_path,dict_123 = algori.main()
    
    new_data = {
    "list": [
        {"num": "1", "address": "1번지"},
        {"num": "2", "address": "2번지"},
        {"num": "3", "address": "11번지"}
    ]
    }

    # JSON 파일 생성 (쓰기)
    with open('new_example.json', 'w') as new_file:
        json.dump(new_data, new_file, indent=2)

    # JSON 파일 읽기
    with open('new_example.json', 'r') as new_file:
        loaded_data = json.load(new_file)

    return loaded_data


# # 데이터 수정
# loaded_data['age'] = 26
# loaded_data['city'] = 'New Wonderland'

# # 수정된 데이터를 다시 JSON 파일에 쓰기
# with open('new_example.json', 'w') as new_file:
#     json.dump(loaded_data, new_file, indent=2)

# # 수정된 JSON 파일 읽기
# with open('new_example.json', 'r') as new_file:
#     final_loaded_data = json.load(new_file)

# 최종 데이터 출력
# print(final_loaded_data)

def jjsonpy() : 
        
    min_path,dict_123 = algori.main()
        

    # 예시 JSON 데이터
    # json_data = {
    #     "list": [
    #         {"num": "3", "address": "3번지"},
    #         {"num": "1", "address": "1번지"},
    #         {"num": "2", "address": "2번지"}
    #     ]
    # }

    json_data = {"list" : []}
    result_dict = {str(key): value for key, value in dict_123.items()}
    all_dict = {}
    for key, value in dict_123.items() :
        part = {"num": str(key), "address": value[0],"coordinate": value[1]}
        json_data["list"].append(part)

    print(" json data : " ,json_data)
        

    # print("r d " , result_dict)

    
    
    # min_path의 int를 str로 바꿈
    path = ['0'] + [str(num) for num in min_path]

    print(path)

    # 'num' 값을 기준으로 정렬
    sorted_users = sorted(json_data["list"], key=lambda x: path.index(str(x["num"])))


    # # 정렬된 순서에 따라 'address' 값을 출력
    result_addresses = [user["address"] for user in sorted_users]

    # 결과 출력
    # print("Sorted Users:", sorted_users)
    # print("Result Addresses:", result_addresses)

    # JSON 데이터에 정렬된 결과를 추가
    json_data["list"] = sorted_users

    # 결과 JSON 출력
    result_json = json.dumps(json_data, indent=2)
    # print("       JSON:", json_data)
    # print("Result JSON:", result_json)
    
    return json_data


