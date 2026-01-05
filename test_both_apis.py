import subprocess
import time
import requests
import os

def run_tests(directory):
    print(f"\n--- Testing {directory} ---")
    # Start the API in the background
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.join(os.getcwd(), directory, "apps", "api")
    
    process = subprocess.Popen(
        ["python3", "-m", "uvicorn", "app.main:app", "--port", "8001"],
        cwd=os.path.join(directory, "apps", "api"),
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    time.sleep(2) # Wait for server to start
    
    try:
        # Run pytest
        result = subprocess.run(
            ["pytest", os.path.join(directory, "apps", "api", "tests", "test_api.py")],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        print(result.stderr)
    finally:
        process.terminate()

if __name__ == "__main__":
    # Ensure pytest is installed
    subprocess.run(["pip", "install", "pytest", "httpx", "fastapi", "uvicorn"])
    
    # Create tests directory in skeleton if it doesn't exist
    os.makedirs("unzipped_skeleton/apps/api/tests", exist_ok=True)
    subprocess.run(["cp", "unzipped_interview/apps/api/tests/test_api.py", "unzipped_skeleton/apps/api/tests/test_api.py"])
    
    run_tests("unzipped_skeleton")
    run_tests("unzipped_interview")
