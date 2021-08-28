# Chương trình tính toán và phân tích điểm thi
Chương trình được dùng để tính toán điểm kiểm thi của sinh viên dựa trên kết quả bài làm và file đáp án cho trước. Kết quả sẽ được hiển thị trên màn hình console và kết quả điểm thi của từng lớp sẽ được lưu vào trong thư mục `./result` ví dụ `./result/class1_grades.txt` cho kết quả của class 1.
## Cài đặt
Chương trình có sử dụng các thư viện [**numpy**](https://numpy.org/install/) và [**pandas**](https://pandas.pydata.org/docs/getting_started/install.html) cần cài đặt trước khi sử dụng. Nhấn vào link để cài đặt nếu chưa có.
```
git clone https://github.com/quanhoangm/MLP301x_asm1_FX10282.git
```
## Sử dụng
Lưu file bài làm của sinh viên cần chấm vào thư mục `./Data Files` ví dụ `./Data Files/class1.txt` Sử dụng terminal cd đến thư mục vừa clone xuống từ _github_ và chạy file _quan_hoangminh_grade_the_exams.py_
```
cd D:\MLP301x_asm1_FX10282
python quan_hoangminh_grade_the_exams.py
```
Sau đó chương trình sẽ có 3 lựa chọn:
```
+-------------------Menu------------------+
Grade the exam:
0.Exit
1.Xử lý thông thường
2.Xử lý bằng Pandas và numpy
+-----------------------------------------+
```
- Nhấn 0 để thoát chương trình
- Nhấn 1 để xử lý thông thường
- Nhấn 2 để xử lý bằng thư viện numpy và pandas
 
Lưu ý chức năng 1 và 2 sẽ cho qua kết quả giống nhau.
Sau đó chương trình sẽ yêu cầu nhập tên file, lưu ý tên file sẽ không bao gồm phần mở rộng, ví dụ nhập `class1` cho file `class1.txt` sau đó chương trình sẽ hiển thị kết quả xử lý ở giao diện console, file điểm sau khi xử lý được lưu ở thư mục `./result` 
Ví dụ kết quả sau khi xử lý bài làm của 1 lớp:
```
Enter a class to grade (i.e. class1 for class1.txt): class1
Successful open  class1.txt

**** ANALYZING ****
No errors found
**** REPORT ****
Total valid lines of data:  20
Total invalid lines of of data:  0
Mean (aveerage) score:  75.6
Highest score:  91
Lowest score:  59
Range of score:  32
Median score:  73.0
```
## Các lỗi thường gặp:
1. Nhập không đúng tên file :
``` 
Enter a class to grade (i.e. class1 for class1.txt): class
File cannot be found. Please try again!
```
Vui lòng nhập đúng tên file, không kèm phần mở rộng
2. Toàn bộ dữ liệu bị lỗi

Thông tin bài làm của sinh viên trong file text phải tuân thủ yêu cầu sau:
- Một dòng hợp lệ chứa danh sách 26 giá trị được phân tách bằng dấu phẩy
- N# cho một học sinh là mục đầu tiên trên dòng. Nó phải chứa ký tự “N” theo sau là 8 ký tự số.





