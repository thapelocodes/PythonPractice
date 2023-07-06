def Hello4(ArgCount, *VarArgs):
    print("You passed", ArgCount, "arguments.")
    for Arg in VarArgs:
        print(Arg)
