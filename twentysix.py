# 'subciph'
# '-..---..--....-........--......--.-....--.......-.'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
pan_a = 'the quick brown fox jumps over the lazy dog'
pan_b = 'sphinx of black quartz judge my vow'

available_a = 'tqbfjotld'
# sibqrasgv
available_b = 'sobqjmv'
# mfbkscmrv 

# => 'abcfgikmqrsv'

sub_a = 'thequickbrownfxjmpsvlazydg'
sub_b = 'sphinxofblackqurtzjdgemyvw'

def translate_a_to_b(a):
    return ''.join([sub_b[sub_a.index(c)] for c in a])

def translate_b_to_a(b):
    return ''.join([sub_a[sub_b.index(c)] for c in b])

print(translate_a_to_b(available_a))
print(translate_b_to_a(available_a))

test = ['phillyssubmarinesandwich', pan_a, pan_b]

def distinctify(s):
    ans = ''
    seen = set()
    for c in s:
        if c in ALPHABET:
            if c not in seen:
                ans += c
                seen.add(c)
        else:
            ans += c
    
    return ans.replace('  ', ' ')

print([distinctify(test_i) for test_i in test])
