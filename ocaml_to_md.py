import re

def parse_ocaml_code(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""
    
    # Remove comments
    code = re.sub(r'\(\*.*?\*\)', '', code, flags=re.DOTALL)

    # Find all type definitions
    types = re.findall(r'type (\w+) =\s*([\s\S]*?)(?=\n\ntype|\Z)', code)

    enum_types = []
    record_types = []

    for type_name, type_body in types:
        type_body = type_body.strip()
        if type_body.startswith('|') or '|' in type_body:
            enum_types.append((type_name, type_body))
        elif type_body.startswith('{') or '{' in type_body:
            record_types.append((type_name, type_body.replace("}","")))

    markdown = "# OCaml Types\n\n"
    summary_table = "| Type Name | Type Category |\n|-----------|----------------|\n"

    if enum_types:
        markdown += "## Enumerated Types\n"
        for enum_name, enum_body in enum_types:
            summary_table += f"| {enum_name} | Enumerated |\n"
            values = [value.strip() for value in enum_body.split('|')]
            markdown += f"### {enum_name}\n"
            markdown += "\n".join([f"- {value}" for value in values if value])
            markdown += "\n\n"

    if record_types:
        markdown += "## Record Types\n"
        for record_name, record_body in record_types:
            summary_table += f"| {record_name} | Record |\n"
            fields = re.findall(r'(\w+)\s*:\s*([^;]+);?', record_body)
            markdown += f"### {record_name}\n\n"
            markdown += "| Field | Type |\n|-|-|\n"
            markdown += "\n".join([f"| {field.strip()} | {ftype.strip()} |" for field, ftype in fields])
            markdown += "\n\n"

    return summary_table + "\n" + markdown

def main():
    input_file = 'types.ml'
    output_file = 'types.md'

    markdown_content = parse_ocaml_code(input_file)

    if markdown_content:
        with open(output_file, 'w') as file:
            file.write(markdown_content)
        print(f"Markdown content written to {output_file}")
    else:
        print("No content to write.")

if __name__ == "__main__":
    main()
