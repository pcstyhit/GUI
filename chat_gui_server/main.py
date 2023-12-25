import os
import sys

PROJECT_PATH = os.path.dirname(__file__)
PACKAGES_PATH = f"{PROJECT_PATH}/packages"

# Add third-part package path.
sys.path.insert(0, PACKAGES_PATH)

if __name__ == '__main__':
    from apis.post import test_demo
    test_demo()
