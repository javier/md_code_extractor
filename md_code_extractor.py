import os
import re
import sys

def extract_code_blocks_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Extract fenced code blocks
        code_blocks = re.findall(r'```.*?\n(.*?)```', content, re.DOTALL)
        return code_blocks

def extract_code_blocks_from_repo(repo_path):
    code_blocks_dict = {}
    for root, _, files in os.walk(repo_path):
        for file in sorted(files):
            if file.endswith('.md') or file.endswith('.mdx'):
                file_path = os.path.join(root, file)
                code_blocks = extract_code_blocks_from_file(file_path)
                if code_blocks:
                    relative_path = os.path.relpath(file_path, repo_path)
                    code_blocks_dict[relative_path] = code_blocks
    return code_blocks_dict

def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_code_blocks.py <repo_path> <output_file>")
        return

    repo_path = sys.argv[1]
    output_file = sys.argv[2]

    code_blocks_dict = extract_code_blocks_from_repo(repo_path)

    sorted_code_blocks = dict(sorted(code_blocks_dict.items()))

    with open(output_file, 'w', encoding='utf-8') as file:
        for file_path, code_blocks in sorted_code_blocks.items():
            file.write(f'## File: {file_path}\n')
            for code_block in code_blocks:
                file.write(f'```\n{code_block}\n```\n\n')

    print(f'Extracted code blocks have been saved to {output_file}')

if __name__ == "__main__":
    main()
