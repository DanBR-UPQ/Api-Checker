import subprocess
import sys

def run_tests():
    print("Welcome to ApiCheck. Testing in progress....\n")

    result = subprocess.run(
        ["pytest", "-v", "--junitxml=reports/results.xml"],
        text=True
    )

    if result.returncode == 0:
        print("\nALL TESTS PASSED")
    else:
        print("\nSOME TESTS FAILED")

    sys.exit(result.returncode)


if __name__ == "__main__":
    run_tests()