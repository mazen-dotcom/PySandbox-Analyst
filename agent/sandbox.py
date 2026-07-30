from e2b_code_interpreter import Sandbox
from pathlib import Path
sandbox = Sandbox.create()



def upload_files_to_sandbox(files_path_list):
    remote_path_list = []

    for path in files_path_list:
        with open(path, 'rb') as f:
            remote_path_list.append(sandbox.files.write(Path(path).name, f))
    


def execute_code(code: str):
    execu = sandbox.run_code(code)
    return execu.results





