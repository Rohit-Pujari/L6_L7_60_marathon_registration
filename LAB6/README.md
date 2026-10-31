# L6_L7_60 — Marathon Registration

Lab 6: Code and Branch Coverage

## About

A small Python module that works out race entry fees by distance, age and early-bird booking, assigns runners to a start wave and decides each runner's finishing status.

## Files

| File | Description |
|------|-------------|
| `marathon_registration.py` | The module under test |
| `test_marathon_registration.py` | Starter test file |
| `CodeCoverageTest_marathon_registration.py` | Test cases used for statement/code coverage |
| `BranchCoverageTest_marathon_registration.py` | Test cases used for branch coverage |

## Lab 6 submission checklist

Submit the following Lab 6 evidence together:

1. **Code coverage test file** — `CodeCoverageTest_marathon_registration.py`.
2. **Branch coverage test file** — `BranchCoverageTest_marathon_registration.py`.
3. **Coverage screenshots** — terminal output showing the code coverage and branch coverage results.
4. **Lab report** — `Marathon_Registration_Lab6_Coverage_Report.docx`, documenting the objective, test approach, commands, coverage results and evidence.
5. **Git commits** — separate commits for the code coverage and branch coverage test files.

The report should be submitted along with the test files and screenshots if the instructor's submission instructions require a report. The lab handout specifically lists the test files, coverage screenshots and commits; it does not explicitly define a separate report format.

## Running the coverage tests

Run these commands from the `LAB6` directory:

```bash
python -m pip install pytest coverage

coverage run -m pytest CodeCoverageTest_marathon_registration.py
coverage report -m

coverage run --branch -m pytest BranchCoverageTest_marathon_registration.py
coverage report -m
```

Keep all Lab 6 work in this `LAB6` folder. Lab 7 will be added to this repo later.

Refer to the lab handout for the complete instructions.
