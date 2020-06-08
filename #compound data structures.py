#compound data structures 
#can include containers in other containers to create compound data structures

#dictionary that maps keys to values that are also dictionaries

elements = {"hydrogen" : {"number": 1,
                          "weight:" : 1.00794,
                          "symbol" : "H" },
              "helium" : {"number" : 2,
                         "weight": 4.002602,
                         "symbol" : 'He'}}

#can access elements in nested dicionary
helium = elements["helium"] #get helium directory
hydrogen_weight = elements["hydrogen"]["weight"] #get hydrogens wieght

#adding new key to element dictionary

oxygen = {"number:8","weight":15.999,"symbol":"O"}
elements["oxygen"] = oxygen
print('elements = ', elements)