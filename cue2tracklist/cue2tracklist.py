import re
import sys

def cue2tracklist(filepath):
    with open(filepath, 'r') as fID:
        exp = re.compile(r'\s{0,}TITLE \"(.*?)\"')
        tracklist = []
        for line in fID:
            test = exp.match(line)
            if test:
                tracklist.append(test.group(1))

    if len(tracklist) != 0:
        print('Track Listing:')
        print('')
        for track in tracklist:
            print('[#] {0}'.format(track))

if __name__ == '__main__':
    cue2tracklist(sys.argv[1])
