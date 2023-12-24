path_fife = input().split("\\")

path_file_args = path_fife[-1]
path_fife_name_with_ext = path_file_args.split(".")
path_name = path_fife_name_with_ext[0]
path_ext = path_fife_name_with_ext[1]

print(f"File name: {path_name}")
print(f"File extension: {path_ext}")
