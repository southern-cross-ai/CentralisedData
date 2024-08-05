# Text to JSON Converter Script

This script converts a text file containing place reviews into a JSON file with a single combined column. Each place and its corresponding reviews are combined into a single string, making it easier to manage and analyze the data.

## Prerequisites

Ensure you have Python installed on your system. This script is compatible with Python 3.

## Usage

1. **Clone the repository**:

    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```


2. **Run the script**:

    ```bash
    python txt_to_json.py <input_txt_file>
    ```

    Replace `<input_txt_file>` with the path to your text file.

## Example

Suppose you have a text file named `reviews.txt`:


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

