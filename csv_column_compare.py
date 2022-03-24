from fileinput import filename
import pandas as pd
import os 

f1 = "Data/2017_v3/calendar/v1_calendar_base.csv" 

f2 = "Data/csv/calendar/v1_calendar_base.csv" 

def column_compare(file1,file2):
    col_diff = file2.columns.difference(file1.columns)
    return col_diff


# for file_name in os.listdir('Data/csv'):
#     # print(filename)
#     file_1_path = os.path.join('./csv', file_name)
#     name, ext = os.path.splitext(file_name)
#     file_2_path = os.path.join('Data/2017_v3', name + name[-1] + ext)
#     file1 = pd.read_csv(f1)
#     file2 = pd.read_csv(f2)
#     diff = column_compare(file1,file2)
#     print(file_name,"\n",ext,"\n",diff)
#     # ( diff logic here )


def listfiles(path):
    files = []
    for dirName, subdirList, fileList in os.walk(path):
        dir = dirName.replace(path, '')
        for fname in fileList:
            files.append(os.path.join(dir, fname))
    return files

def renamefiles(path):
    for file in listfiles(path):
        fpath = os.path.join(d, file)
        if (".csv" in file) and ("v1_" in file):
            os.rename(fpath, os.path.join(d, f"v3_{file[3:]}"))

x = "Data/2017_v3"
y = "Data/csv"

x_data = listfiles(x)
# print(x_data)
y_data = listfiles(y)
# print(y_data)

def file_column_compare(old_folder,new_folder):
    old_data = listfiles(old_folder)
    new_data = listfiles(new_folder)
    counter = 0
    for file in old_data:
        for file_2 in new_data:
            # print("1.",file, "\n","2.",file_2)
            if file.split("/")[-1] == file_2.split("/")[-1]:
                # print("1.",file,"\n","2",file_2)
                f1 = pd.read_csv(x + file)
                f2 = pd.read_csv(y + file_2)
            
                org_names = f1.columns  # [a,b,c]
                new_names = f2.columns  # [d,e,f,g]
                new_cols = dict(zip(org_names,new_names))
                # print(new_cols)
                f1 = f1.rename(index=str,columns=new_cols)
                out_name = file.split("/")[-1]
                outdir = 'Data/files_2017_v3/' + file.split("/")[-2]
                if not os.path.exists(outdir):
                    os.mkdir(outdir)
                fullname = os.path.join(outdir,out_name)
                print(fullname)
                file_csv = f1.to_csv(fullname,index=False)
                counter = counter + 1
                print(counter)
            #     diff = column_compare(f1,f2)
            #        
                # print(file,"\n", file_2,"\n" ,diff)
            # except Exception as e:
            #     print(e)




# file_column_compare(x,y)

path = "Data/files_2017_v3"


print(renamefiles(path))

# print(column_compare(pd.read_csv(f1),pd.read_csv(f2)))

# df.rename(columns={ df.columns[1]: "your value" }, inplace = True)
