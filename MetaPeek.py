

"""
MetaDataExtractor Script
Version 2.0
License: MIT License
Author: Chanuka
"""
import os
import sys
import json
import logging
import argparse
import exifread
import mutagen
import PyPDF2
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from termcolor import colored
from tqdm import tqdm


# Configure logging
logging.basicConfig(
    filename="metadata_extractor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def clean_metadata(metadata):
    """Convert binary/hexadecimal metadata to readable text."""
    if isinstance(metadata, bytes):
        try:
            return metadata.decode('utf-8', errors='replace')
        except UnicodeDecodeError:
            return None
    elif isinstance(metadata, list):
        return [clean_metadata(item) for item in metadata if clean_metadata(item) is not None]
    return metadata


def extract_metadata(file_path):
    """Extract metadata from various file types."""
    if not os.path.exists(file_path):
        logging.error(f"File '{file_path}' does not exist.")
        return None

    file_extension = os.path.splitext(file_path)[-1].lower()
    metadata = {}

    print(colored(f"\nExtracting metadata from file: {file_path}", 'cyan'))
    print("-" * 60)

    try:
        # Image Metadata (EXIF)
        if file_extension in [".jpg", ".jpeg", ".png", ".tiff"]:
            with open(file_path, 'rb') as f:
                tags = exifread.process_file(f)
                image_metadata = {tag: clean_metadata(str(tags[tag])) for tag in tags if clean_metadata(str(tags[tag]))}
                if image_metadata:
                    metadata["Image Metadata"] = image_metadata

        # Audio Metadata
        elif file_extension in [".mp3", ".wav", ".flac"]:
            audio = mutagen.File(file_path)
            audio_metadata = {key: clean_metadata(str(audio[key])) for key in audio.keys() if clean_metadata(str(audio[key]))} if audio else {}
            if audio_metadata:
                metadata["Audio Metadata"] = audio_metadata

        # PDF Metadata
        elif file_extension == ".pdf":
            with open(file_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                pdf_metadata = pdf_reader.metadata
                pdf_metadata = {key: clean_metadata(pdf_metadata[key]) for key in pdf_metadata if clean_metadata(pdf_metadata[key])}
                if pdf_metadata:
                    metadata["PDF Metadata"] = pdf_metadata

        # General Metadata (Using hachoir for videos, docs, etc.)
        else:
            parser = createParser(file_path)
            if parser:
                meta = extractMetadata(parser)
                if meta:
                    general_metadata = {item.key: clean_metadata(item.value) for item in meta.exportPlaintext() if clean_metadata(item.value)}
                    if general_metadata:
                        metadata["General Metadata"] = general_metadata

    except Exception as e:
        logging.error(f"Error extracting metadata from '{file_path}': {e}")
        print(colored(f"Error extracting metadata: {e}", 'red'))

    # Remove "JPEGThumbnail:" results from metadata
    if "Image Metadata" in metadata and "JPEGThumbnail" in metadata["Image Metadata"]:
        del metadata["Image Metadata"]["JPEGThumbnail"]

    return metadata if metadata else None


def print_metadata(metadata):
    """Print the metadata in a readable and structured format with colors and highlights."""
    if metadata:
        for category, data in metadata.items():
            print(colored(f"\n{category}:", 'yellow', attrs=['bold']))
            print("-" * 50)
            if isinstance(data, dict):
                for key, value in data.items():
                    print(colored(f"  - {key}:", 'green'), colored(f"{value}", 'cyan'))
            elif isinstance(data, list):
                for item in data:
                    print(colored(f"  -", 'green'), colored(f"{item}", 'cyan'))
            print("\n" + "-" * 50)
    else:
        print(colored("No readable metadata found.", 'red'))


def save_metadata_to_json(metadata, output_file):
    """Save metadata to a JSON file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(metadata, json_file, indent=4)
        print(colored(f"\nMetadata successfully saved to {output_file}.", 'green'))
    except Exception as e:
        logging.error(f"Error saving metadata to JSON: {e}")
        print(colored(f"Error saving metadata: {e}", 'red'))


def loading_animation():
    """Display a loading animation while the script processes the file."""
    with tqdm(total=100, desc="Processing", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}") as pbar:
        for _ in range(100):
            pbar.update(1)


def main():
    parser = argparse.ArgumentParser(description="Extract metadata from various file types.")
    parser.add_argument("file", help="Path to the file for metadata extraction.")
    parser.add_argument("--save-json", help="Save metadata to a JSON file.", action="store_true")
    parser.add_argument("--log", help="Enable logging to metadata_extractor.log.", action="store_true")

    args = parser.parse_args()

    if args.log:
        logging.info("Metadata extraction started.")

    file_path = args.file

    # Start loading animation
    loading_animation()

    # Extract metadata
    metadata = extract_metadata(file_path)

    # Print metadata
    print_metadata(metadata)

    # Save metadata to JSON if requested
    if args.save_json and metadata:
        json_file = os.path.splitext(file_path)[0] + "_metadata.json"
        save_metadata_to_json(metadata, json_file)


if __name__ == "__main__":
    main()
