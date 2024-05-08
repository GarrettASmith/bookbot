def letter_count():
    count_dict = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered = file_contents.lower()
                
        for letter in lowered:
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1
    return count_dict

def sort_dict(letter_count):
    alpha_list = []
    for letter in letter_count:
        if letter.isalpha() == True:
            alpha_list.append({'letter': letter, 'count': letter_count[letter]})
    alpha_list.sort(reverse=True, key=lambda item: item['count'])
    return alpha_list
    

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
    letter_counts = letter_count()
    sorted_list = sort_dict(letter_counts)

    print("--- Book Report: Frankenstein ---")
    print(f"There are {len(words)} words in this book!")
    print()
    for item in sorted_list:
        print(f"The letter '{item['letter']}' was found {item['count']} times.")
    print("--- End of report ---")   

if __name__ == "__main__":
    main()