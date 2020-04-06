import subprocess

import os

import settings


def main():
    base_command = [
        'commcare-export',
        '--project', settings.PROJECT,
        '--username', settings.USERNAME,
        '--auth-mode', settings.AUTH_MODE,
        '--password', settings.PASSWORD,
        '--output-format', settings.OUTPUT_FORMAT,
    ]
    filenames = ['leadership_governance.xlsx']
    for det_file in filenames:
        det_file_path = os.path.join('det_configs', det_file)
        command = base_command + ['--query', det_file_path]
        print(f"running {' '.join(command)}")
        subprocess.run(command)


main()
