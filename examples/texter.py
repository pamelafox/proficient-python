from texter import uppercase, lowercase, binarize, clapify, emojify, exclamify, mystery

# Try these functions in the console and see what they do!
uppercase('ReplIt is so not intuitive')
lowercase('Learning as I go')
clapify('I have a cold')
emojify('I am sick and tired of having a cold')
exclamify('T00 many hidden links')
binarize('I am not a computer')
mystery('Wee Free Men. I am not gonna be a knee.')

# Examples from class:
uppercase('hi hello')
lowercase('HI HELLO')
clapify('lets all clap')
clapify(uppercase('just do it'))
uppercase('just do it')
clapify('JUST DO IT')
exclamify('i love encanto')
exclamify(clapify(uppercase('just do it')))
uppercase(clapify('just do it'))
binarize('abc')
clapify(binarize('abc'))
emojify('im sick of cake')
exclamify(emojify('im sick of cake'))
mystery('hello world')
mystery('hello world i am just going to type a lot')