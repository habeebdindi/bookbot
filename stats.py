def get_book_text(filepath):         
    with open(filepath) as f:        
        file_content = f.read()      
    return file_content              
                                     
def count_words(text):               
    words = text.split()             
    return len(words)          

def count_char(text):
    lowercase_text = text.lower()
    char_and_count = {}
    for c in lowercase_text:
        if c in char_and_count:
            char_and_count[c] += 1
        else:
            char_and_count[c] = 1
    return char_and_count

def pretty_sort(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        pair = {"char": char, "num": count}
        sorted_list.append(pair)
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
#    print(sorted_list)
    return sorted_list
