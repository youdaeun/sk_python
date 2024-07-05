import os

current_directory = os.getcwd()
print(current_directory) # 현재 디렉토리의 경로를 출력

file_path = os.path.join(current_directory, "test.txt") # 현재 디렉토리와 파일명을 결합

if os.path.isfile(file_path):
    print(f"{file_path} 파일이다.")
else:
    print(f"{file_path} 파일이 아니다.")

if os.path.isdir(file_path):
    print(f"{file_path} 디렉토리이다.")
else:
    print(f"{file_path} 디렉토리가 아니다.")


