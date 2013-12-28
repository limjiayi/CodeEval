# Created on 23/12/2013 by JiaYi Lim

import sys

def find_overlap(str1, str2):
    '''Find the maximum overlap between 2 strings'''
    shorter_len = min(len(str1), len(str2))
    # for the case where the front of str1 overlaps with the back of str2
    front_overlap = 0
    for i in range(1, shorter_len+1):
        if str1[:i] == str2[-i:]:
            front_overlap = i
    # for the case where the back of str1 overlaps with the front of str2
    back_overlap = 0
    for i in range(1, shorter_len+1):
        if str1[-i:] == str2[:i]:
            back_overlap = i
    # the order of the fragments is important when merging
    if front_overlap > back_overlap:
        return str2, str1, front_overlap
    else:
        return str1, str2, back_overlap

def merge_fragments(str1, str2, len_overlap):
    '''Merges 2 fragments'''
    return str1 + str2[len_overlap:]

def get_pair(fragments):
    '''Finds the pair of fragments with the max overlap, merges them and adds them to the collection of fragments'''
    fragment1, fragment2 = None, None
    pos1, pos2 = None, None
    max_overlap = 0
    for i in range(len(fragments)-1):
        for j in range(i+1, len(fragments)):
            frag1, frag2, len_overlap = find_overlap(fragments[i], fragments[j])
            if len_overlap > max_overlap:
                max_overlap = len_overlap
                fragment1 = frag1
                fragment2 = frag2
                pos1 = i
                pos2 = j

    if pos1 == None and pos2 == None: # no more matches, reassembly is complete
        return find_complete(fragments)
    elif pos1 < pos2:
        del fragments[pos2] # always delete the fragment nearer the back of the list first
        del fragments[pos1]
    else:
        del fragments[pos1]
        del fragments[pos2]

    merged = merge_fragments(fragment1, fragment2, max_overlap)
    fragments[0:0] = [merged] # insert the merged fragment at the front of the list 
    return fragments

def find_complete(fragments):
    '''Find the reassembled text, which is the largest fragment'''
    max_idx = None
    max_len = None
    for i, f in enumerate(fragments):
        if len(f) > max_len:
            max_len = len(f)
            max_idx = i
    return [fragments[max_idx]]

def reassemble():
    'Opens the specified file and processes each test case by reading the file line by line'
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            fragments = line.rstrip('\n').split(';')
            while len(fragments) > 1:
                fragments = get_pair(fragments)
            print fragments[0]


if __name__ == '__main__':
    reassemble()