# relative import
# from .sub_package_01.run import runner_from_sub_package
from sub_package_01.run import runner_from_sub_package


def runner_from_main_package():
    print(f"runner_from_main_package: {__name__}")


if __name__ == '__main__':
    runner_from_main_package()
    runner_from_sub_package()
