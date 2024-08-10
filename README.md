# Subtitle Data Cleaning Script
`Created by Xinyu Mao and Haoqing Liu.`
## Introduction

This repository contains a Python script designed to clean subtitle files obtained from [OpenSubtitles](https://www.opensubtitles.com/en/tvshows). OpenSubtitles is a popular platform that provides subtitles for a wide range of TV shows and movies in various languages. The subtitle files are often in formats such as `.srt` and can contain a mix of textual dialogue, timestamps, and other non-dialogue information such as speaker names, sound descriptions, etc.

The goal of this script is to process and clean these raw subtitle files, extracting only the dialogue text while removing timestamps, metadata, and any other extraneous information, making the data ready for further analysis or use in machine learning models.

## Dataset Structure

After cleaning, the script generates cleaned subtitle files which will be stored in a designated directory. The structure of the cleaned files is as follows:

- **File Naming Convention**: Each cleaned subtitle file is named after the original subtitle file but with a `_cleaned` suffix to differentiate it from the raw data.
- **File Content**:
  - **Dialogue Text**: The cleaned files will contain only the dialogue text, with timestamps, speaker names, and other non-dialogue elements removed.

### Example of a Raw Subtitle File:

```
1
00:00:20,000 --> 00:00:24,400
[Music playing]

2
00:00:24,600 --> 00:00:27,800
John: Hello! How are you today?

3
00:00:28,000 --> 00:00:30,200
I'm good, thanks!
```

### Example of a Cleaned Subtitle File:

```
Hello! How are you today?

I'm good, thanks!
```

## How to Run the Script

### Prerequisites

Before running the script, ensure you have the following installed:

- **Python**: Version 3.6 or higher.

### Setup

1. **Subtitle Data**:
   - Download subtitle files from [OpenSubtitles](https://www.opensubtitles.com/en/tvshows).
   - Place the downloaded subtitle files in a directory named `subtitles` (you can change the directory name in the script if needed).

2. **Script Configuration**:
   - Open the `cleanData.py` script in a text editor.
   - Ensure that the input directory for subtitle files (`subtitles`) and the output directory (`cleaned_subtitles`) are correctly specified. The script assumes the input directory is `subtitles` and will create an output directory named `cleaned_subtitles` if it doesn't exist.

### Running the Script

1. **Run the Script**:
   - Open a terminal and navigate to the directory containing `cleanData.py`.
   - Run the script using Python:

   ```bash
   python cleanData.py
   ```

2. **Check the Output**:
   - After running the script, a directory named `cleaned_subtitles` will be created (if it doesn't already exist).
   - The script will save the cleaned subtitle files in this directory, with the `_cleaned` suffix added to each filename.

### Notes

- **Error Handling**: Ensure that the subtitle files are correctly formatted. The script may not work as expected with corrupted or non-standard subtitle files.
- **File Format**: The script is designed to work primarily with `.srt` subtitle files. If you have subtitles in another format, you may need to convert them to `.srt` first or modify the script to handle different formats.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
