import base64

def encrypt_text (text):
    encoded_data = base64.b64encode(text.encode()) # here the input is a string but base64 only accepts bytes so we wrote .enocde to convert the text in bytes 
    print(encoded_data)

parragraph = input("Enter the text you want to make secure : ")

encrypt_text(parragraph)

# in output we can get = which depends on- 
#(length of the string ) % 3 
# if this result is 0 then no = at the end 
# if the result is 1 then == 
# if the result is 2 then =
# because this encoding make pairs of 3 so we need to make the answer in this form 