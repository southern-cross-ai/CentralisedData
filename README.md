# Data from GoogleMap

```
Collected and formatted by Xinyu M. and Haoqing L.
```

There are lots of comments on GoogleMap, such as evaluating restaurants, hotels, etc. These comments are obtained in this reop, with which we are going to train our GPT model.

Now, keep the pace with us and you will obtain the data in the last.

## Environment
```
python 3.x
```

## Guide
### 1. Obtain a Google Places API key
The foundation of our method to obtain data from Google map.
Here's a guide on how to obtain one:

#### 1. Create a Google Cloud Project
1. **Log in to Google Cloud Console**: Visit [Google Cloud Console](https://console.cloud.google.com/) and log in with your Google account.
2. **Create a New Project**:
   - Click the drop-down menu at the top of the console and select "New Project."
   - Name your project, select an organization (if applicable), and click "Create."

#### 2. Enable the Google Places API
**Search and Enable the API in the API Library**:
   - Once in your project, click the navigation menu (≡) in the top-left corner and select "API & Services" > "Library."
   - In the API Library, search for "Places API," click on "Places API" in the search results, and then click "Enable."

#### 3. Set Up Billing Information
Google Cloud requires billing information to be set up for projects using APIs, even within the free usage tier:
1. **Set Up a Billing Account**:
   - If this is your first time using Google Cloud services, you may be prompted to set up a billing account. Follow the prompts to enter the necessary billing information.

#### 4. Obtain the API Key
1. **Create an API Key**:
   - Go to the "API & Services" > "Credentials" page.
   - Click the "Create credentials" button at the top of the page and select "API key."
   - A new API key will be generated for you. You can copy the key by clicking the "Copy" button next to it.

2. **Restrict the API Key (Recommended)**:
   - Click on the name of the newly created API key to enter the details page.
   - In the "Key restrictions" section, you can restrict the usage of this API key, such as by limiting it to specific IP addresses or restricting access to specific APIs.
   - In the "API restrictions" section, click "Restrict key," select "Places API," and then save.

After completing these steps, you will have a Google Places API key that you can use to access the various features of the Google Places API. Be sure to keep your API key secure to prevent unnecessary charges and security risks!

### 2. Coding auxiliary functions

To meet our needs to obtain comments on restaurants, hotel, etc., we need some auxiliary functions, each works on retrieving information about specific types of places around a given location, calling the Google Places API to get detailed information about a specified place and saving the retrieved data in a specific file.

1. **To get expected places around the given location**:
The function will have four input params: your API key, the location coordinate, the searching radius around the location and the type of places to search for, like restaurants or hotels.
```python
def get_places(api_key, location, radius, place_type):
    '''To get comments on specific type of places in the range of given radius around the location
    
    Args:
        api_key: your own api key obtained from 1st step
        location: the location around which you want to search
        radius: the range of searching around the location
        place_type: the type of place you want to search for
        
    Return:
        places: the specific type of places around the given location
    
    '''
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={place_type}&key={api_key}"
    places = []
    while url:
        # Send a request to the Google Places API
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            places.extend(result.get('results', []))  # Get the list of places
            next_page_token = result.get('next_page_token')  # Check if there is a next page
            if next_page_token:
                time.sleep(2)  # Wait 2 seconds to comply with API rate limits
                url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key={api_key}"
            else:
                url = None
        else:
            print(f"Error: {response.status_code}")
            break
    return places
```

2. **To get comments for places**
```python
# Define a function: Get reviews for a specified place
def get_place_reviews(place_id, api_key):
   ''' To get reviews for the places
   
   Args:
       place_id: id for each place
       api_key: your api key
       
   Returns:
       result: comments corresponding to each place
   
   '''
    url = f"https://maps.googleapis.com/maps/api/place/details/json?placeid={place_id}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        if "result" in result and "reviews" in result["result"]:
            return result["result"]["reviews"]
        else:
            return []
    else:
        print(f"Error: {response.status_code}")
        return []
```

3. **Save reviews to a file**
```python
def save_reviews_to_file(place_name, reviews, file):
   ''' To save our reviews to a file
   
   Args:
       place_name, reviews: obtained from previous functions
       file: file name
       
   Returns:
       None
   '''

    with open(file, 'a', encoding='utf-8') as f:
        f.write(f"Place: {place_name}\n")
        for review in reviews:
            author = review.get('author_name', 'Anonymous')
            rating = review.get('rating', 'N/A')
            text = review.get('text', 'No review text')
            f.write(f"Author: {author}\n")
            f.write(f"Rating: {rating}\n")
            f.write(f"Text: {text}\n\n")
        f.write("\n" + "-"*40 + "\n\n")
```

### 3.Main Function
Time to code our main function!
```python
if __name__ == '__main__':
    # Get user input
   api_key = input("Enter your API Key: ")
   location = input("Enter the location coordinates (latitude,longitude): ")
   radius = input("Enter the search radius (in meters): ")
   place_type = input("Enter the place type (e.g., restaurant, cafe, etc.): ")
   
   # Create data folder (if it doesn't exist)
   output_directory = os.path.join(os.getcwd(), 'data')
   os.makedirs(output_directory, exist_ok=True)
   output_file = os.path.join(output_directory, f"{place_type}_reviews.txt")
   
   # Get all places of the specified type at the specified location
   places = get_places(api_key, location, radius, place_type)
   
   # Get reviews for each place and save them to a file
   for place in places:
       place_id = place['place_id']
       place_name = place['name']
       reviews = get_place_reviews(place_id, api_key)
       save_reviews_to_file(place_name, reviews, output_file)
   
   print(f"Reviews have been saved to {output_file}")
```
That's it! All you need is to run the main function, type in the information according to the questions, and BOOM! 
Also, we've prepared a dataset for you to search around the major cities in Australia. That's all you need!

| City         | Latitude  | Longitude | Radius (m)    |
|--------------|-----------|-----------|---------------|
| Sydney       | -33.8688  | 151.2093  | 62,830        |
| Melbourne    | -37.8136  | 144.9631  | 56,380        |
| Brisbane     | -27.4698  | 153.0251  | 70,980        |
| Perth        | -31.9505  | 115.8605  | 45,120        |
| Adelaide     | -34.9285  | 138.6007  | 32,190        |
| Hobart       | -42.8821  | 147.3272  | 23,240        |
| Darwin       | -12.4634  | 130.8456  | 31,700        |
| Canberra     | -35.2809  | 149.1300  | 16,080        |
| Gold Coast   | -28.0167  | 153.4000  | 20,600        |
| Newcastle    | -32.9283  | 151.7817  | 9,100         |

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

The output will be a JSON file named reviews_two_columns.json containing:

```json
[
    {
        "Place_Reviews": "Central Park: Beautiful place to visit.",
        "Additional_Info": ""
    },
    {
        "Place_Reviews": "Statue of Liberty: Iconic landmark.",
        "Additional_Info": ""
    }
]
```

## Conclusion

This script helps you easily convert text files with place reviews into a more manageable JSON format. 

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.
