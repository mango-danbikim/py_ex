import pickle
import pickletools

# Sample data to be pickled
data = {'name': 'John', 'age': 25, 'city': 'New York'}

# Serialize the data using pickle.dump()
with open('data.pkl', 'ab') as file:
    pickle.dump(data, file)
    
with open('data.pkl', 'rb') as file:
    view_data = file.read()
pickletools.dis(view_data)


"""When executing this code,it shows 


    0: \x80 PROTO      4
    2: \x95 FRAME      45
   11: }    EMPTY_DICT
   12: \x94 MEMOIZE    (as 0)
   13: (    MARK
   14: \x8c     SHORT_BINUNICODE 'name'
   20: \x94     MEMOIZE    (as 1)
   21: \x8c     SHORT_BINUNICODE 'John'
   27: \x94     MEMOIZE    (as 2)
   28: \x8c     SHORT_BINUNICODE 'age'
   33: \x94     MEMOIZE    (as 3)
   34: K        BININT1    25
   36: \x8c     SHORT_BINUNICODE 'city'
   42: \x94     MEMOIZE    (as 4)
   43: \x8c     SHORT_BINUNICODE 'New York'
   53: \x94     MEMOIZE    (as 5)
   54: u        SETITEMS   (MARK at 13)
   55: .    STOP

   
   interesting
   """
#With GPT#