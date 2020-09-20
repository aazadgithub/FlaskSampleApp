import compileall

isSuccess = compileall.compile_dir('./', maxlevels=10, force=True)

if isSuccess:
    print("build is successful")
else:
    print("build is failed")