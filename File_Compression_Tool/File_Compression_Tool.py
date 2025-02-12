import os
import zipfile
import tarfile

def compress_to_zip(input_paths, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for input_path in input_paths:
            input_path = input_path.strip()  # Remove spaces around filenames
            if os.path.exists(input_path):  # Ensure the file exists
                zipf.write(input_path, os.path.basename(input_path))
            else:
                print(f"Warning: {input_path} not found and will be skipped.")

def compress_to_tar(input_paths, output_path):
    with tarfile.open(output_path, 'w:gz') as tar:
        for input_path in input_paths:
            input_path = input_path.strip()
            if os.path.exists(input_path):
                tar.add(input_path, arcname=os.path.basename(input_path))
            else:
                print(f"Warning: {input_path} not found and will be skipped.")

def main():
    input_paths = input("Enter the file/folder paths to compress (comma-separated): ").split(',')
    output_path = input("Enter the output file name with extension (.zip or .tar.gz): ").strip()

    if output_path.endswith('.zip'):
        compress_to_zip(input_paths, output_path)
        print(f"Compressed files to {output_path}")
    elif output_path.endswith('.tar.gz'):
        compress_to_tar(input_paths, output_path)
        print(f"Compressed files to {output_path}")
    else:
        print("Unsupported format. Please use .zip or .tar.gz")

if __name__ == "__main__":
    main()
