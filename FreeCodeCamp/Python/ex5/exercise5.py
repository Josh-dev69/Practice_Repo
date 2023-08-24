# Take the string str = "X-DSPAM-Confidence: 0.83567"
# Use find and string slicing to extract the portion of the string

str = "X-DSPAM-Confidence: .83567"

str_pos = str.find(":") # get the position of the string
# print(new_str)

ex_num = str[str_pos + 1:].strip() # Extract number
# print(ex_num)
num = float(ex_num) # convert the extracted number to float
print(num)