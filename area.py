import sys
try:
    file=open(file_name,"w")
    except IOError:
        print("there was an error on writting to", file_name)
        sys.exit()
        print("enter",file_finish)
        print "'when finished"
        while file_text!=file_finish:
            file_text=raw_input("enter text:")
            if file_text==file_finish:
                file.close
                break
            file.write(file_text)
            file.write("\n")
            file.close()
            file_name=input("enter filename:")
            if len(file_name)==0:
                print("next time please enter something")
                sys.exit()
                try:
                    file=open(file_name,"r")
                    except IOError:
                        print("there was an error reading file")
                        sys.exit()
                        file_text=file.read()
                        file.close()
                        print(file_text)
