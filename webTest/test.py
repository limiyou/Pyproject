
import string,random,csv,xlrd,xlwt
all_str = string.ascii_letters + string.digits
file_path = r"C:\Users\lijing\Desktop\test.xls"
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('Sheet1',cell_overwrite_ok=True)
headlist=[u'账号',u'密码',u'邮箱']
row = 0
col = 0
for head in headlist:
    sheet.write(row,col,head)
    col = col+1
for i in range(1,4):
    for j in range(1,3):
        print(i, j)
        username = ''.join(random.sample(all_str,5))+'#$%'
        password = ''.join(random.sample(['1','2','3','4','5','6','a','b','c','d','e','f','g','h','i','j','k','l','m'],3))
        Email = ''.join(random.sample(all_str,9))+'@163.com'
        sheet.write(i,j-1,j-1)
        sheet.write(i,j,j)
        sheet.write(i,j,j)

    workbook.save(file_path)
    print(u'生成第%d个账号'%i)