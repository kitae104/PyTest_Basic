import pytest
import os
import smtplib

# yield을 활용한 Teardown
@pytest.fixture
def make_directory_and_txt_file_yield():
    directory_name = "/data/"
    directory_path = os.getcwd()+directory_name
    print(directory_path)


    # 테스트를 위한 임시 디렉토리 생성한다.
    try:
        if not(os.path.isdir(directory_path)):
            os.makedirs(os.path.join(directory_path))
            print("\nmake directory", directory_path)
    except Exception as e:
        print("make_directory() has error \n error message: {}".format(e)) 

    # 테스트를 위한 임시 파일을 생성한다. 
    file_name = "temp_data.txt"
    print("make file", file_name)
    f = open(directory_path+file_name, 'w')
    yield f   

    f.close()


