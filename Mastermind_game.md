

```python

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
  

```

                              Aufgabe 2


```python
ms_md()
```

    Please give us the first color with integer number from 1 to 6:
    1
    Please give us the second color with integer number from 1 to 6:
    1
    Please give us the third color with integer number from 1 to 6:
    1
    Please give us the fourth color with integer number from 1 to 6:
    1
    

    C:\Users\User\Anaconda3\lib\site-packages\ipykernel_launcher.py:97: DeprecationWarning: 
    .ix is deprecated. Please use
    .loc for label based indexing or
    .iloc for positional indexing
    
    See the documentation here:
    http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
    

    [0, 0, 0, 0]
    Please give us the first color with integer number from 1 to 6:
    2
    Please give us the second color with integer number from 1 to 6:
    2
    Please give us the third color with integer number from 1 to 6:
    2
    Please give us the fourth color with integer number from 1 to 6:
    2
    [0, 0, 0, 'X']
    Please give us the first color with integer number from 1 to 6:
    3
    Please give us the second color with integer number from 1 to 6:
    3
    Please give us the third color with integer number from 1 to 6:
    3
    Please give us the fourth color with integer number from 1 to 6:
    2
    [0, 0, 0, 'X']
    Please give us the first color with integer number from 1 to 6:
    4
    Please give us the second color with integer number from 1 to 6:
    4
    Please give us the third color with integer number from 1 to 6:
    4
    Please give us the fourth color with integer number from 1 to 6:
    2
    [0, 0, 'X', 'X']
    Please give us the first color with integer number from 1 to 6:
    5
    Please give us the second color with integer number from 1 to 6:
    5
    Please give us the third color with integer number from 1 to 6:
    4
    Please give us the fourth color with integer number from 1 to 6:
    2
    [0, 'X', 'X', 'X']
    Please give us the first color with integer number from 1 to 6:
    6
    Please give us the second color with integer number from 1 to 6:
    5
    Please give us the third color with integer number from 1 to 6:
    4
    Please give us the fourth color with integer number from 1 to 6:
    2
    ['X', 'X', 'X', 'X']
    Congratulations!!! You won with your seventh try !
    Do you want to try again?(y/n)n
    

Now we will try to win this game using technique, where you begin with '1111' and then add 1 more if it wasn't right.

We will do it with by passin True to 'auto_hinweis' variable of 'ms_md' function:  


```python
ms_md(auto_hinweis =True)
```

    [1 1 1 1]
    [0, 0, 0, 0]
    [2 2 2 2]
    [0, 0, 0, 'X']
    [3 3 3 2]
    ['X', 0, 'X', 'X']
    [3 4 3 2]
    ['X', 0, 'X', 'X']
    [3 5 3 2]
    ['X', 'X', 'X', 'X']
    5
    

    C:\Users\User\Anaconda3\lib\site-packages\ipykernel_launcher.py:49: DeprecationWarning: 
    .ix is deprecated. Please use
    .loc for label based indexing or
    .iloc for positional indexing
    
    See the documentation here:
    http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
    

We needed 5 times to win the game with this strategy.


And now we will see how long does it take to win this game, if we pick numbers randomly:


```python
ms_md(automated =True)
```

    C:\Users\User\Anaconda3\lib\site-packages\ipykernel_launcher.py:19: DeprecationWarning: 
    .ix is deprecated. Please use
    .loc for label based indexing or
    .iloc for positional indexing
    
    See the documentation here:
    http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
    

    [4 5 1 5]
    1060
    

We needed 1060 times to guess this numbers right.
