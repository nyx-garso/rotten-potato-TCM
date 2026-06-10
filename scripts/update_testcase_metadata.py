import os
import yaml

TEST_CASES_DIR = "Test Suites"

FIELDS = [
    ("Test Schedule", "Enter test schedule (e.g. 2024/04/15)"),
    ("Assigned Tester", "Enter tester name"),
    ("Date of Execution", "Enter execution date (e.g. 2024/04/16)"),
    ("Status", "Enter status (PASSED/FAILED/Draft)"),
    ("Bug ID", "Enter bug ID (or leave blank)"),
    ("Title", "Enter test case title")
]

def update_frontmatter(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if content.startswith("---"):
        parts = content.split("---", 2)
        frontmatter = yaml.safe_load(parts[1]) or {}
        body = parts[2]
    else:
        frontmatter = {}
        body = content

    print(f"\nUpdating metadata for: {file_path}")
    for key, prompt in FIELDS:
        current = frontmatter.get(key, "")
        new_val = input(f"{prompt} [current: {current}] → ").strip()
        if new_val:
            frontmatter[key] = new_val

    new_content = "---\n" + yaml.dump(frontmatter, sort_keys=False) + "---\n" + body

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ Updated successfully.")

def main():
    # Build suite → files mapping
    suites = {}
    for root, _, fs in os.walk(TEST_CASES_DIR):
        section = os.path.basename(root)
        md_files = [os.path.join(root, f) for f in fs if f.endswith(".md")]
        if md_files:
            suites[section] = md_files

    while True:
        print("\nAvailable Test Suites:")
        for i, suite in enumerate(suites.keys(), 1):
            print(f"{i}. {suite}")
        print("Q. Quit")

        choice = input("Select a suite number (or Q to quit): ").strip()
        if choice.lower() == "q":
            print("👋 Exiting updater.")
            break

        try:
            suite_idx = int(choice) - 1
            suite_name = list(suites.keys())[suite_idx]
            files = suites[suite_name]

            while True:
                print(f"\nTest cases in {suite_name}:")
                for j, f in enumerate(files, 1):
                    print(f"{j}. {os.path.basename(f)}")
                print("B. Back to suites")
                print("Q. Quit")

                case_choice = input("Select a test case number: ").strip()
                if case_choice.lower() == "q":
                    print("👋 Exiting updater.")
                    return
                if case_choice.lower() == "b":
                    break

                try:
                    file_idx = int(case_choice) - 1
                    update_frontmatter(files[file_idx])
                except (ValueError, IndexError):
                    print("❌ Invalid selection.")
        except (ValueError, IndexError):
            print("❌ Invalid suite selection.")

if __name__ == "__main__":
    main()
