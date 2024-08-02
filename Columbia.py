import subprocess

def run_script(script_name):
    try:
        print(f"Starting {script_name}...")
        result = subprocess.run(['python3', script_name], capture_output=True, text=True, check=True)
        print(f"Finished {script_name}.")
        print(f"Output:\n{result.stdout}")
        if result.stderr:
            print(f"Errors:\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_name}: {e}")
        print(f"Error output:\n{e.stderr}")

if __name__ == "__main__":
    run_script('download_script.py')
    run_script('import_csv2.py')
