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
        '--output', settings.OUTPUT,
        '--batch-size', settings.BATCH_SIZE,
        '--verbose'
    ]
    det_folder = 'det_configs'
    for det_file in os.listdir(det_folder):
        det_file_path = os.path.join(det_folder, det_file)
        command = base_command + ['--query', det_file_path]
        print(f"running {' '.join(command)}")
        subprocess.run(command)


main()
