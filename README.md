# MetaPeek

![MetaPeek Banner](https://via.placeholder.com/1000x300?text=MetaPeek+-+Your+Go-To+Metadata+Extractor)

MetaPeek is a **lightweight yet powerful** metadata extraction tool that supports a variety of file types, from images and PDFs to audio files and beyond. Built with simplicity and efficiency in mind, MetaPeek helps you uncover hidden details with style and ease.

---

## 🚀 Features

- **Multi-format Support**: Extract metadata from images, audio, PDFs, and general files.
- **Readable Outputs**: Converts binary/hexadecimal metadata into clean, readable text.
- **Detailed Logs**: Generates comprehensive logs for seamless tracking.
- **Customizable**: Save metadata in JSON format for further analysis.
- **Interactive UI**: Beautifully styled CLI output with color-coded highlights and animations.

---

## 🛠️ Technologies Used

- **Programming Language**: Python 3
- **Libraries**:
  - [ExifRead](https://github.com/ianare/exif-py): Image metadata extraction
  - [Mutagen](https://mutagen.readthedocs.io): Audio file handling
  - [PyPDF2](https://github.com/py-pdf/pypdf2): PDF metadata extraction
  - [Hachoir](https://hachoir.readthedocs.io): General file metadata parsing
  - [Termcolor](https://pypi.org/project/termcolor/): CLI text styling
  - [Tqdm](https://tqdm.github.io): Progress bar animations

---

## ⚙️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Chanuka-KL/MetaPeek.git
   cd MetaPeek

2. Install Dependencies:

pip install -r requirements.txt


3. Run the Tool:

python MetaPeek.py --help




---

📂 Supported File Types


---

📖 Usage

Basic Metadata Extraction

python MetaPeek.py <file_path>

Save Metadata as JSON

python MetaPeek.py <file_path> --save-json

Enable Logging

python MetaPeek.py <file_path> --log


---

✨ Sample Output

CLI Output:

Extracting metadata from file: example.jpg
------------------------------------------------------------
Image Metadata:
  - Camera Make: Canon
  - Exposure Time: 1/125
  - ISO Speed: 200
------------------------------------------------------------

JSON File:

{
  "Image Metadata": {
    "Camera Make": "Canon",
    "Exposure Time": "1/125",
    "ISO Speed": "200"
  }
}


---

🤝 Contribution

We welcome contributions to enhance MetaPeek! Here's how you can help:

1. Fork the repo.


2. Create a branch for your feature:

git checkout -b feature/AmazingFeature


3. Commit your changes:

git commit -m "Add some AmazingFeature"


4. Push to the branch:

git push origin feature/Amazing



