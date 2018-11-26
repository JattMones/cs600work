import sys
a = ""
if(sys.argv[1] is "0"):
    print("Method1")
    helpPage().run()
if(sys.argv[1] is "1"):
    print("Method2")
    gamingPage().run()
if(sys.argv[1] is "2"):
    print("Method3")
    workPage().run()
if(sys.argv[1] is "3"):
    print("Method4")
    customPage().run()
else:
    main().run()
