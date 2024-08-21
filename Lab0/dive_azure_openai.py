import getpass
import os


def set_api_key():
    # Get the API key from the user
    api_key = getpass.getpass("Enter your AZURE_OPENAI_API_KEY: ")

    if "AZURE_OPENAI_API_KEY" in os.environ:
        overwrite = (
            input(
                "AZURE_OPENAI_API_KEY environment variable already exists.\nDo you want to overwrite it? [y/N]: "
            )
            .strip()
            .lower()
        )
        if overwrite == "y":
            os.environ["AZURE_OPENAI_API_KEY"] = api_key
            print(f"Updated the environment variable AZURE_OPENAI_API_KEY.")
        else:
            print("No changes made to AZURE_OPENAI_API_KEY.")

    # Get the home directory
    home_dir = os.path.expanduser("~")
    write_api_key_to_file(api_key, os.path.join(home_dir, ".bash_profile"))
    write_api_key_to_file(api_key, os.path.join(home_dir, ".bashrc"))


def write_api_key_to_file(api_key, path):
    # Read the existing file content
    if os.path.exists(path):
        with open(path, "r") as file:
            lines = file.readlines()
    else:
        lines = []

    # Check if the environment variable already exists
    env_var_line = f'export AZURE_OPENAI_API_KEY="{api_key}"\n'
    existing_line_index = next(
        (
            i
            for i, line in enumerate(lines)
            if line.startswith("export AZURE_OPENAI_API_KEY=")
        ),
        None,
    )

    # If the environment variable already exists, ask for confirmation to overwrite
    if existing_line_index is not None:
        overwrite = (
            input(
                f"AZURE_OPENAI_API_KEY already exists in {path}.\nDo you want to overwrite it? [y/N]: "
            )
            .strip()
            .lower()
        )
        if overwrite == "y":
            lines[existing_line_index] = env_var_line
        else:
            print("No changes made to .bash_profile.")
            return None
    else:
        # Add the new environment variable
        lines.append(env_var_line)

    with open(path, "w") as file:
        file.writelines(lines)
    print(f"Updated {path} with AZURE_OPENAI_API_KEY.")