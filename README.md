# MetaSniffer 🔍 

![MetaDataHunter](https://img.shields.io/badge/version-1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow)
![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey)


**MetaSniffer** is a comprehensive metadata extraction tool, powered by the versatile **MetaPeek** engine. Designed for professionals and enthusiasts alike, MetaSniffer supports multiple file types, offering clean, readable metadata output with advanced features for saving, logging, and customization.

---

## ✨ Features  

- 🌟 **Multi-File Support**: Handles images, audio, PDFs, videos, and more.  
- 🚀 **Efficient Extraction**: Quickly retrieves metadata in an organized, user-friendly format.  
- 🧹 **Clean Metadata**: Automatically decodes and formats raw metadata into readable text.  
- 📂 **Export to JSON**: Save metadata in a structured `.json` file for further analysis.  
- 📜 **Detailed Logs**: Keeps a record of all operations in a log file.  
- 🎨 **Colorized Output**: Highlights metadata categories and values for better visibility.  
- 🛠️ **Customizable Options**: Supports advanced features like logging and export customization.

---

## 📂 Supported File Types  

| File Type  | Extensions              | Example Use |
|------------|--------------------------|-------------|
| **Images** | `.jpg`, `.jpeg`, `.png`  | Photo EXIF extraction |
| **Audio**  | `.mp3`, `.wav`, `.flac`  | Music metadata |
| **PDFs**   | `.pdf`                   | Document properties |
| **Videos** | `.mp4`, `.avi`, `.mov`   | General file analysis (via Hachoir) |
| **Others** | Supported by Hachoir    | Metadata from obscure formats |

---

## 🚀 Quick Start  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/<YourGitHubUsername>/MetaSniffer.git
   cd MetaSniffer
   ```

2. Install Dependencies
Install all required Python libraries:
```bash
pip install -r requirements.txt
```

3. Run MetaPeek
Extract metadata by running the script:
```bash
python metadata_extractor.py <file_path>
```



---

## 🛠 Advanced Options

Examples

Basic Extraction:
```bash
python metadata_extractor.py example.jpg
```
Save as JSON:
```bash
python metadata_extractor.py example.mp3 --save-json
```
Enable Logging:
```bash
python metadata_extractor.py example.pdf --log
```


---

## ⚙️ Configuration

MetaSniffer’s core functionality is powered by MetaPeek, ensuring seamless metadata extraction across various file types. Its configuration supports:

Dynamic addition of file formats.

Integration with third-party APIs for extended analysis.

Future-proofing with modular design for scalability.


---

## 📋 License

MetaSniffer is licensed under the MIT License. See the LICENSE file for detailed terms and conditions.


---

## 🌟 Contributing

We welcome contributions from the community!

1. Fork the Repository


2. Create a Feature Branch


3. Submit a Pull Request



For major changes, please open an issue first to discuss what you would like to change.


---

## 🧑‍💻 Author

GitHub: Chanuka-KL

Tool: MetaPeek

Contact: chanuka.dev.kl@gmail.com

[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https//wa.me/+94766576559?text=)


