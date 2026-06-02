# rotten-potato-TCM

Test Case Management Repository for Project Rotten Potato.

## Repository hierarchy

This repository is organized from highest scope to lowest scope:

1. **Test Project** (`test-project/`): top-level container for the Rotten Potato application.
2. **Test Suites** (`test-project/suites/<suite-name>/`): reusable feature/module groupings (for example: `auth`, `ui`, `connectivity`, `performance`).
3. **Test Cases** (`test-project/suites/<suite-name>/test-cases/`): granular and atomic test configurations for single verifiable conditions.

```text
test-project/
└── suites/
    ├── auth/
    │   └── test-cases/
    ├── ui/
    │   └── test-cases/
    ├── connectivity/
    │   └── test-cases/
    └── performance/
        └── test-cases/
```
