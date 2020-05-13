import os


def execute_script_with_args_if_file_does_not_exists(script, file, *args):
    # print(script)
    # print(file)
    # print(args)
    if not os.path.exists(file):
        print("Creating {}".format(file))
        script(*args)
    else:
        print("{} already exists".format(file))
