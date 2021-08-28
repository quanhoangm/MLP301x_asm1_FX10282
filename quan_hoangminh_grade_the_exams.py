import re
import numpy as np
import pandas as pd
class lopHoc:
    def __init__(self,filePath):
        self.filePath=filePath
        # tạo 1 dictionary với key là mã số sinh viên, value là list các câu trả lời
        self.validScore=dict() 
        # Đối với invalid score thì key là thông tin của 1 hàng và value là loại lỗi của hàng thông tin đó
        self.invalidScore=dict()
        # Tạo 1 dictionary để lưu MSSV, điểm để tiện cho việc report và ghi dữ liệu
        self.analyzedScore=dict()
        # Có 2 loại lỗi values ở invalidScode sẽ là chỉ số ở list typeOfFault
        self.typeOfFault=['do not contain exactly 26 values','N# is invalid']
    def analyzing(self):
        print("**** ANALYZING ****")
        # Check MSSV theo pattern là N đầu tiên và tiếp theo có 8 số.
        pattern=re.compile(r'N+(\d{8})')
        with open(self.filePath,'r+') as file:
            for line in file:
                lst=line.strip().split(',')
                mssv=lst[0] 
                checkMssv=pattern.search(mssv)
                # Kiểm tra nếu hợp lệ thì cho vào dict validScore
                if (len(lst)==26 and checkMssv):
                    self.validScore[mssv]=lst[1:]
                else:
                # nếu không hợp lệ thì cho vào dict invalidScore và phân loại lỗi của dữ liệu.
                    if (len(lst)!=26):
                        self.invalidScore[line]=0
                    else:
                        self.invalidScore[line]=1
        if (len(self.invalidScore)==0):
            print("No errors found")
        else:
            for key in self.invalidScore:
                print('Invalid type of data:',self.typeOfFault[self.invalidScore[key]])
                print(key)
    def evaluate(self,lst):
        answer_key=lst.strip().split(',')
        for key in self.validScore:
            score=0
            # Tính điểm nếu đúng thì +4 nếu bỏ qua thì tính 0 còn nếu sai thì tính 1
            for i in range(len(answer_key)):
                if self.validScore[key][i]==answer_key[i]:
                    score+=4
                elif self.validScore[key][i]=='':
                    pass
                else:
                    score-=1
            self.analyzedScore[key]=score

    def report(self):
        print("**** REPORT ****")
        print('Total valid lines of data: ',len(self.validScore))
        print('Total invalid lines of of data: ', len(self.invalidScore))
        scoreList=list(self.analyzedScore.values())
        print('Mean (aveerage) score: ',round(sum(scoreList)/len(scoreList),1))
        print('Highest score: ', max(scoreList))
        print('Lowest score: ', min(scoreList))
        print('Range of score: ',max(scoreList)-min(scoreList))
        # Tìm median, kiểm tra xem số lượng học sinh là số chẵn hay lẻ, nếu lẻ thì lấy điểm giữa
        # nếu chẵn thì lấy trung bình 2 điểm ở giữa
        n=len(scoreList)
        # Trước khi tìm trung vị thì phải sắp xếp lại trước
        scoreList=sorted(scoreList)
        if(n%2!=0):
            median=scoreList[n//2]
        else:
            median= (scoreList[n//2]+scoreList[n//2-1])/2
        print('Median score: ',median)
    def exportResult(self):
        # Lấy thông tin tên file hiện tại
        name=self.filePath.split('/')[-1]
        pureName=name.split('.')[0]

        # Từ thông tin file hiện tại thêm _grades vào và bắt đầu ghi dữ liệu
        newFilePath='./Result/'+pureName+'_grades.txt'
        with open(newFilePath,'w') as file:
            firstLine=pureName+ ' grades: \n'
            file.write(firstLine)
            file.write("Class 1 grades:\n")
            for key,values in self.analyzedScore.items():
                result=key+','+str(values)+'\n'
                file.write(result)

# Tạo class controller để hiển thị menu cho 2 phương án là xử lý thông thường và xử lý theo python
class Controller:
    def __init__(self):
        self.path=''
    def openFile(self):
        check=True
        defaultFolder='./Data files/'
        while check:
            try:
                str=input('Enter a class to grade (i.e. class1 for class1.txt): ')
                filePath=defaultFolder+ str+'.txt'
                with open(filePath,'r') as file:
                    check=False
                    print("Successful open ",str+'.txt','\n')
            except:
                print('File cannot be found. Please try again!')
        self.path=filePath
    def do_1(self):
        "Xử lý thông thường"
        self.openFile()
        chamDiem=lopHoc(self.path)
        chamDiem.analyzing()
        answer_key="B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
        chamDiem.evaluate(answer_key)
        chamDiem.report()
        chamDiem.exportResult()
    def do_2(self):
        "Xử lý bằng Pandas và numpy"
        self.openFile()
        # sử dụng lại class Lophoc để phân tích các dòng dữ liệu bị dư, thiếu hay sai mssv, các dòng dữ liệu hợp lệ sẽ được đưa vào pandas để xử lý
        chamDiem=lopHoc(self.path)
        chamDiem.analyzing()
        df=pd.DataFrame(chamDiem.validScore)
        # Report
        answer_key="B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
        df['answer_key']=answer_key.split(',')

        # Bắt đầu in report
        print("**** REPORT ****")
        print('Total valid lines of data: ',len(chamDiem.validScore))
        print('Total invalid lines of of data: ', len(chamDiem.invalidScore))

        # Tạo 1 dataframe mới thay các dòng đáp án bằng các dòng điểm
        df_score=pd.DataFrame(columns=df.columns[:-1])
        for col in df.columns[:-1]:
            # Dùng điều kiện để xác định nếu đúng thì +4 nếu bỏ trống thì 0 còn sai thì -1 điểm
            condition=[(df[col]==df['answer_key']),df[col]=='']
            choices=[4,0]
            df_score[col]=np.select(condition,choices,default=-1)
        # chuyển dữ liệu và dạng hàng cho dễ tính lúc này index sẽ là MSSV
        df_score=df_score.transpose()
        # Thêm cột total để tính điểm sinh viên
        df_score['total']=df_score.sum(axis=1)

        # In ra các dữ liệu thống kê từ cột total
        print('Mean (aveerage) score: ',df_score['total'].mean())
        print('Highest score: ', df_score['total'].max())
        print('Lowest score: ', df_score['total'].min())
        print('Range of score: ',df_score['total'].max()-df_score['total'].min())
        print('Median score: ',df_score['total'].median())

        # Ghi dữ liệu
        # Lấy thông tin tên file hiện tại
        name=self.path.split('/')[-1]
        pureName=name.split('.')[0]

        # Từ thông tin file hiện tại thêm _grades vào và bắt đầu ghi dữ liệu
        newFilePath='./Result/'+pureName+'_grades.txt'
        with open(newFilePath,'w') as file:
            firstLine=pureName+' grades: \n'
            file.write(firstLine)
            for index in df_score.index:
                line=index+','+str(df_score['total'][index])+'\n'
                file.write(line)

    def do_0(self):
        "Exit"
        print("Thanks")
        exit()
    def execute(self,user_input):
        controller_name="do_"+str(user_input)
        try:
            controller=getattr(Controller,controller_name)
        except AttributeError:
            print("Method not found")
        else:
            controller(self)
    def run(self):
        user_input=-1
        while (user_input!=0):
            user_input=int(input())
            self.execute(user_input)
            Controller.generate_menu()
        print("Program stopped.")
    @staticmethod
    def generate_menu():
        print("+-------------------Menu------------------+\nGrade the exam:")
        do_methods=[m for m in dir(Controller) if m.startswith('do_')]
        menu_string=[str(method.partition("_")[2])+'.'+str(getattr(Controller,method).__doc__) for method in do_methods]
        menu_string.sort(key = lambda x: int(x.split('.')[0]))
        for i in menu_string:
            print(i)
        print("+-----------------------------------------+")
def main():
    OP=Controller()
    OP.generate_menu()
    OP.run()
main()