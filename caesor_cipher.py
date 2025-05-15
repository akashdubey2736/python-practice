alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z']

print("Welcome to caesor cipher program!")
action=input("Enter encode for encoding and decode for decoding : ").lower()
text=input("Enter the text :").lower()
key=int(input("Enter the key : "))

def encode_decode(text,action,key):
    if action=="encode":
        encoded_text=""
        for char in text:
            if char in alphabets:
                index=alphabets.index(char)
                new_index=index+key
                encoded_text+=alphabets[new_index]
            else:
                encoded_text+=char
        print("Encoded text is : "+ encoded_text)
    elif action=="decode":
        decoded_text=""
        for char in text:
            if char in alphabets:
                index=alphabets.index(char)
                new_index=index-key
                decoded_text+=alphabets[new_index]
            else:
                decoded_text+=char
        print("Decoded text is : "+ decoded_text)
    else:
        print("Incorrection action passed!")

encode_decode(text,action,key)