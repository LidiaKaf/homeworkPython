from google_trans_new import google_translator
with open('file_p4.txt', 'r') as f:
    while True:
        en_string = f.readline()
        if not en_string:
            break
        translator = google_translator()
        result = translator.translate(en_string, lang_tgt='ru')
        print(result)
        with open('file_p4_new.txt', 'a', encoding='utf-8') as n:
            n.writelines(result + '\n')

