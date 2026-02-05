import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"


REPO_NAME = "Deepfake-Detection"
AUTHOR_USER_NAME = "pradeepanpp"
SRC_REPO = "cnnClassifier" 
AUTHOR_EMAIL = "pradeep0076@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A production-grade MLOps pipeline for real-time deepfake detection using a lightweight 2.2M parameter MobileNetV2 architecture",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)