import random
img = ['''
                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5#&&&&&&&&&&&&&&&&&&&&&&&&##&##5~.                
                                                .~G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G~.                
                                                .!G&&G7^^:::^^^:::::::^::~JG&@@@&G~.                
                                                .!G&&G~                  :?P&@@@&G~.                
                                                .!G@@G!.                 :?P&@@@&G~.                
                                                .^?YY?^                  :?P&@@@&G~.                
                                                  ....                   :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&P~                 
                                            ............................ ^JG&@@@&G!:.........       
                                           ^?YY5YYYYYYYYYYYYYYYYYY55YY5YY5G#@@@@@#P5YYYYY55YJ!:     
                                          .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^     
                                          .~P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY^     
                                           :~77777777777777777777777777777777777777777777777!~.     
                                                                                                    
''',
'''                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5#&&&&&&&&&&&&&&&&&&&&&&&&##&##5~.                
                                                .!G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G~.                
                                                .~G@@G7^^:::::::::::::^::~JG&@@@&G~.                
                                                .~G@@G~                  :?P&@@@&G~.                
                                                 ~G&@G~                  :?P&@@@&G~.                
                                               :!YB##B5?~:               :?P&@@@&G~.                
                                             .~?557~^~?Y5J^              :?P&@@@&G~.                
                                             :Y5?~.   .~55!:             :?P&@@@&G~.                
                                             :J5J!.   .~55!:             :?P&@@@&G~.                
                                             .^7PPJ7!7YP5?:              :?P&@@@&G~.                
                                               .^!J555J7:.               :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&P~                 
                                            ............................ ^JG&@@@&G!:.........       
                                           ^?YY5YYYYYYYYYYYYYYYYYY55YY5YY5G#@@@@@#P5YYYYY55YJ!:     
                                          .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^     
                                          .~P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY^     
                                           :~77777777777777777777777777777777777777777777777!~.     
                                                                                                    ''',
'''                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5#&&&&&&&&&&&&&&&&&&&&&&&&##&##5~.                
                                                .!G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G~.                
                                                .~G@@G7^^:::::::::::::^::~JG&@@@&G~.                
                                                .~G@@G~                  :?P&@@@&G~.                
                                                 ~G&@G~                  :?P&@@@&G~.                
                                               :!YB##B5?~:               :?P&@@@&G~.                
                                             .~?557~^~?Y5J^              :?P&@@@&G~.                
                                             :Y5?~.   .~55!:             :?P&@@@&G~.                
                                             :J5J!.   .~55!:             :?P&@@@&G~.                
                                             .^7PPJ7~7YP5?:              :?P&@@@&G~.                
                                               .^7YGBGY!:                :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .:!5Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^!5Y^                  :?P&@@@&G~.                
                                                 .^!5Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .:!YJ:                  :?P&@@@&G~.                
                                                  ..::.                  :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&P~                 
                                            ............................ ^JG&@@@&G!:.........       
                                           ^?YY5YYYYYYYYYYYYYYYYYY55YY5YY5G#@@@@@#P5YYYYY55YJ!:     
                                          .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^     
                                          .~P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY^     
                                           :~77777777777777777777777777777777777777777777777!~.     
                                                                                                    ''',
'''                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5#&&&&&&&&&&&&&&&&&&&&&&&&##&##5~.                
                                                .!G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G~.                
                                                .~G@@G7^^:::::::::::::^::~JG&@@@&G~.                
                                                .~G@@G~                  :?P&@@@&G~.                
                                                 ~G&@G~                  :?P&@@@&G~.                
                                               :!YB##B5?~:               :?P&@@@&G~.                
                                             .~?557~^~?Y5J^              :?P&@@@&G~.                
                                             :Y5?~.   .~55!:             :?P&@@@&G~.                
                                             :J5J!.   .~55!:             :?P&@@@&G~.                
                                             .^?PPJ7~7YP5?:              :?P&@@@&G~.                
                                               .^7YGBGY!:                :?P&@@@&G~.                
                                      .:^^....    ^75Y^                  :?P&@@@&G~.                
                                     .^75G5Y?!^:.:^75Y^                  :?P&@@@&G~.                
                                       .:~7JY555YJY5PY^                  :?P&@@@&G~.                
                                              .^~7YPGY^                  :?P&@@@&G~.                
                                                  ^75Y^                  :?P&@@@&G~.                
                                                 .^!5Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .:!YJ:                  :?P&@@@&G~.                
                                                  ..::.                  :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&P~                 
                                            ............................ ^JG&@@@&G!:.........       
                                           ^?YY5YYYYYYYYYYYYYYYYYY55YY5YY5G#@@@@@#P5YYYYY55YJ!:     
                                          .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^     
                                          .~P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY^     
                                           :~77777777777777777777777777777777777777777777777!~.     ''',
'''                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5#&&&&&&&&&&&&&&&&&&&&&&&&##&##5~.                
                                                .!G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G~.                
                                                .~G@@G7^^:::::::::::::^::~JG&@@@&G~.                
                                                .~G@@G~                  :?P&@@@&G~.                
                                                 ~G&@G~                  :?P&@@@&G~.                
                                               :!YB##B5?~:               :?P&@@@&G~.                
                                             .~?557~^~?Y5J^              :?P&@@@&G~.                
                                             :Y5?~.   .~55!:             :?P&@@@&G~.                
                                             :J5J!.   .~55!:             :?P&@@@&G~.                
                                             .^?PPJ!~7YP5J:              :?P&@@@&G~.                
                                               .^7YGBGY!:                :?P&@@@&G~.                
                                      .:^^....    ^75J^    ..::^:.       :?P&@@@&G~.                
                                     .^75G5Y?!^:.:^75Y~:^~!?YPGPJ~.      :?G&@@@&G~.                
                                       .:~7JY555JJJ5GG5Y555Y?!~:.        :?P&@@@&G~.                
                                              .^~7YGBP7^:.               :?P&@@@&G~.                
                                                  :!5Y^                  :?G&@@@&G~.                
                                                 .:!5Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .:!YJ:                  :?P&@@@&G~.                
                                                  ..::.                  :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&P~                 
                                            ............................ ^JG&@@@&G!:.........       
                                           ^?YY5YYYYYYYYYYYYYYYYYY55YY5YY5G#@@@@@#P5YYYYY55YJ!:     
                                          .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^     
                                          .~P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY^     
                                           :~77777777777777777777777777777777777777777777777!~.     ''',
'''                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5#&&&&&&&&&&&&&&&&&&&&&&&&##&##5~.                
                                                .!G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G~.                
                                                .~G@@G7^^:::::::::::::^::~JG&@@@&G~.                
                                                .~G@@G~                  :?P&@@@&G~.                
                                                 ~G&@G~                  :?P&@@@&G~.                
                                               :!YB##B5?~:               :?P&@@@&G~.                
                                             .~?557~^~?Y5J^              :?P&@@@&G~.                
                                             :Y5?~.   .~55!:             :?P&@@@&G~.                
                                             :J5J!.   .~55!:             :?P&@@@&G~.                
                                             .^?PPJ!~7YP5J:              :?P&@@@&G~.                
                                               .^7YGBGY!:                :?P&@@@&G~.                
                                      .:^^....    ^75J^    ..::^:.       :?P&@@@&G~.                
                                     .^75G5Y?!^:.:^75Y~:^~!?YPGPJ~.      :?G&@@@&G~.                
                                       .:~7JY555JJJ5GG5Y555Y?!~:.        :?P&@@@&G~.                
                                              .^~7YGBP7^:.               :?P&@@@&G~.                
                                                  :!5Y^                  :?G&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^75Y^                  :?P&@@@&G~.                
                                                 .^!5Y^                  :?P&@@@&G~.                
                                                 .!J5J^                  :?P&@@@&G~.                
                                               .~JPP7^.                  :?P&@@@&G~.                
                                             .!JGP7^.                    :?P&@@@&G~.                
                                           .!JGP7^.                      :?P&@@@&G~.                
                                         :!YGP!:.                        :?P&@@@&G~.                
                                       .!JP5!:                           :?P&@@@&G~.                
                                     .^755!:                             :?P&@@@&G~.                
                                      ::^:                               :?P&@@@&G~.                
                                                                         :?P&@@@&G~.                
                                                                         :?P&@@@&P~                 
                                            ............................ ^JG&@@@&G!:.........       
                                           ^?YY5YYYYYYYYYYYYYYYYYY55YY5YY5G#@@@@@#P5YYYYY55YJ!:     
                                          .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^     
                                          .~P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY^     
                                           :~77777777777777777777777777777777777777777777777!~.     
                                                                                                    ''',
'''                                                                                                    
                                                                                                    
                                                                                                    
                                                 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                 
                                                .~5B#&&&&&&&&&&&&&&&&&&&&&######B5~.                
                                                .!G@@&BGGGGGGGGGGGGGGGGGGG#&@@@@@G!.                
                                                .!G&&G7^:::::::::::::::::~?P&@@@@G!.                
                                                .!G&&P~                  .75#@@@&G!.                
                                                 ~G@&G~                  .75&@@@@G!.                
                                               .!YB&#B5?^.               :75&@@@&G!.                
                                             .~?55?~~!J55?:              .75&@@@@G!.                
                                             :J5J!.   :!55!.             :75#@@@@G!.                
                                             :J5J!.   .!55!.             .75&@@@@G!.                
                                             .^7PPJ7!75P57:              .75&@@@@G!.                
                                               .^7YGBGJ!:                .75&@@@&G!.                
                                      .:^^:...   .^7YJ:    ..:^^:.       :75&@@@@G!.                
                                     .^75GP5J7~^::^75Y~:~!7JYPGPJ~.      :75#@@@@G!.                
                                        .^!?Y5PP55Y5GBPPPP5Y7!^:.        :75&@@@@G!.                
                                              :^!?5GBP?~:.               .75#@@@@G!.                
                                                  ^7YJ:                  :75&@@@@G!.                
                                                 .^7YJ^                  .75#@@@@G!.                
                                                 .^7YJ^                  .75&@@@@G!.                
                                                 .^7YJ^                  .75&@@@@G!.                
                                                 .^7YJ:                  .75&@@@@G!.                
                                                 .:!YJ:                  .75&@@@@G!.                
                                                 .!JG5^                  .75&@@@@G!.                
                                               .~?PGGP5?:                .75&@@@@G!.                
                                             .~?PP7^:~YP5?^              .75&@@@@G!.                
                                           .~JGP7^.   .~YP5J^            :75#@@@@G!.                
                                         .!JGP7:.        ^JPPJ^.         .75&@@@@G!.                
                                       :!YP5!:.            ^J5PJ~.       .75#@@@@G!.                
                                     .^?P5!:                 ^J5Y?:      .75#@@@@G!.                
                                      .::.                     .^^.      :75#@@@@G!.                
                                                                         :75&@@@&G!.                
                                                                         .75&@@@&G!.                
                                            ...........................  :7P&@@@@G!:..........      
                                           :7YYYYYYYYYYYYYYYYYYYYYYYYYYYY5GB&@@@@#P5YYYYYYYYJ7:     
                                           ~P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&P~     
                                           ~P#&@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@&&&&&@&&@&&@@&#5^     
                                           .^!!77!!!!!!!!!!!!!!!!!!!!77!!!!!!77777!!77!!!!77!~.     ''']



words = ["summer", "winter","butterfly","programming"]

word = random.choice(words)
print(word)

answer = ["_" for s in word]
print(" ".join(answer) )

counter =len(word)
wrong = 0
while counter != 0 and wrong != 6:
    print(img[wrong])
    symbol = input("Enter one symbol : ")
    if len(symbol) != 1:
        print("error input...")
        wrong+=1
        continue

    index = word.find(symbol)
    if index == -1:
        wrong+=1
    if index != -1 and answer[index] != '_':
        wrong+=1
    while index != -1:
        counter-= 1
        answer[index]= symbol
        index = word.find(symbol, index+1)
    print(" ".join(answer) )

if wrong == 6:
    print("Game over")
    print(img[wrong])
else:
    print("Congratulation!!!! You is winner!!!")
