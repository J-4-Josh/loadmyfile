
def loadmyfile():
    """Your data is assigned to loadmyfile.data
    Necessary Packages: os & pandas"""
    import os
    import pandas as pd
    def exp_folders():
        path=os.getcwd()+"/"
        exp_folders.content_list=os.listdir() #gives files and folders in located file
        for i in exp_folders.content_list: 
            print(f" {exp_folders.content_list.index(i)+1}, {i} \n") #dispay those files
        sel_filename = input("Enter file number") #selecting file

        file=exp_folders.content_list[int(sel_filename)-1] #assigning selected file to variable file
        check = file.split(".") #understanding file format using its extension
        exp_folders.path = path + file
        while check[-1] in ["csv", "xlsx"]: #for xlsx and csv
            load_file("./"+file)
            break

        else:
#         exp_folders.path=path+file
            exp_folders_deep(exp_folders.path) #exploring next selected folder

    def exp_folders_deep(path):
        exp_folders_deep.content_list=os.listdir(path)
        for i in exp_folders_deep.content_list:
            print(f" {exp_folders_deep.content_list.index(i)+1}, {i} \n")
        sel_filename = input("Enter file number")

        file=exp_folders_deep.content_list[int(sel_filename)-1]
        check = file.split(".")
        exp_folders_deep.path = path + "/"+ file
        while check[-1] in ["csv", "xlsx"]:
            load_file(exp_folders_deep.path) 
            break

        else:
        
            exp_folders_deep(exp_folders_deep.path)

        
    def load_file(file):
        check = file.split(".")
        if check[-1] in ["csv", "xlsx"]:
            if check[-1]=="xlsx":
                file_path= str(file)
                #print(file_path)
                load_file.df=pd.read_excel(io=file_path, sheet_name = 0, header     = 0)
                raw=load_file.df
            

            
            
            elif check[-1]=="csv":
                file_path= str(file)
                load_file.df=pd.read_csv(file_path)
                raw=load_file.df
                
            
    
                        
        

    exp_folders()
    loadmyfile.data=load_file.df
    return loadmyfile.data
