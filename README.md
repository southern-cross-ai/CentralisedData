# Text to JSON Converter Script

This script converts a text file containing place reviews into a JSON file with a single combined column. Each place and its corresponding reviews are combined into a single string, making it easier to manage and analyze the data.

## Prerequisites

Ensure you have Python installed on your system. This script is compatible with Python 3.

## Usage

1. **Clone the repository** (or create a new one and add this script to it):

    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2. **Save the script** as `txt_to_json.py`:

    ```python
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

        # Create a new list of dictionaries with only one combined column
        one_column_data = [{'Place_Reviews': f"{place['Place']}: {place['Reviews']}"} for place in places]

        json_file = os.path.splitext(txt_file)[0] + '_one_column.json'

        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(one_column_data, file, ensure_ascii=False, indent=4)

        print(f"Conversion complete. Output file: {json_file}")

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python script.py <input_txt_file>")
        else:
            txt_file = sys.argv[1]
            txt_to_json(txt_file)
    ```

3. **Prepare your input text file** in the following format:

    ```
    Place: Example Place 1
    Text: This is the first review.
    ----------------------------------------
    Place: Example Place 2
    Text: This is another review.
    ----------------------------------------
    ```

4. **Run the script**:

    ```bash
    python txt_to_json.py <input_txt_file>
    ```

    Replace `<input_txt_file>` with the path to your text file.

## Example

Suppose you have a text file named `reviews.txt`:

```
Place: Central Park
Text: Beautiful place to visit.
----------------------------------------
Place: Statue of Liberty
Text: Iconic landmark.
----------------------------------------
```

Run the script as follows:

```bash
python txt_to_json.py reviews.txt
```

The output will be a JSON file named `reviews_one_column.json` containing:

```json
[
    {
        "Place_Reviews": "Central Park: Beautiful place to visit."
    },
    {
        "Place_Reviews": "Statue of Liberty: Iconic landmark."
    }
]
```

## Conclusion

This script helps you easily convert text files with place reviews into a more manageable JSON format. Customize the script further to meet your specific needs. Happy coding!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.

---

Now you have a complete guide to use the `txt_to_json.py` script. Copy the contents above into your GitHub repository's README.md file for easy reference.
