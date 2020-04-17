import os, re

for root, dirs, files in os.walk("."):
    for original_filename in files:
        if original_filename == __file__:
            continue #Skip it if it's this .py file

        filename, extention = os.path.splitext(original_filename)
        
        cleaned_filename = re.sub("[\(\[].*?[\)\]]", "", filename).rstrip() #remove anything between parenthesis or brackets
        result = cleaned_filename + extention
        
        if original_filename == result:
            print("Skipping " + original_filename + ", no change needed!")
            continue
        
        print(" Before: " + original_filename)
        print("  After: " + result)
        print("┄───────┄")
        os.rename(original_filename, result)
