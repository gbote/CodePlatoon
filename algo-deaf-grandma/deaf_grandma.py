def deaf_grandma():
        import re
        goodbye = 0

        print('HEY KID!')
        while goodbye < 2:
                says = input()
                if says == "":
                        print("WHAT?!")
                elif says == "GOODBYE!" and goodbye == 0:
                    goodbye += 1
                    print("LEAVING SO SOON?")
                elif says == "GOODBYE!" and goodbye == 1:
                    goodbye = 2
                    print("LATER SKATER!")
                elif re.search("[a-z]",says) != None:
                    print("SPEAK UP, KID!")
                elif re.search("[A-Z]+",says) != None:
                    print("NO, NOT SINCE 1946!")
                elif re.search("[a-zA-Z]+", says) is None:
                        print("SOMETHIN WRONG WITH YOU? YOURE MOVIN YOUR MOUTH BUT NOTHING IS COMING OUT. SAY IT WITH YOUR CHEST SONNY!")


deaf_grandma()
