#https://www.hackerrank.com/challenges/determining-dna-health/problem

# A reattempt at the DNA health problem.
# About 6 months ago I attempted this problem. Since then a 
#   lot has changed and I've learned so much.

# First, off, why didn't I use dictionaries when I originally
#   attempted this problem???  Like, seriously...

# Output format: 
# Print two space-separated integers describing the 
#   respective total health of the unhealthiest and
#   the healthiest strands of DNA.

## Sample input (see problem's page for more details)
#    6
#    a b c aa d b
#    1 2 3 4 5 6
#    3
#    1 5 caaab
#    0 4 xyz
#    2 4 bcdybc

# Output result (see older file for explanation)
#   0 19

# some thoughts
# make a tree where the path along the tree is each 
#   character. 
# For instance consider the following
#
#   gene pool: [abcd, a, ab, ac, ad, bc, cd, a, bb, bcd, abcd, aaaa, aa, a ]
#   health   : [ 11,  3, 4,  5,  1,  20,  0, 6, 13,  15,  56,   99,  38, 45]
#
# will translate to the following tree:


example = {
    'a': {
        'end': 3 + 6 + 45,
        'a': {
            'end': 38,
            'a': {
                'a': {
                    'end': 99
                },
            },
            'b': {
                'end': 1
            }
        },
        'b': {
            'end': 4,
            'a': {
                'end': 8
            },
            'c': {
                'd': {
                    'end': 11 + 56
                }
            }
        },
        'c': {
            'end': 5
        },
        'd': {
            'end': 1
        },
    },
    'b': {
        'b': {
            'end': 13
        },
        'c': {
            'end': 20,
            'd': {
                'end': 15
            }
        }
    },
    'c': {
        'd': {
            'end': 0
        }
    }
}


# This is achieved with build_health_tree. This tree is built on
# the "first" pass over the gene pool.
# Think of this gene pool as a machine filter

# The next step is feeding the dna string, à la a tap feed on
#  a turing machine.

# The machine will check if the character on the dna str is
#   a key in the first dictionary. If so, move inside this
#   dictionary.
#
#   Check if there is an 'end' key in the inner dictionary,
#   if so, add the value to the total health value.
#  
#   Now, Increment to the next char on the dna
#   string. 
#   
#   Repeat the above steps until a key can't be found. 
#   Reset back to the first character and move forward 1 
#   char. 
#   
#   Repeat this whole process.
#
#   However, this can be sped up.
#
# On the other hand it should be possible to make a single pass
#   without back tracking at all.
#
#   Keep a dynamic list of dictionaries, that grows and shrinks
#   over time.
#   
#   For instance, using the example dictionary from earlier,
#   consider the following dna str

#dna_str = 'aabb'

# our dynamic list of dictionaries followes these rules:
# dyn = []
#   look at index 0 of dna_str 
#   since 'a' is in the gene pool, add it to our list
# dyn = [ a ]    (remember this is a list of dictionaires, I'm simply representing them with their keys)
#   move inside the health_tree[a]
#   check for 'end' key at this branch.
#   look at the next index in the dna_str
#   Is the char 'a' a branch on the inner dictionary?
#   yes,
#   move within that dictionary 
#   so update [a] to now be [ aa ]
#   Additionally, is 'a' a branch on the root? 
#   Yes, add it to our list
#   our list now contains [aa, a]
#   
#   next char index for dna_str (at this point we've looked up to 'aab')
#   is 'b' a key in any of the dictionaries within our list. 
#   Yes, in the dictionary 'aa' and dictionary 'a' and in root dictionary
#   So, you now have list of dictionaries [aab, ab, b]
#   
#   look at the 4th char.
#   check key 'b' for each dictionary in the list of dicts.
#       'b' is NOT a key for dict "aab"
#           drop that dictionary as we have exhausted it.
#       'b' is NOT a key for dict "ab"
#           drop that dictionary as we have exhausted it.
#       'b' IS a key for dictionary "b"
#       
#       And also 'b' is a starting key.
#
#   the dynamic list of dictionaries is now [bb, b]
#


# overall order of operations for calculating health value
# for dictionary in dyn_dictionary_list:
# if dna[i] is a key in dictionary: 
#   dyn_dictionary_list[d] = 



def healthDNA(health_tree, regular_dictionary, start, end, dna):
    total_health = 0


    dyn_dictionary_list = []


    for char in dna:
        temp_dictionary_list = []
        for dict_item in dyn_dictionary_list:
            if char in dict_item:
                inner_dict = dict_item[char]
                temp_dictionary_list.append(inner_dict)
                try:
                    total_health += sum_ends(inner_dict['end'], start, end)
                except KeyError:
                    pass
        dyn_dictionary_list = temp_dictionary_list
        if char in health_tree:
            inner_dict = health_tree[char]
            dyn_dictionary_list.append(inner_dict)
            try:
                total_health += sum_ends(inner_dict['end'], start, end)
            except KeyError:
                pass
    return total_health

def sum_ends(end_dict:dict, start, stop):
    end_value = 0
    for key in end_dict.keys():
        if start <= int(key) <= stop:
            end_value += end_dict[key]
    return end_value



def build_health_tree(genes, health_values):
    gene_pool = list(tuple(zip(genes, health_values)))
    uniform = True
    uniform_len = len(gene_pool[0][0])
    regular_dictionary = {}
    health_tree = {}
    for i, gene_health in enumerate(gene_pool):
        gene, health = gene_health
        if uniform_len != len(gene):
            uniform = False
        try:
            regular_dictionary[gene][i] = int(health)
        except KeyError:
            regular_dictionary[gene] = {
                i: int(health)
            }
        dic = health_tree
        while gene:
            ch = gene[0]
            gene = gene[1:]
            if ch not in dic:
                dic[ch] = {}
            dic =  dic[ch]
        try:
            dic['end'][i] = int(health)
        except KeyError:
            dic['end'] = {
                i: int(health)
            }
    
    #print(gene_pool)
    #print(json.dumps(health_tree, indent=3))
    print('done with health tree')
    return health_tree, regular_dictionary, uniform




def run_test(test_file):
    with open(test_file, 'r') as file:
        lines = file.readlines()

    genes = lines[1].rstrip().split()
    healths = list(map(int, lines[2].rstrip().split()))
    
    health_tree, reg_dict, uniform_bool = build_health_tree(genes, healths)

    s = int(lines[3])

    minimum = None
    maximum = 0

    for s_itr in range(s):
        firstLastd = lines[4+s_itr].split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        dna = firstLastd[2]

        result = healthDNA(health_tree, reg_dict, first, last, dna)
        
        if minimum == None:
            minimum = result
        if result < minimum:
            minimum = result
        if result > maximum:
            maximum = result
        #if s_itr%10000 == 0:
        #    print(f'finished: {s_itr}')
    print(f'{minimum}, {maximum}')



run_test('test13.txt')



#test_genes = 'a b c aa d b'.split()
#healths = '1 2 3 4 5 6'.split()
#dna = 'caaab'
#
#print(healthDNA(test_genes, healths, 1, 5, dna))

#test_genes = 'abcd a ab ac ad bc cd a bb bcd abcd aaaa aa a aab aba'.split()
#healths = map(int, '11 3 4 5 1 20 0 6 13 15 56 99 38 45 1 8'.split())
#build_health_tree(test_genes, healths)
