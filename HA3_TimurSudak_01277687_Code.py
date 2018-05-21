
import scipy as sc
import random as rp
import numpy as np 
import pandas as pd
######################## Aufgabe 1 ###########################################
def ms_md(automated = False, auto_hinweis = False):
   rel_cl =np.random.choice([1, 2, 3, 4, 5, 6], size=4, replace=True)
   k=0
   if automated == True:
      while True:
   
         stz =np.random.choice([1, 2, 3, 4, 5, 6], size=4, replace=True)
         iden_vec = list(np.zeros((4,), dtype=int))
         if all(stz!=0):
          
            df = pd.DataFrame(np.nan, index=[0,1,2,3], columns=[0,1,2,3])
            for j in range(0,len(rel_cl)):
                for i in range(0,len(stz)):
                    df.ix[j ,i] = (rel_cl[j] == stz[i])
            if any(np.diag(df)):
                index = [i for i, x in enumerate(np.diag(df)) if x]
                for s in range(0,len(index)):
                    iden_vec[index[s]] = "X"
                    df = df.drop(columns = index[s])
                    df   =  df.drop(index[s])
            for n in df.columns:
                if any(df[n]):
                    iden_vec[n] = "O"
                    df = df.drop(df[n].index[[i for i, x in enumerate(df[n]) if x][0]])
                    df = df.drop(columns = n)
          
         k = k + 1            
         if "X" in iden_vec:
            if  all(np.array(iden_vec) == "X"):
                print(stz)
                print(k)
                break
       
   
   elif  auto_hinweis == True:
       stz = np.array([1,1,1,1])
       while True:
         iden_vec = list(np.zeros((4,), dtype=int))
         if all(stz!=0):
            df = pd.DataFrame(np.nan, index=[0,1,2,3], columns=[0,1,2,3])
            vec =list()
            for j in range(0,len(rel_cl)):
                for i in range(0,len(stz)):
                    df.ix[j ,i] = (rel_cl[j] == stz[i])
            if any(np.diag(df)):
                index = [i for i, x in enumerate(np.diag(df)) if x]
                for s in range(0,len(index)):
                    iden_vec[index[s]] = "X"
                    df = df.drop(columns = index[s])
                    df   =  df.drop(index[s])
            for n in df.columns:
                if any(df[n]):
                    iden_vec[n] = "O"
                    vec.append(n)
                    df = df.drop(df[n].index[[i for i, x in enumerate(df[n]) if x][0]])
                    df = df.drop(columns = n)
         k = k + 1
         if ("X" in iden_vec) or ("O" in iden_vec):
             if all(sc.logical_or(np.array(iden_vec) == "X" ,np.array(iden_vec) == "O")):
                if  all(np.array(iden_vec) == "X"):
                   print(stz)
                   print(iden_vec)
                   print(k)
                   break
                else:
                   rp.shuffle(stz)
         print(stz)
         print(iden_vec)    
         stz[df.index] = stz[df.index] + 1
         
   else: 
      while True:

         stz =np.zeros((4,), dtype=int)
         a = input("Please give us the first color with integer number from 1 to 6:\n")
         b = input("Please give us the second color with integer number from 1 to 6:\n")
         c = input("Please give us the third color with integer number from 1 to 6:\n")
         d = input("Please give us the fourth color with integer number from 1 to 6:\n")
         for i in range(0,len(stz)):
           try:
            stz[i] = int([a,b,c,d][i])
           except ValueError:
            print("Warning:You have to give an integer number from 1 to 6 for the {} color !".format(["first","second","third", "fourth"][i]))
         if any(stz > 6):
            print("Please type integer between 1 and 6 for the {} color !".format(["first","second","third", "fourth"][i]))
         iden_vec = list(np.zeros((4,), dtype=int))
         if all(stz!=0):
          
            df = pd.DataFrame(np.nan, index=[0,1,2,3], columns=[0,1,2,3])
            for j in range(0,len(rel_cl)):
                for i in range(0,len(stz)):
                    df.ix[j ,i] = (rel_cl[j] == stz[i])
            if any(np.diag(df)):
                index = [i for i, x in enumerate(np.diag(df)) if x]
                for s in range(0,len(index)):
                    iden_vec[index[s]] = "X"
                    df = df.drop(columns = index[s])
                    df   =  df.drop(index[s])
            for n in df.columns:
                if any(df[n]):
                    iden_vec[n] = "O"
                    df = df.drop(df[n].index[[i for i, x in enumerate(df[n]) if x][0]])
                    df = df.drop(columns = n)
          
         print(iden_vec)
         k = k + 1                 
         if "X" in iden_vec:
            if  all(np.array(iden_vec) == "X"):
                 print("Congratulations!!! You won with your {} try !".format(["first","second","third", "fourth","fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"][k]))
                 bol = input("Do you want to try again?(y/n)")
                 if bol == "y":
                    return(ms_md())
                 else:
                    break
  
########################################## Aufgabe 2 ########################################################
     
    
  