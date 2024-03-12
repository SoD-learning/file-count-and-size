import os


def list_nested_folders_with_file_count_and_size(folder_path):
    folder_details = {}

    for root, dirs, files in os.walk(folder_path):
        total_size = sum(
            os.path.getsize(os.path.join(root, name))
            for name in files
            if not os.path.islink(os.path.join(root, name))
        )
        file_count = len(
            [name for name in files if not os.path.islink(os.path.join(root, name))]
        )
        relative_path = os.path.relpath(root, folder_path)
        folder_details[relative_path] = {"files": file_count, "size": total_size}

    return folder_details


# Ask the user to provide the target folder
folder_name = input("Please enter the path to the folder you want to analyze: ")
folder_details = list_nested_folders_with_file_count_and_size(folder_name)

print(f"Details for {folder_name}:")
for folder, details in folder_details.items():
    print(f"{folder} = {details['files']} files, {details['size']} bytes")
