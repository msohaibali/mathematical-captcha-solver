from setuptools import find_packages, setup

setup(
    name="mathematical-captcha-solver",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "tensorflow",
        "keras",
        "opencv-python",
        "matplotlib",
        "Pillow",
        "pandas",
        "numpy",
        "pytest",
        "coverage",
    ],
)
