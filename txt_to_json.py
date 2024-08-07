import json
import sys
import os

def txt_to_json(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    places = []
    place = {}
    reviews = []
    review_text = ""

    for line in lines:
        line = line.strip()
        if line.startswith("Place:"):
            if place:
                if review_text:
                    reviews.append(review_text.strip())
                    review_text = ""
                place['Reviews'] = " ".join(reviews)
                places.append(place)
                place = {}
                reviews = []
            place['Place'] = line.replace("Place: ", "")
        elif line.startswith("Text:"):
            review_text += line.replace("Text: ", "") + " "
        elif line.startswith("Author:") or line.startswith("Rating:"):
            continue
        elif line == "----------------------------------------":
            if review_text:
                reviews.append(review_text.strip())
                review_text = ""
            place['Reviews'] = " ".join(reviews)
            places.append(place)
            place = {}
            reviews = []

    # Ensure the last place and review are added
    if review_text:
        reviews.append(review_text.strip())
    if place:
        place['Reviews'] = " ".join(reviews)
        places.append(place)

    # Create a new list of dictionaries with two columns
    two_column_data = [{'Place_Reviews': f"{place['Place']}: {place['Reviews']}", 'Additional_Info': ""} for place in places]

    json_file = os.path.splitext(txt_file)[0] + '_two_columns.json'

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(two_column_data, file, ensure_ascii=False, indent=4)

    print(f"Conversion complete. Output file: {json_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_txt_file>")
    else:
        txt_file = sys.argv[1]
        txt_to_json(txt_file)
