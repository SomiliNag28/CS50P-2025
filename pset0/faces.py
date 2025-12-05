def convert(s : str):
    s = s.replace(":)" , "🙂").replace(":(" , "☹️")
    return s

print(convert(input("Enter Text : ")))
