import zipfile
import os
import shutil

def apply_interview(skeleton_zip_path, interview_zip_path, output_dir):
    """
    Applies the content of the interview zip file onto the skeleton structure.
    """
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    print(f"Extracting skeleton from {skeleton_zip_path}...")
    with zipfile.ZipFile(skeleton_zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

    print(f"Applying interview content from {interview_zip_path}...")
    with zipfile.ZipFile(interview_zip_path, 'r') as zip_ref:
        # Overwrite files in the output directory with files from the interview zip
        zip_ref.extractall(output_dir)

    print(f"Successfully applied interview content to {output_dir}")

if __name__ == "__main__":
    apply_interview("skeleton.zip", "interview.zip", "applied_project")
