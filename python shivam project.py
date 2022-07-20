def to_morse_code(text):
    code = {' ':' |','a':' .-','b':' -...',
'c':' -.-.','d':' -..','e':' .',
'f':' ..-.','g':' --.','h':' ....',
'i':' ..','j':' .---','k':' -.-',
'l':' .-..','m':' --','n':' -.',
'o':' ---','p':' .--.','q':' --.-',
'r':' .-.','s':' ...','t':' -',
'u':' ..-','v':' ...-','w':' .--',
'x':' -..-','y':' -.--','z':' --..',
'1':' .----','2':' ..---','3':' ...--',
'4':' ....-','5':' .....','6':' -....',
'7':' --...','8':' ---..','9':' ----.',
'0':' -----',',':' --..--','.':' .-.-.-',
'(':' -.--.',')':' -.--.-'
}
    morse_code = " "

    for x in text:
        morse_code += code[x.lower()]

    return morse_code

text = input("Enter text (in English) to convert to Morse Code :: ")
print(to_morse_code(text))
