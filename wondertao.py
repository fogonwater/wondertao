import random

TEXT1, TEXT2 = "alice.txt", "tao.txt"

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def write_text(s, fname):
    f = open(fname, 'w')
    f.write(s)
    print fname, "written"
    f.close()

def create_chain(file_paths):
    markov_chain = {}
    word1 = "\n"
    word2 = "\n"
    for path in file_paths:
        with open(path) as file:
            for line in file:
                for current_word in line.split():
                    if current_word.strip() in ("", "*", "PART") or is_number(current_word[0]): continue                        
                    markov_chain.setdefault((word1, word2), []).append(current_word)
                    word1 = word2
                    word2 = current_word
    return markov_chain

def construct_paragraph(markov_chain, word_count=100):
    generated_sentence = ""
    word_tuple = random.choice(markov_chain.keys())
    w1 = word_tuple[0]
    w2 = word_tuple[1]
    
    for i in xrange(word_count):
        newword = random.choice(markov_chain[(w1, w2)])
        generated_sentence = generated_sentence + " " + newword
        #shuffle existing words up
        w1 = w2
        w2 = newword
        
    return generated_sentence

def main():
    markov = create_chain( (TEXT1, TEXT2) )
    paragraph = construct_paragraph(markov_chain = markov, word_count=900)
    lines = paragraph.split('.')

    output = []
    #ignore the first and last partial sentences
    for line in lines[1:-1]:
        wisdom = line.strip() + '.'
        if len(wisdom) <= 140: output.append(wisdom)

    write_text('\n\n'.join(output), 'wondertao_output.txt')


if __name__ == '__main__':
    main()
