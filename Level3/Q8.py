#write a function that accepts an encoded string as a parameter.

def enc_string():
    parts=[]
    string1=input("Enter the encoded string: ")
    encoded=string1.split('0')
    for i in encoded:
        if i!='':
            parts.append(i)
            print(parts)

    first_name = parts[0]
    last_name = parts[1]
    id = parts[2]

    # Build and print dictionary
    result = {
        "first_name": first_name,
        "last_name": last_name,
        "id": id
    }

    print(result)

enc_string()            
       